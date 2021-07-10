#Data goal
# Number of votes cast
# comprehensive list of candidates with votes
# percentage of voates for each candidate
# total votes for each candidate
# winner of election based on popular vote, not the electoral college, which is a garbage system (hello graders please enjoy my commentary)

import csv
import os
#assign variable for the file to load and the path
filetoload = os.path.join('resources','election_results.csv')
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#open results and read file
with open(filetoload) as election_data:
    file_reader = csv.reader(election_data)
    #read and print header row
    headers = next(file_reader)
    print(headers)

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txtfile:
#write to file
    txtfile.write("Counties in Election\n---------------------\nArapahoe\nDenver\nJefferson")

#close the file 
txtfile.close()


# print file object 
print(election_data)
#close the file
election_data.close()
