# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md.md') as f:
    license = f.read()

setup(
    name='pymaster',
    version='0.1.0',
    description='Sample package for pymaster',
    long_description=readme,
    author='Premkumar Salagala',
    author_email='premkumar189@gmail.com',
    url='https://github.com/pksalagala/pymaster',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

