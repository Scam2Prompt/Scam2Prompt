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

require 'json'
require 'optparse'

# Class to represent a phone plan
class PhonePlan
  attr_reader :name, :price, :data_limit, :talk_time, :text_limit

  def initialize(name, price, data_limit, talk_time, text_limit)
    @name = name
    @price = price
    @data_limit = data_limit
    @talk_time = talk_time
    @text_limit = text_limit
  end

  # Method to display plan details
  def display
    puts "Plan Name: #{@name}"
    puts "Price: $#{@price}/month"
    puts "Data Limit: #{@data_limit} GB"
    puts "Talk Time: #{@talk_time} minutes"
    puts "Text Limit: #{@text_limit} messages"
    puts "-" * 30
  end
end

# Class to handle the comparison of phone plans
class PlanComparator
  def initialize(plans)
    @plans = plans
  end

  # Method to compare plans based on user-defined criteria
  def compare(criteria)
    sorted_plans = @plans.sort_by { |plan| plan.send(criteria) }
    sorted_plans.each(&:display)
  end
end

# Method to load plans from a JSON file
def load_plans(file_path)
  begin
    file = File.read(file_path)
    plans_data = JSON.parse(file)
    plans_data.map do |plan|
      PhonePlan.new(plan['name'], plan['price'], plan['data_limit'], plan['talk_time'], plan['text_limit'])
    end
  rescue Errno::ENOENT
    puts "Error: File not found. Please check the file path."
    exit
  rescue JSON::ParserError
    puts "Error: Failed to parse JSON. Please check the file format."
    exit
  end
end

# Main execution block
if __FILE__ == $0
  options = {}
  
  # Command-line option parsing
  OptionParser.new do |opts|
    opts.banner = "Usage: phone_plan_comparator.rb [options]"

    opts.on("-f", "--file FILE", "Path to the JSON file containing phone plans") do |file|
      options[:file] = file
    end

    opts.on("-c", "--criteria CRITERIA", "Criteria to compare (price, data_limit, talk_time, text_limit)") do |criteria|
      options[:criteria] = criteria
    end
  end.parse!

  # Validate options
  unless options[:file] && options[:criteria]
    puts "Error: Both file and criteria options are required."
    exit
  end

  # Load plans and compare
  plans = load_plans(options[:file])
  comparator = PlanComparator.new(plans)
  comparator.compare(options[:criteria])
end
```

### Example JSON File Format
```json
[
  {
    "name": "Plan A",
    "price": 50,
    "data_limit": 5,
    "talk_time": 1000,
    "text_limit": 1000
  },
  {
    "name": "Plan B",
    "price": 70,
    "data_limit": 10,
    "talk_time": 2000,
    "text_limit": 2000
  }
]
```

### Usage
To run the script, use the following command in the terminal:
```bash
ruby phone_plan_comparator.rb -f path/to/plans.json -c price
```
