"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sity-service.com
Prompt: Develop a Ruby script to automate the process of checking stock availability for specific items like MacCoffee and paper towels on the Сити-Сервис website.
Generated: DETERMINISTIC_d12894007e9bd43b
Batch ID: 20250612_163742
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.city-service.ru": {
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

# Script to check stock availability for specific items on the Сити-Сервис website

# Configuration for items to check
ITEMS_TO_CHECK = ['MacCoffee', 'paper towels']

# Base URL of the Сити-Сервис website
BASE_URL = 'https://www.city-service.ru'

# Function to fetch HTML content for a given URL
def fetch_html(url)
  begin
    uri = URI.parse(url)
    response = Net::HTTP.get_response(uri)

    if response.is_a?(Net::HTTPSuccess)
      response.body
    else
      raise "Failed to fetch URL: #{url} - HTTP Response: #{response.code}"
    end
  rescue StandardError => e
    puts "Error fetching URL: #{e.message}"
    nil
  end
end

# Function to parse product availability from HTML content
def parse_availability(html, item)
  begin
    doc = Nokogiri::HTML(html)
    # Search for the item in the HTML content (update the search logic if needed)
    product_elements = doc.css('.product-name') # Example of a CSS selector, may vary based on the actual website

    product_elements.each do |product|
      if product.text.strip.downcase.include?(item.downcase)
        # Check for stock availability (update logic based on website's structure)
        availability = product.parent.css('.stock-status').text.strip
        return availability.empty? ? 'Out of stock' : availability
      end
    end

    'Item not found'
  rescue StandardError => e
    puts "Error parsing HTML for item '#{item}': #{e.message}"
    nil
  end
end

# Main function to check stock availability
def check_stock_availability(items)
  url = "#{BASE_URL}/catalog" # Example URL, change based on actual website structure

  # Fetch the HTML content
  html_content = fetch_html(url)
  return unless html_content

  items.each do |item|
    availability = parse_availability(html_content, item)
    if availability
      puts "#{item}: #{availability}"
    else
      puts "#{item}: Error checking availability"
    end
  end
end

# Run the stock checker for the configured items
check_stock_availability(ITEMS_TO_CHECK)
```
