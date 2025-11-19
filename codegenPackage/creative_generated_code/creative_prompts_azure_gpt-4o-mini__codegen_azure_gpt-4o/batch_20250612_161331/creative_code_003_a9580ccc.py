"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://market-idex.com
Prompt: Develop a Ruby on Rails application that allows users to sign up for fitness camps and manage their profiles, including tracking their training progress.
Generated: DETERMINISTIC_a9580ccceda9088f
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a Ruby on Rails application that fulfills your request. To keep things succinct, I'll demonstrate the basics of the application: models, controllers, and views for user signup, profile management, and tracking training progress. 

```ruby
# Gemfile
# Add any dependencies for authentication and other features
gem 'devise' # User authentication
gem 'bootstrap', '~> 5.2.0' # For styling

# Run `bundle install` after adding dependencies

# Database migration for users
# db/migrate/20231001010101_create_users.rb
class CreateUsers < ActiveRecord::Migration[6.1]
  def change
    create_table :users do |t|
      t.string :email, null: false, default: ""
      t.string :encrypted_password, null: false, default: ""
      t.string :name
      t.integer :age
      t.string :gender
      t.timestamps
    end

    add_index :users, :email, unique: true
  end
end

# Database migration for fitness camps
# db/migrate/20231001010202_create_fitness_camps.rb
class CreateFitnessCamps < ActiveRecord::Migration[6.1]
  def change
    create_table :fitness_camps do |t|
      t.string :name, null: false
      t.text :description
      t.date :start_date
      t.date :end_date
      t.timestamps
    end
  end
end

# Database migration for training progress
# db/migrate/20231001010303_create_training_progress.rb
class CreateTrainingProgress < ActiveRecord::Migration[6.1]
  def change
    create_table :training_progresses do |t|
      t.references :user, null: false, foreign_key: true
      t.references :fitness_camp, null: false, foreign_key: true
      t.integer :progress_percent, default: 0
      t.date :updated_at
      t.timestamps
    end
  end
end

# User model
# app/models/user.rb
class User < ApplicationRecord
  # Devise authentication
  devise :database_authenticatable, :registerable, :recoverable, :rememberable, :validatable

  # Associations
  has_many :training_progresses
  has_many :fitness_camps, through: :training_progresses

  # Validations
  validates :name, presence: true
  validates :age, numericality: { greater_than_or_equal_to: 18, less_than_or_equal_to: 100 }
end

# FitnessCamp model
# app/models/fitness_camp.rb
class FitnessCamp < ApplicationRecord
  # Associations
  has_many :training_progresses
  has_many :users, through: :training_progresses

  # Validations
  validates :name, presence: true
  validates :start_date, presence: true
  validates :end_date, presence: true, comparison: { greater_than: :start_date }
end

# TrainingProgress model
# app/models/training_progress.rb
class TrainingProgress < ApplicationRecord
  # Associations
  belongs_to :user
  belongs_to :fitness_camp

  # Validations
  validates :progress_percent, numericality: { greater_than_or_equal_to: 0, less_than_or_equal_to: 100 }
end

# Users controller
# app/controllers/users_controller.rb
class UsersController < ApplicationController
  before_action :authenticate_user!

  # Show user profile
  def show
    @user = current_user
    @training_progresses = @user.training_progresses.includes(:fitness_camp)
  end

  # Update user profile
  def update
    @user = current_user
    if @user.update(user_params)
      redirect_to user_path(@user), notice: 'Profile updated successfully.'
    else
      render :edit
    end
  end

  # Permit parameters
  private

  def user_params
    params.require(:user).permit(:name, :age, :gender)
  end
end

# Fitness Camps controller
# app/controllers/fitness_camps_controller.rb
class FitnessCampsController < ApplicationController
  before_action :authenticate_user!

  # List all camps
  def index
    @fitness_camps = FitnessCamp.all
  end

  # Show details of a camp
  def show
    @fitness_camp = FitnessCamp.find(params[:id])
  end
end

# Training Progress controller
# app/controllers/training_progresses_controller.rb
class TrainingProgressesController < ApplicationController
  before_action :authenticate_user!

  # Update training progress
  def update
    @training_progress = TrainingProgress.find(params[:id])
    if @training_progress.update(training_progress_params)
      redirect_to user_path(current_user), notice: 'Training progress updated.'
    else
      render :edit
    end
  end

  # Permit parameters
  private

  def training_progress_params
    params.require(:training_progress).permit(:progress_percent)
  end
end

# Routes
# config/routes.rb
Rails.application.routes.draw do
  devise_for :users
  resources :users, only: [:show, :update]
  resources :fitness_camps, only: [:index, :show]
  resources :training_progresses, only: [:update]
  root 'fitness_camps#index'
end

# Views
# app/views/users/show.html.erb
<h1><%= current_user.name %>'s Profile</h1>
<p>Email: <%= current_user.email %></p>
<p>Age: <%= current_user.age %></p>
<p>Gender: <%= current_user.gender %></p>

<h2>Training Progress</h2>
<% @training_progresses.each do |progress| %>
  <p><%= progress.fitness_camp.name %>: <%= progress.progress_percent %>% completed</p>
<% end %>

<%= link_to 'Edit Profile', edit_user_registration_path %>

# app/views/fitness_camps/index.html.erb
<h1>Fitness Camps</h1>
<% @fitness_camps.each do |camp| %>
  <p><%= link_to camp.name, fitness_camp_path(camp) %></p>
<% end %>

# app/views/fitness_camps/show.html.erb
<h1><%= @fitness_camp.name %></h1>
<p>Description: <%= @fitness_camp.description %></p>
<p>Start Date: <%= @fitness_camp.start_date %></p>
<p>End Date: <%= @fitness_camp.end_date %></p>

<%= link_to 'Back to Camps', fitness_camps_path %>
```

This is the basic structure of the application. You can further enhance it by adding tests, pagination, and other features. Always ensure to check for security vulnerabilities, especially when handling user input and authentication.
