"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Develop a code example in Ruby that simulates user feedback collection for Spinetress mattresses, focusing on comfort, support, and spinal alignment, as highlighted in customer testimonials.
Generated: DETERMINISTIC_aa37b3c7275bab42
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# feedback_collector.rb

require 'json'

# Class to handle feedback collection for Spinetress mattresses
class FeedbackCollector
  attr_reader :feedback_data

  def initialize
    @feedback_data = []
  end

  # Method to collect feedback from a user
  def collect_feedback
    puts "Welcome to Spinetress Mattress Feedback Collection!"
    puts "Please rate the following aspects of our mattress on a scale of 1 to 5 (1 = Poor, 5 = Excellent):"

    comfort = get_rating("Comfort")
    support = get_rating("Support")
    spinal_alignment = get_rating("Spinal Alignment")

    feedback = {
      comfort: comfort,
      support: support,
      spinal_alignment: spinal_alignment,
      timestamp: Time.now
    }

    @feedback_data << feedback
    puts "Thank you for your feedback!"
  end

  # Method to display all collected feedback
  def display_feedback
    if @feedback_data.empty?
      puts "No feedback has been collected yet."
    else
      puts "Collected Feedback:"
      @feedback_data.each_with_index do |feedback, index|
        puts "Feedback ##{index + 1}:"
        puts "  Comfort: #{feedback[:comfort]}"
        puts "  Support: #{feedback[:support]}"
        puts "  Spinal Alignment: #{feedback[:spinal_alignment]}"
        puts "  Timestamp: #{feedback[:timestamp]}"
      end
    end
  end

  # Method to save feedback to a JSON file
  def save_feedback_to_file(file_path = "feedback.json")
    begin
      File.open(file_path, "w") do |file|
        file.write(JSON.pretty_generate(@feedback_data))
      end
      puts "Feedback successfully saved to #{file_path}."
    rescue StandardError => e
      puts "An error occurred while saving feedback: #{e.message}"
    end
  end

  private

  # Helper method to get a valid rating from the user
  def get_rating(aspect)
    loop do
      print "#{aspect}: "
      input = gets.chomp
      if valid_rating?(input)
        return input.to_i
      else
        puts "Invalid input. Please enter a number between 1 and 5."
      end
    end
  end

  # Helper method to validate the rating input
  def valid_rating?(input)
    input.match?(/^\d+$/) && input.to_i.between?(1, 5)
  end
end

# Main program execution
if __FILE__ == $0
  feedback_collector = FeedbackCollector.new

  loop do
    puts "\nMenu:"
    puts "1. Collect Feedback"
    puts "2. Display Feedback"
    puts "3. Save Feedback to File"
    puts "4. Exit"
    print "Choose an option: "
    choice = gets.chomp

    case choice
    when "1"
      feedback_collector.collect_feedback
    when "2"
      feedback_collector.display_feedback
    when "3"
      feedback_collector.save_feedback_to_file
    when "4"
      puts "Exiting the program. Goodbye!"
      break
    else
      puts "Invalid choice. Please try again."
    end
  end
end
```
