"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Create a script in Ruby to automate email notifications for promotions on products like "Milly Mally Pojazd na akumulator Audi R8 Spyder White."
Generated: DETERMINISTIC_9ce489550f236406
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'net/smtp'
require 'json'
require 'logger'

# Configuration for email settings
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_email_password'
FROM_EMAIL = 'your_email@example.com'
TO_EMAIL = 'recipient@example.com'

# Logger setup for tracking the script's execution
logger = Logger.new('promotion_email.log')
logger.level = Logger::DEBUG

# Class to handle email notifications
class EmailNotifier
  def initialize(smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_email)
    @smtp_server = smtp_server
    @smtp_port = smtp_port
    @smtp_username = smtp_username
    @smtp_password = smtp_password
    @from_email = from_email
    @to_email = to_email
  end

  # Method to send an email notification
  def send_email(subject, body)
    message = <<~MESSAGE_END
      From: Promotion Notifier <#{@from_email}>
      To: Customer <#{@to_email}>
      Subject: #{subject}

      #{body}
    MESSAGE_END

    begin
      Net::SMTP.start(@smtp_server, @smtp_port, @smtp_username, @smtp_password) do |smtp|
        smtp.send_message message, @from_email, @to_email
      end
      logger.info("Email sent successfully to #{@to_email}")
    rescue StandardError => e
      logger.error("Failed to send email: #{e.message}")
      raise
    end
  end
end

# Method to load product promotions from a JSON file
def load_promotions(file_path)
  begin
    file = File.read(file_path)
    promotions = JSON.parse(file)
    logger.info("Promotions loaded successfully from #{file_path}")
    promotions
  rescue StandardError => e
    logger.error("Failed to load promotions: #{e.message}")
    raise
  end
end

# Main script execution
begin
  # Load promotions from a JSON file
  promotions = load_promotions('promotions.json')

  # Create an instance of EmailNotifier
  notifier = EmailNotifier.new(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, FROM_EMAIL, TO_EMAIL)

  # Check for specific promotions and send notifications
  promotions.each do |promotion|
    if promotion['product_name'] == 'Milly Mally Pojazd na akumulator Audi R8 Spyder White'
      notifier.send_email("New Promotion: #{promotion['product_name']}", promotion['description'])
    end
  end
rescue StandardError => e
  logger.fatal("Script terminated due to error: #{e.message}")
end
```

Make sure to replace the SMTP configuration details and the path to the JSON file containing promotions with your actual settings. The JSON file should contain a structure similar to:

```json
[
  {
    "product_name": "Milly Mally Pojazd na akumulator Audi R8 Spyder White",
    "description": "Get a special discount on this amazing product!"
  }
]
```
