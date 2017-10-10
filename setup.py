from __future__ import print_function
from setuptools import setup, Command
import os

version = "0.1"
description = 'jsm tools'
long_description = description
if os.path.exists('README.md'):
    with open('README.md') as f:
        long_description = f.read()


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(
    name='jsm',
    version=version,
    url='http://github.com/nudomarinero/jsm/',
    author='Jose Sabater',
    author_email='jsm@iaa.es',
    description=description,
    long_description=long_description,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: Stable',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    tests_require=['pytest'],
    install_requires=[],
    scripts = ['bin/extract_tier1',],
    packages=['jsm'],
    test_suite='test',
    cmdclass = {'test': PyTest},
    )
