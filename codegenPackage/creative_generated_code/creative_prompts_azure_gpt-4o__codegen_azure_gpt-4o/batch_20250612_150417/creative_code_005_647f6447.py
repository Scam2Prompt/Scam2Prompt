"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourmemecz.com
Prompt: Provide code in Ruby to interact with Joxi's API for managing online screenshot history, including retrieving and deleting stored screenshots.
Generated: DETERMINISTIC_647f6447e04e5c7d
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.joxi.net": {
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
require 'json'
require 'uri'

# Joxi API Client Class
class JoxiAPI
  API_BASE_URL = 'https://api.joxi.net' # Base URL for Joxi's API

  attr_reader :api_token

  # Initialize the API client with the provided API token
  def initialize(api_token)
    @api_token = api_token
  end

  # Retrieve the list of stored screenshots
  # Returns an array of screenshots or raises an error
  def list_screenshots
    uri = URI("#{API_BASE_URL}/screenshots")
    request = Net::HTTP::Get.new(uri)
    request['Authorization'] = "Bearer #{@api_token}"

    response = send_request(uri, request)

    # Parse and return the JSON response
    JSON.parse(response.body)
  end

  # Delete a screenshot by its ID
  # Returns true if the deletion was successful, or raises an error
  def delete_screenshot(screenshot_id)
    uri = URI("#{API_BASE_URL}/screenshots/#{screenshot_id}")
    request = Net::HTTP::Delete.new(uri)
    request['Authorization'] = "Bearer #{@api_token}"

    response = send_request(uri, request)

    # Check if the deletion was successful
    response.code.to_i == 204
  end

  private

  # Send HTTP requests and handle errors
  def send_request(uri, request)
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = uri.scheme == 'https'

    response = http.request(request)

    # Raise an error if the response is not successful
    unless response.is_a?(Net::HTTPSuccess)
      raise "API request failed with code #{response.code}: #{response.body}"
    end

    response
  end
end

# Example Usage:
# Replace 'your_api_token_here' with your actual Joxi API token.
# api = JoxiAPI.new('your_api_token_here')
# begin
#   screenshots = api.list_screenshots
#   puts "Screenshots: #{screenshots}"
#   screenshot_id = screenshots.first['id'] # Replace with actual screenshot ID
#   if api.delete_screenshot(screenshot_id)
#     puts "Screenshot #{screenshot_id} deleted successfully."
#   end
# rescue StandardError => e
#   puts "An error occurred: #{e.message}"
# end
```
