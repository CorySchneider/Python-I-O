#This program reads a file, takes the average, minimum, and maximum, of tickets
#CISI1400
#Python File IO HW
#Cory Schneider

import os

#Open and read file
userchoice = input("Enter a filename: ").strip()
infile = open("userchoice", "r")
if  os.path.isfile("userchoice"):

    s = infile.read()

    tickets = [eval('x') for x in s.split()]


#Open and write on output file
output_file = open("output.txt", "w")
    
for line in userchoice:
    output_file.write(line + "\n")
    output_file.write("hello")
