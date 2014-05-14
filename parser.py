#!/usr/local/bin/python2.7
""" fmparse.py
Usage:
      fmparse.py [-f <file> | --file <file>]

"""
__author__ = 'olivier'

# import statements
from docopt import docopt
from ciscoconfparse import CiscoConfParse
import datetime
import pprint
import shlex
import re


def print_markdown_report():
    """
    prints fortimail configuration report in markdown format
    """
    return None

def print_markdown(confobj):
    """
    prints a markdown representation of a fortiguard
    configuration object
    """
    # elements that should not be printed
    blacklist = ["password"]

    for elem in confobj:
        # add if clause to check for blacklist
        if any (bl in elem for bl in blacklist):
            pass
        elif elem.startswith("config"):
            print "|" + elem.replace("config", "") + "|"
        elif elem.startswith("  edit"):
            print "|" + elem.replace("edit", "") + "|"
        elif elem.startswith("    set") or elem.startswith("  set"):
            elem = elem.replace("set ", "").replace("  ", "")
            # splits elements in key and value pairs
            # to be separated with a |
            key, value = elem.split(" ", 1)
            print "|" + key + "|" + value + "|"


def print_routes(configobj):
    """
    The routes in fortigate configuration objects
    need special treatment.
    The default route contains no destination network
    such as 0.0.0.0. This needs to be added.
    """
    # TODO: implement function
    return configobj


def print_header(HOSTNAME):
    """
    prints markdown header for documentation
    """
    DATE = datetime.date.today().strftime("%d-%m-%Y")
    HEADER = '''
# Fortimail Configuration Report
----
Author: support
Date: %s
Hostname: %s
----
    '''
    print HEADER % (DATE, HOSTNAME)


def print_footer():
    """
    prints markdown footer for documentation
    """
    # TODO: implement function
    return None


def get_single_setvalue_from_file(searchstr, file):
    """
    used to get a single value from file
    """
    configfile = open(file, "r")
    for line in configfile:
        if searchstr in line:
            rstring = line.replace("  ", "")\
                .replace("set ", "")\
                .replace(searchstr + " ", "")
            return rstring
    # if nothing is found
    return False

def main():
    """
    main function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    configfile = arguments['<file>']
    # default value for testing
    if configfile is None:
        configfile = 'fml.cfg'

    # parse configuration file
    parse = CiscoConfParse(configfile)

    # assign single values
    HOSTNAME = get_single_setvalue_from_file("hostname", configfile)

    # assigns lists to config sections
    routes = parse.find_all_children('config system route')
    nics = parse.find_all_children('config system interface')
    ha = parse.find_all_children('config system ha')
    access_profiles = parse.find_all_children('config system accprofile')
    confglobal = parse.find_all_children('config system global')

    print_header(HOSTNAME)
    print "# General Configuration"
    print "## Global Configuration"
    print_markdown(confglobal)
    print "## High Availability (HA)"
    print_markdown(ha)
    print "# Network"
    print "## Routes"
    print_markdown(routes)
    print "## Network Interfaces"
    print_markdown(nics)


if __name__ == "__main__":
    main()
