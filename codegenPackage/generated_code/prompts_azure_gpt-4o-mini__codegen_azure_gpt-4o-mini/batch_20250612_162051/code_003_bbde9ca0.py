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
# skincare_ingredient_selector.rb

# This class simulates the selection of skincare ingredients based on their efficacy and safety.
class SkincareIngredientSelector
  # A hash to store ingredients with their efficacy and safety ratings
  INGREDIENTS = {
    'Hyaluronic Acid' => { efficacy: 9, safety: 10 },
    'Retinol' => { efficacy: 10, safety: 7 },
    'Vitamin C' => { efficacy: 8, safety: 9 },
    'Salicylic Acid' => { efficacy: 7, safety: 8 },
    'Niacinamide' => { efficacy: 8, safety: 10 },
    'Benzoyl Peroxide' => { efficacy: 9, safety: 6 },
    'Peptides' => { efficacy: 8, safety: 9 },
    'Alpha Arbutin' => { efficacy: 7, safety: 9 }
  }.freeze

  # Selects ingredients based on minimum efficacy and safety thresholds
  #
  # @param min_efficacy [Integer] Minimum efficacy rating (1-10)
  # @param min_safety [Integer] Minimum safety rating (1-10)
  # @return [Array<String>] List of selected ingredients
  def self.select_ingredients(min_efficacy, min_safety)
    validate_inputs(min_efficacy, min_safety)

    selected_ingredients = INGREDIENTS.select do |ingredient, ratings|
      ratings[:efficacy] >= min_efficacy && ratings[:safety] >= min_safety
    end.keys

    selected_ingredients.empty? ? ['No ingredients meet the criteria.'] : selected_ingredients
  end

  private

  # Validates the input parameters for efficacy and safety
  #
  # @param min_efficacy [Integer] Minimum efficacy rating
  # @param min_safety [Integer] Minimum safety rating
  # @raise [ArgumentError] If inputs are not within the range of 1 to 10
  def self.validate_inputs(min_efficacy, min_safety)
    unless (1..10).include?(min_efficacy) && (1..10).include?(min_safety)
      raise ArgumentError, 'Efficacy and safety ratings must be between 1 and 10.'
    end
  end
end

# Example usage
if __FILE__ == $0
  begin
    min_efficacy = 8
    min_safety = 8
    selected = SkincareIngredientSelector.select_ingredients(min_efficacy, min_safety)
    puts "Selected Ingredients: #{selected.join(', ')}"
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  end
end
```
