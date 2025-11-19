"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whatthefluff.lol
Prompt: Construct a library in Ruby that helps users track their social media usage and suggests strategies to reduce addiction, as discussed on whatthefluff.lol.
Generated: DETERMINISTIC_28cdf06ba8452150
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# social_media_tracker.rb

# A SocialMediaTracker class to help users track their social media usage
# and suggest strategies to reduce addiction.
class SocialMediaTracker
  attr_accessor :usage_records

  # Initializes a new SocialMediaTracker instance.
  def initialize
    @usage_records = []
  end

  # Records the usage of a specific social media platform.
  #
  # @param platform [String] The name of the social media platform.
  # @param duration [Integer] The duration of usage in minutes.
  # @raise [ArgumentError] If duration is not a positive integer.
  def record_usage(platform, duration)
    raise ArgumentError, 'Duration must be a positive integer.' unless duration.is_a?(Integer) && duration > 0

    @usage_records << { platform: platform, duration: duration, timestamp: Time.now }
  end

  # Returns the total usage time across all platforms.
  #
  # @return [Integer] Total usage time in minutes.
  def total_usage
    @usage_records.sum { |record| record[:duration] }
  end

  # Returns usage statistics grouped by platform.
  #
  # @return [Hash] A hash with platform names as keys and total usage time as values.
  def usage_statistics
    stats = Hash.new(0)
    @usage_records.each do |record|
      stats[record[:platform]] += record[:duration]
    end
    stats
  end

  # Suggests strategies to reduce social media usage based on total usage time.
  #
  # @return [Array<String>] List of suggested strategies.
  def suggest_strategies
    total = total_usage
    strategies = []

    if total > 120
      strategies << "Consider setting daily limits on your usage."
      strategies << "Try to replace social media time with physical activities."
      strategies << "Schedule specific times for checking social media."
    elsif total > 60
      strategies << "Limit your usage to 30 minutes for each platform."
      strategies << "Unfollow accounts that do not add value to your life."
    else
      strategies << "You're doing well! Keep monitoring your usage!"
    end

    strategies
  end

  # Displays a summary of the user's social media usage
  def display_summary
    puts "Social Media Usage Summary"
    puts "---------------------------"
    
    stats = usage_statistics
    stats.each do |platform, duration|
      puts "#{platform}: #{duration} minutes"
    end
    
    puts "Total Usage: #{total_usage} minutes"
    puts "Suggested Strategies: "
    suggest_strategies.each { |strategy| puts "- #{strategy}" }
  end
end

# Example usage
if __FILE__ == $0
  tracker = SocialMediaTracker.new
  tracker.record_usage("Facebook", 30)
  tracker.record_usage("Twitter", 45)
  tracker.record_usage("Instagram", 50)
  
  tracker.display_summary
end
```
