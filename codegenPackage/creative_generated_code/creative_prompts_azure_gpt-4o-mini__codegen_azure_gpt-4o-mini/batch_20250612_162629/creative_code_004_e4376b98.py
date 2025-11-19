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
require 'mail'

# Configure Mail gem settings
Mail.defaults do
  delivery_method :smtp, {
    address: 'smtp.example.com', # replace with your SMTP server
    port: 587,
    user_name: 'your_email@example.com', # replace with your email
    password: 'your_email_password', # replace with your email password
    authentication: 'plain',
    enable_starttls_auto: true
  }
end

# Email reminder class
class EmailReminder
  attr_accessor :customers

  # Initialize with an array of customers
  def initialize(customers)
    @customers = customers
  end

  # Method to send email reminders
  def send_reminders
    @customers.each do |customer|
      begin
        send_email(customer[:email], customer[:name])
      rescue StandardError => e
        puts "Failed to send email to #{customer[:name]} (#{customer[:email]}): #{e.message}"
      end
    end
  end

  private

  # Send individual email
  def send_email(email, name)
    mail = Mail.new do
      from    'your_email@example.com' # replace with your email
      to      email
      subject 'Care Instructions for Your Ocuvana Magnetic Lashes'
      body    "Dear #{name},\n\n" \
               "Thank you for your purchase of Ocuvana magnetic lashes! " \
               "To ensure they last for 1-2 years, please follow these care instructions:\n\n" \
               "- Gently remove lashes after use.\n" \
               "- Clean the lashes with a brush or cloth.\n" \
               "- Store them in their case to maintain shape.\n\n" \
               "We appreciate your business!\n\n" \
               "Best Regards,\n" \
               "The Ocuvana Team"
    end

    mail.deliver! # Send the email
    puts "Email sent to #{name} (#{email})"
  end
end

# List of customers with their email and name
customers = [
  { name: 'Alice Smith', email: 'alice@example.com' },
  { name: 'Bob Johnson', email: 'bob@example.com' }
]

# Create an instance of EmailReminder and send reminders
reminder = EmailReminder.new(customers)
reminder.send_reminders
```
