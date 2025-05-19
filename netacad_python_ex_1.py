print("Hisssssss.")

import json
import os

data_file = "bugs-file.json"

#Create the file if it does not exist
if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            json.dump([], f)

bugs = input("Enter bugs and ways to debug them: ")

entry = {
    "info" : bugs
}

#Load existing bugs from file
with open(data_file, "r") as f:
    #json.load(every_bug, f) - previous error. Have to initialize every_bug first
    every_bug = json.load(f)

#Append new bug entry
every_bug.append(entry)

#Save updated list back to file
with open(data_file, "w") as f:
    json.dump(every_bug, f, indent=4)

print("Your list of bugs and how to debug them: ")
print(every_bug)
