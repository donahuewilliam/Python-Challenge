#import
import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")
# Create list
total_Votes = 0
candidates = []
votes = []
percent_Votes = []
# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
     
        total_Votes = total_Votes + 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_index = candidates.index(row[2])
            votes.append(1)
        
        else:
            candidate_index = candidates.index(row[2])
            votes[candidate_index] = votes[candidate_index] + 1
    for vote in votes:
        percentage = round((vote/total_Votes) * 100)
        percentage = "%3f%%" %percentage
        percent_Votes.append(percentage)

    winner_index = votes.index(max(votes))
    winningCandidate = candidates[winner_index]
# Print results 
print("Election Results")
print("---------------------")
print(f"Total Votes: {str(total_Votes)}")
print("----------------------")
for c in range(len(candidates)):
    print(f"{candidates[c]}: {str(percent_Votes[c])}({str(votes[c])})")
print("---------------------------")
print(f"Winner: {winningCandidate}")
print("----------------------------")
# Export to txt file 
output_path = os.path.join("analysis","election_analysis.txt")
# Open output file 
with open(output_path, "w") as file:
    file.write ('Election Results')
    file.write('\n')
    file.write('-----------------------------')
    file.write('\n')
    file.write(f'Total Vote: {str(total_Votes)}')
    file.write('\n')
    file.write('-----------------------------')
    file.write('\n')
    for c in range(len(candidates)):
        file.write(f'{candidates[c]}: {str(percent_Votes[c])}({str(votes[c])})')
        file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'Winner: {winningCandidate}')
    file.write('\n')
    file.write('-----------------------')
