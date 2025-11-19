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
# frozen_string_literal: true

# Class representing a user feedback for Spinetress mattresses
class UserFeedback
  attr_accessor :comfort_rating, :support_rating, :spinal_alignment_rating, :testimonial

  def initialize(comfort_rating:, support_rating:, spinal_alignment_rating:, testimonial:)
    @comfort_rating = comfort_rating
    @support_rating = support_rating
    @spinal_alignment_rating = spinal_alignment_rating
    @testimonial = testimonial
  end

  # Validate ratings
  def valid?
    [comfort_rating, support_rating, spinal_alignment_rating].all? { |rating| (1..5).include?(rating) }
  end
end

# Class for collecting and managing user feedback
class FeedbackCollector
  attr_accessor :feedbacks

  def initialize
    @feedbacks = []
  end

  # Collect user feedback
  def collect_feedback
    print "Enter comfort rating (1-5): "
    comfort_rating = gets.chomp.to_i
    print "Enter support rating (1-5): "
    support_rating = gets.chomp.to_i
    print "Enter spinal alignment rating (1-5): "
    spinal_alignment_rating = gets.chomp.to_i
    print "Enter your testimonial: "
    testimonial = gets.chomp

    feedback = UserFeedback.new(
      comfort_rating: comfort_rating,
      support_rating: support_rating,
      spinal_alignment_rating: spinal_alignment_rating,
      testimonial: testimonial
    )

    if feedback.valid?
      @feedbacks << feedback
      puts "Feedback collected successfully!"
    else
      puts "Invalid rating. Please enter a rating between 1 and 5."
    end
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end

  # Display collected feedback
  def display_feedbacks
    @feedbacks.each_with_index do |feedback, index|
      puts "Feedback ##{index + 1}:"
      puts "Comfort Rating: #{feedback.comfort_rating}/5"
      puts "Support Rating: #{feedback.support_rating}/5"
      puts "Spinal Alignment Rating: #{feedback.spinal_alignment_rating}/5"
      puts "Testimonial: #{feedback.testimonial}"
      puts "------------------------"
    end
  end
end

# Main function
def main
  collector = FeedbackCollector.new

  loop do
    puts "Spinetress Mattress Feedback Collector"
    puts "1. Collect Feedback"
    puts "2. Display Feedbacks"
    puts "3. Exit"
    print "Choose an option: "
    option = gets.chomp.to_i

    case option
    when 1
      collector.collect_feedback
    when 2
      collector.display_feedbacks
    when 3
      break
    else
      puts "Invalid option. Please choose a valid option."
    end
  end
end

main
```
