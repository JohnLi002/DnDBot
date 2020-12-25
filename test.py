#Learning to create txt file so that character information can be saved when the bot is not on
f = open("Saved Files/TestFile.txt", "w") #Should create a filed called Test/File.txt in the folder Saved Files

for i in range(3): #writes into file
    if i == 0:
        f.write("Insert name here\n")
    else:
        f.write("{}\n".format(i))

f.close() #good to always close files

#A test to figure out the best way to read a file
f = open("Saved Files/TestFile.txt","r")
count = 0 #0 = name, 1 = health, 2 = defence
for line in f:
    if count == 0:
        print("NAME: {}".format(line.strip()))
        count+=1 #increments by one to indicate different representation
    elif count == 1:
        print("Health: {}".format(line.strip()))
        count+=1
    else: #must be 2/defence otherwise
        print("Defense: {}".format(line.strip()))

f.close()