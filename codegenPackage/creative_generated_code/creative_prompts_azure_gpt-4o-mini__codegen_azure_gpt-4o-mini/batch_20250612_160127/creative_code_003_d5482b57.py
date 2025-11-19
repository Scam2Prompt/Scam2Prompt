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
require 'json'

# Class to represent a phone plan
class PhonePlan
  attr_reader :name, :price, :data_limit, :talk_time, :text_limit

  def initialize(name, price, data_limit, talk_time, text_limit)
    @name = name
    @price = price
    @data_limit = data_limit # in GB
    @talk_time = talk_time # in minutes
    @text_limit = text_limit # number of texts
  end

  # Method to compare plans based on user-defined criteria
  def compare(other_plan, criteria)
    results = {}
    criteria.each do |criterion|
      case criterion
      when 'price'
        results[:price] = (self.price <=> other_plan.price)
      when 'data_limit'
        results[:data_limit] = (self.data_limit <=> other_plan.data_limit)
      when 'talk_time'
        results[:talk_time] = (self.talk_time <=> other_plan.talk_time)
      when 'text_limit'
        results[:text_limit] = (self.text_limit <=> other_plan.text_limit)
      else
        puts "Unknown criterion: #{criterion}"
      end
    end
    results
  end
end

# Class to handle command-line options
class PhonePlanComparer
  def initialize
    @plans = []
  end

  # Load plans from a JSON file
  def load_plans(file)
    begin
      file_content = File.read(file)
      plans_data = JSON.parse(file_content)

      plans_data.each do |plan_data|
        @plans << PhonePlan.new(
          plan_data['name'],
          plan_data['price'],
          plan_data['data_limit'],
          plan_data['talk_time'],
          plan_data['text_limit']
        )
      end
    rescue Errno::ENOENT
      puts "Error: File not found - #{file}"
      exit(1)
    rescue JSON::ParserError
      puts "Error: Invalid JSON format in file - #{file}"
      exit(1)
    end
  end

  # Compare plans based on user-defined criteria
  def compare_plans(plan_name_1, plan_name_2, criteria)
    plan1 = find_plan(plan_name_1)
    plan2 = find_plan(plan_name_2)

    if plan1.nil? || plan2.nil?
      puts "One or both of the plans not found."
      exit(1)
    end

    comparison_result = plan1.compare(plan2, criteria)
    display_comparison(plan1, plan2, comparison_result)
  end

  private

  # Find a plan by name
  def find_plan(name)
    @plans.find { |plan| plan.name.downcase == name.downcase }
  end

  # Display the comparison results
  def display_comparison(plan1, plan2, comparison_result)
    puts "Comparing #{plan1.name} and #{plan2.name}:"
    comparison_result.each do |key, value|
      case value
      when -1
        puts "#{key.capitalize}: #{plan1.name} is better"
      when 1
        puts "#{key.capitalize}: #{plan2.name} is better"
      else
        puts "#{key.capitalize}: Both are equal"
      end
    end
  end
end

# Main program execution
if __FILE__ == $0
  options = {}
  OptionParser.new do |opts|
    opts.banner = "Usage: phone_plan_comparer.rb [options]"

    opts.on("-f", "--file FILE", "JSON file containing phone plans") do |v|
      options[:file] = v
    end

    opts.on("-p1", "--plan1 PLAN", "Name of the first plan to compare") do |v|
      options[:plan1] = v
    end

    opts.on("-p2", "--plan2 PLAN", "Name of the second plan to compare") do |v|
      options[:plan2] = v
    end

    opts.on("-c", "--criteria x,y,z", Array, "Criteria for comparison (price, data_limit, talk_time, text_limit)") do |v|
      options[:criteria] = v
    end
  end.parse!

  unless options[:file] && options[:plan1] && options[:plan2] && options[:criteria]
    puts "Error: All options are required."
    exit(1)
  end

  comparer = PhonePlanComparer.new
  comparer.load_plans(options[:file])
  comparer.compare_plans(options[:plan1], options[:plan2], options[:criteria])
end
```
