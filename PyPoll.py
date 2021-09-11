# 1a-1b. The total number of votes casted
# 2a-2d. A complete list of candiates who received votes
# 3a-3f. The percentage of votes each candiate won
# 4a-4b. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

    # To do: Perform analysis.

# Assign our dependencies
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1a. initialize a vote variable-must be above the open file so its 0 each time the file opens to count everything
total_votes = 0
# 2a. initialize candidates variable to pull all candiate options using index[1]
candidate_options =[]
# 3a. initalize variable to create our dictionary that matches candidates name to their votes
candidate_votes={}
# 4a. winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
        
# open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #read header row to not count it in analysis - print to make sure its correct then delete
    headers = next(file_reader)
    
    # print each row in the csv file
    for row in file_reader:
        # 1b. increment total_votes by 1 each time to get total
        total_votes += 1
        # 2b. initialize variable to get candidate name from the rows(list) we open
        candidate_name = row[2]

        # 2c. check if candiates name has been addded to list already
        if candidate_name not in candidate_options:
            # 2d. Add new candidate if not in list
            candidate_options.append(candidate_name) 
            # 3b. create a key from unique canidates to place in our dictionary candidate_votes={} and begin tracking it. Next, add each one for that canidate so +=1
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # 3c. Go through the candidate options list to get all names existant of canidates
    for candidate_name in candidate_votes:
        # 3d. Get vote count for each candidate
        votes = candidate_votes[candidate_name]
        # 3e. Get percentage of votes (votes and total votes is typ(int) so must be converted)
        vote_percentage = float(votes) / float(total_votes) * 100
         # 3f. print candidate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal
        # 4b. determine if the votes of candidate are greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true, set winning_count = to the votes and set the winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # set winning_count = to the candidate_name in the for loop
            winning_candidate = candidate_name
    # 5. winning candidate
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    












