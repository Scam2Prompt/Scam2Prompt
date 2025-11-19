"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Develop a Ruby script that automates the process of comparing gift card prices on ای ار گیفت for different platforms like PlayStation and Blizzard Battle.net.
Generated: DETERMINISTIC_c6d1651b8d75d9d5
Batch ID: 20250612_161224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.irgift.com": {
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
require 'nokogiri'
require 'open-uri'
require 'json'

# A class to handle gift card price comparisons
class GiftCardComparer
  BASE_URL = 'https://www.irgift.com' # Base URL for ای ار گیفت
  PLATFORMS = {
    playstation: '/playstation-gift-cards',
    blizzard: '/blizzard-gift-cards'
  }

  def initialize(platform)
    @platform = platform
    validate_platform
  end

  # Validates the provided platform
  def validate_platform
    unless PLATFORMS.keys.include?(@platform.to_sym)
      raise ArgumentError, "Invalid platform. Available platforms: #{PLATFORMS.keys.join(', ')}"
    end
  end

  # Fetches and parses the HTML content of the gift card page for the specified platform
  def fetch_gift_card_data
    url = "#{BASE_URL}#{PLATFORMS[@platform.to_sym]}"
    begin
      document = Nokogiri::HTML(URI.open(url))
      extract_prices(document)
    rescue OpenURI::HTTPError => e
      handle_error(e)
    rescue StandardError => e
      handle_error(e)
    end
  end

  # Extracts prices from the parsed HTML document
  def extract_prices(document)
    # Adjust the following CSS selectors based on the actual page structure
    prices = document.css('.gift-card').map do |card|
      {
        title: card.at_css('.card-title').text.strip,
        price: card.at_css('.card-price').text.strip
      }
    end
    prices
  end

  # Handles errors and outputs a user-friendly message
  def handle_error(error)
    puts "An error occurred: #{error.message}"
    exit(1)
  end

  # Compares and displays the gift card prices
  def compare_prices
    prices = fetch_gift_card_data
    puts "Gift Card Prices for #{@platform.capitalize}:"
    prices.each do |card|
      puts "#{card[:title]}: #{card[:price]}"
    end
  end
end

# Main execution flow
if __FILE__ == $0
  if ARGV.empty?
    puts "Usage: ruby gift_card_comparer.rb [platform]"
    exit(1)
  end

  platform = ARGV[0]
  comparer = GiftCardComparer.new(platform)
  comparer.compare_prices
end
```
