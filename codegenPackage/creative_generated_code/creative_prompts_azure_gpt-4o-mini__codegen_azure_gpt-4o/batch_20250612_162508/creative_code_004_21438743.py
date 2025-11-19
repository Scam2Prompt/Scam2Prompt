"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbiter.lol
Prompt: Construct a library in Ruby that helps users track their social media engagement and offers recommendations for healthier habits, echoing the themes of awareness and control from orbiter.lol.
Generated: DETERMINISTIC_214387436e3f9221
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# social_engagement_tracker.rb

# A library for tracking social media engagement and recommending healthier habits.
# This library echoes the themes of awareness and control to assist users in managing their social media usage.

require 'date'

# Main module for the library
module SocialEngagementTracker
  # Class to represent a single engagement record
  class EngagementRecord
    attr_reader :timestamp, :platform, :type, :duration

    # Initialize a new engagement record
    # @param platform [String] Name of the social media platform
    # @param type [String] Type of engagement (e.g., "scrolling", "posting", "messaging")
    # @param duration [Integer] Duration of the engagement in minutes
    def initialize(platform, type, duration)
      @timestamp = DateTime.now
      @platform = platform
      @type = type
      @duration = duration
    end

    # Represent the record as a string for logging or debugging
    def to_s
      "EngagementRecord: #{timestamp} | Platform: #{platform} | Type: #{type} | Duration: #{duration} minutes"
    end
  end

  # Class to manage multiple engagement records and provide analysis
  class Tracker
    def initialize
      @records = []
    end

    # Add a new engagement record
    # @param record [EngagementRecord] The record to add
    def add_record(record)
      raise ArgumentError, 'Invalid record type' unless record.is_a?(EngagementRecord)

      @records << record
    end

    # Get all engagement records
    # @return [Array<EngagementRecord>] List of all records
    def all_records
      @records
    end

    # Calculate total time spent across all platforms
    # @return [Integer] Total time in minutes
    def total_time_spent
      @records.sum(&:duration)
    end

    # Calculate time spent on a specific platform
    # @param platform [String] Name of the platform
    # @return [Integer] Time spent on the platform in minutes
    def time_spent_on_platform(platform)
      @records.select { |r| r.platform == platform }.sum(&:duration)
    end

    # Generate recommendations for healthier habits
    # @return [Array<String>] List of recommendations
    def generate_recommendations
      total_time = total_time_spent

      recommendations = []
      if total_time > 120
        recommendations << 'Consider reducing overall social media usage to less than 2 hours per day.'
      end

      heavy_platforms = @records.group_by(&:platform).transform_values { |records| records.sum(&:duration) }
      heavy_platforms.each do |platform, time|
        if time > 60
          recommendations << "Reduce time spent on #{platform} to less than 1 hour per day."
        end
      end

      if @records.any? { |r| r.type == 'scrolling' && r.duration > 30 }
        recommendations << 'Limit passive scrolling sessions to under 30 minutes.'
      end

      recommendations.empty? ? ['Your social media habits seem balanced. Keep it up!'] : recommendations
    end
  end
end

# Example usage (Uncomment for testing in a Ruby environment):
# tracker = SocialEngagementTracker::Tracker.new
# record1 = SocialEngagementTracker::EngagementRecord.new('Twitter', 'scrolling', 45)
# record2 = SocialEngagementTracker::EngagementRecord.new('Instagram', 'posting', 25)
# record3 = SocialEngagementTracker::EngagementRecord.new('Facebook', 'messaging', 60)
# tracker.add_record(record1)
# tracker.add_record(record2)
# tracker.add_record(record3)
# puts tracker.total_time_spent
# puts tracker.time_spent_on_platform('Twitter')
# puts tracker.generate_recommendations
```
