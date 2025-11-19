"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graylinegeneva.com
Prompt: Develop a Ruby on Rails controller action that fetches and filters tours in Lausanne based on user preferences for guided tours or adventure activities.
Generated: DETERMINISTIC_f1bf4eb8cbf13445
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/tours_controller.rb

class ToursController < ApplicationController
  # Fetches and filters tours in Lausanne based on user preferences
  def filter_tours
    begin
      # Ensure `preferences` are passed in the request parameters
      preferences = params[:preferences]
      unless preferences.present?
        render json: { error: "Preferences parameter is required" }, status: :bad_request and return
      end

      # Fetch tours located in Lausanne
      lausanne_tours = Tour.where(location: 'Lausanne')

      # Filter based on user preferences
      case preferences.downcase
      when 'guided'
        filtered_tours = lausanne_tours.where(category: 'Guided Tour')
      when 'adventure'
        filtered_tours = lausanne_tours.where(category: 'Adventure')
      else
        render json: { error: "Invalid preference value. Choose 'guided' or 'adventure'." }, status: :unprocessable_entity and return
      end

      # Return the filtered tours as JSON
      render json: filtered_tours, status: :ok
    rescue => e
      # Handle unexpected errors and return a generic error message
      render json: { error: "An error occurred: #{e.message}" }, status: :internal_server_error
    end
  end
end
```

**Assumptions:**
1. The `Tour` model exists and has attributes `location` and `category`.
2. The `preferences` parameter is passed as part of the request.
3. Error handling is included for missing parameters and invalid preferences.
