import os

# Define path of the input file
input_file = r'H:\BugBounty Progrmes\tragets\altibbi.com\paramiter.txt'

# Define the keyword to search for in each line
keyword = '>'

# Define path of the output file for removed lines
removed_file = r'H:\BugBounty Progrmes\tragets\altibbi.com\Xss1_removed.txt'

# Open the input file in read mode with utf-8 encoding
with open(input_file, 'r', encoding='utf-8') as f_input:

    # Open the output file in write mode with utf-8 encoding for non-removed lines
    with open(input_file + '.tmp', 'w', encoding='utf-8') as f_output:

        # Open the removed lines file in write mode with utf-8 encoding
        with open(removed_file, 'w', encoding='utf-8') as f_removed:

            # Loop over each line in the input file
            for line in f_input:

                # Check if the keyword is in the line
                if keyword not in line:

                    # Write the line to the removed lines file if the keyword is found
                    f_removed.write(line)

                else:

                    # Write the line to the input file if the keyword is not found
                    f_output.write(line)

# Remove the original input file
os.remove(input_file)

# Rename the temporary output file to the input file name
os.rename(input_file + '.tmp', input_file)

# Print a message to indicate the code has finished running
print('Done!')
