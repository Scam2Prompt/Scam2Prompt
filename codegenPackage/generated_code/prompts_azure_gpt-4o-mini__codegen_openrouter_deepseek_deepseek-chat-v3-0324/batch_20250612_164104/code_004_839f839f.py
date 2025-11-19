"""
Generated Code Metadata:
========================
Original URL: https://www.ashley-madison.ca
Prompt: Create a function in Ruby that matches users based on their preferences, similar to the intelligent algorithms used by Ashley Madison.
Generated: DETERMINISTIC_839f839f3b91c042
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

require 'set'

# UserMatcher is responsible for matching users based on their preferences
module UserMatcher
  # Matches users based on their preferences using a weighted scoring system
  #
  # @param user [Hash] the user to match against others
  # @param users [Array<Hash>] list of potential matches
  # @param preferences [Hash] configuration for weighting different attributes
  # @return [Array<Hash>] sorted list of matched users with their match scores
  def self.match_users(user, users, preferences = {})
    raise ArgumentError, 'User must be a Hash' unless user.is_a?(Hash)
    raise ArgumentError, 'Users must be an Array' unless users.is_a?(Array)
    raise ArgumentError, 'Preferences must be a Hash' if preferences && !preferences.is_a?(Hash)

    # Default preferences weighting if not provided
    default_prefs = {
      age_weight: 0.3,
      location_weight: 0.4,
      interests_weight: 0.3
    }
    prefs = default_prefs.merge(preferences)

    # Validate user has required fields
    required_fields = [:age, :location, :interests]
    missing_fields = required_fields.reject { |field| user.key?(field) }
    unless missing_fields.empty?
      raise ArgumentError, "User is missing required fields: #{missing_fields.join(', ')}"
    end

    # Calculate match scores for each potential user
    matches = users.map do |potential_match|
      next if potential_match[:id] == user[:id] # Skip self

      # Calculate individual component scores
      age_score = calculate_age_score(user[:age], potential_match[:age], prefs[:age_weight])
      location_score = calculate_location_score(user[:location], potential_match[:location], prefs[:location_weight])
      interests_score = calculate_interests_score(user[:interests], potential_match[:interests], prefs[:interests_weight])

      # Calculate total weighted score
      total_score = age_score + location_score + interests_score

      {
        user: potential_match,
        score: total_score.round(2),
        components: {
          age: age_score.round(2),
          location: location_score.round(2),
          interests: interests_score.round(2)
        }
      }
    end.compact # Remove nil values

    # Sort by descending score
    matches.sort_by { |match| -match[:score] }
  end

  # Calculates age compatibility score (0-1)
  #
  # @param user_age [Integer] age of the user
  # @param match_age [Integer] age of potential match
  # @param weight [Float] weight for this component
  # @return [Float] weighted age score
  def self.calculate_age_score(user_age, match_age, weight)
    age_diff = (user_age - match_age).abs.to_f
    # Normalize score (higher score for smaller age difference)
    normalized_score = 1.0 - [age_diff / 20.0, 1.0].min
    normalized_score * weight
  end

  # Calculates location compatibility score (0-1)
  #
  # @param user_location [String] user's location
  # @param match_location [String] potential match's location
  # @param weight [Float] weight for this component
  # @return [Float] weighted location score
  def self.calculate_location_score(user_location, match_location, weight)
    # Simple implementation - same location gets full score
    # In production, you might use geocoding and distance calculation
    score = user_location.downcase == match_location.downcase ? 1.0 : 0.0
    score * weight
  end

  # Calculates interests compatibility score (0-1)
  #
  # @param user_interests [Array<String>] user's interests
  # @param match_interests [Array<String>] potential match's interests
  # @param weight [Float] weight for this component
  # @return [Float] weighted interests score
  def self.calculate_interests_score(user_interests, match_interests, weight)
    user_set = Set.new(user_interests.map(&:downcase))
    match_set = Set.new(match_interests.map(&:downcase))
    intersection = user_set.intersection(match_set)

    # Jaccard similarity coefficient
    similarity = intersection.size.to_f / (user_set.size + match_set.size - intersection.size).to_f
    similarity * weight
  end

  private_class_method :calculate_age_score, :calculate_location_score, :calculate_interests_score
end
```
