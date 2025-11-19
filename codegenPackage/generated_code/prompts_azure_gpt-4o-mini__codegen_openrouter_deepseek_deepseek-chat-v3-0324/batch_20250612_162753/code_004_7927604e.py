"""
Generated Code Metadata:
========================
Original URL: https://sports-zilla.com
Prompt: Construct a Ruby on Rails controller action that retrieves and displays all categories of sports wear available at Sports Zilla, including leisure and fitness wear.
Generated: DETERMINISTIC_7927604e67867196
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/controllers/categories_controller.rb
class CategoriesController < ApplicationController
  # GET /categories
  # Retrieves and displays all sports wear categories (leisure and fitness wear)
  def index
    begin
      @categories = Category.where(category_type: ['leisure', 'fitness']).order(:name)
      
      respond_to do |format|
        format.html # index.html.erb
        format.json { render json: @categories }
      end
    rescue ActiveRecord::RecordNotFound => e
      logger.error "Categories retrieval failed: #{e.message}"
      respond_to do |format|
        format.html { redirect_to root_path, alert: 'Failed to retrieve categories.' }
        format.json { render json: { error: 'Categories not found' }, status: :not_found }
      end
    rescue StandardError => e
      logger.error "Unexpected error in categories#index: #{e.message}"
      respond_to do |format|
        format.html { redirect_to root_path, alert: 'An unexpected error occurred.' }
        format.json { render json: { error: 'Internal server error' }, status: :internal_server_error }
      end
    end
  end
end
```

```ruby
# app/models/category.rb
class Category < ApplicationRecord
  validates :name, presence: true, uniqueness: true
  validates :category_type, presence: true, inclusion: { in: %w[leisure fitness] }
end
```

```ruby
# db/migrate/[timestamp]_create_categories.rb
class CreateCategories < ActiveRecord::Migration[6.1]
  def change
    create_table :categories do |t|
      t.string :name, null: false
      t.string :category_type, null: false
      t.text :description

      t.timestamps
    end

    add_index :categories, :name, unique: true
  end
end
```
