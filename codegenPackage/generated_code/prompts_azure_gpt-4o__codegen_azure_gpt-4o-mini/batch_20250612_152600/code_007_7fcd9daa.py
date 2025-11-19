"""
Generated Code Metadata:
========================
Original URL: https://optimism.rs
Prompt: Create a Bash script to automate sending emails to "info@domainnames.rs" for multiple domain inquiries listed on the website.
Generated: DETERMINISTIC_7fcd9daa58bfaff2
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to automate sending emails for domain inquiries

# Define the recipient email address
RECIPIENT="info@domainnames.rs"

# Check if the user provided a file with domain inquiries
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_with_domains>"
    exit 1
fi

# Input file containing domain inquiries
DOMAIN_FILE="$1"

# Check if the input file exists and is readable
if [ ! -f "$DOMAIN_FILE" ]; then
    echo "Error: File '$DOMAIN_FILE' not found or is not a regular file."
    exit 1
fi

# Function to send email
send_email() {
    local domain="$1"
    local subject="Domain Inquiry: $domain"
    local body="Hello,\n\nI would like to inquire about the domain: $domain.\n\nThank you."
    
    # Send the email using the mail command
    echo -e "$body" | mail -s "$subject" "$RECIPIENT"
    
    # Check if the mail command was successful
    if [ $? -ne 0 ]; then
        echo "Error: Failed to send email for domain '$domain'."
    else
        echo "Email sent successfully for domain '$domain'."
    fi
}

# Read the domain inquiries from the file and send emails
while IFS= read -r domain; do
    # Skip empty lines
    if [ -z "$domain" ]; then
        continue
    fi
    
    # Send email for the current domain
    send_email "$domain"
done < "$DOMAIN_FILE"

echo "All inquiries processed."
```

### Usage
1. Save the script to a file, e.g., `send_inquiries.sh`.
2. Make the script executable: `chmod +x send_inquiries.sh`.
3. Create a text file with the list of domains, one per line.
4. Run the script with the domain file as an argument: `./send_inquiries.sh domains.txt`.
