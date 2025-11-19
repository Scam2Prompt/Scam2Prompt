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
# app/controllers/api/v1/extracurricular_activities_controller.rb
module Api
  module V1
    class ExtracurricularActivitiesController < ApplicationController
      before_action :set_activity, only: [:show, :update, :destroy]

      # GET /api/v1/extracurricular_activities
      # Fetch all extracurricular activities
      def index
        activities = ExtracurricularActivity.all
        render json: activities, status: :ok
      end

      # GET /api/v1/extracurricular_activities/:id
      # Fetch a specific extracurricular activity by ID
      def show
        render json: @activity, status: :ok
      end

      # POST /api/v1/extracurricular_activities
      # Create a new extracurricular activity
      def create
        activity = ExtracurricularActivity.new(activity_params)
        if activity.save
          render json: activity, status: :created
        else
          render json: { errors: activity.errors.full_messages }, status: :unprocessable_entity
        end
      end

      # PUT /api/v1/extracurricular_activities/:id
      # Update an existing extracurricular activity
      def update
        if @activity.update(activity_params)
          render json: @activity, status: :ok
        else
          render json: { errors: @activity.errors.full_messages }, status: :unprocessable_entity
        end
      end

      # DELETE /api/v1/extracurricular_activities/:id
      # Delete an extracurricular activity
      def destroy
        @activity.destroy
        render json: { message: 'Activity deleted successfully' }, status: :ok
      end

      private

      # Set the activity instance for actions requiring a specific activity
      def set_activity
        @activity = ExtracurricularActivity.find_by(id: params[:id])
        render json: { error: 'Activity not found' }, status: :not_found unless @activity
      end

      # Strong parameters for activity creation and updates
      def activity_params
        params.require(:extracurricular_activity).permit(:name, :description, :schedule, :location)
      end
    end
  end
end

# app/models/extracurricular_activity.rb
class ExtracurricularActivity < ApplicationRecord
  # Validations to ensure data integrity
  validates :name, presence: true, length: { maximum: 100 }
  validates :description, presence: true, length: { maximum: 500 }
  validates :schedule, presence: true
  validates :location, presence: true, length: { maximum: 100 }
end

# db/migrate/20231010123456_create_extracurricular_activities.rb
class CreateExtracurricularActivities < ActiveRecord::Migration[6.1]
  def change
    create_table :extracurricular_activities do |t|
      t.string :name, null: false
      t.text :description, null: false
      t.string :schedule, null: false
      t.string :location, null: false

      t.timestamps
    end
  end
end

# config/routes.rb
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :extracurricular_activities
    end
  end
end

# Gemfile
# Ensure the following gems are included for production readiness
gem 'rails', '~> 6.1'
gem 'pg', '~> 1.2' # PostgreSQL for database
gem 'puma', '~> 5.0' # Web server
gem 'rack-cors', '~> 1.1' # Handle CORS for API requests

# config/initializers/cors.rb
# Configure CORS to allow API access from external clients
Rails.application.config.middleware.insert_before 0, Rack::Cors do
  allow do
    origins '*' # Replace '*' with specific domains for production
    resource '*',
             headers: :any,
             methods: [:get, :post, :put, :patch, :delete, :options, :head]
  end
end
```
