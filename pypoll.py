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

#initialize vote counter
total_votes = 0

#candidates
candidates = []

#candidate's votes
c_votes = {}

# winner variable
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open results and read file
with open(filetoload) as election_data:
    file_reader = csv.reader(election_data)
    
    #read and print header row
    headers = next(file_reader)
    print(headers)
   
    #print each row in the file
    for row in file_reader:
        total_votes += 1  
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            c_votes[candidate_name] = 0
        c_votes[candidate_name] += 1



print(total_votes)
print(candidates)
print(c_votes)

# percetnage of votes
for candidate_name in c_votes:
    votes = c_votes[candidate_name]
    vote_percentage = (float(votes) / float(total_votes))*100
    if (votes > winning_count) and (vote_percentage > winning_percentage):

         winning_count = votes
         winning_percentage = vote_percentage
         winning_candidate = candidate_name    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")     

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

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
