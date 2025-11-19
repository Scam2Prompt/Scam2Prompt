"""
Generated Code Metadata:
========================
Original URL: https://token-graph.net
Prompt: Develop a command-line tool in Ruby that allows users to compare AT&T phone plans based on user-defined criteria.
Generated: DETERMINISTIC_d5482b571efc540d
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
#!/usr/bin/env ruby

require 'optparse'
require 'json'

# Define a list of AT&T phone plans for comparison
PHONE_PLANS = [
  { name: 'Basic Plan', price: 30, data: 5, talk: 'Unlimited', text: 'Unlimited' },
  { name: 'Standard Plan', price: 50, data: 15, talk: 'Unlimited', text: 'Unlimited' },
  { name: 'Premium Plan', price: 70, data: 50, talk: 'Unlimited', text: 'Unlimited' },
  { name: 'Family Plan', price: 100, data: 100, talk: 'Unlimited', text: 'Unlimited' }
]

# Function to filter plans based on user-defined criteria
def filter_plans(criteria)
  PHONE_PLANS.select do |plan|
    criteria.all? do |key, value|
      plan[key].is_a?(Numeric) ? plan[key] >= value : plan[key] == value
    end
  end
end

# Function to display plans in a user-friendly format
def display_plans(plans)
  if plans.empty?
    puts "No plans match your criteria."
  else
    puts "Matching Plans:"
    plans.each do |plan|
      puts "Name: #{plan[:name]}"
      puts "Price: $#{plan[:price]} per month"
      puts "Data: #{plan[:data]} GB"
      puts "Talk: #{plan[:talk]}"
      puts "Text: #{plan[:text]}"
      puts "-" * 40
    end
  end
end

# Main script logic
begin
  options = {}
  OptionParser.new do |opts|
    opts.banner = "Usage: phone_plan_comparator.rb [options]"

    opts.on("-pPRICE", "--price=PRICE", Integer, "Minimum price (in dollars)") do |price|
      options[:price] = price
    end

    opts.on("-dDATA", "--data=DATA", Integer, "Minimum data (in GB)") do |data|
      options[:data] = data
    end

    opts.on("-tTALK", "--talk=TALK", String, "Talk plan (e.g., 'Unlimited')") do |talk|
      options[:talk] = talk
    end

    opts.on("-xTEXT", "--text=TEXT", String, "Text plan (e.g., 'Unlimited')") do |text|
      options[:text] = text
    end

    opts.on("-h", "--help", "Display help information") do
      puts opts
      exit
    end
  end.parse!

  # Filter plans based on user-defined criteria
  matching_plans = filter_plans(options)

  # Display the matching plans
  display_plans(matching_plans)

rescue OptionParser::InvalidOption => e
  puts "Error: #{e.message}"
  puts "Use --help for usage information."
  exit 1
rescue => e
  puts "An unexpected error occurred: #{e.message}"
  exit 1
end
```
