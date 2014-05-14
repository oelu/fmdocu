#!/usr/local/bin/python2.7
""" Fortimail Configuration Report
Usage:
    fmdocu.py [-f <file> | --file <file>]

Options:
    -h --help  shows help message
"""
__author__ = 'olivier'

# import statements
from docopt import docopt
import datetime
import re
import mmap


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
        if any(bl in elem for bl in blacklist):
            pass
        elif elem.startswith("next"):
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
            print "|" + key + " | " + value + "|"


def print_header(hostname):
    """
    prints markdown header for documentation
    """
    date = datetime.date.today().strftime("%d-%m-%Y")
    header = '''
# Fortimail Configuration Report
----
Author: support
Date: %s
Hostname: %s
----
    '''
    print header % (date, hostname)


def print_footer():
    """
    prints markdown footer for documentation
    """
    # TODO: implement function
    return None


def get_single_setvalue_from_file(searchstr, configfile):
    """
    used to get a single value from file
    """
    configfile = open(configfile, "r")
    for line in configfile:
        if searchstr in line:
            rstring = line.replace("  ", "")\
                .replace("set ", "")\
                .replace(searchstr + " ", "")
            configfile.close()
            return rstring
    # if nothing is found
    configfile.close()
    return False


def get_config_section_as_list(data, section):
    """
    reads configuration file and returns a list of
    a section.

    example sections are:
        config system global
        config system dns
        etc..
    """
    configsection = [section]
    searchstring = section + "(.*?)\nend"
    for result in re.findall(searchstring, data, re.S):
        configsection.extend(result.split('\n'))
    return configsection


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

    # assign single values
    hostname = get_single_setvalue_from_file("hostname", configfile)

    # assign config lists
    with open(configfile, 'r+') as filehandle:
        data = mmap.mmap(filehandle.fileno(), 0)
        confglobal = get_config_section_as_list(data, 'config system global')
        highavailability = get_config_section_as_list(data, 'config system ha')
        dns = get_config_section_as_list(data, 'config system dns')
        routes = get_config_section_as_list(data, 'config system route')
        nics = get_config_section_as_list(data, 'config system interface')
        mailserver = get_config_section_as_list \
            (data, 'config system mailserver')
        session = get_config_section_as_list \
            (data, 'config profile session')
        antivirus = get_config_section_as_list(data, 'config profile antivirus')
        domainassociation = get_config_section_as_list \
            (data, 'config  domain-association')

    # get values from user
    # TODO: add interactive option and gather input from user
    # customername = raw_input("please enter customer name: ")

    print_header(hostname)
    print "# General Configuration"
    print "## Global Configuration"
    print_markdown(confglobal)
    print "## High Availability (HA)"
    print_markdown(highavailability)
    print "# Network"
    print "# DNS"
    print_markdown(dns)
    print "## Routes"
    print_markdown(routes)
    print "## Network Interfaces"
    print_markdown(nics)
    print "# Mailserver"
    print "## Session"
    print_markdown(session)
    print_markdown(mailserver)
    print '## Antivirus'
    print_markdown(antivirus)
    print "## Domain Association"
    print_markdown(domainassociation)


if __name__ == "__main__":
    main()
