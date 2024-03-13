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

    Dates = []
    Amount = []
    #create a new empty list
    res_list = []


    for row in csvreader:
        #Make a list of the dates and amount
        Dates.append(row[0])
        Amount.append(row[1])
        
    #calcutlating number of months. Making sure months are not repeated, so finding out unique values in list:
    #(url used for code: https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python)
    for date in Dates:
        if date not in res_list:
            res_list.append(date)
    
    print("Unique dates are: \n")
    for date in res_list:
        print(date)
    
    Number_of_months=len(res_list)
    print(Number_of_months)
        


    

#export as a txt file
#specify the path
output_file = os.path.join('PyBank', 'Analysis', 'analysis.txt')
#create 
with open(output_file, "w") as datafile:
    datafile.writelines = (["results1", "results2"])
    
    


   






    
