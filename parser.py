#!/usr/local/bin/python2.7
""" fmparse.py
Usage:
      fmparse.py (-f <file> | --file <file>)

"""
__author__ = 'olivier'

# import statements
from docopt import docopt
from ciscoconfparse import CiscoConfParse
import pprint
import re


def print_markdown_report():
    """
    prints fortimail configuration report in markdown format
    """
    None


def main():
    """
    main function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    configfile = arguments['<file>']

    # parse configuration file
    parse = CiscoConfParse(configfile)

    # assigns lists to config sections
    routes = parse.find_all_children('config system route')
    nics = parse.find_all_children('config system interface')
    ha = parse.find_all_children('config system ha')
    access_profiles = parse.find_all_children('config system accprofile')

if __name__ == "__main__":
    main()
