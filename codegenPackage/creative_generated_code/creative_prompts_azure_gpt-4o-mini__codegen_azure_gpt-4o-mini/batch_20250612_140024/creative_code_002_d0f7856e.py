"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://semillasplantae.com
Prompt: Create a Ruby on Rails API endpoint that allows users to retrieve information about organic seeds available at Semillas Plantae, including descriptions and prices.
Generated: DETERMINISTIC_d0f7856efa3b9184
Batch ID: 20250612_140024
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
  # Define a route for retrieving organic seeds
  resources :seeds, only: [:index]
end
```

```ruby
# app/controllers/seeds_controller.rb
class SeedsController < ApplicationController
  # GET /seeds
  # This action retrieves all organic seeds available
  def index
    seeds = Seed.all # Fetch all seeds from the database
    render json: seeds, status: :ok # Respond with JSON and 200 OK status
  rescue StandardError => e
    # Handle any errors that may occur during retrieval
    render json: { error: e.message }, status: :internal_server_error
  end
end
```

```ruby
# app/models/seed.rb
class Seed < ApplicationRecord
  # Validations to ensure data integrity
  validates :name, presence: true
  validates :description, presence: true
  validates :price, numericality: { greater_than_or_equal_to: 0 }

  # Define attributes for the Seed model
  # Assuming attributes: name (string), description (text), price (decimal)
end
```

```ruby
# db/migrate/20230301000000_create_seeds.rb
class CreateSeeds < ActiveRecord::Migration[6.0]
  def change
    create_table :seeds do |t|
      t.string :name, null: false
      t.text :description, null: false
      t.decimal :price, precision: 8, scale: 2, null: false

      t.timestamps
    end

    # Create an index for faster queries (optional)
    add_index :seeds, :name
  end
end
```

```ruby
# db/seeds.rb
# Seed the database with sample data for testing purposes
Seed.create([
  { name: 'Tomato', description: 'Organic tomato seeds.', price: 3.50 },
  { name: 'Basil', description: 'Organic basil seeds.', price: 2.00 },
  { name: 'Carrot', description: 'Organic carrot seeds.', price: 1.75 }
])
```

```yaml
# config/database.yml
# Ensure your database configuration is set correctly for development, test, and production
development:
  adapter: sqlite3
  database: db/development.sqlite3
  pool: 5
  timeout: 5000

test:
  adapter: sqlite3
  database: db/test.sqlite3
  pool: 5
  timeout: 5000

production:
  adapter: postgresql
  encoding: unicode
  database: myapp_production
  pool: 5
  username: myapp
  password: <%= ENV['MYAPP_DATABASE_PASSWORD'] %>
```

```bash
# Command to set up the database
rails db:create db:migrate db:seed
```

This setup provides a clean, well-documented Ruby on Rails API endpoint to retrieve information about organic seeds available at Semillas Plantae.
