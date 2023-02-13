import csv
import os

fuel = ['BP', 'Mobile', 'GULL']
fuel_cost = 0

script_dir = os.path.dirname(__file__) 
csv_input_dir = "input"

abs_file_path = os.path.join(script_dir, csv_input_dir)

with open('{abs_file_path}\\amex_transaction.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row[4])
        if(fuel in row[1]):
            fuel_cost =+ row[4]
        #print(', '.join(row))

total_cost = fuel_cost
print(fuel_cost)