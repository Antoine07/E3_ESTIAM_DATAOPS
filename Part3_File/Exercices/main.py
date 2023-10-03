import csv
import os
file_path = 'notes.csv'
path = os.path.abspath(file_path)


stream = open('notes.csv', 'r',  newline='')

reader = csv.reader(stream, delimiter = ';')

# print( list( reader) ) 
s = 0
counter = 0 
for line in reader:
    for column in line:
        s += int( column )
        counter += 1

print(f"la moyenne : {round(s/counter)}")

