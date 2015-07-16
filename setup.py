from setuptools import setup, find_packages

setup(name='enchanted-pelican',
      version='0.1',
      description='Spellchecking plugin for Pelican static site generator.',
      classifiers=[],
      keywords="pelican spellcheck",
      author='zombie.guru',
      author_email='geoffrey@zombie.guru',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'pelican',
          'pyenchant',
      ],
      entry_points={},
      extras_require={
          'test': [
              'mock',
              'nose',
          ]
      }
      )
