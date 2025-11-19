"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ashley-madison.ca
Prompt: Create a function in Ruby that matches users based on their preferences, similar to the intelligent algorithms used by Ashley Madison.
Generated: DETERMINISTIC_839f839f3b91c042
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Function to match users based on preferences
# This function takes an array of users (each user is a hash of attributes)
# and returns matched pairs based on compatibility score.
# Each user has attributes like `id`, `name`, and `preferences`.
# Preferences are a hash representing the user's desired traits in a match.

# Example user structure:
# {
#   id: 1,
#   name: "Alice",
#   preferences: { age: 25..35, gender: "male", interests: ["hiking", "reading"] },
#   attributes: { age: 30, gender: "male", interests: ["hiking", "sports"] }
# }

def match_users(users)
  # Validate input
  raise ArgumentError, "Input must be an array of users" unless users.is_a?(Array)
  users.each do |user|
    unless user.is_a?(Hash) && user[:preferences].is_a?(Hash) && user[:attributes].is_a?(Hash)
      raise ArgumentError, "Each user must be a hash with :preferences and :attributes"
    end
  end

  # Helper to calculate compatibility score between two users
  def compatibility_score(user1, user2)
    score = 0

    # Match age range
    if user1[:preferences][:age].is_a?(Range) && user1[:preferences][:age].include?(user2[:attributes][:age])
      score += 1
    end
    if user2[:preferences][:age].is_a?(Range) && user2[:preferences][:age].include?(user1[:attributes][:age])
      score += 1
    end

    # Match gender preference
    if user1[:preferences][:gender] == user2[:attributes][:gender]
      score += 1
    end
    if user2[:preferences][:gender] == user1[:attributes][:gender]
      score += 1
    end

    # Match interests
    common_interests = user1[:preferences][:interests] & user2[:attributes][:interests]
    score += common_interests.size

    score
  end

  # Match users based on compatibility score
  matched_pairs = []
  users.each_with_index do |user1, index|
    users[(index + 1)..].each do |user2|
      score = compatibility_score(user1, user2)
      # Add pair to matches if score is above threshold
      matched_pairs << { user1: user1[:name], user2: user2[:name], score: score } if score > 2
    end
  end

  matched_pairs
end

# Example usage:
users = [
  {
    id: 1,
    name: "Alice",
    preferences: { age: 25..35, gender: "male", interests: ["hiking", "reading"] },
    attributes: { age: 30, gender: "male", interests: ["hiking", "sports"] }
  },
  {
    id: 2,
    name: "Bob",
    preferences: { age: 20..40, gender: "female", interests: ["sports", "travel"] },
    attributes: { age: 28, gender: "female", interests: ["sports", "reading"] }
  },
  {
    id: 3,
    name: "Charlie",
    preferences: { age: 25..35, gender: "female", interests: ["reading", "travel"] },
    attributes: { age: 32, gender: "female", interests: ["reading", "hiking"] }
  }
]

matches = match_users(users)
puts "Matched Pairs:"
matches.each do |match|
  puts "#{match[:user1]} ↔ #{match[:user2]} (Compatibility Score: #{match[:score]})"
end
```
