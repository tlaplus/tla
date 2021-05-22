"""Installation script."""
from setuptools import setup


PACKAGE_NAME = 'tla'
DESCRIPTION = (
    'Parser and abstract syntax tree for TLA+, '
    'the temporal logic of actions.')
README = 'README.md'
long_description = open(README).read()
URL = 'https://github.com/tlaplus/tla_python'
VERSION_FILE = '{name}/_version.py'.format(name=PACKAGE_NAME)
MAJOR = 0
MINOR = 0
MICRO = 2
VERSION = '{major}.{minor}.{micro}'.format(
    major=MAJOR, minor=MINOR, micro=MICRO)
VERSION_FILE_TEXT = (
    '# This file was generated from `setup.py`\n'
    "version = '{version}'\n").format(version=VERSION)
INSTALL_REQUIRES = [
    'infix >= 1.2',
    'ply >= 3.4, <= 3.10',
    ]
TESTS_REQUIRE = ['nose']
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Compilers',
    ]
KEYWORDS = [
    'TLA+', 'TLA', 'temporal logic of actions',
    'formal', 'specification',
    'expression', 'formula', 'module',
    'mathematics', 'theorem', 'proof',
    'parser', 'lexer', 'parsing',
    'ast', 'abstract syntax tree', 'syntax tree',
    'ply', 'lex',
    ]


def run_setup():
    """Write version file and install package."""
    with open(VERSION_FILE, 'w') as f:
        f.write(VERSION_FILE_TEXT)
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Ioannis Filippidis',
        author_email='jfilippidis@gmail.com',
        url=URL,
        license='BSD',
        install_requires=INSTALL_REQUIRES,
        tests_require=TESTS_REQUIRE,
        packages=[PACKAGE_NAME],
        package_dir={PACKAGE_NAME: PACKAGE_NAME},
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS)


if __name__ == '__main__':
    run_setup()
