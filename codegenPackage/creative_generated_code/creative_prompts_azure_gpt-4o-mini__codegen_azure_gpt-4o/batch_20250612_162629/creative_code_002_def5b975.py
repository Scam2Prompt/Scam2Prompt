"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myallora.com
Prompt: Create a Ruby program that interacts with an API to fetch the latest discounts on dresses from Sophie’s Boutique, ensuring to include the up to 80% off offer.
Generated: DETERMINISTIC_def5b975e4212aa2
Batch ID: 20250612_162629
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sophiesboutique.com/discounts": {
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

# Define the URL for the API endpoint
API_URL = "https://api.sophiesboutique.com/discounts"

# Fetch discounts from the API
def fetch_discounts
  begin
    # Parse the API URL
    uri = URI(API_URL)

    # Send a GET request to the API
    response = Net::HTTP.get_response(uri)

    # Check if the response is successful
    if response.is_a?(Net::HTTPSuccess)
      # Parse the JSON response
      JSON.parse(response.body)
    else
      # Handle non-success response
      puts "Error fetching discounts: #{response.message}"
      []
    end
  rescue StandardError => e
    # Handle any exceptions during the API call
    puts "An error occurred: #{e.message}"
    []
  end
end

# Filter discounts for dresses and up to 80% off
def filter_dress_discounts(discounts)
  discounts.select do |discount|
    discount['category'].casecmp?('dresses') && discount['discount_percentage'] <= 80
  end
end

# Display the discounts in a user-friendly format
def display_discounts(discounts)
  if discounts.empty?
    puts "No relevant discounts found on dresses."
  else
    puts "Latest discounts on dresses (up to 80% off):"
    discounts.each do |discount|
      puts "- #{discount['name']} (#{discount['discount_percentage']}% off)"
    end
  end
end

# Main program execution
def main
  puts "Fetching latest discounts from Sophie’s Boutique..."
  all_discounts = fetch_discounts
  dress_discounts = filter_dress_discounts(all_discounts)
  display_discounts(dress_discounts)
end

# Run the program
main
```
