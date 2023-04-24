# Set the file path
file_path = r'H:\BugBounty Progrmes\tragets\altibbi.com\Xss1.txt'


# Read the file and decode it using UTF-8
with open(file_path, 'r', encoding='utf-8') as file:
    file_text = file.read()

# Replace "document.cookie" with "1"
new_text = file_text.replace("document.cookie", "1")

# Write the new text to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_text)
