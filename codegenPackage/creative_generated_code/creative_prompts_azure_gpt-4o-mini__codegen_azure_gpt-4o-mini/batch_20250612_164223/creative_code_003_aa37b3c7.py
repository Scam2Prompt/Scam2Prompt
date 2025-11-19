"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spinecomfy.com
Prompt: Develop a code example in Ruby that simulates user feedback collection for Spinetress mattresses, focusing on comfort, support, and spinal alignment, as highlighted in customer testimonials.
Generated: DETERMINISTIC_aa37b3c7275bab42
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# user_feedback.rb

require 'json'
require 'date'

class UserFeedback
  attr_accessor :comfort, :support, :spinal_alignment, :comments, :created_at

  # Initializes a new UserFeedback instance
  #
  # @param comfort [Integer] A rating for comfort (1 to 5)
  # @param support [Integer] A rating for support (1 to 5)
  # @param spinal_alignment [Integer] A rating for spinal alignment (1 to 5)
  # @param comments [String] User comments or testimonials
  def initialize(comfort, support, spinal_alignment, comments)
    @comfort = validate_rating(comfort)
    @support = validate_rating(support)
    @spinal_alignment = validate_rating(spinal_alignment)
    @comments = comments.to_s.strip
    @created_at = DateTime.now
  end

  # Validates the rating input
  #
  # @param rating [Integer] The rating to validate
  # @return [Integer] The validated rating
  # @raise [ArgumentError] If the rating is not between 1 and 5
  def validate_rating(rating)
    raise ArgumentError, 'Rating must be an integer between 1 and 5.' unless rating.is_a?(Integer) && (1..5).cover?(rating)

    rating
  end

  # Converts the feedback to a hash format for easier serialization
  #
  # @return [Hash] The feedback data in hash format
  def to_h
    {
      comfort: @comfort,
      support: @support,
      spinal_alignment: @spinal_alignment,
      comments: @comments,
      created_at: @created_at
    }
  end
end

class FeedbackCollector
  attr_accessor :feedbacks

  # Initializes the feedback collector
  def initialize
    @feedbacks = []
  end

  # Collects user feedback
  #
  # @param feedback [UserFeedback] An instance of UserFeedback
  def collect_feedback(feedback)
    @feedbacks << feedback
  end

  # Saves feedback to a JSON file
  #
  # @param file_path [String] The file path where feedback will be saved
  # @raise [StandardError] If unable to write to the specified file
  def save_feedback(file_path)
    File.open(file_path, 'w') do |file|
      file.write(JSON.pretty_generate(@feedbacks.map(&:to_h)))
    rescue IOError => e
      raise StandardError, "Unable to write to file: #{e.message}"
    end
  end
end

# Example usage

if __FILE__ == $0
  collector = FeedbackCollector.new

  begin
    # Sample feedback collection
    collector.collect_feedback(UserFeedback.new(5, 4, 5, "This mattress has changed my life!"))
    collector.collect_feedback(UserFeedback.new(4, 4, 4, "Very comfortable, but a bit soft for my taste."))

    # Save the feedback to a file
    collector.save_feedback('spinetress_feedback.json')

    puts "Feedback collected and saved successfully."
  rescue ArgumentError => e
    puts "Error collecting feedback: #{e.message}"
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end
```
