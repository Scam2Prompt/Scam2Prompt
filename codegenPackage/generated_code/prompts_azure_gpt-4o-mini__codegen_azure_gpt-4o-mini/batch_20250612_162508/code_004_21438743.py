"""
Generated Code Metadata:
========================
Original URL: https://orbiter.lol
Prompt: Construct a library in Ruby that helps users track their social media engagement and offers recommendations for healthier habits, echoing the themes of awareness and control from orbiter.lol.
Generated: DETERMINISTIC_214387436e3f9221
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# social_media_tracker.rb

# A library to track social media engagement and provide recommendations for healthier habits.
class SocialMediaTracker
  attr_accessor :engagement_data

  # Initializes a new SocialMediaTracker instance with an empty engagement data hash.
  def initialize
    @engagement_data = {}
  end

  # Records engagement data for a specific platform.
  # @param platform [String] The name of the social media platform.
  # @param time_spent [Integer] The time spent on the platform in minutes.
  # @param interactions [Integer] The number of interactions (likes, comments, shares).
  def record_engagement(platform, time_spent, interactions)
    validate_input(platform, time_spent, interactions)

    @engagement_data[platform] ||= { time_spent: 0, interactions: 0 }
    @engagement_data[platform][:time_spent] += time_spent
    @engagement_data[platform][:interactions] += interactions
  end

  # Provides a summary of engagement data.
  # @return [Hash] A summary of engagement data for each platform.
  def summary
    @engagement_data
  end

  # Generates recommendations based on engagement data.
  # @return [Array] An array of recommendations for healthier social media habits.
  def recommendations
    recs = []
    @engagement_data.each do |platform, data|
      if data[:time_spent] > 120
        recs << "Consider reducing your time on #{platform} to improve your well-being."
      end
      if data[:interactions] < 5
        recs << "Engage more meaningfully on #{platform} by interacting with content you enjoy."
      end
    end
    recs.empty? ? ["You're doing great! Keep it up!"] : recs
  end

  private

  # Validates the input parameters for recording engagement.
  # @param platform [String] The name of the social media platform.
  # @param time_spent [Integer] The time spent on the platform in minutes.
  # @param interactions [Integer] The number of interactions (likes, comments, shares).
  def validate_input(platform, time_spent, interactions)
    raise ArgumentError, "Platform must be a non-empty string." if platform.nil? || platform.empty?
    raise ArgumentError, "Time spent must be a non-negative integer." unless time_spent.is_a?(Integer) && time_spent >= 0
    raise ArgumentError, "Interactions must be a non-negative integer." unless interactions.is_a?(Integer) && interactions >= 0
  end
end

# Example usage:
# tracker = SocialMediaTracker.new
# tracker.record_engagement("Instagram", 150, 3)
# tracker.record_engagement("Twitter", 30, 10)
# puts tracker.summary
# puts tracker.recommendations
```
