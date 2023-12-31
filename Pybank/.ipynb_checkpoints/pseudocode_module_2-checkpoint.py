# Import necessary libraries (assuming Python)
import csv
import os
# Import the necessary libraries for reading csv files


# Set the path for the csv file
csvpath = os.path.join("Pybank", "budget_data.csv")


# Initialize variables
total_months = 0
total_profit_losses = 0
changes_in_profit_losses = []
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0

# Read data from CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader, None)
    previous_profit_loss = 0
    
    for row in csvreader:
        # Calculate total number of months
        total_months += 1
        
        # Calculate total Profit/Losses
        total_profit_losses += int(row[1])
        
        # Store Profit/Loss for later change calculation
        profit_loss = int(row[1])
        change_in_profit_loss = profit_loss - previous_profit_loss
        changes_in_profit_losses.append(change_in_profit_loss)
        
        # Check for the greatest increase in profits
        if int(row[1]) > greatest_increase_amount:
            greatest_increase_amount = int(row[1])
            greatest_increase_date = row[0]
        
        # Check for the greatest decrease in losses
        if int(row[1]) < greatest_decrease_amount:
            greatest_decrease_amount = int(row[1])
            greatest_decrease_date = row[0]

# Calculate average change in Profit/Losses
average_change = sum(changes_in_profit_losses) / (total_months - 1)

# Print the financial analysis results
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