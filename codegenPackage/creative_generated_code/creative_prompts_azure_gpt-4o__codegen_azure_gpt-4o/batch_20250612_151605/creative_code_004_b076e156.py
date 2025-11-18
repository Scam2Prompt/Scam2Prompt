"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runetech0.github.io
Prompt: Provide a step-by-step guide to integrate a "new content available" notification feature in a Jekyll blog, inspired by Rune Tech's implementation.
Generated: DETERMINISTIC_b076e15615c7d3e6
Batch ID: 20250612_151605
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-jekyll-blog.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
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
# notification_script.rb
# This Ruby script is designed to notify users when new content is published on a Jekyll blog.
# It can be configured to send notifications via email, SMS, or other external services.

require 'net/http'
require 'json'
require 'yaml'
require 'mail'

# Load configuration from a YAML file
CONFIG_FILE = "config.yml"

begin
  config = YAML.load_file(CONFIG_FILE)
rescue Errno::ENOENT => e
  puts "Error: Configuration file not found. Ensure #{CONFIG_FILE} exists."
  exit
rescue Psych::SyntaxError => e
  puts "Error: Syntax error in configuration file. Check #{CONFIG_FILE}."
  exit
end

# Configuration parameters
BLOG_URL = config["blog_url"] || "https://example.com"
NOTIFICATION_EMAIL = config["notification_email"]
SMTP_SETTINGS = config["smtp_settings"]

# Function to fetch the latest Jekyll blog post metadata
def fetch_latest_post(blog_url)
  uri = URI("#{blog_url}/api/posts/latest.json") # Ensure your Jekyll site exposes an API endpoint for post metadata
  response = Net::HTTP.get_response(uri)

  if response.is_a?(Net::HTTPSuccess)
    JSON.parse(response.body)
  else
    raise "Failed to fetch the latest post: HTTP #{response.code}"
  end
end

# Function to send an email notification
def send_email_notification(to_email, subject, body)
  Mail.defaults do
    delivery_method :smtp, SMTP_SETTINGS
  end

  mail = Mail.new do
    from SMTP_SETTINGS[:user_name]
    to to_email
    subject subject
    body body
  end

  mail.deliver!
end

# Check for new blog content
begin
  latest_post = fetch_latest_post(BLOG_URL)

  # Read the last notified post ID from a file to avoid duplicate notifications
  LAST_POST_FILE = "last_post_id.txt"
  last_post_id = nil

  if File.exist?(LAST_POST_FILE)
    last_post_id = File.read(LAST_POST_FILE).strip
  end

  # If the latest post ID is different from the last notified ID, send a notification
  if latest_post["id"].to_s != last_post_id
    subject = "New Content Available on Your Jekyll Blog!"
    body = "A new post has been published: '#{latest_post['title']}'. Check it out here: #{latest_post['url']}"

    send_email_notification(NOTIFICATION_EMAIL, subject, body)

    # Update the last notified post ID
    File.write(LAST_POST_FILE, latest_post["id"].to_s)
    puts "Notification sent successfully."
  else
    puts "No new content available."
  end
rescue StandardError => e
  puts "An error occurred: #{e.message}"
end
```

```yaml
# config.yml
# Configuration file for the notification script

blog_url: "https://your-jekyll-blog.com"
notification_email: "user@example.com"

smtp_settings:
  address: "smtp.example.com"
  port: 587
  user_name: "your_email@example.com"
  password: "your_password"
  authentication: "plain"
  enable_starttls_auto: true
```

```bash
# Usage Instructions:
# 1. Save the Ruby script as `notification_script.rb`.
# 2. Create a configuration file named `config.yml` with the required settings.
# 3. Ensure your Jekyll blog exposes an API endpoint at `/api/posts/latest.json` that returns the metadata of the latest post.
# 4. Run the script periodically using a cron job or task scheduler:
#    ruby notification_script.rb
```
