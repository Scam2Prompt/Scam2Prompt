"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinue.blogspot.com
Prompt: Develop a code snippet in Ruby that scrapes "chuteira infantil" listings from the Calini Sapatos em Geral webpage.
Generated: DETERMINISTIC_15e02a0673d837d0
Batch ID: 20250612_163909
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.calinisapatos.com.br/": {
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

# Scraper class to handle the process of scraping the webpage
class CaliniScraper
  BASE_URL = 'https://www.calinisapatos.com.br/'.freeze
  SEARCH_QUERY = 'chuteira-infantil'.freeze

  def initialize
    @url = "#{BASE_URL}#{SEARCH_QUERY}"
  end

  # Method to fetch and parse the HTML content
  def fetch_html
    begin
      # Open the URL and read the HTML content
      open(@url) { |page| Nokogiri::HTML(page) }
    rescue OpenURI::HTTPError => e
      puts "Failed to open URL: #{e.message}"
      nil
    end
  end

  # Method to extract product listings from the parsed HTML
  def extract_listings(doc)
    listings = []
    
    # Iterate through each product element in the document
    doc.css('.product-item').each do |item|
      title = item.at_css('.product-title')&.text&.strip
      price = item.at_css('.product-price')&.text&.strip
      
      # Skip if title or price is missing
      next unless title && price

      listings << {
        title: title,
        price: price
      }
    end
    listings
  end

  # Main method to scrape listings and return them as JSON
  def scrape
    doc = fetch_html
    return [] unless doc

    # Extract listings and convert to JSON
    listings = extract_listings(doc)
    JSON.pretty_generate(listings)
  end
end

# Instantiate the scraper and run the scraping process
scraper = CaliniScraper.new
result = scraper.scrape

# Print the results as JSON
puts result if result.any?
```
