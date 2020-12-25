#Learning to create txt file so that character information can be saved when the bot is not on
f = open("Saved Files/TestFile.txt", "w") #Should create a filed called Test/File.txt in the folder Saved Files

for i in range(10): #writes into file
    f.write("line {num}\n".format(num = i))

f.close() #good to always close files