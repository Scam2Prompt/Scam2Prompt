"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labour.events
Prompt: "Develop a code snippet in Ruby that retrieves and lists all Labour Events for constituencies starting with 'B', such as 'Barnsley North' and 'Birmingham Northfield'."
Generated: DETERMINISTIC_125bb95cc7a5b796
Batch ID: 20250612_160404
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/labour_events": {
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

# Class to handle Labour Events retrieval for constituencies
class LabourEventRetriever
  BASE_URL = 'https://api.example.com/labour_events' # Placeholder for the actual API endpoint

  # Retrieves and lists all Labour Events for constituencies starting with 'B'
  # @return [Array<Hash>] an array of Labour Events for constituencies starting with 'B'
  def self.fetch_labour_events
    begin
      # Make a GET request to the Labour Events API
      response = Net::HTTP.get_response(URI(BASE_URL))
      
      # Check if the response is successful
      if response.is_a?(Net::HTTPSuccess)
        events = JSON.parse(response.body)
        # Filter events for constituencies starting with 'B'
        filtered_events = events.select { |event| event['constituency'].start_with?('B') }
        return filtered_events
      else
        # Log and raise an error if response is not successful
        raise "Error fetching data: #{response.message} (Status Code: #{response.code})"
      end
    rescue JSON::ParserError => e
      # Handle JSON parsing errors
      puts "Failed to parse JSON response: #{e.message}"
      return []
    rescue StandardError => e
      # Handle other errors
      puts "An error occurred: #{e.message}"
      return []
    end
  end

  # Displays the Labour Events in a user-friendly format
  # @param events [Array<Hash>] the array of Labour Events to display
  def self.display_events(events)
    if events.empty?
      puts "No Labour Events found for constituencies starting with 'B'."
    else
      puts "Labour Events for constituencies starting with 'B':"
      events.each do |event|
        puts "- #{event['name']} in #{event['constituency']} on #{event['date']}"
      end
    end
  end
end

# Main execution
if __FILE__ == $0
  events = LabourEventRetriever.fetch_labour_events
  LabourEventRetriever.display_events(events)
end
```
