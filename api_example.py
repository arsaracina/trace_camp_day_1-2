import csv

with open('assignments/create_api/Kickstarter.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    rows = [row for row in csv_reader]
    print(rows[0])
