import csv
import json

def convert_csv_to_json(input_file, output_file):
    data = []
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    convert_csv_to_json('profiles1.csv', 'data.json')
