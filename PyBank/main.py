import os
import csv

# csvpath = os.path.join('..', 'Resources', 'accounting.csv')
csvpath = "Resources/budget_data.csv"
print
total = 0
monthstotal = 0
average = 0
changeTotal = 0
greatestIncrease = 0
greatestDecrease = 0
greatestIncreaseDate = ""
greatestDecreateDate = ""
previousBudget = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(csv_header)

    change = 0
    changeCount = 0
    
    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total = total + int(row[1])
        monthstotal = monthstotal + 1

        CurrentBudget = int(row[1])
        
        if previousBudget != 0:
            change = CurrentBudget - previousBudget
            changeTotal += change
            changeCount += 1

        previousBudget = CurrentBudget          

        if change > greatestIncrease:
            greatestIncrease = change
            greatestIncreaseDate = row[0]

        if change < greatestDecrease:
            greatestDecrease= change
            greatestDecreaseDate = row[0]  

   
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {monthstotal}\n"
    f"Total: ${total:,}\n"
    f"Average  Change: ${changeTotal/changeCount:.2f}\n"
    f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease:,})\n"
    f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease:,})\n")
    
print(output)


# Write to text file

with open("pybank_result.txt", "w") as text:
    text.write ("Pybank")
    text.write ('-------------------------------------------------')
    text.write ("Total months: " + str(monthstotal))
    text.write ("Total profit: " + "$" + str(total))
    text.write ("Average change: " + "$" + str(int(changeTotal)))
    text.write ("Greatest increase in profit: " + str(greatestIncreaseDate) + ", " + "$" + str(greatestIncrease))
    text.write ("Greatest decrease in profit: " + str(greatestDecreaseDate) + ", " + "$" + str(greatestDecrease))
    text.write ('-------------------------------------------------')
