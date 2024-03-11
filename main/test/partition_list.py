import os
import re

regex = r"([^\\s]*:)"
driver = os.popen("wmic logicaldisk get name").read()
drives = re.findall(regex, driver)

partition_list = [partition.strip() for drive in drives for partition in drive.split(":") if partition.strip()]
partition_list[0] = partition_list[0].strip("Name  \n\n" )
print(partition_list)
