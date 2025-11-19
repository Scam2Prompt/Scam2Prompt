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
# authentic_oil_explorer.rb

# A class representing a cooking oil and its regional characteristics
class CookingOil
  attr_reader :name, :region, :characteristics

  def initialize(name, region, characteristics)
    @name = name
    @region = region
    @characteristics = characteristics
  end

  def to_s
    "#{name} from #{region}: #{characteristics.join(', ')}"
  end
end

# A class to manage a collection of cooking oils
class OilCollection
  attr_reader :oils

  def initialize
    @oils = []
  end

  # Adds a new cooking oil to the collection
  def add_oil(oil)
    @oils << oil
  end

  # Lists all available oils in the collection
  def list_oils
    return "No oils available." if @oils.empty?

    @oils.each_with_index.map { |oil, index| "#{index + 1}. #{oil}" }.join("\n")
  end

  # Finds oils by region
  def find_oils_by_region(region)
    found_oils = @oils.select { |oil| oil.region.downcase == region.downcase }
    return "No oils found for region: #{region}" if found_oils.empty?

    found_oils.map(&:to_s).join("\n")
  end
end

# Main program execution
def main
  oils = OilCollection.new

  # Sample data: Adding diverse oils with their characteristics
  oils.add_oil(CookingOil.new("Olive Oil", "Mediterranean", ["Rich in monounsaturated fats", "Strong flavor", "Great for dressings"]))
  oils.add_oil(CookingOil.new("Coconut Oil", "Tropical", ["High in saturated fats", "Sweet aroma", "Ideal for baking"]))
  oils.add_oil(CookingOil.new("Avocado Oil", "Central America", ["High smoke point", "Neutral taste", "Rich in vitamins"]))
  oils.add_oil(CookingOil.new("Peanut Oil", "Southeast Asia", ["Nutty flavor", "High smoke point", "Perfect for frying"]))

  puts "Welcome to the Authentic Oil Explorer!"
  puts "Here are the available cooking oils:"
  puts oils.list_oils

  # User interaction to find oils by region
  print "\nEnter a region to explore its cooking oils: "
  region = gets.chomp.strip

  begin
    puts "\nSearching for oils from #{region}..."
    puts oils.find_oils_by_region(region)
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end

# Run the main program
if __FILE__ == $0
  main
end
```
