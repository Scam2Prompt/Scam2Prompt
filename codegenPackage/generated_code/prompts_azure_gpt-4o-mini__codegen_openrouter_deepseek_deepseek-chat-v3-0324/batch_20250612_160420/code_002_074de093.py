"""
Generated Code Metadata:
========================
Original URL: https://agoda.host
Prompt: Create a code snippet in Ruby that generates a list of recommended self-care gifts based on user preferences, such as fidget rings and crystal healing stones.
Generated: DETERMINISTIC_074de093fb3277b9
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

# SelfCareGiftRecommender generates personalized self-care gift recommendations
# based on user preferences.
class SelfCareGiftRecommender
  # Available gift categories and their items
  GIFT_CATEGORIES = {
    fidget_toys: [
      { name: 'Fidget Ring', description: 'Elegant ring with spinning mechanism', price_range: '$15-$30' },
      { name: 'Fidget Cube', description: 'Multi-sided cube with various tactile features', price_range: '$10-$25' },
      { name: 'Spinner Ring', description: 'Sleek ring with rotating outer band', price_range: '$20-$40' }
    ],
    crystal_healing: [
      { name: 'Amethyst Stone', description: 'Promotes calm and relaxation', price_range: '$10-$50' },
      { name: 'Rose Quartz', description: 'Encourages self-love and compassion', price_range: '$8-$40' },
      { name: 'Clear Quartz', description: 'Amplifies energy and clarity', price_range: '$12-$60' }
    ],
    aromatherapy: [
      { name: 'Lavender Essential Oil', description: 'Calming and sleep-inducing', price_range: '$10-$30' },
      { name: 'Eucalyptus Oil', description: 'Invigorating and respiratory support', price_range: '$12-$35' }
    ],
    journaling: [
      { name: 'Gratitude Journal', description: 'Guided prompts for daily reflection', price_range: '$15-$25' },
      { name: 'Bullet Journal Kit', description: 'Includes journal and accessories', price_range: '$20-$45' }
    ]
  }.freeze

  # Initializes the recommender with user preferences
  # @param preferences [Array<Symbol>] Array of preferred categories (e.g., [:fidget_toys, :crystal_healing])
  def initialize(preferences)
    @preferences = preferences
    validate_preferences
  end

  # Generates recommendations based on user preferences
  # @return [Array<Hash>] Array of recommended gift items
  def generate_recommendations
    @preferences.flat_map do |category|
      GIFT_CATEGORIES[category] || []
    end
  end

  private

  # Validates that all user preferences are valid categories
  # @raise [ArgumentError] if any preference is invalid
  def validate_preferences
    invalid = @preferences.reject { |pref| GIFT_CATEGORIES.key?(pref) }
    return if invalid.empty?

    raise ArgumentError, "Invalid preferences: #{invalid.join(', ')}. Valid options are: #{GIFT_CATEGORIES.keys.join(', ')}"
  end
end

# Example usage:
# preferences = [:fidget_toys, :crystal_healing]
# recommender = SelfCareGiftRecommender.new(preferences)
# puts recommender.generate_recommendations
```
