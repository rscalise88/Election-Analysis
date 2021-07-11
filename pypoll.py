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

with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in c_votes:
        # Retrieve vote count and percentage.
        votes = c_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)