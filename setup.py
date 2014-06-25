# -*- coding: utf-8 -*-
##
## This file is part of Flask-Registry
## Copyright (C) 2013 CERN.
##
## Flask-Registry is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Flask-Registry is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Flask-Registry; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

from setuptools import setup
import os
import re

# Get the version string.  Cannot be done with import!
with open(os.path.join('flask_registry', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='Flask-Registry',
    version=version,
    url='http://github.com/inveniosoftware/flask-registry/',
    license='GPLv2',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description='Flask-Registry is an extension for Flask that allow '
        'frameworks to dynamically assemble your Flask application from '
        'reusable packages.',
    long_description=open('README.rst').read(),
    packages=['flask_registry', 'flask_registry.registries'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'six',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
        #'Development Status :: 5 - Production/Stable',
    ],
    entry_points={
        'flask_registry.test_entry': [
            'testcase = flask_registry:RegistryBase',
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose', 'coverage'],
)
