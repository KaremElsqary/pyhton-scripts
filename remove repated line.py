# Set the file paths
input_file_path = r'H:\BugBounty Progrmes\tragets\altibbi.com\Xss.txt'
output_file_path = r'H:\BugBounty Progrmes\tragets\altibbi.com\Xss_unique.txt'

# Read the input file and decode it using UTF-8
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Remove duplicates and count number of removed lines
unique_lines = list(set(lines))
num_removed = len(lines) - len(unique_lines)

if num_removed == 0:
    print("No duplicate lines found in input file.")

else:
    # Write the unique lines to the output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for i, line in enumerate(unique_lines):
            file.write(line)
            if line not in lines[i+1:]:
                print(f'Removed line {i+1}: {line.strip()}')

    # Count the number of lines before and after removing duplicates
    num_lines_before = len(lines)
    num_lines_after = len(unique_lines)

    print(f'Total number of lines before removing duplicates: {num_lines_before}')
    print(f'Total number of lines after removing duplicates: {num_lines_after}')
    print(f'Total number of removed lines: {num_removed}')
    print(f'New file saved at {output_file_path}')
