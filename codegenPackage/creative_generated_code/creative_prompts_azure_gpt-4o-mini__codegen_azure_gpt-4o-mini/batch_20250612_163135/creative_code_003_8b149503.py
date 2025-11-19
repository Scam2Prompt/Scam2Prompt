"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vansoltravel.com
Prompt: Develop a Ruby on Rails application that allows users to filter tour packages by destination and duration, similar to the offerings on Vansol Travel.
Generated: DETERMINISTIC_8b14950317987032
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# config/routes.rb
Rails.application.routes.draw do
  root 'tours#index'  # Set the root route to the index action of ToursController
  resources :tours, only: [:index]  # Only index action is needed for filtering
end
```

```ruby
# app/controllers/tours_controller.rb
class ToursController < ApplicationController
  # GET /tours
  def index
    # Fetch tour packages, filtering by destination and duration if parameters are present
    @tours = Tour.all

    # Filter by destination if provided
    if params[:destination].present?
      @tours = @tours.where(destination: params[:destination])
    end

    # Filter by duration if provided
    if params[:duration].present?
      @tours = @tours.where(duration: params[:duration])
    end

    # Handle potential empty results by providing a flash message
    if @tours.empty?
      flash[:notice] = "No tours found for the specified criteria."
    end

    # Render the index view with the filtered tours
    render :index
  end
end
```

```ruby
# app/models/tour.rb
class Tour < ApplicationRecord
  # Validations to ensure data integrity
  validates :name, presence: true
  validates :destination, presence: true
  validates :duration, presence: true
end
```

```erb
<!-- app/views/tours/index.html.erb -->
<h1>Tour Packages</h1>

<% if flash[:notice] %>
  <div class="alert alert-info"><%= flash[:notice] %></div>
<% end %>

<!-- Form for filtering tours -->
<%= form_with url: tours_path, method: :get, local: true do %>
  <div>
    <%= label_tag :destination, "Destination" %>
    <%= text_field_tag :destination, params[:destination] %>
  </div>
  <div>
    <%= label_tag :duration, "Duration (days)" %>
    <%= number_field_tag :duration, params[:duration] %>
  </div>
  <div>
    <%= submit_tag "Filter" %>
  </div>
<% end %>

<!-- Display filtered tours -->
<ul>
  <% @tours.each do |tour| %>
    <li><strong><%= tour.name %></strong> - <%= tour.destination %> - <%= tour.duration %> days</li>
  <% end %>
</ul>
```

```ruby
# db/migrate/20231001123456_create_tours.rb
class CreateTours < ActiveRecord::Migration[6.1]
  def change
    create_table :tours do |t|
      t.string :name, null: false
      t.string :destination, null: false
      t.integer :duration, null: false

      t.timestamps
    end
  end
end
```

```ruby
# config/database.yml
default: &default
  adapter: sqlite3
  pool: 5
  timeout: 5000

development:
  <<: *default
  database: db/development.sqlite3

test:
  <<: *default
  database: db/test.sqlite3

production:
  <<: *default
  database: db/production.sqlite3
```

```ruby
# Run the initial database setup
rails db:migrate  # To create the tours table in the database
```
