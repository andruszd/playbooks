#!/usr/bin/env python
import sys

DEFAULT_RACK = "/etc/hadoop/conf/default-rack"
HOST_RACK_FILE = "/etc/hadoop/conf/host-rack.map"
host_rack = {}
for line in open(HOST_RACK_FILE):
    (host, rack) = line.split()
    host_rack[host] = rack
for host in sys.argv[1:]:
    if host in host_rack:
        var = host_rack[host]
        print(var)
    else:
        print(DEFAULT_RACK)