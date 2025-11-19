"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wenwendrop.com
Prompt: Develop a code snippet in Ruby that filters a list of fruits based on their freshness and color, ensuring only the best quality fruits are selected.
Generated: DETERMINISTIC_1fd1695bf1a54f36
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# fruit_filter.rb

# Class representing a Fruit with its attributes: name, freshness, and color
class Fruit
  attr_accessor :name, :freshness, :color

  def initialize(name, freshness, color)
    @name = name
    @freshness = freshness
    @color = color
  end
end

# Method to filter fruits based on freshness and color
# 
# @param fruits [Array<Fruit>] - An array of Fruit objects to filter
# @param min_freshness [Integer] - Minimum freshness level (1 to 10)
# @param desired_color [String] - Color of fruits to filter
# @return [Array<Fruit>] - Array of filtered fruits
def filter_fruits(fruits, min_freshness, desired_color)
  # Validate inputs
  raise ArgumentError, 'Fruits must be an array' unless fruits.is_a?(Array)
  raise ArgumentError, 'Minimum freshness must be an integer' unless min_freshness.is_a?(Integer)
  raise ArgumentError, 'Desired color must be a string' unless desired_color.is_a?(String)

  # Filter fruits based on freshness and color
  fruits.select do |fruit|
    fruit.freshness >= min_freshness && fruit.color.downcase == desired_color.downcase
  end
rescue StandardError => e
  puts "An error occurred: #{e.message}"
  []
end

# Example usage
if __FILE__ == $PROGRAM_NAME
  # Create a sample array of fruits
  fruits = [
    Fruit.new('Apple', 8, 'Red'),
    Fruit.new('Banana', 5, 'Yellow'),
    Fruit.new('Orange', 9, 'Orange'),
    Fruit.new('Kiwi', 6, 'Green'),
    Fruit.new('Grapes', 7, 'Red')
  ]

  # Filtering fruits that have a freshness of at least 7 and are Red
  begin
    filtered_fruits = filter_fruits(fruits, 7, 'Red')
    puts "Filtered Fruits: #{filtered_fruits.map(&:name).join(', ')}"
  rescue StandardError => e
    puts "Failed to filter fruits: #{e.message}"
  end
end
```
