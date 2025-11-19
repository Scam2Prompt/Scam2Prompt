"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moraragora.com.br
Prompt: Develop a Ruby on Rails controller action that fetches and displays a list of residential properties managed by Morar Agora, including filtering options by price range and type.
Generated: DETERMINISTIC_8290bbacbb0e30f0
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
class PropertiesController < ApplicationController
  # GET /properties
  # Fetch and display residential properties managed by Morar Agora
  def index
    begin
      # Initialize the base query for properties managed by Morar Agora
      @properties = Property.where(manager: 'Morar Agora', property_type: 'residential')

      # Apply filtering by price range if parameters are provided
      if params[:min_price].present? && params[:max_price].present?
        min_price = params[:min_price].to_f
        max_price = params[:max_price].to_f
        @properties = @properties.where(price: min_price..max_price)
      end

      # Apply filtering by property type if parameter is provided
      if params[:type].present?
        @properties = @properties.where(type: params[:type])
      end

      # Render the properties in JSON format (can be adapted for other formats)
      render json: { properties: @properties }, status: :ok
    rescue StandardError => e
      # Handle unexpected errors gracefully
      render json: { error: 'An error occurred while fetching properties', details: e.message }, status: :internal_server_error
    end
  end
end
```
