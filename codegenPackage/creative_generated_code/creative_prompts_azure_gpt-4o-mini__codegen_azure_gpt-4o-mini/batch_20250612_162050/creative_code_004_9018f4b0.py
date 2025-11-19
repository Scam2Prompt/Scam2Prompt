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
require 'uri'

# Class to handle booking confirmation for photo shoots
class BookingConfirmationEmail
  attr_reader :recipient_email, :shoot_date, :tour_service

  # Initialize the booking confirmation with necessary details
  #
  # @param recipient_email [String] The email address of the recipient
  # @param shoot_date [String] The date of the photo shoot
  # @param tour_service [String] The name of the tour service provider
  def initialize(recipient_email, shoot_date, tour_service = 'Budi Bromo Tour')
    @recipient_email = recipient_email
    @shoot_date = shoot_date
    @tour_service = tour_service
  end

  # Sends the booking confirmation email
  def send_confirmation
    message = build_email_message
    smtp = setup_smtp

    # Attempt to send the email
    begin
      smtp.start do
        smtp.send_message message, 'from@example.com', @recipient_email
      end
      puts "Booking confirmation email sent to #{@recipient_email} successfully."
    rescue StandardError => e
      puts "Failed to send email: #{e.message}"
    ensure
      smtp.finish
    end
  end

  private

  # Builds the email message body
  #
  # @return [String] The formatted email message
  def build_email_message
    <<~MESSAGE
      Subject: Booking Confirmation for Your Photo Shoot
      From: Budi Bromo Tour <from@example.com>
      To: #{@recipient_email}

      Dear Valued Customer,

      Thank you for choosing #{@tour_service} for your pre-wedding photo shoot at Gunung Bromo.
      We are pleased to confirm your booking for the date: #{@shoot_date}.

      Please feel free to reach out to us for any further inquiries.

      Best Regards,
      Budi Bromo Tour Team
    MESSAGE
  end

  # Sets up the SMTP settings for sending emails
  #
  # @return [Net::SMTP] Configured SMTP object
  def setup_smtp
    smtp = Net::SMTP.new('smtp.example.com', 587) # Use your SMTP server and port
    smtp.enable_starttls # Enable STARTTLS for secure email sending
    smtp.start('example.com', 'user@example.com', 'password', :login) # Provide your SMTP authentication details
    smtp
  end
end

# Example usage of the BookingConfirmationEmail class
if __FILE__ == $0
  # Replace with actual recipient email and shoot date
  email = BookingConfirmationEmail.new('customer@example.com', '2023-10-20')
  email.send_confirmation
end
```
