#!/usr/bin/env python3
# encoding: utf-8

import re
import json
import subprocess
import sys

def get_diskinformation():
    name = []
    with open("/proc/partitions") as fp:
        for line in fp.readlines():
            try:
                value = line.split()[3]
                if re.match("nvme[0-9]n[0-9]$", value):
                    name.append('/dev/' + value[:5])
                if re.match("sd[a-z]$", value):
                    name.append('/dev/' + value)
            except:
                # just ignore parse errors in header/separator lines
                pass
    return name

def get_temperatures(device):
    a = subprocess.run(["sudo", "/usr/sbin/smartctl", "-A", device], encoding='utf-8', stdout=subprocess.PIPE)
    for line in a.stdout.split('\n'):
        if line.startswith('Temperature'):
            return line.split()[1]
        if "Temperature_Celsius" in line:
            return line.split()[9]
    return "0"


def main():
    # Check arguments.
    aggr = sys.argv
    if len(aggr) == 2:
        print (get_temperatures(aggr[1]))
        exit()

    diskinf = get_diskinformation()
    data = []
    if diskinf:
        for device in diskinf:
            data.append( {"{#DEVICENAME}": device, "Temperature": get_temperatures(device)})
    print(json.dumps({"data": data}, indent=4))


if __name__ == "__main__":
    main()