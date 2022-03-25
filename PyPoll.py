# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initiallize the vote counter
total_votes = 0
# prepare a list to get the candidate names
candidate_options = []
# prepare a dictionary to get their votes
candidate_votes = {}
# prepare holders for the winning place
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # skip the CSV file header row.
    headers = next(file_reader)
    # count the votes
    for row in file_reader:
        total_votes += 1
        # check the name of the candidate
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # get the candidate's name
            candidate_options.append(candidate_name)
            # track that candidate's votes
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


# give the vote count
# print(total_votes)
# give the names of the candidates
# print(candidate_votes)

# 3. the percentage of votes each candidate won
# check through the candidate list
for candidate_name in candidate_votes:
    #retrieve the candidate vote count
    votes = candidate_votes[candidate_name]
    #calculate the percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    #print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #determin if this candidate is winning.  Get their info if they are.
    if votes > winning_count:
        winning_candidate = candidate_name 
        winning_count = votes
        winning_percentage = vote_percentage
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# 4. the total number of votes each candidate won
# 5. The winner of the election based on popular vote.
