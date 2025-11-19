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
# user_feedback.rb

# This class simulates a user feedback collection system for Spinetress mattresses.
class UserFeedback
  attr_accessor :feedbacks

  def initialize
    # Initialize an empty array to store feedbacks
    @feedbacks = []
  end

  # Method to collect feedback from users
  # @param comfort [Integer] Rating for comfort (1-5)
  # @param support [Integer] Rating for support (1-5)
  # @param spinal_alignment [Integer] Rating for spinal alignment (1-5)
  # @param comments [String] Optional comments from the user
  def collect_feedback(comfort, support, spinal_alignment, comments = nil)
    # Validate input ratings
    validate_rating(comfort)
    validate_rating(support)
    validate_rating(spinal_alignment)

    # Create a feedback hash
    feedback = {
      comfort: comfort,
      support: support,
      spinal_alignment: spinal_alignment,
      comments: comments,
      created_at: Time.now
    }

    # Store the feedback
    @feedbacks << feedback
    puts "Feedback collected successfully!"
  rescue StandardError => e
    puts "Error collecting feedback: #{e.message}"
  end

  # Method to display all collected feedbacks
  def display_feedbacks
    if @feedbacks.empty?
      puts "No feedback available."
    else
      @feedbacks.each_with_index do |feedback, index|
        puts "Feedback ##{index + 1}:"
        puts "Comfort: #{feedback[:comfort]}, Support: #{feedback[:support]}, Spinal Alignment: #{feedback[:spinal_alignment]}"
        puts "Comments: #{feedback[:comments]}" if feedback[:comments]
        puts "Submitted at: #{feedback[:created_at]}"
        puts "-" * 30
      end
    end
  end

  private

  # Validates that the rating is an integer between 1 and 5
  # @param rating [Integer] The rating to validate
  # @raise [ArgumentError] If the rating is not valid
  def validate_rating(rating)
    unless rating.is_a?(Integer) && (1..5).include?(rating)
      raise ArgumentError, "Rating must be an integer between 1 and 5."
    end
  end
end

# Example usage
if __FILE__ == $0
  feedback_system = UserFeedback.new

  # Collecting some sample feedback
  feedback_system.collect_feedback(5, 4, 5, "Very comfortable mattress!")
  feedback_system.collect_feedback(3, 3, 4, "Decent support but could be better.")
  feedback_system.collect_feedback(2, 1, 2, "Not what I expected.")

  # Display all collected feedbacks
  feedback_system.display_feedbacks
end
```
