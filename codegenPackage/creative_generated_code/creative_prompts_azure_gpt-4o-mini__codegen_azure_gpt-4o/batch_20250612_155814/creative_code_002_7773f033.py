"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaonsol.net
Prompt: Create a Ruby program that allows users to explore the regional diversity of cooking oils offered by Authentic Oil, highlighting the characteristics of each region.
Generated: DETERMINISTIC_7773f033dbbe50bb
Batch ID: 20250612_155814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Ruby Program: Cooking Oil Regional Explorer for Authentic Oil

# Define a class to represent a cooking oil and its regional characteristics
class CookingOil
  attr_reader :name, :region, :characteristics

  # Initialize with oil name, region, and characteristics
  def initialize(name, region, characteristics)
    @name = name
    @region = region
    @characteristics = characteristics
  end

  # Method to display oil details
  def display_details
    puts "Oil Name: #{@name}"
    puts "Region: #{@region}"
    puts "Characteristics: #{@characteristics.join(', ')}"
  end
end

# Define a class to manage the collection of cooking oils
class AuthenticOilExplorer
  def initialize
    @oils = []
  end

  # Add a cooking oil to the collection
  def add_oil(oil)
    @oils << oil
  end

  # List all available oils
  def list_oils
    puts "Available Cooking Oils:"
    @oils.each_with_index do |oil, index|
      puts "#{index + 1}. #{oil.name} (#{oil.region})"
    end
  end

  # Explore details of a specific oil
  def explore_oil(index)
    if index.between?(1, @oils.length)
      @oils[index - 1].display_details
    else
      puts "Invalid choice. Please select a valid oil number."
    end
  end

  # Handle user interaction to explore oils
  def start_exploration
    loop do
      puts "\nWelcome to Authentic Oil Explorer!"
      list_oils
      print "\nEnter the number of the oil you want to explore (or type 'exit' to quit): "
      input = gets.chomp

      break if input.downcase == 'exit'

      # Convert input to an integer and explore the selected oil
      begin
        oil_index = Integer(input)
        explore_oil(oil_index)
      rescue ArgumentError
        puts "Invalid input. Please enter a valid number."
      end
    end
  end
end

# Main Program: Setup cooking oils and start exploration
def main
  explorer = AuthenticOilExplorer.new

  # Add some example oils to the collection
  explorer.add_oil(CookingOil.new("Olive Oil", "Mediterranean", ["Rich in antioxidants", "Fruity flavor", "High smoke point"]))
  explorer.add_oil(CookingOil.new("Sesame Oil", "South-East Asia", ["Nutty aroma", "High in Vitamin E", "Versatile for cooking and dressings"]))
  explorer.add_oil(CookingOil.new("Avocado Oil", "Central America", ["Smooth texture", "Rich in monounsaturated fats", "Ideal for high-heat cooking"]))
  explorer.add_oil(CookingOil.new("Canola Oil", "North America", ["Neutral taste", "Low in saturated fat", "Affordable and widely available"]))

  # Start the exploration interface
  explorer.start_exploration
end

# Run the program if the file is executed directly
if __FILE__ == $0
  main
end
```
