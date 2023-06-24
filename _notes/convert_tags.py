import re

# Define the regular expression pattern to match the tags
pattern = r'#([\w/]+)'

# Define the replacement pattern
replacement = r'[[\1]]'

# Read the markdown document from a file
input_file = '01 Master of Medical Education Bern (MME).md'
with open(input_file, 'r') as file:
    markdown_text = file.read()

# Use re.sub() to replace the tags with the desired format
converted_text = re.sub(pattern, replacement, markdown_text)

# Specify the output file name
output_file = '01 Master of Medical Education Bern (MME)2.md'

# Save the converted text to the output file
with open(output_file, 'w') as file:
    file.write(converted_text)

print(f"Conversion complete. Converted content saved to '{output_file}'.")
