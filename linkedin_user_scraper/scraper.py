#!/usr/bin/python3

import requests
from lxml import html
from selenium import webdriver
import re
import os


class Person(object):
    name = None
    experiences = []
    educations = []
    also_viewed_urls = []
    linkedin_url = None
    driver = None

    def __init__(self, linkedin_url = None, experiences = [], educations = [], driver = None, scrape = True):
        self.linkedin_url = linkedin_url
        self.experiences = experiences
        self.educations = educations

        if driver is None:
            try:
                if os.getenv("CHROMEDRIVER") == None:
                    driver_path = os.path.join(os.path.dirname(__file__), 'drivers/chromedriver')
                else:
                    driver_path = os.getenv("CHROMEDRIVER")

                driver = webdriver.Chrome(driver_path)
            except:
                driver = webdriver.Chrome()

        driver.get("http://linkedin.com")
        self.driver = driver

        if scrape:
            self.scrape()
 

    def add_experience(self, experience):
        self.experiences.append(experience)

    def add_education(self, education):
        self.educations.append(education)

    def scrape(self):
        driver = self.driver
        page = driver.get(self.linkedin_url)

        # get name
        self.name = driver.find_element_by_id("name").text

        # get experience
        exp = driver.find_element_by_id("experience")
        for position in exp.find_elements_by_class_name("position"):
            position_title = position.find_element_by_class_name("item-title").text
            company = position.find_element_by_class_name("item-subtitle").text

            try:
                times = position.find_element_by_class_name("date-range").text
                from_date, to_date, duration = time_divide(times)
            except:
                from_date, to_date = (None, None)
            experience = Experience( position_title = position_title , from_date = from_date , to_date = to_date)
            experience.institution_name = company
            self.add_experience(experience)

        # get education
        edu = driver.find_element_by_id("education")
        for school in edu.find_elements_by_class_name("school"):
            university = school.find_element_by_class_name("item-title").text
            degree = school.find_element_by_class_name("original").text
            try:
                times = school.find_element_by_class_name("date-range").text
                from_date, to_date, duration = time_divide(times)
            except:
                from_date, to_date = (None, None)
            education = Education(from_date = from_date, to_date = to_date, degree=degree)
            education.institution_name = university
            self.add_education(education)

        # get 

        driver.close()

    def __repr__(self):
        return "{name}\n\nExperience\n{exp}\n\nEducation\n{edu}".format(name = self.name, exp = self.experiences, edu = self.educations)

class Institution(object):
    institution_name = None
    website = None
    industry = None
    type = None
    headquarters = None
    company_size = None
    founded = None

    def __init__(self, name=None, website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None):
        self.name = name
        self.website = website
        self.industry = industry
        self.type = type
        self.headquarters = headquarters
        self.company_size = company_size
        self.founded = founded

class Experience(Institution):
    from_date = None
    to_date = None
    description = None
    position_title = None

    def __init__(self, from_date = None, to_date = None, description = None, position_title = None):
        self.from_date = from_date
        self.to_date = to_date
        self.description = description
        self.position_title = position_title

    def __repr__(self):
        return "{position_title} at {company} from {from_date} to {to_date}".format( from_date = self.from_date, to_date = self.to_date, position_title = self.position_title, company = self.institution_name)


class Education(Institution):
    from_date = None
    to_date = None
    description = None
    degree = None

    def __init__(self, from_date = None, to_date = None, description = None, degree = None):
        self.from_date = from_date
        self.to_date = to_date
        self.description = description
        self.degree = degree

    def __repr__(self):
        return "{degree} at {company} from {from_date} to {to_date}".format( from_date = self.from_date, to_date = self.to_date, degree = self.degree, company = self.institution_name)

def time_divide(string):
    duration = re.search("\((.*?)\)", string)

    if duration != None:
        duration = duration.group(0)
        string = string.replace(duration, "").strip()
    else:
        duration = "()"

    times = string.split("–")
    return (times[0].strip(), times[1].strip(), duration[1:-1])

