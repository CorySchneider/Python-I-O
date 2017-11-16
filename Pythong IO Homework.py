#This program reads a file, takes the average, minimum, and maximum, of tickets
#CISI1400
#Python File IO HW
#Cory Schneider
import os

userchoice = input("Enter a filename: ").strip()

if os.path.isfile(userchoice):
    infile = open(userchoice, "r")
    s = infile.read()
    tickets = [eval('x') for x in s.split()]
    sum_a = []
    for i in tickets:
        try:
            sum_a.append(float(i))
        except ValueError:
            next
    print("**********************************")
    print("          TICKET REPORT           ")
    print("**********************************")
    print("\nThere are ",len(tickets)," tickets in the database.\n")
    print("Maximum Ticket price is $",max(sum_a))
    print("Minimum Ticket price is $",min(sum_a))
    print("Average Ticket price is $","{:.2f}".format(sum(sum_a)/len(tickets)),"\n")
    print("Thank you for using our ticket system!\n")
    print("**********************************\n")
    infile.close()
else:
    print("Failed to open file")
    
output_file = open("output.txt", "w")

for line in userchoice:
    output_file.write(line + "\n")
    output_file.write("hello\n")

output_file.close()
