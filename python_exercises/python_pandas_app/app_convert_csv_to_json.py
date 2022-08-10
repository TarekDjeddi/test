import csv
import json

def csv_2_json(input_csv, output_json):
    jsonList = []

    #read csv file
    with open(input_csv) as csvf:
        #load csv file using csv dictionary reader
        csvReader = csv.DictReader(csvf)

        #convert each csv row into dictin
        for row in csvReader:
            jsonList.append(row)

    with open(output_json, 'w') as jsonf:
        jsonString = json.dumps(jsonList, indent=3)
        jsonf.write(jsonString)

input_csv = r'members.csv'
output_json = r'members.json'
csv_2_json(members.csv, output_json)
