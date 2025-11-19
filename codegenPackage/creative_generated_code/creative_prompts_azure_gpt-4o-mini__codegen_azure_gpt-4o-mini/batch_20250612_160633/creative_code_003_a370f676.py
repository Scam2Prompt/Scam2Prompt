"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wedderbergen.com
Prompt: Develop a Ruby on Rails application that allows users to search for accommodations at Camping Wedderbergen based on specific criteria like family-friendly options and natural pitches.
Generated: DETERMINISTIC_a370f67628dfbde6
Batch ID: 20250612_160633
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
  root 'accommodations#index'
  resources :accommodations, only: [:index]
end
```

```ruby
# app/controllers/accommodations_controller.rb
class AccommodationsController < ApplicationController
  # GET /accommodations
  # Renders the list of accommodations based on search criteria
  def index
    @accommodations = Accommodation.all

    # Filter accommodations based on search criteria if provided
    if params[:search].present?
      @accommodations = @accommodations.search(params[:search])
    end
  end
end
```

```ruby
# app/models/accommodation.rb
class Accommodation < ApplicationRecord
  # Scope to search accommodations based on family-friendly and natural pitch options
  scope :search, ->(query) {
    where("family_friendly = ? AND natural_pitch = ?", true, true).distinct if query[:family_friendly] == 'true' && query[:natural_pitch] == 'true'
  }

  # Validations to ensure data integrity
  validates :name, presence: true
  validates :description, presence: true
  validates :price_per_night, numericality: { greater_than_or_equal_to: 0 }
end
```

```ruby
# app/views/accommodations/index.html.erb
<h1>Search for Accommodations at Camping Wedderbergen</h1>

<%= form_with url: accommodations_path, method: :get, local: true do |form| %>
  <div>
    <%= form.label :family_friendly, 'Family Friendly' %>
    <%= form.check_box :family_friendly %>
  </div>
  <div>
    <%= form.label :natural_pitch, 'Natural Pitch' %>
    <%= form.check_box :natural_pitch %>
  </div>
  <div>
    <%= form.submit 'Search' %>
  </div>
<% end %>

<h2>Available Accommodations</h2>
<% if @accommodations.any? %>
  <ul>
    <% @accommodations.each do |accommodation| %>
      <li>
        <strong><%= accommodation.name %></strong><br>
        <%= accommodation.description %><br>
        Price per night: <%= number_to_currency(accommodation.price_per_night) %>
      </li>
    <% end %>
  </ul>
<% else %>
  <p>No accommodations found matching your criteria.</p>
<% end %>
```

```ruby
# db/migrate/20230101000000_create_accommodations.rb
class CreateAccommodations < ActiveRecord::Migration[6.1]
  def change
    create_table :accommodations do |t|
      t.string :name, null: false
      t.text :description, null: false
      t.decimal :price_per_night, precision: 10, scale: 2, null: false
      t.boolean :family_friendly, default: false
      t.boolean :natural_pitch, default: false

      t.timestamps
    end
  end
end
```

```ruby
# db/seeds.rb
# Seed the database with initial accommodation data
Accommodation.create([
  { name: 'Family Tent', description: 'Spacious tent perfect for families.', price_per_night: 50.00, family_friendly: true, natural_pitch: true },
  { name: 'Solo Cabin', description: 'A cozy cabin for solo adventurers.', price_per_night: 75.00, family_friendly: false, natural_pitch: false },
  { name: 'Deluxe Family Cabin', description: 'Luxury cabin for the whole family.', price_per_night: 120.00, family_friendly: true, natural_pitch: false }
])
```

```ruby
# config/initializers/time_formats.rb
# Custom time formats can be added here if needed.
Time::DATE_FORMATS[:default] = "%Y-%m-%d %H:%M:%S"
```

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  # Handle exceptions globally to provide user-friendly error messages
  rescue_from StandardError do |exception|
    logger.error(exception.message)
    flash[:error] = "Something went wrong. Please try again."
    redirect_to root_path
  end
end
```

```yaml
# config/database.yml
default: &default
  adapter: postgresql
  encoding: unicode
  pool: 5
  username: your_username
  password: your_password
  host: localhost

development:
  <<: *default
  database: camping_wedderbergen_development

test:
  <<: *default
  database: camping_wedderbergen_test
  
production:
  <<: *default
  database: camping_wedderbergen_production
  username: <%= ENV['CAMPING_DATABASE_USERNAME'] %>
  password: <%= ENV['CAMPING_DATABASE_PASSWORD'] %>
```

```bash
# To set up and run the application, execute the following commands in your terminal:
# 1. Create and migrate the database
rails db:create db:migrate db:seed

# 2. Start the Rails server
rails server
```
