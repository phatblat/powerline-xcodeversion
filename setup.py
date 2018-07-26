# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name         = 'powerline-xcodeversionj',
    description  = 'A Powerline segment for showing the active version of Xcode',
    version      = '0.0.1',
    keywords     = 'powerline status prompt xcode version',
    license      = 'MIT',
    author       = 'Ben Chatelain',
    author_email = 'ben@octop.ad
    url          = 'https://github.com/phatblat/powerline-xcodeversion',
    packages     = ['powerline_xcodeversion'],
    classifiers  = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
