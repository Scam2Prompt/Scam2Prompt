"""
Generated Code Metadata:
========================
Original URL: https://wenwendrop.com
Prompt: Develop a code snippet in Ruby that filters a list of fruits based on their freshness and color, ensuring only the best quality fruits are selected.
Generated: DETERMINISTIC_1fd1695bf1a54f36
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

# A utility class for filtering fruits based on freshness and color criteria.
class FruitFilter
  # Initializes the FruitFilter with a list of fruits.
  # @param fruits [Array<Hash>] An array of fruit hashes with :name, :freshness, and :color keys
  def initialize(fruits)
    @fruits = fruits
    validate_input
  end

  # Filters fruits based on freshness and color criteria.
  # @param min_freshness [Integer] Minimum freshness score (1-10)
  # @param desired_colors [Array<String>] Array of acceptable color strings
  # @return [Array<Hash>] Filtered array of fruits meeting criteria
  def filter(min_freshness:, desired_colors:)
    validate_filter_params(min_freshness, desired_colors)

    @fruits.select do |fruit|
      fruit[:freshness] >= min_freshness && desired_colors.include?(fruit[:color])
    end
  end

  private

  # Validates that the input fruits array has the correct structure
  def validate_input
    unless @fruits.is_a?(Array)
      raise ArgumentError, 'Fruits must be provided as an array'
    end

    @fruits.each do |fruit|
      unless fruit.is_a?(Hash) && fruit.key?(:name) && fruit.key?(:freshness) && fruit.key?(:color)
        raise ArgumentError, 'Each fruit must be a hash with :name, :freshness, and :color keys'
      end

      unless (1..10).cover?(fruit[:freshness])
        raise ArgumentError, "Freshness score for #{fruit[:name]} must be between 1-10"
      end
    end
  end

  # Validates filter parameters
  # @param min_freshness [Integer] Minimum freshness score
  # # @param desired_colors [Array<String>] Array of color strings
  def validate_filter_params(min_freshness, desired_colors)
    unless min_freshness.is_a?(Integer) && (1..10).cover?(min_freshness)
      raise ArgumentError, 'min_freshness must be an integer between 1-10'
    end

    unless desired_colors.is_a?(Array) && desired_colors.all? { |c| c.is_a?(String) }
      raise ArgumentError, 'desired_colors must be an array of strings'
    end
  end
end

# Example usage:
# fruits = [
#   { name: 'Apple', freshness: 8, color: 'red' },
#   { name: 'Banana', freshness: 5, color: 'yellow' },
#   { name: 'Grape', freshness: 9, color: 'purple' }
# ]
# 
# filter = FruitFilter.new(fruits)
# fresh_red_fruits = filter.filter(min_freshness: 7, desired_colors: ['red'])
# puts fresh_red_fruits
```
