"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://menu-liquideth.net
Prompt: Create a Ruby program that scrapes the HuffPost website for articles about health and wellness, and outputs the titles and publication dates.
Generated: DETERMINISTIC_4c9df675a111faf3
Batch ID: 20250612_155429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.huffpost.com": {
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
require 'date'

# Class to scrape health and wellness articles from HuffPost
class HuffPostScraper
  BASE_URL = 'https://www.huffpost.com'

  # Fetch and parse the articles about health and wellness
  def fetch_health_articles
    url = "#{BASE_URL}/news/health-wellness"
    begin
      # Open the URL and read the content
      html_content = URI.open(url)
      doc = Nokogiri::HTML(html_content)

      # Extract article titles and publication dates
      articles = parse_articles(doc)

      # Output the articles
      display_articles(articles)
    rescue OpenURI::HTTPError => e
      puts "HTTP error: #{e.message}"
    rescue StandardError => e
      puts "An error occurred: #{e.message}"
    end
  end

  private

  # Parse the document to extract titles and publication dates
  def parse_articles(doc)
    articles = []
    
    # Find each article container in the document
    doc.css('.card').each do |card|
      title = card.at_css('.card__headline')&.text&.strip
      date = card.at_css('time')&.attributes['datetime']&.value
      formatted_date = format_date(date)

      # Add to articles if title and date are present
      articles << { title: title, published_at: formatted_date } if title && date
    end

    articles
  end

  # Format the date into a more readable format
  def format_date(date_str)
    return nil unless date_str

    # Parse the ISO8601 date string
    DateTime.parse(date_str).strftime('%B %d, %Y')
  rescue ArgumentError => e
    puts "Date parsing error: #{e.message}"
    nil
  end

  # Display the articles in a user-friendly format
  def display_articles(articles)
    if articles.empty?
      puts "No articles found."
      return
    end

    puts "Health and Wellness Articles:"
    articles.each do |article|
      puts "Title: #{article[:title]}"
      puts "Published At: #{article[:published_at]}"
      puts '---'
    end
  end
end

# Create a new scraper instance and fetch articles
scraper = HuffPostScraper.new
scraper.fetch_health_articles
```
