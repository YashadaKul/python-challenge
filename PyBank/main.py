#Import necessary modules:
import os
import csv
#Set the path for the file:
PyBank = os.path.join('Resources', 'budget_data.csv' )
PyBank
#Open the csv file:
with open(PyBank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")

    #create variables
    Dates = []
    Amount = []
    month_number = 0
    total_net_profit = 0
    res_list = []
    changes = []
    sum_changes = 0

    #create a for loop to get the number of months, net profit/loss and to create lists of date and amount. 
    for row in csvreader:
        #Count the number of months. 
        month_number += 1
        #calculate the net profit/loss
        total_net_profit += int((row[1]))
        #make lists of date and amount
        Dates.append(row[0])
        Amount.append(row[1])

    #convert data type of Amount to integer:
    print(f"Data type of Amount is: {type(Amount[1])}")
    for i in range(0, len(Amount)):
        Amount[i] = int(Amount[i])
    print(f"Data type of Amount is: {type(Amount[1])}")

    #Populate an object with changes in profit/loss:
    for j in range(0, len(Amount)-1):
        changes.append(Amount[j+1] - Amount[j]) 
    
    #Calculate the average change:
    for k in changes:
        sum_changes = sum_changes + k

    average_change = sum_changes/(len(Amount)- 1)
    
    print(f"Average change: {average_change}")
  
    #greatest increase in profits:
    greatest_increase = max(changes)
    print(greatest_increase)
    #Find the index of greatest_increase:
    changes.index(greatest_increase)
    #The index is 78. Thus, the month for this would be the 79th in the Dates list:
    month_greatest = Dates[79]

    #greatest decrease in profits:
    greatest_decrease = min(changes)
    print(greatest_decrease)
    changes.index(greatest_decrease)    
    month_lowest = Dates[49]


    #Printing results:
    Results = print(f"Financial Analysis \n -------------- \n Total months: {month_number} \n\n Total: {total_net_profit} \n\n Average change: {average_change} \n\n Greatest increase in profits: {month_greatest} {greatest_increase} \n\n Greatest decrease in profits: {month_lowest} {greatest_decrease}")
    

#export as a txt file
#specify the path
output_file = os.path.join('Analysis', 'analysis.txt')

#create the file
file = open(output_file, "w")

#write to the file
file.writelines(f"Financial Analysis \n -------------- \n Total months: {month_number} \n\n Total: {total_net_profit} \n\n Average change: {average_change} \n\n Greatest increase in profits: {month_greatest} {greatest_increase} \n\n Greatest decrease in profits: {month_lowest} {greatest_decrease}")
    
    


   






    
