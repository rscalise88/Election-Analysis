# Election-Analysis
Python election data audit

## Project Overview
Using python, we attempt to process all of the votes cast in the recent election to determine:
  - Total voter turnout
  - Voter turnout at the county level, including each county's percentage of total voter turnout
  - The county with the highest voter turnout
  - All candidates for which votes were cast
  - Total vote count for each candidate and their share (percentage) of the total votes cast
  - The winner of the election

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code 1.58.0

## Results
The results of the election audit indicate that:
- There were 369,711 votes cast in the election
- The counties in which votes were cast were
  - Arapahoe
  - Denver
  - Jefferson
- The county-by-county breakdown of voter turnout was:
  - 24,801 votes were cast in Arapahoe County, 6.7% of the total votes
  - 306,055 votes were cast in Denver County, 82.8% of the total votes
  - 38,855 votes were cast in Jefferson County, 10.5% of the total votes
- The candidates were
  - Charles Casper Stockholm
  - Raymon Anthony Doane
  - Diana DeGette
- Each candidate's results were:
  - Charles Casper Stockholm received 23% of the vote and 85,213 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
- The winner of the election was:
  - Diana DeGette, who received 3.1% of the vote and 11,606 votes.

## Summary
As seen above, this program can be used to quickly sort through election data to quickly determine not just the outcome of an election, but provide useful data analytics beyond determining a winner.  This code could be easily manipulated to work in many other scenarios.  As currently presented, the code analyzes a local election at the country-level specifically.  An example of this:

    for county_ID in counties:
        c_votes = county_votes.get(county_ID)
        c_votes_percentage = float(c_votes) / float(total_votes) *100
        county_results = (f"{county_ID}: {c_votes_percentage:.1f}% ({c_votes:,})\n")
        
This could be modified to read data at a statewide level for a national election.  As an example:

    for state_ID in states:
        state_votes = statewide_votes.get(state_ID)
        state_votes_percentage = float(state_votes) / float(total_votes) *100
        state_results = (f"{state_ID}: {state_votes_percentage:.1f}% ({state_votes:,})\n")
        
Further, we are not restricted solely to elections for office.  This program could also be used to determine the outcome of a referendum or down-ballot measure on proposed bills, etc.  For example, where the data is processed for elected officials:

    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        
The code could be modified to read "for" and "against" votes instead of names:

    for row in reader:
        total_votes = total_votes + 1
        selection = row[2]
        if for_or_against not in selection_options:
            selection.append(selection)
            selection_votes[selection] = 0
        selection_votes[selection] += 1
        
From this we could determine the votes cast in total for "for" and "against" and further down the code, continue the modification to analyze the data for each to determine if the ballot measure passes or not my majority.
