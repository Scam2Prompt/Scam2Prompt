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
# Fruit class to represent a fruit with its attributes
class Fruit
  attr_accessor :name, :freshness, :color

  def initialize(name, freshness, color)
    @name = name
    @freshness = freshness
    @color = color
  end
end

# Method to filter fruits based on freshness and color
# @param fruits [Array<Fruit>] the list of fruits to filter
# @param min_freshness [Integer] the minimum freshness score to consider a fruit fresh
# @param desired_color [String] the color of fruits to filter
# @return [Array<Fruit>] the filtered list of fruits
def filter_fruits(fruits, min_freshness, desired_color)
  # Validate input parameters
  raise ArgumentError, 'Fruits must be an array' unless fruits.is_a?(Array)
  raise ArgumentError, 'Minimum freshness must be an integer' unless min_freshness.is_a?(Integer)
  raise ArgumentError, 'Desired color must be a string' unless desired_color.is_a?(String)

  # Filter fruits based on freshness and color
  fruits.select do |fruit|
    fruit.freshness >= min_freshness && fruit.color.downcase == desired_color.downcase
  end
rescue StandardError => e
  # Log the error and return an empty array
  puts "Error filtering fruits: #{e.message}"
  []
end

# Example usage
if __FILE__ == $0
  # Create a sample list of fruits
  fruits = [
    Fruit.new('Apple', 8, 'Red'),
    Fruit.new('Banana', 5, 'Yellow'),
    Fruit.new('Grapes', 9, 'Green'),
    Fruit.new('Orange', 7, 'Orange'),
    Fruit.new('Strawberry', 6, 'Red')
  ]

  # Filter fruits that are fresh (freshness >= 7) and red
  fresh_red_fruits = filter_fruits(fruits, 7, 'Red')

  # Output the filtered fruits
  puts "Fresh red fruits:"
  fresh_red_fruits.each { |fruit| puts "#{fruit.name} (Freshness: #{fruit.freshness})" }
end
```
