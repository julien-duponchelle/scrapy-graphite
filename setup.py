from distutils.core import setup

setup(name='ScrapyGraphite',
      version='0.1',
      license='Apache License, Version 2.0',
      description='Output scrapy statistics to carbon/graphite.',
      author='Julien Duponchelle',
      author_email='julien@duponchelle.info',
      url='http://github.com/noplay/scrapy-graphite',
      keywords="scrapy carbon graphite",
      py_modules=['scrapygraphite'],
      platforms = ['Any'],
      install_requires = ['scrapy', 'galena'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'Environment :: No Input/Output (Daemon)',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
