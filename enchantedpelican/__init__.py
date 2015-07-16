import logging
import re
import textwrap

import enchant
import pelican

LOG = logging.getLogger(__name__)
IGNORE = (
    # <pre> and <tt> tags
    re.compile('<(pre|tt).*?>.*?</(pre|tt)>', re.DOTALL),
    # numbers
    re.compile('\d+'),
    # any remaining tags
    re.compile('<.*?>')
    )
WORDS = re.compile(r'(\w[\'\w]+)')


class SpellingError(ValueError):
    def __init__(self, words, dictionary, filename):
        mistakes = '\n'.join(words)
        msg = textwrap.dedent('''
        filename: %(filename)s
        %(mistakes)s
        '''.strip()) % {'filename': filename, 'mistakes': mistakes}
        super(SpellingError, self).__init__('\n' + msg)


class EnchantedPelican(object):

    def __init__(self, language='en_US', words=None):
        self.d = None

    def on_initialized(self, pelican):
        """ This is called on pelican initialization.

        Read optional settings from the variable ENCHANTED_PELICAN_SETTINGS
        in pelicanconf.py. Expects the following keys:

        - wordfile: Path to a newline deliminated word list. Defaults to None.
        - languange: Language to spellcheck against. Defaults to en_US.
        """
        settings = pelican.settings.get('ENCHANTED_PELICAN_SETTINGS', dict())
        words = settings.get('wordfile')
        language = settings.get('language', 'en_US')
        if words:
            self.d = enchant.DictWithPWL('en_US', words)
        else:
            self.d = enchant.Dict(language)

    def on_article_generator_write_article(self, article_generator, content):
        cleaned = content.content
        for exp in IGNORE:
            cleaned = exp.sub('', cleaned)
        mistakes = []
        for word in (x.group(0) for x in WORDS.finditer(cleaned)):
            if any(self.d.check(x()) for x in (
                   word.lower, word.upper, word.capitalize)):
                pass
            else:
                mistakes.append(word)

        if len(mistakes) > 0:
            raise SpellingError(mistakes, self.d, content.source_path)


ep = EnchantedPelican()


def register():
    pelican.signals.initialized.connect(
        ep.on_initialized)
    pelican.signals.article_generator_write_article.connect(
        ep.on_article_generator_write_article)
