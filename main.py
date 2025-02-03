import json
import csv


def json_to_csv():
    # Read JSON data from the input file
    with open('input.json', 'r') as json_file:
        data = json.load(json_file)

    # Specify the CSV output file
    csv_file = 'output.csv'

    # Extract the header (column names) from the first JSON object
    header = list(data[0].keys())

    # Open the CSV file and write the header
    with open(csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)

        # Write the data from the JSON file to the CSV file
        for row in data:
            csv_writer.writerow(row.values())

    print(f'JSON data has been successfully converted to CSV and saved as output.csv')


def csv_to_json():
    
    # Specify the CSV input file and JSON output file
    csv_file = 'input.csv'
    json_file = 'output.json'

    # Initialize an empty list to store the JSON data
    json_data = []

    # Open the CSV file and read its contents
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert each row (dictionary) in the CSV to JSON and append it to the list
        for row in csv_reader:
            json_data.append(row)

    # Write the JSON data to the output file
    with open(json_file, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f'CSV data has been successfully converted to JSON and saved as {json_file}.')


if __name__ == '__main__':
    print("Hello User , What operation you want to conduct in here ?")
    print("1 . JSON to CSV")
    print("2 . CSV to JSON") 
    choice = int(input())
    if(choice == 1):
         json_to_csv()
    elif(choice == 2):
        csv_to_json()
    else:
        exit

#here are some minor changes