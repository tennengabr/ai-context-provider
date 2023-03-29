import argparse
import json

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='config.json', help='Path to the config file')
args = parser.parse_args()

# Read the config file
with open(args.config, 'r') as f:
    config = json.load(f)

# Process each file in the config
for file in config['files']:
    # Read the contents of the code file
    with open(file['name'], 'r') as f:
        file_data = f.read()

    # Update the data field in the config with the code file data
    file['data'] = file_data

# Write the updated config to a new JSON file
with open('output.json', 'w') as f:
    json.dump(config, f, indent=2)