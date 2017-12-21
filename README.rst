Linkedin Scraper
================

Scrapes Linkedin User Data

Installation
------------

.. code:: bash

    pip3 install --user linkedin_scraper

Version **2.0.0** and before is called ``linkedin_user_scraper`` and can
be installed via ``pip3 install --user linkedin_user_scraper``

Setup
-----

First, you must set your chromedriver location by

.. code:: bash

    export CHROMEDRIVER=~/chromedriver

Usage
-----

To use it, just create the class

User Scraping
~~~~~~~~~~~~~

.. code:: python

    from linkedin_scraper import Person
    person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5")

Company Scraping
~~~~~~~~~~~~~~~~

.. code:: python

    from linkedin_scraper import Company
    company = Company("https://ca.linkedin.com/company/google")

API
---

Person
~~~~~~

Overall, to a Person object can be created with the following inputs:

.. code:: python

    Person( linkedin_url=None, experiences = [], educations = [], driver = None, scrape = True)

``linkedin_url``
^^^^^^^^^^^^^^^^

This is the linkedin url of their profile

``experiences``
^^^^^^^^^^^^^^^

This is the past experiences they have. A list of
``linkedin_scraper.scraper.Experience``

``educations``
^^^^^^^^^^^^^^

This is the past educations they have. A list of
``linkedin_scraper.scraper.Education``

``driver``
^^^^^^^^^^

This is the driver from which to scraper the Linkedin profile. A driver
using Chrome is created by default. However, if a driver is passed in,
that will be used instead.

For example

.. code:: python

    driver = webdriver.Chrome()
    person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver = driver)

``scrape``
^^^^^^^^^^

When this is **True**, the scraping happens automatically. To scrape
afterwards, that can be run by the ``scrape()`` function from the
``Person`` object.

``scrape(close_on_complete=True)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the meat of the code, where execution of this function scrapes
the profile. If *close_on_complete* is True (which it is by default),
then the browser will close upon completion. If scraping of other
profiles are desired, then you might want to set that to false so you
can keep using the same driver.

Company
~~~~~~~

.. code:: python

    Company(linkedin_url = None, name = None, about_us =None, website = None, headquarters = None, founded = None, company_type = None, company_size = None, specialties = None, showcase_pages =[], affiliated_companies = [], driver = None, scrape = True)

.. linkedin_url-1:

``linkedin_url``
^^^^^^^^^^^^^^^^

This is the linkedin url of their profile

``name``
^^^^^^^^

This is the name of the company

``about_us``
^^^^^^^^^^^^

The description of the company

``website``
^^^^^^^^^^^

The website of the company

``headquarters``
^^^^^^^^^^^^^^^^

The headquarters location of the company

``founded``
^^^^^^^^^^^

When the company was founded

``company_type``
^^^^^^^^^^^^^^^^

The type of the company

``company_size``
^^^^^^^^^^^^^^^^

How many people are employeed at the company

``specialties``
^^^^^^^^^^^^^^^

What the company specializes in

``showcase_pages``
^^^^^^^^^^^^^^^^^^

Pages that the company owns to showcase their products

``affiliated_companies``
^^^^^^^^^^^^^^^^^^^^^^^^

Other companies that are affiliated with this one

.. driver-1:

``driver``
^^^^^^^^^^

This is the driver from which to scraper the Linkedin profile. A driver
using Chrome is created by default. However, if a driver is passed in,
that will be used instead.

For example

.. code:: python

    driver = webdriver.Chrome()
    company = Company("https://ca.linkedin.com/company/googl://ca.linkedin.com/company/google", driver = driver)

.. scrapeclose_on_completetrue-1:

``scrape(close_on_complete=True)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the meat of the code, where execution of this function scrapes
the company. If *close_on_complete* is True (which it is by default),
then the browser will close upon completion. If scraping of other
companies are desired, then you might want to set that to false so you
can keep using the same driver.

Versions
--------

**2.0.x** \* Modified the way the objects are called \* Added Company \*
Changed name from ``linkedin_user_scraper`` to ``linkedin_scraper``

**1.2.x** \* Allows scraping later

**1.1.x** \* Addes additional API where user can use their own webdriver

**1.0.x** \* first publish and fixes
