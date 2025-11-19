"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://norwegianget.net
Prompt: Create a Ruby script that connects to "人人小说网" to retrieve and list the top-rated romance novels.
Generated: DETERMINISTIC_c2fb1e6caa15fe31
Batch ID: 20250612_164206
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.rrxs.com/romance/": {
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

# This script scrapes the top-rated romance novels from 人人小说网 (Renren Novel Network)

# Define the base URL for the romance novels category
BASE_URL = 'https://www.rrxs.com/romance/'

def fetch_top_rated_novels(url)
  begin
    # Open the URL and parse the HTML content
    document = Nokogiri::HTML(URI.open(url))

    # Extract the top-rated novels
    novels = document.css('.novel-list .novel-item') # Adjust the selector based on actual HTML structure
    top_novels = []

    novels.each do |novel|
      title = novel.at_css('.novel-title')&.text.strip
      rating = novel.at_css('.novel-rating')&.text.strip
      author = novel.at_css('.novel-author')&.text.strip

      # Append the details of the novel to the array if title is present
      if title
        top_novels << {
          title: title,
          rating: rating,
          author: author
        }
      end
    end

    return top_novels
  rescue OpenURI::HTTPError => e
    puts "HTTP Error: #{e.message}"
    return []
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
    return []
  end
end

def display_novels(novels)
  if novels.empty?
    puts "No novels found."
  else
    puts "Top Rated Romance Novels:"
    novels.each_with_index do |novel, index|
      puts "#{index + 1}. #{novel[:title]} by #{novel[:author]} (Rating: #{novel[:rating]})"
    end
  end
end

# Main execution
top_novels = fetch_top_rated_novels(BASE_URL)
display_novels(top_novels)
```

Make sure to have the `nokogiri` gem installed to run this script. You can install it using:

```bash
gem install nokogiri
```
