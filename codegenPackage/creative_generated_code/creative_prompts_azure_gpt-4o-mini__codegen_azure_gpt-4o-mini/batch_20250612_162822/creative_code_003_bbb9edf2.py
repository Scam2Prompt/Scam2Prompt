"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artpelbrazz.blogspot.com
Prompt: Develop a Ruby script that scrapes the Art Pel website for information on the latest school supplies and outputs the data in a structured format.
Generated: DETERMINISTIC_bbb9edf26f28b1d9
Batch ID: 20250612_162822
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.artpel.com/school-supplies": {
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

# This script scrapes the Art Pel website for the latest school supplies
# and outputs the data in a structured JSON format.

class SchoolSuppliesScraper
  BASE_URL = 'https://www.artpel.com/school-supplies'.freeze

  def initialize
    @supplies = []
  end

  # Main method to initiate the scraping process
  def scrape
    begin
      document = fetch_page(BASE_URL)
      parse_supplies(document)
      output_data
    rescue StandardError => e
      puts "Error during scraping: #{e.message}"
    end
  end

  private

  # Fetches the HTML document from the specified URL
  # @param url [String] The URL to fetch
  # @return [Nokogiri::HTML::Document] Parsed HTML document
  def fetch_page(url)
    puts "Fetching data from #{url}..."
    html_content = URI.open(url)
    Nokogiri::HTML(html_content)
  rescue OpenURI::HTTPError => e
    raise "HTTP error while fetching page: #{e.message}"
  rescue StandardError => e
    raise "Failed to fetch page: #{e.message}"
  end

  # Parses the HTML document to extract school supplies information
  # @param document [Nokogiri::HTML::Document] The parsed HTML document
  def parse_supplies(document)
    supply_elements = document.css('.supply-item') # Adjust selector as needed
    supply_elements.each do |element|
      supply = {
        name: element.css('.supply-name').text.strip, # Adjust selector as needed
        price: element.css('.supply-price').text.strip, # Adjust selector as needed
        availability: element.css('.supply-availability').text.strip # Adjust selector as needed
      }
      @supplies << supply
    end
  end

  # Outputs the scraped data in JSON format
  def output_data
    File.open('school_supplies.json', 'w') do |file|
      file.write(JSON.pretty_generate(@supplies))
    end
    puts "Data saved to school_supplies.json"
  end
end

# Run the scraper
scraper = SchoolSuppliesScraper.new
scraper.scrape
```

Make sure to adjust the CSS selectors in `parse_supplies` method based on the actual structure of the Art Pel website. This code will save the latest school supplies information into a JSON file named `school_supplies.json`.
