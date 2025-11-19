"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop24.com
Prompt: Develop a Ruby script that checks for the latest airdrop guides on Airdrop24 and sends notifications to users via email.
Generated: DETERMINISTIC_d7ee098a41ab00bd
Batch ID: 20250612_161017
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.airdrop24.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```ruby
require 'net/http'
require 'uri'
require 'nokogiri'
require 'mail'

# Configuration for the script
SMTP_SETTINGS = {
  address: 'smtp.example.com',
  port: 587,
  domain: 'example.com',
  user_name: 'your_email@example.com',
  password: 'your_password',
  authentication: 'plain',
  enable_starttls_auto: true
}

# Notification email settings
EMAIL_FROM = 'your_email@example.com'
EMAIL_SUBJECT = 'Latest Airdrop Guides from Airdrop24'

# Users to notify
USER_EMAILS = ['user1@example.com', 'user2@example.com']

# URL of the Airdrop24 website
AIRDROP24_URL = 'https://www.airdrop24.org/'

# Function to fetch the latest airdrop guides from Airdrop24
def fetch_latest_airdrop_guides
  uri = URI.parse(AIRDROP24_URL)
  response = Net::HTTP.get_response(uri)

  unless response.is_a?(Net::HTTPSuccess)
    raise "Failed to fetch airdrop guides: #{response.message}"
  end

  # Parse the response body using Nokogiri
  doc = Nokogiri::HTML(response.body)

  # Extract guides (assuming they are in <a> tags within a specific container)
  guides = doc.css('.guide-link') # Replace '.guide-link' with the actual CSS selector for guides
  raise 'No airdrop guides found.' if guides.empty?

  # Extract the title and URL for each guide
  guides.map { |guide| { title: guide.text.strip, url: guide['href'] } }
end

# Function to send notification emails
def send_notifications(guides)
  Mail.defaults do
    delivery_method :smtp, SMTP_SETTINGS
  end

  USER_EMAILS.each do |email|
    mail = Mail.new do
      from    EMAIL_FROM
      to      email
      subject EMAIL_SUBJECT
      body    build_email_body(guides)
    end

    begin
      mail.deliver!
      puts "Notification sent to #{email}"
    rescue StandardError => e
      puts "Failed to send notification to #{email}: #{e.message}"
    end
  end
end

# Helper function to build the email body
def build_email_body(guides)
  body = "Here are the latest airdrop guides from Airdrop24:\n\n"
  guides.each do |guide|
    body += "#{guide[:title]} - #{guide[:url]}\n"
  end
  body
end

# Main script execution
begin
  puts 'Fetching latest airdrop guides...'
  guides = fetch_latest_airdrop_guides

  puts 'Sending notifications...'
  send_notifications(guides)

  puts 'Done!'
rescue StandardError => e
  puts "Error: #{e.message}"
end
```
