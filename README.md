# Fortimail Configuration Documentation
Prints a configuration report in markdown

## Usage
    » ./fmdocu.py -h
    Fortimail Configuration Report
    Usage:
      fmdocu.py [-f <file> | --file <file>]
      
      Options:
          -h --help  shows help message

## Example Session
generate the report: 
$ fmdocu.py -f fml.cfg >> fmdocu.md
$cat fmdocu.md

# Fortimail Configuration Report
----
Author: support
Date: 21-05-2014
Hostname: fm01

----
    
# General Configuration
## Global Configuration
|  system global |
| operation-mode | server |
| default-certificate | fm01 |
| hostname | fm01 |
## High Availability (HA)
|  system ha |
| mode | config-master |
| config-peer-ip | 192.168.0.42  |
# Network
# DNS
|  system dns |
| primary | 8.8.8.8 |
| secondary | 8.8.4.4 |
## Routes
|  system route |
| gateway | 192.168.0.1 |
| destination | 192.168.4.0/24 |
| gateway | 192.168.4.1 |
## Network Interfaces
|  system interface |
| ip | 192.168.0.41/24 |
| allowaccess | https ping ssh snmp  |
| ip | 192.168.4.10/24 |
| allowaccess | https ping ssh snmp  |
# Mailserver
## Session
|  profile session |
| conn-rate-number | 500 |
| conn-concurrent | 5 |
| session-recipient-domain-check | enable  |
| session-command-checking | enable  |
| limit-email | 20 |
| session-sender-domain-check | enable  |
| session-command-checking | enable  |
| error-drop-after | 3 |
| sender-reputation-status | enable  |
| dkim-validation | enable  |
| domain-key-validation | enable  |
|  system mailserver |
| local-domain-name | testag.local |
## Antivirus
|  profile antivirus |
| scanner | enable  |
| heuristic | enable  |
| action-heuristic | predefined_av_discard |
| action-default | predefined_av_discard |
| scanner | enable  |
| heuristic | enable  |
| action-default | predefined_av_reject |
## System Domains
## Domain Association
|   domain-association |
