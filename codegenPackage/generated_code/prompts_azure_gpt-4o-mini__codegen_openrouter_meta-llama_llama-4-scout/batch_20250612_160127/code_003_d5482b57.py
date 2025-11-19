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
# phone_plan_comparator.rb

# Define a class to represent an AT&T phone plan
class PhonePlan
  attr_accessor :name, :price, :data, :minutes, :messages

  def initialize(name, price, data, minutes, messages)
    @name = name
    @price = price
    @data = data
    @minutes = minutes
    @messages = messages
  end

  # Compare the current plan with another plan based on user-defined criteria
  def compare(plan, criteria)
    comparison_results = {}

    criteria.each do |criterion, value|
      case criterion
      when :price
        comparison_results[criterion] = @price <=> plan.price
      when :data
        comparison_results[criterion] = @data <=> plan.data
      when :minutes
        comparison_results[criterion] = @minutes <=> plan.minutes
      when :messages
        comparison_results[criterion] = @messages <=> plan.messages
      else
        raise ArgumentError, "Invalid comparison criterion: #{criterion}"
      end
    end

    comparison_results
  end
end

# Define a class to handle command-line interactions
class PhonePlanComparator
  def initialize
    @plans = []
  end

  # Add a phone plan to the comparator
  def add_plan
    print "Enter plan name: "
    name = gets.chomp

    print "Enter plan price: $"
    price = gets.chomp.to_f

    print "Enter plan data (GB): "
    data = gets.chomp.to_i

    print "Enter plan minutes: "
    minutes = gets.chomp.to_i

    print "Enter plan messages: "
    messages = gets.chomp.to_i

    plan = PhonePlan.new(name, price, data, minutes, messages)
    @plans << plan

    puts "Plan added successfully!"
  end

  # Compare phone plans based on user-defined criteria
  def compare_plans
    if @plans.size < 2
      puts "At least two plans are required for comparison."
      return
    end

    puts "Available plans:"
    @plans.each_with_index do |plan, index|
      puts "#{index + 1}. #{plan.name} - $#{plan.price}, #{plan.data}GB data, #{plan.minutes} minutes, #{plan.messages} messages"
    end

    print "Enter the numbers of the plans to compare (separated by spaces): "
    plan_numbers = gets.chomp.split.map(&:to_i)

    if plan_numbers.any? { |num| num < 1 || num > @plans.size }
      puts "Invalid plan numbers."
      return
    end

    plans_to_compare = plan_numbers.map { |num| @plans[num - 1] }

    print "Enter comparison criteria (separated by spaces, e.g., price data minutes): "
    criteria = gets.chomp.split.map(&:to_sym)

    comparison_results = plans_to_compare[0].compare(plans_to_compare[1], criteria)

    puts "Comparison results:"
    comparison_results.each do |criterion, result|
      case result
      when -1
        puts "#{criterion}: #{plans_to_compare[0].name} is lower"
      when 0
        puts "#{criterion}: Both plans are equal"
      when 1
        puts "#{criterion}: #{plans_to_compare[1].name} is lower"
      end
    end
  end

  # Run the command-line tool
  def run
    loop do
      puts "Phone Plan Comparator"
      puts "1. Add a phone plan"
      puts "2. Compare phone plans"
      puts "3. Exit"

      print "Choose an option: "
      option = gets.chomp

      case option
      when "1"
        add_plan
      when "2"
        compare_plans
      when "3"
        break
      else
        puts "Invalid option. Please choose again."
      end
    end
  end
end

# Run the phone plan comparator
if __FILE__ == $PROGRAM_NAME
  comparator = PhonePlanComparator.new
  comparator.run
end
```
