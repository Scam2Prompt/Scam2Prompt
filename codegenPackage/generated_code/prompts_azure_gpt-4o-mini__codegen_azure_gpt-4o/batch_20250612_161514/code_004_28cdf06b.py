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

# SocialMediaTracker: A library to track social media usage and suggest strategies to reduce addiction.
# Author: [Your Name]
# Version: 1.0.0

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

    # Ends the session and calculates the duration
    def end_session
      @end_time = Time.now
    end

    # Calculates the duration of the session in minutes
    def duration
      return 0 unless @end_time
      ((@end_time - @start_time) / 60).round
    end
  end

  # Class to track usage and provide strategies
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
      raise "No active session found for platform: #{platform}" unless session

      session.end_session
    end

    # Calculates total usage time for a given platform
    def total_usage(platform)
      @sessions.select { |s| s.platform == platform }.map(&:duration).sum
    end

    # Suggests strategies to reduce addiction based on usage
    def suggest_strategies(platform)
      usage = total_usage(platform)
      strategies = []

      if usage > 120
        strategies << "Consider setting daily limits for #{platform}."
        strategies << "Try using apps that block #{platform} after a certain time."
      elsif usage > 60
        strategies << "Take regular breaks while using #{platform}."
        strategies << "Avoid using #{platform} during meals or before bed."
      else
        strategies << "Your usage of #{platform} seems reasonable. Keep it up!"
      end

      strategies
    end
  end
end

# Example usage:
# tracker = SocialMediaTracker::Tracker.new
# session = tracker.start_session("Instagram")
# sleep(5) # Simulate usage
# tracker.end_session("Instagram")
# puts "Total usage: #{tracker.total_usage("Instagram")} minutes"
# puts tracker.suggest_strategies("Instagram")
```
