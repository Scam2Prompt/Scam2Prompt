"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Develop a script in Ruby to automate contest and promotion creation for an event, incorporating Pozy Media's approach to boosting conversions and attendee engagement.
Generated: DETERMINISTIC_d2100cc943e60964
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# contest_promotion_creator.rb

require 'json'
require 'date'

# Class to handle contest and promotion creation
class ContestPromotionCreator
  # Initialize with event details
  def initialize(event_name, start_date, end_date, max_entries)
    @event_name = event_name
    @start_date = parse_date(start_date)
    @end_date = parse_date(end_date)
    @max_entries = max_entries
    @contests = []
    @promotions = []
    validate_dates
  end

  # Create a contest for the event
  def create_contest(contest_name, prize)
    contest = {
      contest_name: contest_name,
      prize: prize,
      event_name: @event_name,
      start_date: @start_date,
      end_date: @end_date,
      max_entries: @max_entries,
      created_at: Time.now
    }
    @contests << contest
    puts "Contest '#{contest_name}' created successfully!"
    contest
  end

  # Create a promotion for the event
  def create_promotion(promotion_name, discount_code, discount_percentage)
    promotion = {
      promotion_name: promotion_name,
      discount_code: discount_code,
      discount_percentage: discount_percentage,
      event_name: @event_name,
      start_date: @start_date,
      end_date: @end_date,
      created_at: Time.now
    }
    @promotions << promotion
    puts "Promotion '#{promotion_name}' created successfully!"
    promotion
  end

  # Export all contests and promotions to a JSON file
  def export_to_json(file_name)
    data = {
      event_name: @event_name,
      contests: @contests,
      promotions: @promotions
    }

    begin
      File.open(file_name, 'w') do |file|
        file.write(JSON.pretty_generate(data))
      end
      puts "Data exported successfully to #{file_name}!"
    rescue IOError => e
      puts "An error occurred while writing to the file: #{e.message}"
    end
  end

  private

  # Parse and validate date format
  def parse_date(date_string)
    begin
      Date.parse(date_string)
    rescue ArgumentError
      raise ArgumentError, "Invalid date format: #{date_string}. Expected format: YYYY-MM-DD"
    end
  end

  # Validate start and end dates
  def validate_dates
    raise ArgumentError, 'End date cannot be before start date' if @end_date < @start_date
  end
end

# Example usage (Uncomment to run the script)
# begin
#   creator = ContestPromotionCreator.new('Tech Conference 2023', '2023-11-01', '2023-11-05', 1000)
#   creator.create_contest('Hackathon', 'MacBook Pro 16-inch')
#   creator.create_promotion('Early Bird Discount', 'EARLYBIRD50', 50)
#   creator.export_to_json('event_data.json')
# rescue ArgumentError => e
#   puts "Error: #{e.message}"
# end
```
