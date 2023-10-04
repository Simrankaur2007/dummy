import csv
import os
from datetime import datetime

# Determine the script directory and account file path
script_dir = os.path.dirname(os.path.abspath(__file__))
account_file_path = os.path.join(script_dir, "account_balances.txt")

# Read account balances from a text file and store them in a dictionary
account_dict = {}
with open(account_file_path, "r") as f:
    for line in f:
        acc, bal = line.strip().split("|")
        account_dict[acc] = float(bal)

# Update account balances based on interest rates
for acc, bal in account_dict.items():
    if bal > 0:
        if bal < 1000:
            rate = 0.01
        elif bal < 5000:
            rate = 0.025
        else:
            rate = 0.05
    else:
        rate = 0.1
    account_dict[acc] = bal + ((bal * rate) / 12)

# Write the updated balances to a CSV file
filename = os.path.join(script_dir, f"{datetime.now().strftime('%Y-%m-%d')}-FL.csv")
with open(filename, "w", newline="") as csvfile:
    fieldnames = ["Account", "Balance"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for acc, bal in account_dict.items():
        writer.writerow({"Account": acc, "Balance": bal})

print(f"CSV file generated: {filename}")

# Read and display the updated balances from the CSV file
with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
