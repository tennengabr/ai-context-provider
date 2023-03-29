#!/usr/bin/env python3

import argparse
import json
import re

print("Generating AI context... \n")

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='config.json', help='Path to the config file')
args = parser.parse_args()

# Read the config file
try:
    with open(args.config, 'r') as f:
        config = json.load(f)
    print(f"Config file found: {args.config}")
except FileNotFoundError:
    print(f"Error: Config file not found {args.config}")
    exit(1)

# Process each file in the config
print("Retrieving file data...")
for file in config['files']:
    try:
        # Read the contents of the code file
        with open(file['name'], 'r') as f:
            file_data = f.read()
         # Remove all lines that begin with # or //
        # file_data = re.sub(r'^(#|//).*\n?', '', file_data, flags=re.MULTILINE)
        file_data = re.sub(r'(#|//).*', '', file_data)
        # Update the data field in the config with the code file data and remove unecessary spaces
        file['data'] = re.sub(r'\s{2,}', ' ', file_data)
        print(f"File found: {file['name']}")
    except FileNotFoundError:
        print(f"Error: File not found {file['name']}")
print("Finished retrieving file data... \n")

# Write the updated config to a new JSON file
print("Uploading file data...")
try:
    with open('output.json', 'w') as f:
        json.dump(config, f, indent=2)
    print(f"File data uploaded: output.json")
except Exception as e:
    print(f"Error: File output.json data failed to upload. Reason: {e}")
print("Finished uploading file data. \n")


print("Finished generating AI context...")
