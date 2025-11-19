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

# AthletePerformanceMetrics calculates and tracks the average performance metrics
# of athletes over time, focusing on their growth.
class AthletePerformanceMetrics
  # Initializes the AthletePerformanceMetrics with an empty list of athletes.
  def initialize
    @athletes = {}
  end

  # Adds or updates an athlete's performance metrics for a specific date.
  #
  # @param athlete_id [String] Unique identifier for the athlete
  # @param date [Date] The date of the performance metrics
  # @param metrics [Hash] Performance metrics (e.g., { speed: 10, strength: 5 })
  # @raise [ArgumentError] if metrics is empty or date is invalid
  def add_metrics(athlete_id, date, metrics)
    raise ArgumentError, 'Metrics cannot be empty' if metrics.empty?
    raise ArgumentError, 'Invalid date' unless date.respond_to?(:to_date)

    @athletes[athlete_id] ||= {}
    @athletes[athlete_id][date.to_date] = metrics
  end

  # Calculates the average performance metrics for a specific athlete over time.
  #
  # @param athlete_id [String] Unique identifier for the athlete
  # @return [Hash] Average metrics (e.g., { speed: 8.5, strength: 6.0 })
  # @raise [KeyError] if athlete_id is not found
  def average_metrics_for_athlete(athlete_id)
    athlete_data = @athletes.fetch(athlete_id) { raise KeyError, "Athlete #{athlete_id} not found" }
    return {} if athlete_data.empty?

    sum_metrics = athlete_data.values.each_with_object({}) do |metrics, sum|
      metrics.each { |k, v| sum[k] ||= 0; sum[k] += v }
    end

    count = athlete_data.size.to_f
    sum_metrics.transform_values { |v| v / count }
  end

  # Calculates the overall average performance metrics across all athletes.
  #
  # @return [Hash] Average metrics (e.g., { speed: 7.5, strength: 5.5 })
  def overall_average_metrics
    return {} if @athletes.empty?

    sum_metrics = {}
    total_entries = 0

    @athletes.each_value do |dates|
      dates.each_value do |metrics|
        metrics.each { |k, v| sum_metrics[k] ||= 0; sum_metrics[k] += v }
        total_entries += 1
      end
    end

    return {} if total_entries.zero?

    sum_metrics.transform_values { |v| v.to_f / total_entries }
  end

  # Calculates the growth rate of a specific metric for an athlete over time.
  #
  # @param athlete_id [String] Unique identifier for the athlete
  # @param metric [Symbol] The metric to calculate growth for (e.g., :speed)
  # @return [Float] Growth rate (percentage increase per entry)
  # @raise [KeyError] if athlete_id or metric is not found
  def growth_rate_for_metric(athlete_id, metric)
    athlete_data = @athletes.fetch(athlete_id) { raise KeyError, "Athlete #{athlete_id} not found" }
    raise KeyError, "No data for athlete #{athlete_id}" if athlete_data.empty?

    sorted_dates = athlete_data.keys.sort
    raise KeyError, "Metric #{metric} not found for athlete #{athlete_id}" unless athlete_data.values.first.key?(metric)

    values = sorted_dates.map { |date| athlete_data[date][metric] }
    return 0.0 if values.size <= 1

    initial_value = values.first.to_f
    final_value = values.last.to_f
    ((final_value - initial_value) / initial_value) * 100
  end
end
```
