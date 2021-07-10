import os
import csv

# csvpath = os.path.join('..', 'Resources', 'accounting.csv')
csvpath = "Resources/election_data.csv"

total = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
maxVotes = 0
candidate = {}
winner = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(csv_header)

  
    # Read each row of data after the header
    for row in csvreader:
        total += 1

        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O\'Tooley":
            OTooley_votes += 1   

    print(f'khan= {Khan_votes}')
    print(f"Correy= {Correy_votes}")
    print(f"Li= {Li_votes}")
    print(f"OTooley= {OTooley_votes}")
    print(f"Total Votes= {total}")

# find the percentage of votes
    percentage = (Khan_votes/total)*100
    percentage1 = (Correy_votes/total)*100
    percentage2 = (Li_votes/total)*100
    percentage3 = (OTooley_votes/total)*100
    print(f"Khan%= {percentage}")
    print(f"Correy%= {percentage1}")
    print(f"Li%= {percentage2}")
    print(f"O'Tooley%= {percentage3}")
# Winner of the election

input =[Khan_votes,Correy_votes,Li_votes,OTooley_votes]
# winner(input)
