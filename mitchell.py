#! /usr/bin/env python

"""
Scraping http://www.mitchellhogan.com/blog/ for book updates.

Checks for updates and adds a time stamp to show time between changes.

This script  uses 4 text files make sure to create them and add
the locations to the per, per-old, new and old varibles.
"""

import filecmp
import re
from datetime import datetime
from shutil import copy2
from urllib.request import urlopen
from bs4 import BeautifulSoup


per = "create a file and add its location to here"
per_old = "create a file and add its location to here"
new = "create a file and add its location to here"
old = "create a file and add its location to here"



def copy():
    """Copy per to per.old"""
    copy2(per, per_old)


def get_soup():
    """Open with urlopen || run through bs4."""
    global soup
    html = urlopen("http://www.mitchellhogan.com/blog/")
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_text():
    """Get text div class meterbox. Write text to per."""
    log = open(per, "w")
    for i in soup.body("div", {"class": "meterbox"}):
        x = i.get_text()
        xx = re.sub(r'((\W*Book\W\d{1}))', r'\1 ', x)
        xxx = re.sub(r'(\d{1,3}%)', r' \1 \n', xx)
        print(xxx, file=log)
    log.close()


def Check_status_time_stamp():
    """Check for changes per vs per.old || If loop, for change || Adds time stamp."""
    X = filecmp.cmp(per, per_old, shallow=False)
    if X is True:
        output = open(new, "r")
        output2 = open(per, "r")
        print(16 * "#", "NO CHANGES", 18 * "#", "\n")
        print("      Updated:",  output.read().replace("\n", ' '))
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


def mitchell():
    copy()
    get_soup()
    get_text()
    Check_status_time_stamp()


mitchell()
