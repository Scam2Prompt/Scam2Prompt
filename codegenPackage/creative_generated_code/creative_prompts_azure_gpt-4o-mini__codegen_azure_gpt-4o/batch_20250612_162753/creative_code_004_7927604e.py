"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sports-zilla.com
Prompt: Construct a Ruby on Rails controller action that retrieves and displays all categories of sports wear available at Sports Zilla, including leisure and fitness wear.
Generated: DETERMINISTIC_7927604e67867196
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/categories_controller.rb

class CategoriesController < ApplicationController
  # GET /categories/sports_wear
  # Retrieves and displays all categories of sports wear including leisure and fitness wear.
  def sports_wear
    begin
      # Fetch all sports wear categories
      @categories = Category.where(category_type: ['leisure', 'fitness'])

      # Respond with the categories in JSON format
      render json: { status: 'success', data: @categories }, status: :ok
    rescue => e
      # Handle any potential errors
      render json: { status: 'error', message: e.message }, status: :internal_server_error
    end
  end
end
```

```ruby
# app/models/category.rb

class Category < ApplicationRecord
  # Validations to ensure data integrity
  validates :name, presence: true
  validates :category_type, presence: true

  # Scopes for reusability (if needed in future extensions)
  scope :leisure_wear, -> { where(category_type: 'leisure') }
  scope :fitness_wear, -> { where(category_type: 'fitness') }
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  # Define the route for sports wear categories
  get '/categories/sports_wear', to: 'categories#sports_wear'
end
```

```ruby
# db/migrate/XXXX_create_categories.rb

class CreateCategories < ActiveRecord::Migration[7.0]
  def change
    create_table :categories do |t|
      t.string :name, null: false
      t.string :category_type, null: false # e.g., 'leisure', 'fitness', etc.

      t.timestamps
    end

    # Add an index for category_type for faster query performance
    add_index :categories, :category_type
  end
end
```

```ruby
# Example seed data: db/seeds.rb

Category.create(name: 'Yoga Wear', category_type: 'fitness')
Category.create(name: 'Running Shoes', category_type: 'fitness')
Category.create(name: 'Casual Sports Jackets', category_type: 'leisure')
Category.create(name: 'Relaxed Fit Pants', category_type: 'leisure')
```
