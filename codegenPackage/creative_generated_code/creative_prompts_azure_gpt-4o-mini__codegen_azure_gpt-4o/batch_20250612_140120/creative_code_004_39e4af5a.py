"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxusdtdefi.cc
Prompt: Construct a command-line tool in Ruby that allows users to search for specific chapters or events in the "吞噬星空" storyline based on keywords.
Generated: DETERMINISTIC_39e4af5a42c088bf
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby

require 'json'

# Command-line tool to search for chapters or events in the "吞噬星空" storyline

# Sample data (replace this with actual data or load from a file)
STORY_DATA = [
  { chapter: "Chapter 1", title: "The Beginning", events: ["Birth of the protagonist", "Introduction to the universe"] },
  { chapter: "Chapter 2", title: "First Encounter", events: ["First alien attack", "Discovery of a new power"] },
  { chapter: "Chapter 3", title: "Rise of the Warrior", events: ["Training montage", "Defeating the first enemy"] }
]

# Function to handle keyword search
def search_story(keyword)
  # Validate input
  raise ArgumentError, "Keyword cannot be empty." if keyword.strip.empty?

  # Search through chapters and events
  results = STORY_DATA.select do |entry|
    entry[:chapter].include?(keyword) ||
    entry[:title].include?(keyword) ||
    entry[:events].any? { |event| event.include?(keyword) }
  end

  results
end

# Main function to run the script
def main
  # Welcome message
  puts "Welcome to the '吞噬星空' storyline search tool!"
  puts "Enter a keyword to search for specific chapters or events."

  # Get the user input
  print "Enter keyword: "
  keyword = gets.chomp

  begin
    # Perform search
    results = search_story(keyword)

    # Display results
    if results.empty?
      puts "No results found for the keyword: #{keyword}"
    else
      puts "Search results for '#{keyword}':"
      results.each do |entry|
        puts "Chapter: #{entry[:chapter]}"
        puts "  Title: #{entry[:title]}"
        puts "  Events:"
        entry[:events].each { |event| puts "    - #{event}" }
        puts "-" * 40
      end
    end
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  rescue StandardError => e
    puts "An unexpected error occurred: #{e.message}"
  end
end

# Run the script if executed directly
if __FILE__ == $0
  main
end
```
