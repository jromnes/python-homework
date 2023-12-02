
import csv
import os
from pathlib import Path

Path.cwd()



csvpath = os.path.join("/Users/jordanromnes/Desktop/python-challenge/Pybank/budget_data.csv")



total_months = 0
total_profit_losses = 0
changes_in_profit_losses = []
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader, None)
    previous_profit_loss = None
    
    for row in csvreader:
        total_months += 1
        total_profit_losses += int(row[1])
        profit_loss = int(row[1])
        if previous_profit_loss is not None:
            change_in_profit_loss = profit_loss - previous_profit_loss
            changes_in_profit_losses.append(change_in_profit_loss)

        if profit_loss > greatest_increase_amount:
            greatest_increase_amount = profit_loss
            greatest_increase_date = row[1]
        if profit_loss < greatest_decrease_amount:
            greatest_decrease_amount = profit_loss
            greatest_decrease_date = row[1]

        previous_profit_loss = profit_loss
average_change = sum(changes_in_profit_losses) / (total_months - 1)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

output_file_path = 'financial_analysis_results.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

print(f"Results exported to {output_file_path}")