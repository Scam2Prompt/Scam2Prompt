"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Write a script in Ruby to extract and display the tour package names and their corresponding durations from the Batur Jeep Tour website.
Generated: DETERMINISTIC_ebf5eaaecdd7412d
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://baturjeep.com/tour-packages": {
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
require 'logger'

# Initialize a logger for debugging purposes
logger = Logger.new(STDOUT)

# Class to handle the extraction of tour packages
class BaturJeepTourScraper
  BASE_URL = 'https://baturjeep.com/tour-packages' # Replace with the actual URL if different

  def initialize
    @tour_packages = []
  end

  # Fetch the HTML content from the given URL
  def fetch_html(url)
    begin
      Nokogiri::HTML(URI.open(url)) # Open and parse the URL
    rescue OpenURI::HTTPError => e
      logger.error("HTTP Error: #{e.message}")
      nil
    rescue StandardError => e
      logger.error("Error fetching HTML: #{e.message}")
      nil
    end
  end

  # Extract tour package names and durations from the HTML document
  def extract_packages(doc)
    doc.css('.tour-package').each do |package| # Adjust the selector to match the actual HTML structure
      name = package.css('.package-name').text.strip # Adjust selector for package name
      duration = package.css('.package-duration').text.strip # Adjust selector for duration
      
      unless name.empty? || duration.empty?
        @tour_packages << { name: name, duration: duration }
      else
        logger.warn("Found empty package name or duration")
      end
    end
  end

  # Display the extracted tour packages
  def display_packages
    if @tour_packages.empty?
      logger.info("No tour packages found.")
    else
      puts "Tour Packages:"
      @tour_packages.each do |package|
        puts "Name: #{package[:name]}, Duration: #{package[:duration]}"
      end
    end
  end

  # Main method to orchestrate the scraping process
  def scrape
    logger.info("Starting the scraping process...")
    document = fetch_html(BASE_URL)
    
    if document
      extract_packages(document)
      display_packages
    else
      logger.error("Failed to fetch the HTML document.")
    end
  end
end

# Execute the scraper
if __FILE__ == $PROGRAM_NAME
  scraper = BaturJeepTourScraper.new
  scraper.scrape
end
```
