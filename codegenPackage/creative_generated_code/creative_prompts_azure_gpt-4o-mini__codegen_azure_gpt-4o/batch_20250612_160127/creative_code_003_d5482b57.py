"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-graph.net
Prompt: Develop a command-line tool in Ruby that allows users to compare AT&T phone plans based on user-defined criteria.
Generated: DETERMINISTIC_d5482b571efc540d
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby

require 'optparse'

# Define the phone plans for comparison
PLANS = [
  { name: 'Unlimited Starter', price: 65, data: 'Unlimited', hotspot: false, perks: 'None' },
  { name: 'Unlimited Extra', price: 75, data: 'Unlimited', hotspot: true, perks: '15GB hotspot' },
  { name: 'Unlimited Elite', price: 85, data: 'Unlimited', hotspot: true, perks: '40GB hotspot, HBO Max' },
  { name: 'Value Plus', price: 50, data: 'Unlimited', hotspot: false, perks: 'None' }
].freeze

# Error class for invalid criteria
class InvalidCriteriaError < StandardError; end

# Function to filter plans based on criteria
def filter_plans(criteria)
  PLANS.select do |plan|
    criteria.all? do |key, value|
      plan[key] == value || 
      (plan[key].is_a?(Numeric) && plan[key] <= value) || 
      (value == true && plan[key] == true)
    end
  end
end

# Parse command-line options
options = {}
OptionParser.new do |opts|
  opts.banner = 'Usage: phone_plan_comparator.rb [options]'

  opts.on('--price-max PRICE', Float, 'Maximum price for the plan') do |price|
    options[:price] = price
  end

  opts.on('--hotspot', 'Require hotspot availability') do
    options[:hotspot] = true
  end

  opts.on('--perks PERKS', String, 'Specific perks required (e.g., HBO Max)') do |perks|
    options[:perks] = perks
  end

  opts.on('--help', 'Display help information') do
    puts opts
    exit
  end
end.parse!

begin
  # Validate criteria
  unless options.keys.any?
    raise InvalidCriteriaError, 'Please specify at least one search criteria.'
  end

  # Filter plans based on user-defined criteria
  filtered_plans = filter_plans(options)

  # Display results
  if filtered_plans.any?
    puts 'Matching Phone Plans:'
    filtered_plans.each do |plan|
      puts "Name: #{plan[:name]}, Price: $#{plan[:price]}, Data: #{plan[:data]}, Hotspot: #{plan[:hotspot]}, Perks: #{plan[:perks]}"
    end
  else
    puts 'No matching plans found based on the provided criteria.'
  end
rescue InvalidCriteriaError => e
  puts "Error: #{e.message}"
rescue StandardError => e
  puts "An unexpected error occurred: #{e.message}"
end
```

This script allows users to compare AT&T phone plans based on their criteria, using command-line options to specify preferences. To use, save this code in a file (e.g., `phone_plan_comparator.rb`), and run it with options such as `--price-max` or `--hotspot`.
