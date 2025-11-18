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
require 'mail'

# Configuration for email settings
Mail.defaults do
  delivery_method :smtp, {
    address:              'smtp.example.com',     # Replace with your SMTP server
    port:                 587,                   # Common SMTP port
    user_name:            'your_email@example.com', # Replace with your email
    password:             'your_password',       # Replace with your email password
    authentication:       :plain,
    enable_starttls_auto: true
  }
end

# Function to send an email notification for promotion
def send_promotion_email(recipient_email, product_name, promotion_details)
  begin
    # Create email
    mail = Mail.new do
      from    'your_email@example.com'          # Sender email
      to      recipient_email                   # Recipient email
      subject "Promotion on #{product_name}!"   # Email subject
      body    <<~EMAIL_BODY                     # Email body
        Hello,

        Great news! There's a new promotion on "#{product_name}".
        Promotion Details:
        #{promotion_details}

        Don't miss out on this amazing deal!

        Best regards,
        Your Friendly Store
      EMAIL_BODY
    end

    # Send email
    mail.deliver!
    puts "Promotion email sent successfully to #{recipient_email}."
  rescue StandardError => e
    # Handle errors gracefully
    puts "Failed to send email. Error: #{e.message}"
  end
end

# Example usage
# Replace with actual data or integrate with a product promotion system
recipient_email = 'customer@example.com'                # Replace with recipient's email
product_name = 'Milly Mally Pojazd na akumulator Audi R8 Spyder White' # Product name
promotion_details = '20% off until October 15th!'       # Promotion details

# Send the promotion email
send_promotion_email(recipient_email, product_name, promotion_details)
```
