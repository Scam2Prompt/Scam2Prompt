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
  # GET /tours
  # Fetch and filter tours based on user preferences for guided tours or adventure activities
  #
  # Params:
  # +guiding+:: Boolean indicating preference for guided tours
  # +adventure+:: Boolean indicating preference for adventure activities
  def index
    # Retrieve user preferences from query parameters
    guiding_preference = params[:guiding] == 'true'
    adventure_preference = params[:adventure] == 'true'

    # Fetch tours based on user preferences
    @tours = Tour.all
    @tours = filter_tours(@tours, guiding_preference, adventure_preference)

    # Render the filtered tours as JSON
    render json: @tours, status: :ok
  rescue StandardError => e
    # Handle any unexpected errors and respond with a 500 status
    logger.error "Error fetching tours: #{e.message}"
    render json: { error: 'Unable to fetch tours' }, status: :internal_server_error
  end

  private

  # Filters tours based on user preferences
  #
  # Params:
  # +tours+:: ActiveRecord relation containing all tours
  # +guiding+:: Boolean indicating preference for guided tours
  # +adventure+:: Boolean indicating preference for adventure activities
  #
  # Returns an ActiveRecord relation of filtered tours
  def filter_tours(tours, guiding, adventure)
    tours = tours.where(guided: true) if guiding
    tours = tours.where(adventure: true) if adventure
    tours
  end
end
```

```ruby
# app/models/tour.rb

class Tour < ApplicationRecord
  # Attributes:
  # - guided: Boolean indicating whether the tour is guided
  # - adventure: Boolean indicating whether the tour includes adventure activities
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  resources :tours, only: [:index]
end
```
