from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='prologue',
    version='0.0.1',

    description="Python package providing horrifying "
                "welcome messages for your application",

    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hypernormalisation/prologue',

    author='Stephen Ogilvy',
    author_email='sogilvy@tuta.io',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='welcome',
    packages=find_packages(exclude=[]),
    python_requires='>=3.6',

    project_urls={
        'Source': 'https://github.com/hypernormalisation/prologue',
        'Bug Reports': 'https://github.com/hypernormalisation/timbermafia/prologue',
    },
)
