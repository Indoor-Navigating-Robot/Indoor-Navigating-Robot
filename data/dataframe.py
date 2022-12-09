import pandas as pd  
import os
import re
  
# Creating Empty DataFrame and Storing it in variable df
df = pd.DataFrame(columns=["D0:4D:C6:02:E5:C0","D0:4D:C6:02:95:61","D0:4D:C6:02:95:70","D0:D3:E0:B1:87:00","D0:4D:C6:02:47:F0","D0:4D:C6:02:47:E0",
                            "D0:4D:C6:02:C2:81","D0:4D:C6:01:E6:20","D0:4D:C6:02:C2:80","D0:4D:C6:01:E6:21","D0:4D:C6:02:D3:A0",
                            "D0:4D:C6:02:7E:50","00:4E:35:CF:97:B0","D0:D3:E0:B1:3A:71","D0:D3:E0:B1:3A:60","D0:4D:C6:02:C2:91",
                            "D0:4D:C6:02:7E:51","D0:4D:C6:02:C2:90","D0:4D:C6:01:E6:30","D0:4D:C6:02:7E:41","00:4E:35:CF:97:A1",
                            "D0:4D:C6:03:4D:51","D0:4D:C6:01:E6:31","00:4E:35:CF:97:B1","D0:4D:C6:02:7E:40","D0:4D:C6:02:47:E1",
                            "D0:D3:E0:B1:A0:00","D0:4D:C6:03:4D:41","D0:4D:C6:02:E5:C1","00:4E:35:CF:97:A0","00:4E:35:CF:2E:50",
                            "00:4E:35:CF:CE:20","D0:D3:E0:B1:3A:61","00:4E:35:CF:2E:51","D0:4D:C6:02:47:F1","00:4E:35:CF:2E:41",
                            "D0:4D:C6:02:95:60","40:E3:D6:24:25:32","D0:4D:C6:03:4D:40","40:E3:D6:24:25:33","D0:4D:C6:03:4D:50",
                            "D0:4D:C6:02:E5:D1","D0:D3:E0:B1:3A:70","D0:4D:C6:02:95:71","40:E3:D6:24:25:23","00:4E:35:CF:2E:40",
                            "D0:D3:E0:B1:87:01","D0:4D:C6:02:E5:D0","40:E3:D6:24:25:22","x","y"])


files = [filename for filename in os.listdir('.') if len(filename.split('-')) > 1] # All files were named using a x-y naming convention

for filename in files:
    with open(filename, 'r') as file:
        data = file.read()#.replace('\n', '')

    result = re.findall(r"Address[\S\s]{265}", data) # Find the section of data contain the SSID, RSSI value, and MAC address

    csuAPs = []
    for item in result:
        if "csu-net" in item or "csu-visitor" in item:
            csuAPs.append(item)

    qualities = {}
    for ap in csuAPs:
        mac = re.findall(r"[\S\s]{2}:[\S\s]{2}:[\S\s]{2}:[\S\s]{2}:[\S\s]{2}:[\S\s]{2}", ap)[0] # Get the MAC address
        quality = re.findall(r"\d\d/\d\d", ap)[0] # Get the RSSI value
        qualityInt = int(quality[0:2])
        qualities[mac] = quality

    nums = filename.split('-')
    x = nums[0]
    y = nums[1]
    dictionary = {}
    for column in df.columns:
        if column == "x":
            dictionary[column] = x
        elif column == "y":
            dictionary[column] = y
        else:
            dictionary[column] = qualities[column].split('/')[0] if column in qualities else "0"
        
    df = df.append(dictionary, ignore_index = True)
df.to_csv('collected_rssi.csv', index=False)
