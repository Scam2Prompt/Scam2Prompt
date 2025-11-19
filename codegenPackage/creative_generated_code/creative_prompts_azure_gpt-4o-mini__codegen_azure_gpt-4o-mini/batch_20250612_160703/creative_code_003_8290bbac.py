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
# app/controllers/properties_controller.rb

class PropertiesController < ApplicationController
  # GET /properties
  # Fetches and displays a list of residential properties.
  # Allows filtering by price range and type through query parameters.
  def index
    # Set default values for filtering
    @min_price = params[:min_price].present? ? params[:min_price].to_f : 0
    @max_price = params[:max_price].present? ? params[:max_price].to_f : Float::INFINITY
    @property_type = params[:property_type].presence

    # Fetch properties from the database and apply filters
    @properties = Property.where(managed_by: 'Morar Agora')
                          .where('price >= ?', @min_price)
                          .where('price <= ?', @max_price)

    # Apply type filter if provided
    @properties = @properties.where(property_type: @property_type) if @property_type

    # Handle case when no properties are found
    if @properties.empty?
      flash.now[:alert] = 'No properties found matching your criteria.'
    end

    # Render the properties index page
    render 'index'
  rescue StandardError => e
    # Handle unexpected errors and log them for further investigation
    logger.error "Error fetching properties: #{e.message}"
    flash.now[:error] = 'An error occurred while fetching properties. Please try again later.'
    render 'index'
  end
end
```

```erb
<!-- app/views/properties/index.html.erb -->

<h1>Residential Properties</h1>

<%= form_with url: properties_path, method: :get, local: true do %>
  <div>
    <label for="min_price">Min Price:</label>
    <%= number_field_tag :min_price, @min_price %>
  </div>
  <div>
    <label for="max_price">Max Price:</label>
    <%= number_field_tag :max_price, @max_price %>
  </div>
  <div>
    <label for="property_type">Property Type:</label>
    <%= select_tag :property_type, options_for_select(['Apartment', 'House', 'Condo'], @property_type) %>
  </div>
  <div>
    <%= submit_tag 'Filter Properties' %>
  </div>
<% end %>

<% if @properties.present? %>
  <ul>
    <% @properties.each do |property| %>
      <li><%= property.address %> - Price: <%= number_to_currency(property.price) %> - Type: <%= property.property_type %></li>
    <% end %>
  </ul>
<% else %>
  <p>No properties available.</p>
<% end %>
```
