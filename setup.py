""" setup.py
REPOSITORY:
  https://github.com/DavidJLambert/eBay-API-Sample

SUMMARY:
  Fetch title, current price, and currency name for all eBay items with UPC
  753759077600, using HTTP GET.
  Written for Python 2.7.

AUTHOR:
  David J. Lambert

VERSION:
  0.1.1

DATE:
  May 31, 2019
"""

from distutils.core import setup

with open("README.rst", 'r') as f:
    long_description = f.read()

setup(
    author='David J. Lambert',
    author_email='David5Lambert7@gmail.com',
    description='Sample use of the eBay API',
    install_requires=[],
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    name='eBay-API-Sample',
    py_modules=["sample"],
    url='https://github.com/DavidJLambert/eBay-API-Sample',
    version='0.1.1',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
)
