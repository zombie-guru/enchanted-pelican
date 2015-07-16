enchanted-pelican
#################

Spellcheck plugin for Pelican_ using PyEnchant_.

Installation
============

This plugin only requires PyEnchant. See PyEnchant_ for installation
instructions.

Usage
=====

Add ``enchantedpelican`` to your list of ``PLUGINS`` in your ``pelicanconf.py``.

.. code-block:: python

    PLUGINS = ['enchantedpelican']

Optionally, provide some extra settings

.. code-block:: python

    ENCHANTED_PELICAN_SETTINGS = {
        'word_file': '/path/to/word/file.txt',
        'languange': 'en_US'
    }

.. _Pelican: http://docs.getpelican.com/en/latest/plugins.html
.. _PyEnchant: http://www.python.org/
