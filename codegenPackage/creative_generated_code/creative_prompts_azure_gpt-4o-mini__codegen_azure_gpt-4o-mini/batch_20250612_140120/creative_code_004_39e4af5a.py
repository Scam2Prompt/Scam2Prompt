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
require 'optparse'

# Chapter data structure
class Chapter
  attr_reader :number, :title, :summary

  def initialize(number, title, summary)
    @number = number
    @title = title
    @summary = summary
  end

  def to_s
    "Chapter #{@number}: #{@title}\nSummary: #{@summary}\n\n"
  end
end

# Storyline class to manage chapters
class Storyline
  def initialize(file_path)
    @chapters = []
    load_chapters(file_path)
  end

  # Load chapters from a JSON file
  def load_chapters(file_path)
    begin
      data = JSON.parse(File.read(file_path))
      data.each do |chapter_data|
        @chapters << Chapter.new(chapter_data['number'], chapter_data['title'], chapter_data['summary'])
      end
    rescue Errno::ENOENT
      puts "Error: File not found - #{file_path}"
      exit 1
    rescue JSON::ParserError
      puts "Error: Failed to parse JSON data in file - #{file_path}"
      exit 1
    end
  end

  # Search chapters based on a keyword
  def search(keyword)
    results = @chapters.select do |chapter|
      chapter.title.include?(keyword) || chapter.summary.include?(keyword)
    end

    if results.empty?
      puts "No chapters found containing '#{keyword}'."
    else
      results.each { |chapter| puts chapter }
    end
  end
end

# Command-line interface
class CLI
  def initialize
    @options = {}
    parse_options
  end

  def parse_options
    OptionParser.new do |opts|
      opts.banner = "Usage: ruby storyline_search.rb [options]"

      opts.on("-f", "--file FILE", "Path to the JSON file containing storyline chapters") do |file|
        @options[:file] = file
      end

      opts.on("-k", "--keyword KEYWORD", "Keyword to search for in chapters") do |keyword|
        @options[:keyword] = keyword
      end

      opts.on("-h", "--help", "Display help") do
        puts opts
        exit
      end
    end.parse!

    validate_options
  end

  def validate_options
    if @options[:file].nil? || @options[:keyword].nil?
      puts "Error: Both file and keyword options are required."
      exit 1
    end
  end

  def run
    storyline = Storyline.new(@options[:file])
    storyline.search(@options[:keyword])
  end
end

# Entry point for the command-line tool
if __FILE__ == $0
  cli = CLI.new
  cli.run
end
```

**Note:** Make sure to have a JSON file with the structure like this before running the script:

```json
[
  {
    "number": 1,
    "title": "The Beginning",
    "summary": "This chapter introduces the main character..."
  },
  {
    "number": 2,
    "title": "The Conflict",
    "summary": "In this chapter, the protagonist faces..."
  }
]
``` 

You can run the script from the command line using:
```bash
ruby storyline_search.rb --file path_to_your_json_file.json --keyword "search_term"
```
