"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csl-seqirus.co.uk
Prompt: Create a code snippet in Ruby that fetches CSL Seqirus's latest news releases regarding their contributions to seasonal influenza vaccination efforts.
Generated: DETERMINISTIC_c38b2fb3f3f5a496
Batch ID: 20250612_160625
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.cslseqirus.com.au/news-releases": {
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

# Class to fetch and display CSL Seqirus latest news releases
class CslSeqirusNews
  BASE_URL = 'https://www.cslseqirus.com.au/news-releases'

  # Fetches the latest news releases from CSL Seqirus
  def fetch_latest_news
    uri = URI(BASE_URL)

    begin
      response = Net::HTTP.get_response(uri)

      if response.is_a?(Net::HTTPSuccess)
        parse_news(response.body)
      else
        puts "Error fetching news: #{response.code} #{response.message}"
      end
    rescue SocketError => e
      puts "Network error: #{e.message}"
    rescue StandardError => e
      puts "An error occurred: #{e.message}"
    end
  end

  private

  # Parses the HTML response to extract news titles and links
  def parse_news(html)
    require 'nokogiri'

    # Initialize Nokogiri to parse the HTML document
    doc = Nokogiri::HTML(html)

    # Extract news items (assuming they are contained within <article> tags)
    news_items = doc.css('article')

    # Iterate over each news item and print the title and link
    news_items.each do |item|
      title = item.at_css('h2 a')&.text
      link = item.at_css('h2 a')&['href']

      puts "Title: #{title}" if title
      puts "Link: #{link}" if link
      puts '---'
    end
  end
end

# Create an instance of the CslSeqirusNews class and fetch the latest news
csl_seqirus_news = CslSeqirusNews.new
csl_seqirus_news.fetch_latest_news
```
