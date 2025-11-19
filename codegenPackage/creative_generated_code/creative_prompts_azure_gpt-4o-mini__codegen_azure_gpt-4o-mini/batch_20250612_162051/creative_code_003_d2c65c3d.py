"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercedariasgye.edu.ec
Prompt: Develop a Ruby on Rails API that manages extracurricular activities for students, reflecting the offerings mentioned on the MercedariasGye site.
Generated: DETERMINISTIC_d2c65c3ddf6655fd
Batch ID: 20250612_162051
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
  resources :extracurricular_activities, only: [:index, :show, :create, :update, :destroy]
end
```

```ruby
# app/controllers/extracurricular_activities_controller.rb
class ExtracurricularActivitiesController < ApplicationController
  before_action :set_activity, only: [:show, :update, :destroy]

  # GET /extracurricular_activities
  # Fetch all extracurricular activities
  def index
    activities = ExtracurricularActivity.all
    render json: activities, status: :ok
  end

  # GET /extracurricular_activities/:id
  # Fetch a specific extracurricular activity
  def show
    render json: @activity, status: :ok
  end

  # POST /extracurricular_activities
  # Create a new extracurricular activity
  def create
    activity = ExtracurricularActivity.new(activity_params)
    if activity.save
      render json: activity, status: :created
    else
      render json: activity.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /extracurricular_activities/:id
  # Update an existing extracurricular activity
  def update
    if @activity.update(activity_params)
      render json: @activity, status: :ok
    else
      render json: @activity.errors, status: :unprocessable_entity
    end
  end

  # DELETE /extracurricular_activities/:id
  # Delete an extracurricular activity
  def destroy
    @activity.destroy
    head :no_content
  end

  private

  # Set the extracurricular activity based on id
  def set_activity
    @activity = ExtracurricularActivity.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Extracurricular activity not found' }, status: :not_found
  end

  # Strong parameters for creating/updating activities
  def activity_params
    params.require(:extracurricular_activity).permit(:name, :description, :schedule, :location)
  end
end
```

```ruby
# app/models/extracurricular_activity.rb
class ExtracurricularActivity < ApplicationRecord
  # Validations to ensure data integrity
  validates :name, presence: true, uniqueness: true
  validates :description, presence: true
  validates :schedule, presence: true
  validates :location, presence: true
end
```

```ruby
# db/migrate/20230301000000_create_extracurricular_activities.rb
class CreateExtracurricularActivities < ActiveRecord::Migration[6.1]
  def change
    create_table :extracurricular_activities do |t|
      t.string :name, null: false
      t.text :description, null: false
      t.string :schedule, null: false
      t.string :location, null: false

      t.timestamps
    end

    add_index :extracurricular_activities, :name, unique: true
  end
end
```

```ruby
# config/database.yml
# Ensure your database configuration is set properly for the environment you are using.
# Example for development:
development:
  adapter: postgresql
  encoding: unicode
  database: your_database_name
  pool: 5
  username: your_database_user
  password: your_database_password
  host: localhost
```

```bash
# To create the database and run migrations
rails db:create
rails db:migrate

# To start the Rails server
rails server
```

```ruby
# Gemfile
# Ensure to include necessary gems for the application
gem 'rails', '6.1.4'
gem 'pg', '~> 1.2'
```

```bash
# Run the following command to install the gems
bundle install
```

This Ruby on Rails API provides a basic CRUD interface for managing extracurricular activities for students, ensuring proper error handling and data validation.
