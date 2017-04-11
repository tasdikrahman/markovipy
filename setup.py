#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# requirements = [
#     'Click>=6.0',
#     # TODO: put package requirements here
# ]

test_requirements = [
    'pytest==2.9.2'
]

setup(
    name='markovipy',
    version='0.1.0',
    description="Sentence generation using Markov Chains",
    long_description=readme + '\n\n' + history,
    author="Tasdik Rahman",
    author_email='prodicus@outlook.com',
    url='https://github.com/prodicus/markovipy',
    packages=[
        'markovipy',
    ],
    package_dir={'markovipy':
                 'markovipy'},
    include_package_data=True,
    # install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='markovipy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
