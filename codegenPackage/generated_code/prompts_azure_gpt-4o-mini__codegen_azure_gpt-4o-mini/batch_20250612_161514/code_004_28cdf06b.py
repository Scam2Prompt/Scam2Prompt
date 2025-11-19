"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Construct a library in Ruby that helps users track their social media usage and suggests strategies to reduce addiction, as discussed on whatthefluff.lol.
Generated: DETERMINISTIC_28cdf06ba8452150
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# social_media_tracker.rb

# A library to track social media usage and suggest strategies to reduce addiction.
class SocialMediaTracker
  attr_accessor :usage_data

  # Initializes a new SocialMediaTracker instance.
  def initialize
    @usage_data = {}
  end

  # Records the time spent on a specific social media platform.
  # @param platform [String] The name of the social media platform.
  # @param duration [Integer] The duration spent on the platform in minutes.
  def record_usage(platform, duration)
    raise ArgumentError, 'Platform name must be a non-empty string' if platform.nil? || platform.empty?
    raise ArgumentError, 'Duration must be a positive integer' unless duration.is_a?(Integer) && duration.positive?

    @usage_data[platform] ||= 0
    @usage_data[platform] += duration
  end

  # Retrieves the total usage time for a specific platform.
  # @param platform [String] The name of the social media platform.
  # @return [Integer] The total duration spent on the platform in minutes.
  def get_usage(platform)
    raise ArgumentError, 'Platform name must be a non-empty string' if platform.nil? || platform.empty?

    @usage_data[platform] || 0
  end

  # Suggests strategies to reduce social media addiction based on usage data.
  # @return [Array<String>] An array of suggested strategies.
  def suggest_strategies
    strategies = []

    total_usage = @usage_data.values.sum

    if total_usage > 120
      strategies << "Consider limiting your social media usage to 2 hours a day."
    end

    if total_usage > 60
      strategies << "Try setting specific time slots for social media usage."
    end

    if total_usage > 30
      strategies << "Unfollow accounts that do not add value to your life."
    end

    strategies.empty? ? ["Great job! Keep it up!"] : strategies
  end

  # Displays a summary of social media usage.
  # @return [String] A summary of usage data.
  def display_summary
    summary = "Social Media Usage Summary:\n"
    @usage_data.each do |platform, duration|
      summary += "#{platform}: #{duration} minutes\n"
    end
    summary += "Total Usage: #{total_usage} minutes\n"
    summary
  end

  private

  # Calculates the total usage time across all platforms.
  # @return [Integer] The total duration spent on all platforms in minutes.
  def total_usage
    @usage_data.values.sum
  end
end

# Example usage:
if __FILE__ == $0
  tracker = SocialMediaTracker.new
  tracker.record_usage("Facebook", 30)
  tracker.record_usage("Instagram", 45)
  tracker.record_usage("Twitter", 50)

  puts tracker.display_summary
  puts tracker.suggest_strategies
end
```
