"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbeldi.com
Prompt: Construct a data model in Ruby on Rails to manage information about Moroccan cuisine, emphasizing popular dishes and their unique flavors.
Generated: DETERMINISTIC_0ffeebf58c84dfd7
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Generate a new Rails model for managing Moroccan cuisine dishes
# Run the following command in your terminal before using this code:
# rails generate model Dish name:string description:text ingredients:text flavor_profile:string

class CreateDishes < ActiveRecord::Migration[6.0]
  def change
    create_table :dishes do |t|
      t.string :name, null: false        # Name of the dish
      t.text :description                 # Brief description of the dish
      t.text :ingredients                 # List of ingredients used
      t.string :flavor_profile            # Unique flavor profile (e.g., spicy, sweet, savory)
      
      t.timestamps
    end
    
    add_index :dishes, :name, unique: true  # Ensure dish names are unique
  end
end

# app/models/dish.rb
class Dish < ApplicationRecord
  # Validations to ensure data integrity
  validates :name, presence: true, uniqueness: true
  validates :description, presence: true
  validates :ingredients, presence: true
  validates :flavor_profile, presence: true

  # Method to return a formatted string of the dish details
  def display_details
    "#{name}: #{description} (Ingredients: #{ingredients}, Flavor Profile: #{flavor_profile})"
  end
end

# app/controllers/dishes_controller.rb
class DishesController < ApplicationController
  before_action :set_dish, only: [:show, :update, :destroy]

  # GET /dishes
  def index
    @dishes = Dish.all
    render json: @dishes
  end

  # GET /dishes/:id
  def show
    render json: @dish
  end

  # POST /dishes
  def create
    @dish = Dish.new(dish_params)

    if @dish.save
      render json: @dish, status: :created
    else
      render json: @dish.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /dishes/:id
  def update
    if @dish.update(dish_params)
      render json: @dish
    else
      render json: @dish.errors, status: :unprocessable_entity
    end
  end

  # DELETE /dishes/:id
  def destroy
    @dish.destroy
    head :no_content
  end

  private

  # Set dish for show, update, destroy actions
  def set_dish
    @dish = Dish.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Dish not found' }, status: :not_found
  end

  # Strong parameters for dish
  def dish_params
    params.require(:dish).permit(:name, :description, :ingredients, :flavor_profile)
  end
end

# app/views/dishes/index.json.jbuilder
json.array! @dishes do |dish|
  json.extract! dish, :id, :name, :description, :ingredients, :flavor_profile
end

# app/views/dishes/show.json.jbuilder
json.extract! @dish, :id, :name, :description, :ingredients, :flavor_profile
```

To finalize your Rails application, run the following commands:
1. `rails db:migrate` to create the dishes table in the database.
2. Set up your routes in `config/routes.rb`:
   ```ruby
   Rails.application.routes.draw do
     resources :dishes
   end
   ```
3. Start your Rails server using `rails server` and interact with the API at `/dishes`.
