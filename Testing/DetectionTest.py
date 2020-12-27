#testing a way to find out what files are within a folder
import os


entries = os.listdir('Saved Files/') #Create a list of every file name within a directory

for f in entries:
    print(f) 

#the entries within the list seem to go in order. 
#Will make it easier when i make a dictionary and search throught the keys to find correct key