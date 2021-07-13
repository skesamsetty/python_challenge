# import required modules
import pathlib  # Allows to create path to data files
import csv      # Allows to read and create data from csv files

# Header title and formatting line for the report
header_line=f"Election Results"
dash_line="--------------------------------------------------"

# Defines 2 lists to store the list of candidates and
#   to store count of votes each candidate received.
candidates_list=[]
vote_count_list=[]

# Setting up some initial values for data elements
total_votes=0
max_votes = 0
winner = ""

# set path to be able to access and read electoral polling data.
poll_data_file_path = pathlib.Path('Resources/election_data.csv')

with open(poll_data_file_path, newline='') as poll_data_file:

    # CSV reader specifies delimiter and variable that holds contents
    poll_reader = csv.reader(poll_data_file, delimiter=',')

    # Read the header row first as there is column header in the csv file 
    #   (skip this step if there is now header)
    poll_header = next(poll_reader)    

    # Loop through each Voter row to perform required operations & generate report
    for row in poll_reader:

        total_votes += 1

        # If candidate is not already part of candidate list, add the candidate and
        #   initialize the corresponding vote count to zero.
        #   Vote count to zero because its the first time, candidate is appearing in the poll 

        if not candidates_list.__contains__(row[2]):
            candidates_list.append(row[2])
            vote_count_list.append(0)

        # For every vote, locate the position of candidate in the candidate list, 
        #   add the vote to the candidates vote count.
        candidate_pos=candidates_list.index(row[2])
        vote_count_list[candidate_pos] += 1

    # Set path to store the electoral results in Text file.
    poll_result_file_path = pathlib.Path('Analysis/poll_results.txt')
    with open(poll_result_file_path,'w') as poll_result_file:
        
        # Formatting and Header line for Terminal and Text file
        print(dash_line + "\n" + header_line + "\n" + dash_line)
        poll_result_file.write(dash_line + "\n" + header_line + "\n" + dash_line)

        # Form one total votes line and use the same string to print on terminal and 
        #   to write into text file
        total_vote_line=f"Total Votes: {total_votes}"

        print(total_vote_line + "\n" + dash_line)
        poll_result_file.write("\n" + total_vote_line + "\n" + dash_line)

        # For each candidate in the candidate list, print the vote counts and percantage of votes received
        for candidate in range(len(candidates_list)):

            vote_percent = round((vote_count_list[candidate]/total_votes)*100,3)
            candidate_line = f"{candidates_list[candidate]}: {vote_percent:.3f}% ({vote_count_list[candidate]})"

            print(candidate_line)
            poll_result_file.write("\n" + candidate_line)

            # Identify the winner based on maximum number of votes gained by the candidate
            if max_votes<vote_count_list[candidate]:
                max_votes=vote_count_list[candidate]
                winner=candidates_list[candidate]

        #Print and write the winner line along with formatting 
        winner_line = f"Winner: {winner}"
        print(dash_line + "\n" + winner_line + "\n" + dash_line)
        poll_result_file.write("\n" + dash_line +"\n" + winner_line + "\n" + dash_line)