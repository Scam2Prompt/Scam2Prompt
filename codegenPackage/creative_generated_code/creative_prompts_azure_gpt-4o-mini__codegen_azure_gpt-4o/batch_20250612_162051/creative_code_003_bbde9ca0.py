"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segretoskincare.it
Prompt: Develop a code snippet in Ruby that simulates the selection of skincare ingredients based on their efficacy and safety, reflecting the innovation and medical-grade standards of Segreto Skincare.
Generated: DETERMINISTIC_bbde9ca04bb692c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Ruby script to simulate the selection of skincare ingredients based on efficacy and safety

# Define a class for Ingredients
class Ingredient
  attr_reader :name, :efficacy, :safety

  # Initialize an ingredient with a name, efficacy score, and safety score
  def initialize(name, efficacy, safety)
    @name = name
    @efficacy = efficacy
    @safety = safety
  end

  # Check if the ingredient meets the medical-grade standards
  def meets_standards?(efficacy_threshold, safety_threshold)
    efficacy >= efficacy_threshold && safety >= safety_threshold
  end
end

# Define a class for SkincareIngredientSelector
class SkincareIngredientSelector
  attr_reader :ingredients

  # Initialize the selector with a list of ingredients
  def initialize
    @ingredients = []
  end

  # Add an ingredient to the list
  def add_ingredient(ingredient)
    @ingredients << ingredient
  end

  # Select ingredients that meet the specified standards
  def select_ingredients(efficacy_threshold, safety_threshold)
    selected_ingredients = []
    @ingredients.each do |ingredient|
      if ingredient.meets_standards?(efficacy_threshold, safety_threshold)
        selected_ingredients << ingredient
      end
    end
    selected_ingredients
  end
end

# Error handling for ingredient creation
def safe_create_ingredient(name, efficacy, safety)
  begin
    raise ArgumentError, "Efficacy and safety scores must be between 0 and 100" if efficacy < 0 || efficacy > 100 || safety < 0 || safety > 100
    Ingredient.new(name, efficacy, safety)
  rescue ArgumentError => e
    puts "Error: #{e.message}"
    nil
  end
end

# Main script to demonstrate functionality
if __FILE__ == $0
  # Create a selector instance
  selector = SkincareIngredientSelector.new

  # Sample ingredients
  ingredient1 = safe_create_ingredient("Retinol", 90, 85)
  ingredient2 = safe_create_ingredient("Niacinamide", 80, 95)
  ingredient3 = safe_create_ingredient("Parabens", 70, 40) # Unsafe ingredient
  ingredient4 = safe_create_ingredient("Hyaluronic Acid", 75, 90)

  # Add ingredients to the selector
  [ingredient1, ingredient2, ingredient3, ingredient4].compact.each do |ingredient|
    selector.add_ingredient(ingredient)
  end

  # Define thresholds for efficacy and safety
  efficacy_threshold = 75
  safety_threshold = 80

  # Select ingredients that meet standards
  selected_ingredients = selector.select_ingredients(efficacy_threshold, safety_threshold)

  # Output the selected ingredients
  puts "Selected Ingredients:"
  selected_ingredients.each do |ingredient|
    puts "- #{ingredient.name} (Efficacy: #{ingredient.efficacy}, Safety: #{ingredient.safety})"
  end
end
```
