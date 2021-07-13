""" This object analyzes the bank transaction Profit/losses.
    Writes analysis information into Terminal and 
    also creates a text file
"""
# import required modules
import pathlib  # Allows to create path to data files
import csv      # Allows to read and create data from csv files

header_line=f"    Financial Analysis of Bank Transactions"
dash_line=f"--------------------------------------------------"

budget_file_path = pathlib.Path('Resources/budget_data.csv')

with open(budget_file_path, newline='') as budget_file:
    # CSV reader specifies delimiter and variable that holds contents
    budget_reader = csv.reader(budget_file, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    budget_header = next(budget_reader)

    row_count=0
    transaction_total=0
    first_iteration=True
    change = 0
    change_total = 0
    average_change = 0.0
    max_month = ''
    min_month = ''

    # Read each row of data after the header
    for row in budget_reader:

        # Loop through each Bank transaction row to check tha count
        row_count=row_count + 1
        transaction_total=transaction_total + int(row[1])
        
        if first_iteration:
            # Set all initial values in the first iteration
            first_iteration=False
            change=0
            change_total = 0
            max_change=0
            min_change=0
            previous_transaction_amount=int(row[1])
            current_transaction_amount = 0
        else:
            current_transaction_amount=int(row[1])
            change=current_transaction_amount - previous_transaction_amount
            change_total += change
            previous_transaction_amount = current_transaction_amount
        
        # Identify maximum increase in the profit change
        if max_change < change:
            max_change=change
            max_month = row[0]
        
        # Identify minimum increase in the profit change
        if min_change > change:
            min_change=change
            min_month=row[0]

    # Since the number of changes are going to be 1 less than the total records,
    # for average change calculation, I am subtracting 1 from row count.
    average_change=round((change_total / (row_count - 1)),2)

# Calculate required KPIs
total_months_line=f"Total Months: {row_count}"
transaction_total_line=f"Total: ${transaction_total}"
average_change_line=f"Average Change: ${average_change:.2f}"
max_increase_line=f"Greatest Increase in Profits: {max_month} (${max_change})"
min_increase_line=f"Greatest Decrease in Profits: {min_month} (${min_change})"

# Load data into List to print to terminal and to write to file
lines=[total_months_line, transaction_total_line, average_change_line,
        max_increase_line, min_increase_line]

# Write to file and print to terminal together
output_file_path = pathlib.Path('Analysis/FinancialAnalysis.txt')

with open(output_file_path, 'w') as export_file:

    export_file.write(dash_line + "\n" + header_line + "\n" + dash_line + "\n")
    print(dash_line + "\n" + header_line + "\n" + dash_line)
    
    for line in lines:
        export_file.write(line + "\n")
        print(line)
        
    export_file.write(dash_line)
    print(dash_line)