#!/usr/local/bin/python2.7
""" fmparse.py
Usage:
      fmparse.py [-f <file> | --file <file>]

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
    return None

def print_markdown(confobj):
    """
    prints a markdown representation of a fortiguard
    configuration object
    """
    for elem in confobj:
        if "config" in elem:
            print "|" + elem.replace("config", "") + "|"
        elif "edit" in elem:
            print "|" + elem.replace("edit", "") + "|"
        elif "set" in elem:
            # TODO: has to be splitted in key and value words
            # with break of |
            print "|" + elem.replace("set", "") + "|"

def print_routes(configobj)
    """
    The routes in fortigate configuration objects
    need special treatment.
    The default route contains no destination network
    such as 0.0.0.0. This needs to be added.
    """
    # TODO: implement function
    return configobj

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

    # assigns lists to config sections
    routes = parse.find_all_children('config system route')
    nics = parse.find_all_children('config system interface')
    ha = parse.find_all_children('config system ha')
    access_profiles = parse.find_all_children('config system accprofile')

    print_markdown(routes)


if __name__ == "__main__":
    main()
