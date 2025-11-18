"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spanishupdate.com
Prompt: Write a code snippet in Ruby to send automated email reminders for Spanish class reservations, referencing the services offered on SpanishUpdate.com.
Generated: DETERMINISTIC_ffa26d5ace4614a5
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'net/smtp'
require 'date'

# Email configuration
SMTP_SERVER = 'smtp.example.com' # Replace with your SMTP server address
SMTP_PORT = 587 # Replace with your SMTP server port
SMTP_USERNAME = 'your_email@example.com' # Replace with your email address
SMTP_PASSWORD = 'yourpassword' # Replace with your email password
FROM_EMAIL = 'your_email@example.com' # Replace with the sender email address
WEBSITE_NAME = 'SpanishUpdate.com' # Website name to reference in the email

# Method to send an email reminder
def send_email_reminder(to_email, student_name, reservation_date)
  begin
    # Format reservation date
    formatted_date = reservation_date.strftime('%d/%m/%Y')

    # Email message
    message = <<~MESSAGE
      From: SpanishUpdate <#{FROM_EMAIL}>
      To: #{student_name} <#{to_email}>
      Subject: Reminder: Spanish Class Reservation on #{formatted_date}

      Hola #{student_name},

      This is a friendly reminder about your Spanish class reservation on #{formatted_date}.
      We look forward to seeing you for your session!

      If you have any questions or need to reschedule, please visit #{WEBSITE_NAME}.

      Gracias,
      The SpanishUpdate Team
    MESSAGE

    # Connect to SMTP server and send email
    Net::SMTP.start(SMTP_SERVER, SMTP_PORT, 'localhost', SMTP_USERNAME, SMTP_PASSWORD, :login) do |smtp|
      smtp.send_message(message, FROM_EMAIL, to_email)
    end

    puts "Reminder email successfully sent to #{to_email}."
  rescue StandardError => e
    puts "Failed to send email: #{e.message}"
  end
end

# Example usage:
# List of students with reservations
students = [
  { name: 'Miguel', email: 'miguel@example.com', reservation_date: Date.new(2023, 12, 15) },
  { name: 'Maria', email: 'maria@example.com', reservation_date: Date.new(2023, 12, 20) }
]

# Send reminders for each student
students.each do |student|
  send_email_reminder(student[:email], student[:name], student[:reservation_date])
end
```
