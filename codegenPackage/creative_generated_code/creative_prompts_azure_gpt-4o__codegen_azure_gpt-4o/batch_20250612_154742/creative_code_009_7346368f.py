"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status.ttec.smartteam.chat
Prompt: Write a script in Ruby that fetches the "Status updates" from the TTEC STC Cluster Status page and sends an alert if the service status changes from "Up" to "Down."
Generated: DETERMINISTIC_7346368fcc20b79f
Batch ID: 20250612_154742
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/ttec-stc-cluster-status": {
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

# This script fetches the status updates from the TTEC STC Cluster Status page
# and sends an alert if the service status changes from "Up" to "Down".

class ServiceStatusMonitor
  # Initialize the monitor with the URL to check and the status tracking variables
  def initialize(url)
    @url = url
    @previous_status = nil
  end

  # Main method to start monitoring service status.
  def monitor_status
    loop do
      begin
        current_status = fetch_service_status
        if status_changed_to_down?(current_status)
          send_alert(current_status)
        end
        @previous_status = current_status
      rescue StandardError => e
        puts "Error occurred during monitoring: #{e.message}"
      end
      sleep 60 # Wait for 60 seconds before checking again
    end
  end

  private

  # Fetch the service status from the webpage
  def fetch_service_status
    uri = URI.parse(@url)
    response = Net::HTTP.get_response(uri)

    if response.is_a?(Net::HTTPSuccess)
      parse_service_status(response.body)
    else
      raise "Failed to fetch status page: HTTP #{response.code}"
    end
  end

  # Parse the service status from the HTML response
  def parse_service_status(html)
    document = Nokogiri::HTML(html)
    # Assume the status is contained in a specific element with ID or class.
    # Update the selector based on the actual page structure.
    status_element = document.at_css('.service-status')
    raise "Service status element not found" unless status_element

    status_element.text.strip
  end

  # Check if the status has changed from "Up" to "Down"
  def status_changed_to_down?(current_status)
    @previous_status == 'Up' && current_status == 'Down'
  end

  # Send an alert notification to the administrator
  def send_alert(current_status)
    puts "ALERT: Service status changed to #{current_status}!"
    # Implement actual alert logic here, such as sending an email, SMS, or push notification.
  end
end

# URL of the TTEC STC Cluster Status page
status_page_url = 'https://example.com/ttec-stc-cluster-status'

# Start monitoring the service status
monitor = ServiceStatusMonitor.new(status_page_url)
monitor.monitor_status
```
