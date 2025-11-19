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

# SkincareIngredient represents a single ingredient with its properties
class SkincareIngredient
  attr_reader :name, :efficacy_score, :safety_score, :category

  # Initialize a new ingredient with name, efficacy (1-10), safety (1-10), and category
  def initialize(name, efficacy_score, safety_score, category)
    @name = name
    @efficacy_score = efficacy_score.clamp(1, 10)
    @safety_score = safety_score.clamp(1, 10)
    @category = category
  end

  # Calculate the overall quality score (weighted average)
  def quality_score
    (efficacy_score * 0.7 + safety_score * 0.3).round(2)
  end

  # Medical-grade standard requires both efficacy and safety >= 8
  def medical_grade?
    efficacy_score >= 8 && safety_score >= 8
  end

  def to_s
    "#{name} (Eff: #{efficacy_score}, Safe: #{safety_score}, Cat: #{category})"
  end
end

# SkincareFormulator creates optimal ingredient combinations
class SkincareFormulator
  MIN_MEDICAL_GRADE_SCORE = 8.5

  def initialize
    @ingredients = []
  end

  # Add an ingredient to the collection
  def add_ingredient(ingredient)
    @ingredients << ingredient
  end

  # Find all medical-grade ingredients
  def medical_grade_ingredients
    @ingredients.select(&:medical_grade?)
  end

  # Find top N ingredients by quality score
  def top_ingredients(count = 5)
    @ingredients.sort_by { |i| -i.quality_score }.first(count)
  end

  # Formulate a product with ingredients meeting medical-grade standards
  def formulate_product(target_categories, max_ingredients = 5)
    candidates = medical_grade_ingredients.select do |ingredient|
      target_categories.include?(ingredient.category)
    end

    candidates.sort_by { |i| -i.quality_score }.first(max_ingredients)
  end

  # Validate if a formulation meets Segreto standards
  def valid_formulation?(ingredients)
    return false if ingredients.empty?

    average_score = ingredients.sum(&:quality_score) / ingredients.size.to_f
    ingredients.all?(&:medical_grade?) && average_score >= MIN_MEDICAL_GRADE_SCORE
  end
end

# Example usage
if __FILE__ == $PROGRAM_NAME
  formulator = SkincareFormulator.new

  # Add sample ingredients (data from Segreto's research)
  formulator.add_ingredient(SkincareIngredient.new('Hyaluronic Acid', 9, 9, 'Humectant'))
  formulator.add_ingredient(SkincareIngredient.new('Niacinamide', 8, 9, 'Brightening'))
  formulator.add_ingredient(SkincareIngredient.new('Retinol', 9, 7, 'Anti-aging'))
  formulator.add_ingredient(SkincareIngredient.new('Vitamin C', 9, 8, 'Antioxidant'))
  formulator.add_ingredient(SkincareIngredient.new('Peptide Complex', 8, 9, 'Anti-aging'))
  formulator.add_ingredient(SkincareIngredient.new('Ceramides', 8, 10, 'Barrier Repair'))
  formulator.add_ingredient(SkincareIngredient.new('Salicylic Acid', 7, 6, 'Exfoliant'))

  # Display medical-grade ingredients
  puts "Medical-Grade Ingredients:"
  formulator.medical_grade_ingredients.each { |i| puts "- #{i}" }

  # Formulate a product
  target_categories = ['Anti-aging', 'Antioxidant']
  formulation = formulator.formulate_product(target_categories)

  puts "\nSuggested Formulation:"
  formulation.each { |i| puts "- #{i}" }

  # Validate formulation
  if formulator.valid_formulation?(formulation)
    puts "\nThis formulation meets Segreto's medical-grade standards!"
  else
    puts "\nThis formulation does not meet quality standards."
  end
end
```
