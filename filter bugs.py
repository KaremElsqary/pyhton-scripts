file_path = r'path/to/your/file.txt'

# Open the file for reading and writing
with open(file_path, 'r+') as f:
    # Read the contents of the file
    file_contents = f.read()

    # Replace all instances of "document.cookie" with "karem"
    updated_contents = file_contents.replace('document.cookie', 'karem')

    # Move the file pointer back to the beginning of the file
    f.seek(0)

    # Write the updated contents back to the file
    f.write(updated_contents)

    # Truncate any remaining content in the file
    f.truncate()

# Print a message to indicate that the file has been updated
print("File updated successfully.")
