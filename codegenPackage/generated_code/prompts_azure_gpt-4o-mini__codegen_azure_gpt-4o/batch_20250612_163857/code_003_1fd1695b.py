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
# Ruby script to filter a list of fruits based on freshness and color

# Define a Fruit class to encapsulate fruit properties
class Fruit
  attr_reader :name, :freshness, :color

  # Initialize a fruit with name, freshness, and color attributes
  def initialize(name, freshness, color)
    @name = name
    @freshness = freshness
    @color = color
  end
end

# Method to filter fruits based on freshness and color criteria
def filter_fruits(fruits, freshness_threshold, desired_color)
  # Validate input parameters
  raise ArgumentError, 'Fruits must be an array of Fruit objects' unless fruits.is_a?(Array) && fruits.all? { |f| f.is_a?(Fruit) }
  raise ArgumentError, 'Freshness threshold must be a number' unless freshness_threshold.is_a?(Numeric)
  raise ArgumentError, 'Desired color must be a string' unless desired_color.is_a?(String)

  # Filter fruits based on the given criteria
  fruits.select do |fruit|
    fruit.freshness >= freshness_threshold && fruit.color.downcase == desired_color.downcase
  end
end

# Example usage:

# Create a list of fruits
fruits = [
  Fruit.new('Apple', 8, 'Red'),
  Fruit.new('Banana', 5, 'Yellow'),
  Fruit.new('Cherry', 9, 'Red'),
  Fruit.new('Grape', 7, 'Purple'),
  Fruit.new('Orange', 6, 'Orange')
]

# Define filtering criteria
freshness_threshold = 7
desired_color = 'Red'

# Filter fruits based on criteria
begin
  selected_fruits = filter_fruits(fruits, freshness_threshold, desired_color)

  # Output the filtered fruits
  puts 'Selected Fruits:'
  selected_fruits.each { |fruit| puts "#{fruit.name} (Freshness: #{fruit.freshness}, Color: #{fruit.color})" }
rescue ArgumentError => e
  # Handle invalid input errors
  puts "Error: #{e.message}"
end
```
