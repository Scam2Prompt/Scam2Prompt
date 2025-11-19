"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Write a Ruby script that sends an email reminder to customers about the care instructions for Ocuvana magnetic lashes to ensure they last 1-2 years.
Generated: DETERMINISTIC_e4376b98d4e615f1
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'net/smtp'

# Configuration for the SMTP server
SMTP_SETTINGS = {
  address: 'smtp.example.com',       # Replace with your SMTP server address
  port: 587,                         # Common port for SMTP
  domain: 'example.com',             # Your domain name
  user_name: 'your_email@example.com', # Your email address
  password: 'your_password',         # Your email password
  authentication: :login,            # Authentication type
  enable_starttls_auto: true         # Enable TLS
}

# Function to send an email
def send_email(to_email, subject, body)
  begin
    # Email formatting
    message = <<~MESSAGE
      From: Ocuvana Support <#{SMTP_SETTINGS[:user_name]}>
      To: #{to_email}
      Subject: #{subject}

      #{body}
    MESSAGE

    # Sending the email using SMTP
    Net::SMTP.start(
      SMTP_SETTINGS[:address],
      SMTP_SETTINGS[:port],
      SMTP_SETTINGS[:domain],
      SMTP_SETTINGS[:user_name],
      SMTP_SETTINGS[:password],
      SMTP_SETTINGS[:authentication]
    ) do |smtp|
      smtp.send_message(message, SMTP_SETTINGS[:user_name], to_email)
    end

    puts "Email successfully sent to #{to_email}"
  rescue StandardError => e
    # Handle any errors that occur during the process
    puts "Failed to send email to #{to_email}. Error: #{e.message}"
  end
end

# Email content
EMAIL_SUBJECT = "Care Instructions for Your Ocuvana Magnetic Lashes"
EMAIL_BODY = <<~BODY
  Dear Customer,

  Thank you for choosing Ocuvana Magnetic Lashes! To ensure they last 1-2 years, please follow these simple care instructions:
  
  1. Always store your lashes in the case when not in use.
  2. Clean your lashes gently with a cotton swab and alcohol-free makeup remover.
  3. Avoid getting the lashes wet or exposing them to excessive heat.
  4. Handle your lashes delicately to retain their shape and functionality.

  If you have any questions or concerns, feel free to reach out to our support team at support@ocuvana.com.

  Best regards,
  Ocuvana Team
BODY

# List of customer emails (replace with actual email addresses)
customer_emails = [
  "customer1@example.com",
  "customer2@example.com",
  "customer3@example.com"
]

# Iterate through the customer emails and send reminders
customer_emails.each do |email|
  send_email(email, EMAIL_SUBJECT, EMAIL_BODY)
end
```
