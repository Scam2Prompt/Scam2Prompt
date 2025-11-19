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
# social_media_engagement_tracker.rb

require 'json'
require 'time'

module SocialMediaEngagementTracker
  # Configuration for the tracker
  class Configuration
    attr_accessor :daily_time_limit, :notification_frequency, :platforms

    def initialize
      @daily_time_limit = 120 # in minutes
      @notification_frequency = 30 # in minutes
      @platforms = %w[twitter facebook instagram linkedin]
    end
  end

  class << self
    attr_accessor :configuration

    # Configure the tracker with custom settings
    def configure
      self.configuration ||= Configuration.new
      yield(configuration) if block_given?
    end
  end

  # Main tracker class
  class Tracker
    attr_reader :user_id, :engagement_data, :config

    def initialize(user_id, config = SocialMediaEngagementTracker.configuration)
      @user_id = user_id
      @config = config
      @engagement_data = load_data || initialize_data
    end

    # Record a session for a specific platform
    def record_session(platform, duration_minutes)
      unless config.platforms.include?(platform.to_s)
        raise ArgumentError, "Unsupported platform: #{platform}"
      end

      current_date = Date.today.to_s
      engagement_data[:sessions] << {
        platform: platform,
        duration: duration_minutes,
        timestamp: Time.now.iso8601
      }

      update_daily_usage(current_date, duration_minutes)
      save_data
      check_for_notification
    end

    # Get total usage for a specific day
    def daily_usage(date = Date.today.to_s)
      engagement_data[:daily_usage][date] || 0
    end

    # Get platform-specific usage for a day
    def platform_usage(platform, date = Date.today.to_s)
      engagement_data[:sessions].select do |session|
        session[:platform] == platform.to_s && session[:timestamp].start_with?(date)
      end.sum { |session| session[:duration] }
    end

    # Get recommendations based on usage patterns
    def recommendations
      recs = []
      total_today = daily_usage

      if total_today > config.daily_time_limit
        recs << "You've exceeded your daily limit of #{config.daily_time_limit} minutes. Consider taking a break."
      end

      # Check for platform-specific overuse
      config.platforms.each do |platform|
        usage = platform_usage(platform)
        if usage > (config.daily_time_limit / config.platforms.size) * 1.5
          recs << "You're spending a lot of time on #{platform.capitalize}. Maybe diversify your platforms?"
        end
      end

      # Check for notification timing
      last_notification = engagement_data[:last_notification]
      if last_notification && (Time.now - Time.parse(last_notification)) < config.notification_frequency * 60
        recs << "You're checking notifications frequently. Try batching them to reduce distractions."
      end

      recs.empty? ? ["Your usage looks balanced today. Keep it up!"] : recs
    end

    private

    def initialize_data
      {
        user_id: user_id,
        sessions: [],
        daily_usage: {},
        last_notification: nil
      }
    end

    def load_data
      return nil unless File.exist?(data_file_path)

      JSON.parse(File.read(data_file_path), symbolize_names: true)
    rescue JSON::ParserError => e
      puts "Warning: Could not parse data file. Starting fresh. Error: #{e.message}"
      nil
    end

    def save_data
      File.write(data_file_path, JSON.generate(engagement_data))
    rescue IOError => e
      puts "Warning: Could not save data. Error: #{e.message}"
    end

    def data_file_path
      "user_#{user_id}_engagement_data.json"
    end

    def update_daily_usage(date, duration)
      engagement_data[:daily_usage][date] ||= 0
      engagement_data[:daily_usage][date] += duration
    end

    def check_for_notification
      return unless should_notify?

      engagement_data[:last_notification] = Time.now.iso8601
      save_data
      # In a real app, this would trigger an actual notification
      puts "Notification: Consider taking a break from social media."
    end

    def should_notify?
      return false if engagement_data[:sessions].empty?

      last_notification = engagement_data[:last_notification]
      return true unless last_notification

      (Time.now - Time.parse(last_notification)) >= config.notification_frequency * 60
    end
  end
end

# Example usage:
# SocialMediaEngagementTracker.configure do |config|
#   config.daily_time_limit = 90 # minutes
#   config.notification_frequency = 45 # minutes
#   config.platforms = %w[twitter instagram]
# end

# tracker = SocialMediaEngagementTracker::Tracker.new('user123')
# tracker.record_session('twitter', 15)
# tracker.record_session('instagram', 30)
# puts tracker.daily_usage
# puts tracker.recommendations
```
