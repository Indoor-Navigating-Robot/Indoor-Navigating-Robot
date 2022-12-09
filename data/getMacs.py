import os
import re

files = [filename for filename in os.listdir('.') if len(filename.split('-')) > 1]
# files = [filename for filename in os.listdir(folder) if filename.startswith('spam')]
macs = set()
for filename in files:
    with open(filename, 'r') as file:
        data = file.read()#.replace('\n', '')

    result = re.findall(r"Address[\S\s]{265}", data)

    csuAPs = []
    for item in result:
        if "csu-net" in item or "csu-visitor" in item:
            csuAPs.append(item)

    qualities = {}
    for ap in csuAPs:
        mac = re.findall(r"[\S\s]{2}:[\S\s]{2}:[\S\s]{2}:[\S\s]{2}:[\S\s]{2}:[\S\s]{2}", ap)[0]
        quality = re.findall(r"\d\d/\d\d", ap)[0]
        qualityInt = int(quality[0:2])
        qualities[mac] = quality
        macs.add(mac)


import json
f = open("macs.txt", "a")
# nums = filename.split('-')
# x = nums[0]
# y = nums[1]
for i in macs:
    f.write(f"{i},")
    
f.close()
