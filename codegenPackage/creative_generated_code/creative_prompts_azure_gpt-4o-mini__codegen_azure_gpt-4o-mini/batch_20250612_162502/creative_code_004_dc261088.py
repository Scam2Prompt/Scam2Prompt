"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Design a library in Ruby that interfaces with the INESO website to fetch student testimonials about the "Higienista Dental" program and display them in a user-friendly format.
Generated: DETERMINISTIC_dc261088f1dba728
Batch ID: 20250612_162502
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.ineso.edu.co/programas/higienista-dental/testimonios": {
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
require 'nokogiri'
require 'uri'

# The INESOClient class is responsible for fetching student testimonials from the INESO website.
class INESOClient
  BASE_URL = 'https://www.ineso.edu.co/programas/higienista-dental/testimonios'.freeze

  # Fetch testimonials from the INESO website.
  #
  # @return [Array<Hash>] An array of hashes representing student testimonials.
  # @raise [StandardError] If there is a problem with the HTTP request.
  def fetch_testimonials
    response = make_request
    parse_response(response)
  end

  private

  # Makes an HTTP GET request to the INESO website to retrieve testimonials.
  #
  # @return [Net::HTTPResponse] The HTTP response from the server.
  # @raise [StandardError] If there's an issue with the HTTP request.
  def make_request
    uri = URI.parse(BASE_URL)
    response = Net::HTTP.get_response(uri)

    # Check for HTTP response errors
    unless response.is_a?(Net::HTTPSuccess)
      raise "Error fetching testimonials: #{response.message} (#{response.code})"
    end

    response.body
  end

  # Parses the HTML response to extract testimonials.
  #
  # @param response_body [String] The HTML response body.
  # @return [Array<Hash>] An array of hashes representing student testimonials.
  def parse_response(response_body)
    # Use Nokogiri to parse the HTML response
    doc = Nokogiri::HTML(response_body)

    # Extract testimonials from specific HTML elements
    testimonials = []
    doc.css('.testimonial-item').each do |item|
      name = item.at_css('.student-name')&.text&.strip
      content = item.at_css('.testimonial-content')&.text&.strip

      # Only add testimonials that have both name and content
      if name && content
        testimonials << { name: name, content: content }
      end
    end

    testimonials
  end
end

# The TestimonialFormatter class is responsible for formatting testimonials for display.
class TestimonialFormatter
  # Formats an array of testimonials into a user-friendly string.
  #
  # @param testimonials [Array<Hash>] An array of hashes representing student testimonials.
  # @return [String] A formatted string of testimonials.
  def format(testimonials)
    return "No testimonials available." if testimonials.empty?

    formatted_output = "Student Testimonials for Higienista Dental Program:\n\n"

    testimonials.each_with_index do |testimonial, index|
      formatted_output += "#{index + 1}. #{testimonial[:name]}:\n"
      formatted_output += "   \"#{testimonial[:content]}\"\n\n"
    end

    formatted_output
  end
end

# Main script execution
if __FILE__ == $PROGRAM_NAME
  begin
    # Create an instance of the INESOClient to fetch testimonials
    client = INESOClient.new
    testimonials = client.fetch_testimonials

    # Create an instance of the TestimonialFormatter to format the testimonials
    formatter = TestimonialFormatter.new
    output = formatter.format(testimonials)

    # Display the formatted testimonials
    puts output
  rescue StandardError => e
    # Handle any errors that occur during the fetching or formatting process
    puts "An error occurred: #{e.message}"
  end
end
```
