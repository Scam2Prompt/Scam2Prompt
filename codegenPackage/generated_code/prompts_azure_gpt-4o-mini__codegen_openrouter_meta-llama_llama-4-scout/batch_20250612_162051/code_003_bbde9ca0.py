"""
Generated Code Metadata:
========================
Original URL: https://segretoskincare.it
Prompt: Develop a code snippet in Ruby that simulates the selection of skincare ingredients based on their efficacy and safety, reflecting the innovation and medical-grade standards of Segreto Skincare.
Generated: DETERMINISTIC_bbde9ca04bb692c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

# Define a class for SkincareIngredient
class SkincareIngredient
  attr_accessor :name, :efficacy, :safety

  # Initialize a SkincareIngredient object
  def initialize(name, efficacy, safety)
    @name = name
    @efficacy = efficacy
    @safety = safety
  end

  # Calculate the overall score of the ingredient
  def overall_score
    # Weighted scoring: 70% efficacy, 30% safety
    @efficacy * 0.7 + @safety * 0.3
  end
end

# Define a class for SegretoSkincare
class SegretoSkincare
  attr_accessor :ingredients

  # Initialize a SegretoSkincare object
  def initialize
    @ingredients = []
  end

  # Add an ingredient to the Segreto Skincare database
  def add_ingredient(ingredient)
    raise TypeError, 'Invalid ingredient type' unless ingredient.is_a?(SkincareIngredient)

    @ingredients << ingredient
  end

  # Select ingredients based on their overall score
  def select_ingredients(min_efficacy = 0.5, min_safety = 0.5)
    @ingredients.select do |ingredient|
      ingredient.efficacy >= min_efficacy && ingredient.safety >= min_safety
    end.sort_by(&:overall_score).reverse
  end
end

# Example usage
begin
  segreto = SegretoSkincare.new

  ingredient1 = SkincareIngredient.new('Hyaluronic Acid', 0.9, 0.95)
  ingredient2 = SkincareIngredient.new('Retinol', 0.8, 0.8)
  ingredient3 = SkincareIngredient.new('Salicylic Acid', 0.7, 0.9)

  segreto.add_ingredient(ingredient1)
  segreto.add_ingredient(ingredient2)
  segreto.add_ingredient(ingredient3)

  selected_ingredients = segreto.select_ingredients

  puts 'Selected Ingredients:'
  selected_ingredients.each do |ingredient|
    puts "#{ingredient.name}: Efficacy=#{ingredient.efficacy}, Safety=#{ingredient.safety}, Overall Score=#{ingredient.overall_score.round(2)}"
  end
rescue StandardError => e
  puts "Error: #{e.message}"
end
```
