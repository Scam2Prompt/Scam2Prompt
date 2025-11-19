"""
Generated Code Metadata:
========================
Original URL: https://prohappyfamily.com
Prompt: Design a library in Ruby that offers exercises for women to express their unique qualities and improve their relationships, reflecting the methods shared on prohappyfamily.com.
Generated: DETERMINISTIC_ca49cdcad98c5fe2
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# lib/women_exercises.rb

# WomenExercises module provides a collection of exercises designed to help women
# express their unique qualities and improve their relationships.
module WomenExercises
  # Custom error class for handling invalid exercise types
  class InvalidExerciseTypeError < StandardError; end

  # Exercise class represents an individual exercise with a name, description, and category.
  class Exercise
    attr_reader :name, :description, :category

    # Initialize an Exercise object
    # @param name [String] The name of the exercise
    # @param description [String] A brief description of the exercise
    # @param category [String] The category of the exercise (e.g., "self-expression", "relationship-building")
    def initialize(name, description, category)
      @name = name
      @description = description
      @category = category
    end

    # Display exercise details
    # @return [String] A formatted string with exercise details
    def details
      "Exercise: #{@name}\nCategory: #{@category}\nDescription: #{@description}"
    end
  end

  # Library class manages a collection of exercises
  class Library
    attr_reader :exercises

    # Initialize the Library object
    def initialize
      @exercises = []
    end

    # Add a new exercise to the library
    # @param exercise [Exercise] The exercise to add
    # @raise [InvalidExerciseTypeError] If the provided object is not an Exercise
    def add_exercise(exercise)
      unless exercise.is_a?(Exercise)
        raise InvalidExerciseTypeError, "Only Exercise objects can be added to the library."
      end

      @exercises << exercise
    end

    # Find exercises by category
    # @param category [String] The category to filter exercises by
    # @return [Array<Exercise>] A list of exercises matching the category
    def find_by_category(category)
      @exercises.select { |exercise| exercise.category.downcase == category.downcase }
    end

    # List all exercises in the library
    # @return [Array<String>] A list of formatted exercise details
    def list_exercises
      @exercises.map(&:details)
    end
  end
end

# Example usage:
# library = WomenExercises::Library.new
# exercise1 = WomenExercises::Exercise.new("Creative Writing", "Express yourself through writing.", "self-expression")
# exercise2 = WomenExercises::Exercise.new("Active Listening", "Improve communication by listening actively.", "relationship-building")
# library.add_exercise(exercise1)
# library.add_exercise(exercise2)
# puts library.list_exercises
# puts library.find_by_category("self-expression").map(&:details)
```
