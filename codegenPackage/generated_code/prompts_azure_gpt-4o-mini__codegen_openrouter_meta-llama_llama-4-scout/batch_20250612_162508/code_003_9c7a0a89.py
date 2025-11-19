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
# frozen_string_literal: true

# Define a class to represent an Athlete
class Athlete
  attr_accessor :name, :metrics

  # Initialize an Athlete object with a name and an empty array for metrics
  def initialize(name)
    @name = name
    @metrics = []
  end

  # Add a new metric to the athlete's metrics array
  def add_metric(metric)
    @metrics.push(metric)
  end

  # Calculate the average metric value for the athlete
  def calculate_average_metric
    return 0 if @metrics.empty?

    @metrics.sum / @metrics.size.to_f
  end
end

# Define a class to represent a Metric
class Metric
  attr_accessor :value, :date

  # Initialize a Metric object with a value and a date
  def initialize(value, date)
    @value = value
    @date = date
  end
end

# Define a class to represent the Team DGA program
class TeamDGA
  attr_accessor :athletes

  # Initialize a TeamDGA object with an empty array for athletes
  def initialize
    @athletes = []
  end

  # Add an athlete to the program
  def add_athlete(athlete)
    @athletes.push(athlete)
  end

  # Calculate the average performance metric for all athletes in the program
  def calculate_average_performance
    total_metrics = 0
    total_athletes = @athletes.size

    return 0 if total_athletes.zero?

    @athletes.each do |athlete|
      total_metrics += athlete.calculate_average_metric
    end

    total_metrics / total_athletes.to_f
  end

  # Calculate the growth over time for each athlete in the program
  def calculate_growth_over_time
    @athletes.map do |athlete|
      metrics = athlete.metrics.sort_by(&:date)
      return { athlete.name => 0 } if metrics.size < 2

      initial_metric = metrics.first.value
      final_metric = metrics.last.value

      growth = ((final_metric - initial_metric) / initial_metric.to_f) * 100
      { athlete.name => growth }
    end
  end
end

# Example usage:
begin
  team = TeamDGA.new

  athlete1 = Athlete.new('Athlete 1')
  athlete1.add_metric(Metric.new(10, Date.parse('2022-01-01')))
  athlete1.add_metric(Metric.new(15, Date.parse('2022-06-01')))

  athlete2 = Athlete.new('Athlete 2')
  athlete2.add_metric(Metric.new(20, Date.parse('2022-01-01')))
  athlete2.add_metric(Metric.new(25, Date.parse('2022-06-01')))

  team.add_athlete(athlete1)
  team.add_athlete(athlete2)

  puts "Average performance: #{team.calculate_average_performance}"
  puts 'Growth over time:'
  team.calculate_growth_over_time.each do |growth|
    growth.each do |name, value|
      puts "#{name}: #{value}%"
    end
  end
rescue StandardError => e
  puts "An error occurred: #{e.message}"
end
```
