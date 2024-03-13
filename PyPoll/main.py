#Import necessary modules:
import os
import csv

#Set the path for the file:
PyPoll = os.path.join('Resources', 'election_data.csv' )
PyPoll  

#Open the csv file:
with open(PyPoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")

    #Make variables
    BallotID = []
    County = []
    Candidate = []
    Total_votes = []
    List_of_candidates = []
    votes_Charles = []
    votes_Diana = []
    votes_Raymon = []
    votes_list = []
 

    #Make a list of each column:
    for row in csvreader:
        BallotID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
    
    #Find the total number of votes cast:
    Total_votes = (len(BallotID))
    print(f"Total Votes: {Total_votes}")

    #Find the unique names in candiate list to get a complete list of candidates
    for candidate in Candidate:
        if candidate not in List_of_candidates:
            List_of_candidates.append(candidate)
    
    #Print the candidate list:
    print("Candidates are: \n")
    for candidate in List_of_candidates:
        print(candidate)
    
    #total number of votes each received
    for candidate in Candidate:
        if candidate == "Charles Casper Stockham":
            votes_Charles.append(candidate)
        elif candidate == "Diana DeGette":
            votes_Diana.append(candidate)
        else: 
            votes_Raymon.append(candidate)
    
    print(f"Votes for Charles: {len(votes_Charles)}")
    print(f"Votes for Diana: {len(votes_Diana)}")
    print(f"Votes for Raymon: {len(votes_Raymon)}")

    #Calculate winner 
    #votes_list.append(len(votes_Charles), len(votes_Diana), len(votes_Raymon))
    

    votes_dict = {"Charles Casper Stockham": len(votes_Charles),
                  "Diana DeGette": len(votes_Diana),
                  "Raymon Anthony Doane": len(votes_Raymon)}
    winner = max(zip(votes_dict.values(), votes_dict.keys()))
    print(f"The winner is: {winner}")

    #Calculate percentage of votes 
    #Create a function for percentage
    def percentage(numer, denom):
        return str(numer/denom * 100) + "%"
    
    percent_charles = percentage(len(votes_Charles), Total_votes)
    print(percent_charles)
    percent_diana = percentage(len(votes_Diana), Total_votes)
    print(percent_diana)
    percent_raymon = percentage(len(votes_Raymon), Total_votes)
    print(percent_raymon)

print(f"Election Results \n, Total Votes: {Total_votes} \n, {List_of_candidates[0]}, {percent_charles}, {len(votes_Charles)} \n, {List_of_candidates[1]}, {percent_diana}, {len(votes_Diana)} \n, {List_of_candidates[2]}, {len(votes_Raymon)}, {percent_raymon}")

#Results = print(f"Total months: {month_number}, Total: {total_net_profit}, Average change: {average_change}, Greatest increase in profits: {month_greatest} {greatest_increase}, Greatest decrease in profits: {month_lowest} {greatest_decrease}" )

#export as a txt file
#specify the path
output_file = os.path.join('Analysis', 'analysis.txt')

#create the file
file = open(output_file, "w")

#write to the file
file.writelines(f"Election Results \n Total Votes: {Total_votes} \n {List_of_candidates[0]}, {percent_charles}, {len(votes_Charles)} \n {List_of_candidates[1]}, {percent_diana}, {len(votes_Diana)} \n {List_of_candidates[2]}, {len(votes_Raymon)}, {percent_raymon}")
    