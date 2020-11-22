import os

import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")



#List funcitons 

total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for c in range(len(total_profit)-1):

         monthly_profit_change.append(total_profit[c+1]-total_profit[c])


  #The greatest increase in profits (date and amount) over the entire period
max_increase_value = max(monthly_profit_change)
  # The greatest decrease in losses (date and amount) over the entire period
max_decrease_value = min(monthly_profit_change)


max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


output_path = os.path.join("analysis", "budget_analysis.txt")

with open(output_path, "w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
