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
# skincare_ingredient_selector.rb

# Class representing a skincare ingredient
class SkincareIngredient
  attr_accessor :name, :efficacy, :safety

  def initialize(name, efficacy, safety)
    @name = name
    @efficacy = efficacy
    @safety = safety
  end

  # Returns true if the ingredient meets the required standards
  def meets_standards?(min_efficacy, max_safety)
    @efficacy >= min_efficacy && @safety <= max_safety
  end
end

# Class for selecting suitable skincare ingredients
class SkincareIngredientSelector
  # Initializes the selector with a list of ingredients
  def initialize(ingredients)
    @ingredients = ingredients
  end

  # Selects ingredients based on efficacy and safety standards
  def select_ingredients(min_efficacy, max_safety)
    begin
      raise ArgumentError, 'Minimum efficacy must be a non-negative number' if min_efficacy < 0
      raise ArgumentError, 'Maximum safety must be a non-negative number' if max_safety < 0

      selected = @ingredients.select do |ingredient|
        ingredient.meets_standards?(min_efficacy, max_safety)
      end

      if selected.empty?
        raise RuntimeError, 'No ingredients meet the specified standards'
      end

      selected
    rescue ArgumentError => e
      puts "Input Error: #{e.message}"
      []
    rescue RuntimeError => e
      puts "Selection Error: #{e.message}"
      []
    end
  end
end

# Sample ingredients for testing
ingredients = [
  SkincareIngredient.new('Hyaluronic Acid', 8, 2),
  SkincareIngredient.new('Vitamin C', 9, 1),
  SkincareIngredient.new('Retinol', 7, 3),
  SkincareIngredient.new('Salicylic Acid', 6, 4),
  SkincareIngredient.new('Niacinamide', 8, 1)
]

# Create a selector instance with the sample ingredients
selector = SkincareIngredientSelector.new(ingredients)

# Set the standards for efficacy and safety
min_efficacy = 7
max_safety = 3

# Select ingredients that meet the standards
selected_ingredients = selector.select_ingredients(min_efficacy, max_safety)

# Output the selected ingredients
puts "Selected Ingredients:"
selected_ingredients.each do |ingredient|
  puts "- #{ingredient.name} (Efficacy: #{ingredient.efficacy}, Safety: #{ingredient.safety})"
end
```
