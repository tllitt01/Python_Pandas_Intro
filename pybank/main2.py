#PyBank Assignment
from pathlib import Path
import csv

#set path
csvpath = ('budget_data.csv')

#initialize variables and list
total_months = 0
net_profit_loss = 0
total_diff = 0
profit_loss = []
dates = []
max_increase_date = ""
max_increase = 0
max_decrease_date = ""
max_decrease = 0

#open file as object
with open (csvpath, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    
#iterating over object to find total months
#establishing lists for dates and profit loss 
    for row in csv_reader:
        total_months += 1
        date = row['Date']
        dates.append(date)
        pnl = int(row['PNL'])
        profit_loss.append(pnl)       
#iterating through profit/loss list to find total net pnl          
    for point in profit_loss:
        net_profit_loss += point

#making new list by iterating through profit/loss list to find differences
    diff = [profit_loss[i+1]-profit_loss[i] for i in range(len(profit_loss)-1)]
    x = len(diff)
    for value in diff:
        total_diff += value
    average = total_diff / x
    average_rounded = round(average, 2)

#deleting first entry in date list so it has same number of entries as diff
del dates[0]

#creating a dictionary making dates the key and difference the value
differences = {dates[i] : diff[i] for i in range(len(dates))}

#iterating through dictionary to find max increase/decrease in profit
for key in differences:
    if differences[key] > max_increase:
        max_increase = differences[key]
        max_increase_date = key
    if differences[key] < max_decrease:
        max_decrease = differences[key]
        max_decrease_date = key

print(f"Financial Analysis \n")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_rounded}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")
        

    
#set output path  
output = 'pybankhw.txt'

#writing to new file
with open(output, 'w') as file:
    file.write(f"Financial Analysis \n")
    file.write("--------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit_loss}\n")
    file.write(f"Average Change: ${average_rounded}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n)")
    file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n)")
        
        
            
        
        
    

    
