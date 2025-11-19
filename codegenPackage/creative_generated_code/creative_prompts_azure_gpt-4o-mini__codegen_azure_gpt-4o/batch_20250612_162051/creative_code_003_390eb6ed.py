"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ratnarajfoods.in
Prompt: Develop a code snippet in Ruby that sends a request to Ratnaraj Foods' API to get a list of their top-selling spices and formats the response for display.
Generated: DETERMINISTIC_390eb6ed11760b8a
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.ratnarajfoods.com/v1/top-selling-spices": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.ratnarajfoods.com/v1/top-selling-spices`": {
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

# Define a method to fetch and display top-selling spices from Ratnaraj Foods' API
def fetch_top_selling_spices
  # Base URL for Ratnaraj Foods' API
  api_url = 'https://api.ratnarajfoods.com/v1/top-selling-spices'

  begin
    # Create a URI object
    uri = URI(api_url)

    # Send GET request to the API
    response = Net::HTTP.get_response(uri)

    # Handle HTTP response codes
    case response.code.to_i
    when 200
      # Parse JSON response
      spices = JSON.parse(response.body)

      # Check if the response contains the expected data
      if spices.is_a?(Array) && spices.any?
        # Format and display the top-selling spices
        puts 'Top-Selling Spices:'
        spices.each_with_index do |spice, index|
          puts "#{index + 1}. #{spice['name']} - #{spice['sales']} units sold"
        end
      else
        puts 'No spice data available.'
      end
    when 404
      puts 'API endpoint not found.'
    when 500..599
      puts 'Server error occurred. Please try again later.'
    else
      puts "Unexpected error occurred. HTTP Status: #{response.code}"
    end
  rescue SocketError => e
    # Handle network-related errors
    puts "Network error: #{e.message}"
  rescue JSON::ParserError => e
    # Handle JSON parsing errors
    puts "Error parsing response: #{e.message}"
  rescue StandardError => e
    # Handle other unexpected errors
    puts "An unexpected error occurred: #{e.message}"
  end
end

# Run the method to fetch and display top-selling spices
fetch_top_selling_spices
```

#### Notes:
- Replace `https://api.ratnarajfoods.com/v1/top-selling-spices` with the actual API endpoint provided by Ratnaraj Foods if it's different.
- Ensure the API key or authentication mechanism (if required) is added appropriately.
