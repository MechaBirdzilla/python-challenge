# import library
import csv

# define location of csv file
budgetdata_csv = "./Resources/budget_data.csv"

def write(line):
    with open("results.txt", "a") as outfile:
        print(line)
        print(line, file=outfile)

# open csv file with "," as delimiter
with open(budgetdata_csv,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # remove header from the data
    header = next(csvreader)

    # set initial variable values and set up an array for changes
    months = 0
    total = 0
    changes = []
    previous_profit = None
    min_profit = None
    max_profit = None


    # set for loop in csv file
    for row in csvreader:
        # count each row
        months = months + 1
        # sum each rows profit/loss
        total = total + int(row[1])
        # if previous profit has a value assigned, append difference to the changes array. 
        if previous_profit != None:
            difference = int(row[1]) - previous_profit
            changes.append(difference)
            # store for each row if the difference is min or max profit and change values if appropriate
            if min_profit == None or difference < min_profit[1]:
                min_profit = (row[0], difference)
                
                
            if max_profit == None or difference > max_profit[1]:
                max_profit = (row[0], difference)
             
        # Store the current row for the next loop    
        previous_profit = int(row[1])
       
# Print the data 
write("Financial Analysis")
write("---------------------------------------")
write("Total Months: " + str(months))
write("Total: $" + str(total))
write("Average Change: $" + str(round(sum(changes) / len(changes),2)))
write("Greatest Increase in Profits: " + max_profit[0] + " ($" + str(max_profit[1]) + ")")
write("Greatest Decrease in Profits: " + min_profit[0] + " ($" + str(min_profit[1]) + ")") 
