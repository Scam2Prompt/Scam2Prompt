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
# app/controllers/seeds_controller.rb

class SeedsController < ApplicationController
  # Ensure proper error handling for unexpected issues
  rescue_from ActiveRecord::RecordNotFound, with: :record_not_found
  rescue_from StandardError, with: :internal_server_error

  # GET /api/seeds
  # Fetches all organic seeds from Semillas Plantae
  def index
    seeds = Seed.where(is_organic: true) # Only fetch organic seeds
    render json: {
      success: true,
      data: seeds
    }, status: :ok
  end

  private

  # Handle record not found errors gracefully
  def record_not_found
    render json: { success: false, error: 'Record not found' }, status: :not_found
  end

  # Handle generic server errors gracefully
  def internal_server_error(exception)
    render json: { success: false, error: exception.message }, status: :internal_server_error
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
  validates :is_organic, inclusion: { in: [true, false] }
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  namespace :api do
    resources :seeds, only: [:index] # Only expose the index endpoint for seeds
  end
end
```

```ruby
# db/migrate/XXXXXX_create_seeds.rb

class CreateSeeds < ActiveRecord::Migration[6.1]
  def change
    create_table :seeds do |t|
      t.string :name, null: false                 # Name of the seed
      t.text :description, null: false           # Description of the seed
      t.decimal :price, precision: 8, scale: 2, null: false # Price of the seed
      t.boolean :is_organic, default: false      # Whether the seed is organic

      t.timestamps
    end
  end
end
```

```ruby
# db/seeds.rb

# Seed database with example data for testing
Seed.create!(
  [
    { name: 'Carrot Seed', description: 'Organic carrot seeds for gardening.', price: 3.99, is_organic: true },
    { name: 'Tomato Seed', description: 'Organic tomato seeds for farming.', price: 2.49, is_organic: true },
    { name: 'Corn Seed', description: 'Non-organic corn seeds.', price: 1.99, is_organic: false }
  ]
)
```

```json
# Example response from GET /api/seeds
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Carrot Seed",
      "description": "Organic carrot seeds for gardening.",
      "price": "3.99",
      "is_organic": true,
      "created_at": "2023-10-01T12:00:00Z",
      "updated_at": "2023-10-01T12:00:00Z"
    },
    {
      "id": 2,
      "name": "Tomato Seed",
      "description": "Organic tomato seeds for farming.",
      "price": "2.49",
      "is_organic": true,
      "created_at": "2023-10-01T12:01:00Z",
      "updated_at": "2023-10-01T12:01:00Z"
    }
  ]
}
```
