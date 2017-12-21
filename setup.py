from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'linkedin_scraper',
        packages = ['linkedin_scraper'], # this must be the same as the name above
        version = '2.0.0',
        description = 'Scrapes user data from Linkedin',
        author = 'Joey Sham',
        author_email = 'sham.joey@gmail.com',
        url = 'https://github.com/joeyism/linkedin_scraper', # use the URL to the github repo
        download_url = 'https://github.com/joeyism/linkedin_scraper/dist/2.0.0.tar.gz',
        keywords = ['linkedin', 'scraping', 'scraper'], 
        classifiers = [],
        install_requires=['lxml', 'request', 'selenium'],
        )
