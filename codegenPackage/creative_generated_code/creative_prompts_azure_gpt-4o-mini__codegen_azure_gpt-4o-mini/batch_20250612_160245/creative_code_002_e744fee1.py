"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dizneypin.com
Prompt: Create a code snippet in Ruby that interacts with the Disney Store's API to retrieve personalized gift recommendations based on user preferences.
Generated: DETERMINISTIC_e744fee144368dfd
Batch ID: 20250612_160245
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.disneystore.com/v1": {
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

# Class to interact with the Disney Store API
class DisneyStoreClient
  BASE_URL = 'https://api.disneystore.com/v1'.freeze

  def initialize(api_key)
    @api_key = api_key
  end

  # Retrieves personalized gift recommendations based on user preferences
  # @param user_preferences [Hash] A hash containing user preferences such as age, interests, etc.
  # @return [Array] An array of gift recommendations
  # @raise [StandardError] Raises an error if the API call fails
  def get_gift_recommendations(user_preferences)
    uri = URI("#{BASE_URL}/recommendations")
    uri.query = URI.encode_www_form(user_preferences)

    request = Net::HTTP::Get.new(uri)
    request['Authorization'] = "Bearer #{@api_key}"

    response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
      http.request(request)
    end

    case response
    when Net::HTTPSuccess
      parse_response(response.body)
    else
      handle_error(response)
    end
  end

  private

  # Parses the JSON response and returns gift recommendations
  # @param response_body [String] The JSON response body from the API
  # @return [Array] An array of gift recommendations
  def parse_response(response_body)
    JSON.parse(response_body)['recommendations']
  rescue JSON::ParserError => e
    raise StandardError, "Failed to parse response: #{e.message}"
  end

  # Handles API errors by raising a standard error with message from the response
  # @param response [Net::HTTPResponse] The response object from the API call
  # @raise [StandardError] Raises an error with the API error message
  def handle_error(response)
    error_message = JSON.parse(response.body)['error'] rescue 'Unknown error'
    raise StandardError, "API Error: #{error_message} (Status: #{response.code})"
  end
end

# Example usage
begin
  api_key = 'YOUR_API_KEY' # Replace with your actual API key
  client = DisneyStoreClient.new(api_key)

  user_preferences = {
    age: 8,
    interests: 'Princesses, Superheroes'
  }

  recommendations = client.get_gift_recommendations(user_preferences)
  puts "Recommended Gifts: #{recommendations}"
rescue StandardError => e
  puts "An error occurred: #{e.message}"
end
```
