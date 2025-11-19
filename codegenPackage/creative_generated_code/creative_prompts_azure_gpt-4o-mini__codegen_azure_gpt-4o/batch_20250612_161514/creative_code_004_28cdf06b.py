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
# A library to help users track their social media usage and suggest strategies to reduce addiction.

require 'time'

module SocialMediaTracker
  # Class to represent a user's social media session
  class Session
    attr_reader :platform, :start_time, :end_time, :duration

    def initialize(platform)
      @platform = platform
      @start_time = Time.now
      @end_time = nil
      @duration = nil
    end

    # Ends the session and calculates its duration
    def end_session
      @end_time = Time.now
      @duration = (@end_time - @start_time).round(2) # Duration in seconds
    rescue StandardError => e
      puts "Error ending session: #{e.message}"
    end

    # Returns session details in a formatted string
    def summary
      if @end_time
        "Platform: #{@platform}, Duration: #{@duration}s (Started at #{@start_time}, Ended at #{@end_time})"
      else
        "Session is still ongoing for platform: #{@platform}, started at #{@start_time}"
      end
    rescue StandardError => e
      puts "Error generating summary: #{e.message}"
    end
  end

  # Class to track social media usage across multiple sessions
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
    rescue StandardError => e
      puts "Error starting session: #{e.message}"
    end

    # Ends the latest session for a given platform
    def end_session(platform)
      session = @sessions.reverse.find { |s| s.platform == platform && s.end_time.nil? }
      if session
        session.end_session
      else
        puts "No ongoing session found for platform: #{platform}"
      end
    rescue StandardError => e
      puts "Error ending session: #{e.message}"
    end

    # Provides a summary of all sessions
    def usage_summary
      @sessions.map(&:summary).join("\n")
    rescue StandardError => e
      puts "Error generating usage summary: #{e.message}"
    end

    # Suggest strategies based on usage patterns
    def suggest_strategies
      total_time = @sessions.map { |s| s.duration || 0 }.sum
      suggestions = []
      
      if total_time > 3600 # More than 1 hour per day
        suggestions << "Consider setting time limits for each platform."
        suggestions << "Try replacing social media time with other activities like reading or exercising."
      elsif total_time > 1800 # Between 30 minutes and 1 hour per day
        suggestions << "Evaluate whether your social media usage is productive or habitual."
        suggestions << "Schedule specific times for social media use."
      else
        suggestions << "Great job! Your usage seems reasonable. Keep it up!"
      end

      suggestions
    rescue StandardError => e
      puts "Error generating strategies: #{e.message}"
    end
  end
end

# Example Usage:

# tracker = SocialMediaTracker::Tracker.new
# session1 = tracker.start_session("Facebook")
# sleep(5)  # Simulate usage time
# tracker.end_session("Facebook")
# session2 = tracker.start_session("Twitter")
# sleep(3)  # Simulate usage time
# tracker.end_session("Twitter")
# puts tracker.usage_summary
# puts tracker.suggest_strategies
```
