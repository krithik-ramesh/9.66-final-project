import pandas as pd 
import json 
import contextlib
import re
import io
from tqdm import tqdm

# Load the CSV data (replace with your file path)
file_path = 'data_emnlp_final/data_06b8f2a1/2.2,2.3_train.csv'
df = pd.read_csv(file_path)

# Load the JSON data from the file
file_path = 'clutrr_pyro_code_results_with_gender_GPT4_turbo_v5.json'

# Reading the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract just the Pyro code from each entry
pyro_codes = [entry['pyro_code'] for entry in data if 'pyro_code' in entry]


# Extracting only the Python code from the pyro_code field in each entry of the JSON data
python_codes = []

for entry in tqdm(pyro_codes, desc="extracting python code"):
    if entry is not None:
        # Check for both types of code block markers
        start_code = entry.find("```python")
        if start_code == -1:
            # If ```python not found, look for just ```
            start_code = entry.find("```")
            code_block_marker_length = len("```")
        else:
            code_block_marker_length = len("```python")

        end_code = entry.find("```", start_code + code_block_marker_length)

        if start_code != -1 and end_code != -1 and end_code > start_code:
            # Extract the Python code
            python_code = entry[start_code + code_block_marker_length:end_code].strip()
            python_codes.append(python_code)
        else: 
            python_codes.append("NO CODE") 

    else:
        python_codes.append("NO CODE") 


# Display the first few Python codes for verification


# Add columns for the GPT Pyro response and correctness
df['GPT_pyro_response'] = None
df['correct'] = 0  # Initialize the 'correct' column with 0

for i, (code, target) in enumerate(zip(tqdm(python_codes, desc="Running and Evaluating Extracted Code"), df['target'])):
    # Modify the code to return the most likely relationship
    modified_code = code + '\nmost_likely_relationship'

    # Execute the script and capture the output
    try:
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            exec(modified_code)
            output = buf.getvalue().strip()
        # Use regex to extract the relationship from the output
        df.at[i, 'GPT_pyro_response'] = output
        df.at[i, 'correct'] = int(target in output)
    except Exception as e:
        print(e)
        df.at[i, 'GPT_pyro_response'] = 'Error'
        df.at[i, 'correct'] = 0

# Save the results to a new CSV file
output_csv_path = 'clutrr_results.csv'  # Replace with your desired output path
df.to_csv(output_csv_path, index=False)