# JSON to CSV and CSV to JSON Converter

This Python script allows you to convert data between JSON and CSV formats. You can choose to convert JSON data to CSV or CSV data to JSON, depending on your needs.

## Usage

1. **JSON to CSV Conversion:**

   To convert JSON data to CSV, select option 1 when prompted. Provide the input JSON data in a file named `input.json` in the same directory as the script. The script will extract the data and create a CSV file named `output.csv` containing the converted data.

2. **CSV to JSON Conversion:**

   To convert CSV data to JSON, select option 2 when prompted. Provide the input CSV data in a file named `input.csv` in the same directory as the script. The script will extract the data and create a JSON file named `output.json` containing the converted data.

## File Structure

- `json_to_csv()`: Function to convert JSON data to CSV format.
- `csv_to_json()`: Function to convert CSV data to JSON format.
- `if __name__ == '__main__':`: Main script execution block.

## Input and Output Files

- **JSON to CSV Conversion:**
  - Input: `input.json` (JSON file containing data to be converted)
  - Output: `output.csv` (CSV file with converted data)

- **CSV to JSON Conversion:**
  - Input: `input.csv` (CSV file containing data to be converted)
  - Output: `output.json` (JSON file with converted data)

## Running the Script

1. Run the script in a Python environment.

2. Choose the conversion operation by entering `1` for JSON to CSV or `2` for CSV to JSON when prompted.

3. Follow the instructions and ensure the input files (`input.json` or `input.csv`) are placed in the same directory as the script.

4. The converted data will be saved in the respective output files (`output.csv` or `output.json`).

## Example

Suppose you have a JSON file named `input.json` with the following content:

```json
[
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"}
]
```

Running the script with option 1 will create an `output.csv` file with the following content:

```
Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
```

And running the script with option 2 using an `input.csv` file with the content:

```
Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
```

Will create an `output.json` file with the following content:

```json
[
    {"Name": "Alice", "Age": "30", "City": "New York"},
    {"Name": "Bob", "Age": "25", "City": "Los Angeles"}
]
```

## Notes

- Make sure the required input files are present in the same directory as the script.
- The script uses the first row of CSV data as column headers when converting from CSV to JSON. Ensure that your CSV file has a header row.
- This script can be useful for converting data between JSON and CSV formats for various data manipulation and analysis tasks.