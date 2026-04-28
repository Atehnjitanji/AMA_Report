import  re
import csv
from Cleaning import *

#TODO: add to this program
    # clean the data using your functions 
    # write the cleaned data into a new csv file (optional but helpful for next step)
    # put the cleaned data into a dataframe
    #    - use your cereal_analysis python file as a template to read from csv

with open('alumni_anonymized.csv') as records:
    reader = csv.reader(records)
    entries = [] #this will store the rows in dictionary form
    next(reader)  #skip header
    count = 0
    for row in reader:
        new_row = dict()
        if year_format(row[1]) == '' or row[0] == '' or row[3] == '' or just_year(row[4]) == '':
            continue
        if just_year(row[4]) > year_format(row[1]):
            continue
        new_row['Exit_Year'] = year_format(row[1])
        new_row['Last_Name'] = row[0]
        new_row['Id'] = row[3]
        new_row['Birth_Year'] = just_year(row[4])
        entries.append(new_row)
        #count+=1

with open('alumni_clean.csv', 'w', newline='') as new_file:
    csv_writer = csv.DictWriter(new_file,fieldnames=['Last_Name','Exit_Year','Id','Birth_Year'])
    csv_writer.writeheader()
    csv_writer.writerows(entries)
