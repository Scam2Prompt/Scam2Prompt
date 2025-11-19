"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treasury.casino
Prompt: Write a Ruby script that sends notifications to users about upcoming events and promotions at Treasury Brisbane Casino based on their preferences.
Generated: DETERMINISTIC_9182316a33eae04e
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'net/smtp'
require 'json'

# Class to send notifications to users
class NotificationService
  # Initialize the service with SMTP settings
  def initialize(smtp_settings)
    @smtp_settings = smtp_settings
  end

  # Send an email notification
  def send_email(to, subject, message)
    begin
      Net::SMTP.start(@smtp_settings[:address], @smtp_settings[:port], @smtp_settings[:domain], 
                      @smtp_settings[:user_name], @smtp_settings[:password], @smtp_settings[:authentication]) do |smtp|
        smtp.send_message compose_email(to, subject, message), @smtp_settings[:user_name], to
      end
    rescue StandardError => e
      puts "Failed to send email: #{e.message}"
    end
  end

  private

  # Compose an email message
  def compose_email(to, subject, message)
    <<~EMAIL
      From: Treasury Brisbane Casino <#{@smtp_settings[:user_name]}>
      To: #{to}
      Subject: #{subject}

      #{message}
    EMAIL
  end
end

# Class to manage user preferences and events
class EventManager
  attr_reader :users, :events

  # Initialize with user data and event data
  def initialize(users_file, events_file)
    @users = load_users(users_file)
    @events = load_events(events_file)
  end

  # Load user data from a JSON file
  def load_users(file)
    JSON.parse(File.read(file), symbolize_names: true)
  rescue StandardError => e
    puts "Error loading users: #{e.message}"
    []
  end

  # Load event data from a JSON file
  def load_events(file)
    JSON.parse(File.read(file), symbolize_names: true)
  rescue StandardError => e
    puts "Error loading events: #{e.message}"
    []
  end

  # Notify users about events based on their preferences
  def notify_users(notification_service)
    @users.each do |user|
      user_events = find_events_by_preferences(user[:preferences])
      next if user_events.empty?

      subject = "Upcoming Events & Promotions Just for You!"
      message = compose_notification_message(user_events)

      notification_service.send_email(user[:email], subject, message)
    end
  end

  private

  # Find events matching user preferences
  def find_events_by_preferences(preferences)
    @events.select { |event| preferences.include?(event[:type]) }
  end

  # Compose a message detailing the events
  def compose_notification_message(events)
    events.map { |event| "#{event[:name]}: #{event[:description]} on #{event[:date]}" }.join("\n")
  end
end

# Main execution block
if __FILE__ == $0
  # SMTP configuration settings
  smtp_settings = {
    address: 'smtp.example.com',
    port: 587,
    domain: 'example.com',
    user_name: 'your_email@example.com',
    password: 'your_password',
    authentication: :login
  }

  # Create an instance of NotificationService
  notification_service = NotificationService.new(smtp_settings)

  # Create an instance of EventManager and notify users
  event_manager = EventManager.new('users.json', 'events.json')
  event_manager.notify_users(notification_service)
end
```

**Note:** Ensure that the `users.json` and `events.json` files exist in the same directory as the script and are formatted correctly. The SMTP settings must be replaced with valid credentials for sending emails.
