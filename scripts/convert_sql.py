input_file = '/Users/user/Downloads/bincom_test.sql'
output_file = '/Users/user/Downloads/bincom_test_postgres.sql'

# Define replacements
replacements = {
    "int(11)": "INTEGER",
    "AUTO_INCREMENT": "SERIAL",
    "ENGINE=InnoDB": "",  # MySQL-specific storage engine, not needed in PostgreSQL
    "`": '"',  # Replace MySQL backticks with PostgreSQL double quotes
    "UNSIGNED": "",  # PostgreSQL doesn't support unsigned integers
    "DEFAULT CHARSET=latin1;": ""  # Remove MySQL charset specification
}

# Function to replace the strings
def replace_in_file(input_file, output_file, replacements):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            for old, new in replacements.items():
                line = line.replace(old, new)
            outfile.write(line)

# Call the function to apply the changes
replace_in_file(input_file, output_file, replacements)

print(f"SQL file has been successfully modified and saved to {output_file}")