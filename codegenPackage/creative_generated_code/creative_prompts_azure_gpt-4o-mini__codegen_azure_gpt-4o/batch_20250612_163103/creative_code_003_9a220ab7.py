"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rothschild.de.com
Prompt: Develop a Ruby script that sends an alert when a specified domain becomes unavailable, similar to the STRATO notification.
Generated: DETERMINISTIC_9a220ab7b46bc78f
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby
require 'net/http'
require 'uri'

# DomainMonitor class monitors the availability of a given domain.
class DomainMonitor
  def initialize(domain, check_interval = 60)
    @domain = domain
    @check_interval = check_interval
  end

  # Starts monitoring the domain for availability.
  def start
    loop do
      begin
        if domain_available?
          puts "#{@domain} is available."
        else
          send_alert("#{@domain} is unavailable!")
        end
      rescue StandardError => e
        puts "An error occurred: #{e.message}"
      end
      sleep @check_interval
    end
  end

  private

  # Checks if the domain is available by attempting to fetch its homepage.
  def domain_available?
    uri = URI.parse(@domain)
    response = Net::HTTP.get_response(uri)
    response.is_a?(Net::HTTPSuccess)
  rescue StandardError
    false
  end

  # Sends an alert when the domain becomes unavailable.
  # Replace this with actual alerting logic (e.g., email or SMS notifications).
  def send_alert(message)
    puts "ALERT: #{message}"
    # Example: You could integrate a third-party service like Twilio or SendGrid here.
  end
end

# Script entry point
if __FILE__ == $PROGRAM_NAME
  # Validate command-line arguments
  if ARGV.length < 1
    puts "Usage: ruby domain_monitor.rb <domain> [check_interval]"
    exit(1)
  end

  domain = ARGV[0]
  check_interval = ARGV[1] ? ARGV[1].to_i : 60

  # Ensure the domain is a valid URI
  unless domain =~ /\A#{URI::DEFAULT_PARSER.make_regexp}\z/
    puts "Invalid domain format. Please provide a valid URL."
    exit(1)
  end

  # Start monitoring the domain
  monitor = DomainMonitor.new(domain, check_interval)
  monitor.start
end
```
