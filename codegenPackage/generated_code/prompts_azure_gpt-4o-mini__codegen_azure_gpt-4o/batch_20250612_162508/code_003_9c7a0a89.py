"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Develop a code snippet in Ruby that calculates the average performance metrics of athletes participating in a program like Team DGA, focusing on their growth over time.
Generated: DETERMINISTIC_9c7a0a89eea5a385
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# Ruby script to calculate the average performance metrics of athletes
# and track their growth over time.

# Define a class to represent an Athlete
class Athlete
  attr_accessor :name, :performance_metrics

  # Initialize an athlete with a name and an array of performance metrics
  def initialize(name, performance_metrics = [])
    @name = name
    @performance_metrics = performance_metrics
  end

  # Calculate the average performance metric for the athlete
  def average_performance
    return 0 if @performance_metrics.empty?

    @performance_metrics.sum.to_f / @performance_metrics.size
  end

  # Calculate the growth percentage over time
  def growth_percentage
    return 0 if @performance_metrics.size < 2

    initial = @performance_metrics.first
    final = @performance_metrics.last
    return 0 if initial == 0 # Avoid division by zero

    ((final - initial).to_f / initial * 100).round(2)
  end
end

# Define a method to calculate the overall average performance of all athletes
def overall_average_performance(athletes)
  return 0 if athletes.empty?

  total_performance = athletes.map(&:average_performance).sum
  (total_performance / athletes.size).round(2)
end

# Sample data for athletes
athletes = [
  Athlete.new("Alice", [10, 15, 20, 25]),
  Athlete.new("Bob", [5, 10, 15, 20]),
  Athlete.new("Charlie", [8, 12, 16, 20])
]

# Calculate and display individual metrics
athletes.each do |athlete|
  puts "Athlete: #{athlete.name}"
  puts "  Average Performance: #{athlete.average_performance}"
  puts "  Growth Percentage: #{athlete.growth_percentage}%"
end

# Calculate and display overall average performance
puts "\nOverall Average Performance: #{overall_average_performance(athletes)}"
```
