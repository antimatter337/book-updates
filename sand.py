#! /usr/bin/env python

"""
Scraping www.brandonsanderson.com for book updates.

Checks for updates and adds a time stamp to show time between changes.

This script uses 4 text files make sure to create them and add the locations to
the per, per-old, new and old varibles
"""

from urllib.request import urlopen
import re
import filecmp
from shutil import copy2
from bs4 import BeautifulSoup


per = "create a file and add its location to here"
per_old = "create a file and add its location to here"
new = "create a file and add its location to here"
old = "create a file and add its location to here"



def copy():
    """Make copy of old scan."""
    copy2(per, per_old)


def get_soup():
    """Open with urlopen || runs through bs4."""
    global soup
    html = urlopen("http://brandonsanderson.com/")
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_text():
    """Get text from the div tags with the class progress-titles."""
    global x
    for i in soup.body("div", {"class": "progress-titles"}):
        x = i.get_text()
    return x


def change_write_text():
    """Make text more readable || Then write to file"""
    global out
    xx = x.replace("\n", ' ').replace(' %', '%').lstrip()
    xxx = re.sub("(%  )", "\\1\n", xx, 0, re.DOTALL)
    out = xxx.strip()
    log = open(per, "w")
    print(out, file=log)


def Check_status_time_stamp():
    """Check for changes per vs per.old || If loop, for change || Adds time stamp."""
    X = filecmp.cmp(per, per_old, shallow=False)
    if X is True:
        output = open(new, "r")
        output2 = open(per, "r")
        print(16 * "#", "NO CHANGES", 18 * "#", "\n")
        print("      Updated:", output.read().replace("\n", ' '))
        print(output2.read())
        output.close()
        output2.close()
    elif X is False:
        copy2(new, old)
        log2 = open(new, "w")
        dt = datetime.now()
        date = dt.strftime("%m/%d/%Y %I:%M%p")
        print(date, file=log2)
        log2.close()
        output = open(old, "r")
        output2 = open(per_old, "r")
        print(18 * "-", " CHANGES", 18 * "-", "\n")
        print(18 * "#", "BEFORE", 18 * "#", "\n")
        print("      Updated:", output.read().replace("\n", ' '))
        print(output2.read())
        output.close()
        output2.close()
        output = open(new, "r")
        output2 = open(per, "r")
        print(18 * "#", "AFTER", 18 * "#", "\n")
        print("      Updated:", output.read().replace("\n", ' '))
        print(output2.read(), "\n")
        output.close()
        output2.close()


def sand():
    """One function to rule them all."""
    copy()
    get_soup()
    get_text()
    change_write_text()
    Check_status_time_stamp()

sand()
