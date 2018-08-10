# vim:fileencoding=utf-8:noet

import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name         = 'powerline-xcodeversion',
    version      = '0.0.1',
    description  = 'A Powerline segment for showing the active version of Xcode',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords     = 'powerline status prompt xcode version',
    license      = 'MIT',
    author       = 'Ben Chatelain',
    author_email = 'ben@octop.ad',
    url          = 'https://github.com/phatblat/powerline-xcodeversion',
    packages     = setuptools.find_packages(),
    classifiers  = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Terminals"
    ]
)
