"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamdga.com
Prompt: Develop a code snippet in Ruby that calculates the average performance metrics of athletes participating in a program like Team DGA, focusing on their growth over time.
Generated: DETERMINISTIC_9c7a0a89eea5a385
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Ruby Program to Calculate Average Performance Metrics and Growth Over Time

# Athlete class to store individual data
class Athlete
  attr_reader :name, :performance_metrics

  # Initialize an athlete with a name and performance metrics (array of numbers)
  def initialize(name, performance_metrics)
    @name = name
    @performance_metrics = performance_metrics
  end

  # Calculate the average performance of the athlete
  def average_performance
    return 0 if @performance_metrics.empty?

    @performance_metrics.sum.to_f / @performance_metrics.size
  end

  # Calculate growth over time as percentage change between the first and last metric
  def growth_over_time
    return 0 if @performance_metrics.size < 2

    first_metric = @performance_metrics.first
    last_metric = @performance_metrics.last
    return 0 if first_metric.zero?

    ((last_metric - first_metric) / first_metric.to_f) * 100
  end
end

# Program class to manage multiple athletes and calculate statistics
class TeamPerformance
  def initialize(athletes)
    @athletes = athletes
  end

  # Calculate the average performance across all athletes
  def average_team_performance
    return 0 if @athletes.empty?

    total_performance = @athletes.sum { |athlete| athlete.average_performance }
    total_performance.to_f / @athletes.size
  end

  # Calculate the average growth across all athletes
  def average_team_growth
    return 0 if @athletes.empty?

    total_growth = @athletes.sum { |athlete| athlete.growth_over_time }
    total_growth.to_f / @athletes.size
  end
end

# Error handling for invalid input data
def validate_metrics(metrics)
  unless metrics.is_a?(Array) && metrics.all? { |m| m.is_a?(Numeric) }
    raise ArgumentError, 'Performance metrics must be an array of numbers.'
  end
end

# Sample Data
begin
  athlete1 = Athlete.new('Alice', [10, 15, 20, 25])
  athlete2 = Athlete.new('Bob', [20, 25, 30])
  athlete3 = Athlete.new('Charlie', [5, 10, 15, 20, 25])

  validate_metrics(athlete1.performance_metrics)
  validate_metrics(athlete2.performance_metrics)
  validate_metrics(athlete3.performance_metrics)

  athletes = [athlete1, athlete2, athlete3]
  team_performance = TeamPerformance.new(athletes)

  puts "Average Team Performance: #{team_performance.average_team_performance.round(2)}"
  puts "Average Team Growth: #{team_performance.average_team_growth.round(2)}%"
rescue ArgumentError => e
  puts "Error: #{e.message}"
end
```
