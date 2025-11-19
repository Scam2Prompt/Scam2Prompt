"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Create a script in Ruby to automate email notifications for promotions on products like "Milly Mally Pojazd na akumulator Audi R8 Spyder White."
Generated: DETERMINISTIC_9ce489550f236406
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
require 'net/smtp'
require 'json'
require 'date'

# EmailNotification class to handle email notifications for product promotions
class EmailNotification
  attr_reader :smtp_server, :smtp_port, :username, :password, :from_email, :to_email

  # Initialize the EmailNotification with SMTP settings and email addresses
  def initialize(smtp_server, smtp_port, username, password, from_email, to_email)
    @smtp_server = smtp_server
    @smtp_port = smtp_port
    @username = username
    @password = password
    @from_email = from_email
    @to_email = to_email
  end

  # Send an email notification
  def send_notification(product_name, promotion_details)
    message = build_email_message(product_name, promotion_details)

    begin
      Net::SMTP.start(@smtp_server, @smtp_port, @username, @password) do |smtp|
        smtp.send_message message, @from_email, @to_email
      end
      puts "Email sent successfully for #{product_name}!"
    rescue StandardError => e
      puts "Failed to send email: #{e.message}"
    end
  end

  private

  # Build the email message
  def build_email_message(product_name, promotion_details)
    <<~MESSAGE
      From: #{@from_email}
      To: #{@to_email}
      Subject: Promotion Alert: #{product_name}

      Hello,

      We are excited to inform you about a new promotion on the following product:

      Product: #{product_name}
      Details: #{promotion_details}
      Date: #{Date.today}

      Don't miss out on this great opportunity!

      Best regards,
      Your Promotion Team
    MESSAGE
  end
end

# Configuration for SMTP and email addresses
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
USERNAME = 'your_username'
PASSWORD = 'your_password'
FROM_EMAIL = 'from@example.com'
TO_EMAIL = 'to@example.com'

# Example product and promotion details
product_name = 'Milly Mally Pojazd na akumulator Audi R8 Spyder White'
promotion_details = '20% off for the first 100 customers!'

# Create an instance of EmailNotification and send the notification
notification = EmailNotification.new(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD, FROM_EMAIL, TO_EMAIL)
notification.send_notification(product_name, promotion_details)
```
