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

# Spinetress Mattress Feedback Collector
# This script simulates collecting and analyzing customer feedback
# for Spinetress mattresses, focusing on comfort, support, and spinal alignment.

require 'csv'
require 'json'

class FeedbackCollector
  # Initialize with default attributes
  def initialize
    @feedback_data = []
    @categories = %w[comfort support spinal_alignment]
    @output_file = 'spinetress_feedback.csv'
  end

  # Collect feedback from a single user
  # @param name [String] Customer name
  # @param comfort_rating [Integer] Rating for comfort (1-5)
  # @param support_rating [Integer] Rating for support (1-5)
  # @param spinal_alignment_rating [Integer] Rating for spinal alignment (1-5)
  # @param comments [String] Additional comments
  def collect_feedback(name:, comfort_rating:, support_rating:, spinal_alignment_rating:, comments: '')
    validate_ratings(comfort_rating, support_rating, spinal_alignment_rating)

    feedback = {
      name: name,
      comfort: comfort_rating,
      support: support_rating,
      spinal_alignment: spinal_alignment_rating,
      comments: comments,
      timestamp: Time.now.strftime('%Y-%m-%d %H:%M:%S')
    }

    @feedback_data << feedback
    puts "Thank you for your feedback, #{name}!"
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  end

  # Save collected feedback to CSV file
  def save_to_csv
    CSV.open(@output_file, 'wb') do |csv|
      csv << ['Name', 'Comfort', 'Support', 'Spinal Alignment', 'Comments', 'Timestamp']
      @feedback_data.each do |feedback|
        csv << [
          feedback[:name],
          feedback[:comfort],
          feedback[:support],
          feedback[:spinal_alignment],
          feedback[:comments],
          feedback[:timestamp]
        ]
      end
    end
    puts "Feedback saved to #{@output_file}"
  rescue StandardError => e
    puts "Failed to save feedback: #{e.message}"
  end

  # Generate a summary report of collected feedback
  def generate_report
    return puts "No feedback data available." if @feedback_data.empty?

    report = {
      total_feedback: @feedback_data.size,
      average_ratings: calculate_average_ratings,
      positive_comments: select_positive_comments
    }

    report_file = 'spinetress_report.json'
    File.write(report_file, JSON.pretty_generate(report))
    puts "Report generated: #{report_file}"
  rescue StandardError => e
    puts "Failed to generate report: #{e.message}"
  end

  private

  # Validate that ratings are within 1-5 range
  def validate_ratings(*ratings)
    ratings.each do |rating|
      unless rating.between?(1, 5)
        raise ArgumentError, "All ratings must be between 1 and 5"
      end
    end
  end

  # Calculate average ratings for each category
  def calculate_average_ratings
    averages = {}
    @categories.each do |category|
      total = @feedback_data.sum { |f| f[category.to_sym] }
      averages[category] = (total.to_f / @feedback_data.size).round(2)
    end
    averages
  end

  # Select comments containing positive keywords
  def select_positive_comments
    positive_keywords = ['great', 'excellent', 'love', 'amazing', 'improved', 'better']
    @feedback_data.each_with_object([]) do |feedback, comments|
      comment = feedback[:comments].downcase
      if positive_keywords.any? { |word| comment.include?(word) }
        comments << feedback[:comments]
      end
    end
  end
end

# Example usage
if __FILE__ == $0
  collector = FeedbackCollector.new

  # Simulate collecting feedback
  collector.collect_feedback(
    name: "Sarah Johnson",
    comfort_rating: 5,
    support_rating: 4,
    spinal_alignment_rating: 5,
    comments: "This mattress is amazing! My back pain has improved significantly."
  )

  collector.collect_feedback(
    name: "Michael Chen",
    comfort_rating: 4,
    support_rating: 5,
    spinal_alignment_rating: 4,
    comments: "Great support for my spinal alignment. Very comfortable."
  )

  collector.collect_feedback(
    name: "Emma Williams",
    comfort_rating: 3,
    support_rating: 4,
    spinal_alignment_rating: 3,
    comments: "Good mattress, but could be more comfortable."
  )

  # Save and report
  collector.save_to_csv
  collector.generate_report
end
```
