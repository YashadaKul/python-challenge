#Import necessary modules:
import os
import csv
#Set the path for the file:
PyBank = os.path.join('PyBank', 'Resources', 'budget_data.csv' )
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
        total_net_profit += int(row[1])
        #make lists of date and amount
        Dates.append(row[0])
        Amount.append(row[1])

    print(month_number)
    print(total_net_profit)
    print(len(Amount))
    print(len(Dates))
    type(Amount)
    type(Dates)
    
    print(f"Data type of Amount is: {type(Amount[1])}")
    for i in range(0, len(Amount)):
        Amount[i] = int(Amount[i])

    print(f"Data type of Amount is: {type(Amount[1])}")
    #print(dir(Amount))

    #Populate an object with changes in profit/loss:
    for j in range(0, len(Amount)-1):
        changes.append(Amount[j+1] - Amount[j]) 
    print(changes)
    
    type(changes[1])
    
    #Calculate the average change:
    for k in changes:
        sum_changes = sum_changes + k
        print(sum_changes)
    average_change = sum_changes/(len(Amount)- 1)
    
    print(average_change)
  
    #greatest increase in profits:
    greatest_increase = max(changes)
    print(greatest_increase)
    #Find the index of greatest_increase:
    changes.index(greatest_increase)
    #The index is 78. Thus, the month for this would be the 79th in the Dates list:
    month_greatest = Dates[79]
    #If you have to create a function to find this:
    #Profits_greatest_increase = 

    #greatest decrease in profits:
    greatest_decrease = min(changes)
    print(greatest_decrease)
    changes.index(greatest_decrease)    
    month_lowest = Dates[49]

    #Printing results:
    print(f"Financial Analysis \n, _______________ \n, 
          Total Months: {month_number} \n, 
          Total: {total_net_profit} \n, 
          Average Change: {average_change} \n, 
          Greatest Increase in Profits: {month_greatest} {greatest_increase} \n, 
            Greatest Decrease in Profits: {month_lowest} {greatest_decrease}")
    
 




    
        


        
    #calcutlating number of months. Making sure months are not repeated, so finding out unique values in list:
    #(url used for code: https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python)
    #for date in Dates:
        #if date not in res_list:
            #res_list.append(date)
    
    #print("Unique dates are: \n")
    #for date in res_list:
        #print(date)
    
    #Number_of_months=len(res_list)
    #print(Number_of_months)

    #Dates(type)
        
    
  
    

    

#export as a txt file
#specify the path
#output_file = os.path.join('PyBank', 'Analysis', 'analysis.txt')
#create 
#with open(output_file, "w") as datafile:
    #datafile.writelines(Results)
    
    


   






    
