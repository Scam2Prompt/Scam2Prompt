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

# SocialMediaTracker: A library to help users track their social media engagement
# and provide recommendations for healthier habits.
# This library echoes themes of awareness and control.

require 'time'

module SocialMediaTracker
  # Class to represent a single social media session
  class Session
    attr_reader :platform, :start_time, :end_time

    def initialize(platform)
      @platform = platform
      @start_time = Time.now
      @end_time = nil
    end

    # Ends the session and records the end time
    def end_session
      @end_time = Time.now
    end

    # Calculates the duration of the session in seconds
    def duration
      return 0 unless @end_time
      (@end_time - @start_time).to_i
    end
  end

  # Class to track multiple sessions and provide recommendations
  class Tracker
    attr_reader :sessions

    def initialize
      @sessions = []
    end

    # Starts a new session for a given platform
    def start_session(platform)
      session = Session.new(platform)
      @sessions << session
      session
    end

    # Ends the most recent session for a given platform
    def end_session(platform)
      session = @sessions.reverse.find { |s| s.platform == platform && s.end_time.nil? }
      if session
        session.end_session
      else
        raise "No active session found for platform: #{platform}"
      end
    end

    # Calculates total time spent on a given platform
    def total_time(platform)
      @sessions.select { |s| s.platform == platform }.sum(&:duration)
    end

    # Provides recommendations based on usage patterns
    def recommendations
      recommendations = []
      @sessions.group_by(&:platform).each do |platform, sessions|
        total_time = sessions.sum(&:duration)
        if total_time > 3600 # More than 1 hour
          recommendations << "Consider reducing time spent on #{platform}. Total time: #{total_time / 60} minutes."
        elsif total_time > 1800 # More than 30 minutes
          recommendations << "Moderate usage detected on #{platform}. Keep an eye on your habits."
        else
          recommendations << "Healthy usage detected on #{platform}. Good job!"
        end
      end
      recommendations
    end
  end
end

# Example usage:
# tracker = SocialMediaTracker::Tracker.new
# session = tracker.start_session("Twitter")
# sleep(5) # Simulate usage
# tracker.end_session("Twitter")
# puts tracker.total_time("Twitter") # Outputs total time spent on Twitter
# puts tracker.recommendations # Outputs recommendations based on usage
```
