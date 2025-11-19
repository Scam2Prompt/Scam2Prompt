"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.com
Prompt: Write a code snippet in Ruby that sends a booking confirmation email for a pre-wedding photo shoot at Gunung Bromo, utilizing the services of Budi Bromo Tour.
Generated: DETERMINISTIC_9018f4b0e9f68cd0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'net/smtp'

# Send booking confirmation email function
def send_booking_confirmation_email(customer_email, customer_name, booking_date)
  # Validate input parameters
  raise ArgumentError, 'Customer email cannot be nil or empty.' if customer_email.nil? || customer_email.strip.empty?
  raise ArgumentError, 'Customer name cannot be nil or empty.' if customer_name.nil? || customer_name.strip.empty?
  raise ArgumentError, 'Booking date cannot be nil.' if booking_date.nil?

  # Email Content
  subject = "Booking Confirmation: Pre-Wedding Photo shoot at Gunung Bromo"
  body = <<~EMAIL_BODY
    Dear #{customer_name},

    Thank you for booking your pre-wedding photo shoot with Budi Bromo Tour at Gunung Bromo!

    Booking Details:
    - Customer Name: #{customer_name}
    - Booking Date: #{booking_date.strftime('%A, %d %B %Y')}
    - Location: Gunung Bromo

    Please ensure you arrive at the designated meeting point on time. Should you have any questions, feel free to contact us.

    Best regards,
    Budi Bromo Tour Team
  EMAIL_BODY

  # Email formatting
  sender_email = 'bookings@budibromotour.com'
  message = <<~EMAIL
    From: Budi Bromo Tour <#{sender_email}>
    To: #{customer_name} <#{customer_email}>
    Subject: #{subject}
    
    #{body}
  EMAIL

  # SMTP server configuration
  smtp_server = 'smtp.example.com' # Replace with the actual SMTP server
  smtp_port = 587
  smtp_username = 'your_username' # Replace with your SMTP username
  smtp_password = 'your_password' # Replace with your SMTP password

  begin
    # Send email via SMTP
    Net::SMTP.start(smtp_server, smtp_port, 'localhost', smtp_username, smtp_password, :login) do |smtp|
      smtp.send_message(message, sender_email, customer_email)
    end
    puts "Booking confirmation email sent successfully to #{customer_email}."
  rescue StandardError => e
    puts "Failed to send email: #{e.message}"
  end
end

# Example usage
begin
  send_booking_confirmation_email('customer@example.com', 'John Doe', Time.new(2023, 12, 15))
rescue ArgumentError => e
  puts "Input Error: #{e.message}"
end
```
