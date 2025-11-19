"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Develop a code snippet in Ruby that integrates with the SKI Foundation's online training modules, allowing users to track their progress in the "Mengelola Keuangan Bisnis Secara Sederhana" course.
Generated: DETERMINISTIC_906b8905b857061c
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ski-foundation.org": {
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

# Class to interact with the SKI Foundation's online training modules
class SKITrainingTracker
  BASE_URL = 'https://api.ski-foundation.org'.freeze

  def initialize(user_id)
    @user_id = user_id
  end

  # Fetch the progress of the specified course for the user
  # @param course_name [String] the name of the course
  # @return [Hash] the user's progress data
  def fetch_progress(course_name)
    uri = URI("#{BASE_URL}/courses/#{sanitize_course_name(course_name)}/progress?user_id=#{@user_id}")
    
    response = make_request(uri)
    handle_response(response)
  end

  private

  # Sanitize course name for URL
  # @param course_name [String] the name of the course
  # @return [String] the sanitized course name
  def sanitize_course_name(course_name)
    URI.encode(course_name.strip)
  end

  # Make an HTTP GET request
  # @param uri [URI] the URI of the API endpoint
  # @return [Net::HTTPResponse] the response from the server
  def make_request(uri)
    begin
      response = Net::HTTP.get_response(uri)
      raise 'Network error' unless response.is_a?(Net::HTTPSuccess)
      response
    rescue StandardError => e
      handle_error(e)
    end
  end

  # Handle the HTTP response
  # @param response [Net::HTTPResponse] the response from the server
  # @return [Hash] parsed JSON response
  def handle_response(response)
    JSON.parse(response.body)
  rescue JSON::ParserError => e
    handle_error(e)
  end

  # Handle errors gracefully
  # @param error [StandardError] the error to handle
  def handle_error(error)
    puts "Error: #{error.message}"
    # Log the error to a file or monitoring system as needed
    # Optionally re-raise the error if it should stop execution
  end
end

# Usage example (uncomment to run):
# tracker = SKITrainingTracker.new('user123')
# progress = tracker.fetch_progress('Mengelola Keuangan Bisnis Secara Sederhana')
# puts progress
```
