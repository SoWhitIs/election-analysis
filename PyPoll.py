
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
 #Path-"C:\Users\whdlgr\Documents\course_work\AnalysisProjects\ElectionAnalysis\Resources\election_results.csv"

 # Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Print the file object.
    print(election_data)
 
 # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

  # Write three counties to the file.
       txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Open the election results and read the file.
candidate_options =[]
 # Declare the empty dictionary
candidate_votes = {}
 
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
      
    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
      # Add to the total vote count.
      total_votes += 1

      # Print the candidate name from each row.
      candidate_name = row[2]

        # If the candidate does not match any existing candidate...
      if candidate_name not in candidate_options:
            # 1. Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0
            # 3. Add a vote to that candiadte's count. 
      candidate_votes[candidate_name] += 1
        
# Print the candidate list.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name, vote count, and percentage of votes. 
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Determine the percentage of votes for each cadidate by looping through the counts.
# Interate through the candidate list
if (votes > winning_count) and (vote_percentage > winning_percentage):
      # if true then set winning_count = votes and winning_percent =
      # vote_percentage.
      winning_count = votes
      winning_percentage = vote_percentage
      # Set the winning_count to the variable, candidate's name
      winning_count = candidate_name
winning_candidate_summary =(
  f"-------------------------\n"
  f"Winner: {winning_candidate}\n"
  f"Winning Vote Count: {winning_count:,}\n"
  f"Winning Percentage: {winning_percentage:.1f}%\n"
  f"-------------------------\n")
print(winning_candidate_summary)