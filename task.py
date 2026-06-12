import re

# Read the source text file
with open("input.txt", "r") as file:
    content = file.read()

# Regular expression to find email addresses
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

# Save extracted emails to a new file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print(f"{len(emails)} email(s) extracted and saved to 'emails.txt'.")