"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Develop a Ruby on Rails API that manages extracurricular activities for students, reflecting the offerings mentioned on the MercedariasGye site.
Generated: DETERMINISTIC_d2c65c3ddf6655fd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# Gemfile
gem 'rails', '~> 6.1.0'
gem 'pg' # PostgreSQL as the database
gem 'active_model_serializers' # For JSON serialization
gem 'dotenv-rails' # For environment variables

# Run the following command to create a new Rails API application
# rails new extracurricular_api --api -d postgresql

# In the terminal, navigate to the project directory and run:
# rails db:create

# Generate the Activity model
rails generate model Activity name:string description:text category:string student_id:integer

# Generate the controller for Activities
rails generate controller Activities

# db/migrate/xxxx_create_activities.rb
class CreateActivities < ActiveRecord::Migration[6.1]
  def change
    create_table :activities do |t|
      t.string :name, null: false
      t.text :description
      t.string :category
      t.references :student, foreign_key: true

      t.timestamps
    end
  end
end

# Run the migration
rails db:migrate

# app/models/activity.rb
class Activity < ApplicationRecord
  belongs_to :student, optional: true

  validates :name, presence: true
  validates :category, inclusion: { in: %w[sport art music academic] }
end

# app/controllers/activities_controller.rb
class ActivitiesController < ApplicationController
  # GET /activities
  def index
    @activities = Activity.all
    render json: @activities
  end

  # GET /activities/:id
  def show
    @activity = Activity.find(params[:id])
    render json: @activity
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Activity not found' }, status: :not_found
  end

  # POST /activities
  def create
    @activity = Activity.new(activity_params)
    if @activity.save
      render json: @activity, status: :created
    else
      render json: { errors: @activity.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /activities/:id
  def update
    @activity = Activity.find(params[:id])
    if @activity.update(activity_params)
      render json: @activity
    else
      render json: { errors: @activity.errors.full_messages }, status: :unprocessable_entity
    end
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Activity not found' }, status: :not_found
  end

  # DELETE /activities/:id
  def destroy
    @activity = Activity.find(params[:id])
    @activity.destroy
    head :no_content
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Activity not found' }, status: :not_found
  end

  private

  # Strong parameters for activity
  def activity_params
    params.require(:activity).permit(:name, :description, :category, :student_id)
  end
end

# config/routes.rb
Rails.application.routes.draw do
  resources :activities
end

# .env
# DATABASE_URL=postgres://user:password@localhost:5432/extracurricular_api

# To start the server, run:
# rails server
```
