# What: I want a program that does bulk renaming for my files. 
# eg. 01-aqualung-cinderella_www.file24ever.com.mp3 to Aqualung - Cinderella.mp3

# How: 
# 1. The files and directories to be renamed are specified in a list.
# 2. New names for the files.
# 3. mv oldname newname 

import os, re

directory = "/home/iris/Music/Aqualung - Memory Man [2007]/"
pattern = 'com.mp3$'
list = []

for file in os.listdir(directory):
    if (re.search(pattern, file)):
        list.append(file)

for filename in list:
    newFilename = "Aqualung - " + (filename.split("_w")[0].split("-")[2]) + ".mp3"
    print directory + filename + "," + directory + newFilename
    os.rename(directory + filename, directory + newFilename)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
