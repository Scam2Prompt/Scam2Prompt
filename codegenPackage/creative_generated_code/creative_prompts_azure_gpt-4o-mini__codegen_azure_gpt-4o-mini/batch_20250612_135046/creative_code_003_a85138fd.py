"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmask.com
Prompt: Develop a Ruby script that retrieves and displays the latest fishing gear available on metmask.com, focusing on items like telescopic rods and tackle accessories.
Generated: DETERMINISTIC_a85138fda9326952
Batch ID: 20250612_135046
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://metmask.com": {
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

# This class is responsible for scraping the latest fishing gear from metmask.com
class FishingGearScraper
  BASE_URL = 'https://metmask.com'

  # Fetch the HTML content of the page
  def fetch_page(url)
    begin
      URI.open(url)
    rescue OpenURI::HTTPError => e
      puts "HTTP Error: #{e.message}"
      nil
    rescue StandardError => e
      puts "An error occurred: #{e.message}"
      nil
    end
  end

  # Parse the HTML and extract fishing gear information
  def parse_fishing_gear(html_content)
    doc = Nokogiri::HTML(html_content)
    fishing_gear = []

    # Search for telescopic rods and tackle accessories
    doc.css('.product-item').each do |item|
      title = item.at_css('.product-title')&.text&.strip
      category = item.at_css('.product-category')&.text&.strip
      price = item.at_css('.product-price')&.text&.strip

      # Filter for specific categories
      if title&.include?('telescopic rod') || title&.include?('tackle')
        fishing_gear << {
          title: title,
          category: category,
          price: price,
          link: BASE_URL + item.at_css('a')['href']
        }
      end
    end

    fishing_gear
  end

  # Display the fishing gear information
  def display_fishing_gear(gear)
    if gear.empty?
      puts "No fishing gear found."
    else
      gear.each do |item|
        puts "Title: #{item[:title]}"
        puts "Category: #{item[:category]}"
        puts "Price: #{item[:price]}"
        puts "Link: #{item[:link]}"
        puts "-" * 40
      end
    end
  end

  # Main method to orchestrate the scraping process
  def run
    puts "Fetching latest fishing gear from #{BASE_URL}..."
    html_content = fetch_page(BASE_URL + '/fishing-gear')

    if html_content
      fishing_gear = parse_fishing_gear(html_content)
      display_fishing_gear(fishing_gear)
    else
      puts "Failed to retrieve the content."
    end
  end
end

# Entry point for the script
if __FILE__ == $0
  scraper = FishingGearScraper.new
  scraper.run
end
```
