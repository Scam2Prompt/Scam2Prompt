"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Develop a Ruby on Rails application that connects to the PerúMakers database to manage community maker projects.
Generated: DETERMINISTIC_cf65bf4c477f7e47
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rubygems.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```ruby
# Gemfile
source 'https://rubygems.org'

# Rails framework
gem 'rails', '~> 6.1.0'

# Database adapter for PostgreSQL
gem 'pg'

# Add other necessary gems for your application as needed
gem 'devise' # For user authentication
gem 'pundit' # For authorization
gem 'kaminari' # For pagination

# Run bundle install after adding gems

# Run rails new command
# rails new PeruMakers -d postgresql

# Generate User model with Devise
# rails generate devise User
# rails db:migrate

# Generate MakerProject model
rails generate scaffold MakerProject title:string description:text user:references

# Set up associations in models

# app/models/user.rb
class User < ApplicationRecord
  # Devise modules to use for user authentication
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
  
  has_many :maker_projects, dependent: :destroy
end

# app/models/maker_project.rb
class MakerProject < ApplicationRecord
  belongs_to :user
  
  # Validations to ensure data integrity
  validates :title, presence: true
  validates :description, presence: true, length: { minimum: 10 }
end

# Set up the database configuration (config/database.yml)
# Ensure you have the following configuration set for PostgreSQL
development:
  <<: *default
  database: peru_makers_development

test:
  <<: *default
  database: peru_makers_test

production:
  <<: *default
  database: peru_makers_production
  username: <%= ENV['PERU_MAKERS_DATABASE_USER'] %>
  password: <%= ENV['PERU_MAKERS_DATABASE_PASSWORD'] %>

# Migrate the database
rails db:create
rails db:migrate

# Configure routes (config/routes.rb)
Rails.application.routes.draw do
  devise_for :users
  resources :maker_projects
  
  root "maker_projects#index"
end

# Create a controller for MakerProjects (app/controllers/maker_projects_controller.rb)
class MakerProjectsController < ApplicationController
  before_action :authenticate_user!, only: [:new, :create, :edit, :update, :destroy]
  before_action :set_maker_project, only: [:show, :edit, :update, :destroy]

  # GET /maker_projects
  def index
    @maker_projects = MakerProject.all
  end

  # GET /maker_projects/:id
  def show
  end

  # GET /maker_projects/new
  def new
    @maker_project = MakerProject.new
  end

  # POST /maker_projects
  def create
    @maker_project = current_user.maker_projects.build(maker_project_params)

    if @maker_project.save
      redirect_to @maker_project, notice: 'Maker project was successfully created.'
    else
      render :new
    end
  end

  # GET /maker_projects/:id/edit
  def edit
  end

  # PATCH/PUT /maker_projects/:id
  def update
    if @maker_project.update(maker_project_params)
      redirect_to @maker_project, notice: 'Maker project was successfully updated.'
    else
      render :edit
    end
  end

  # DELETE /maker_projects/:id
  def destroy
    @maker_project.destroy
    redirect_to maker_projects_url, notice: 'Maker project was successfully destroyed.'
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_maker_project
    @maker_project = MakerProject.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to maker_projects_url, alert: 'Maker project not found.'
  end

  # Only allow a list of trusted parameters through.
  def maker_project_params
    params.require(:maker_project).permit(:title, :description)
  end
end

# Create views for MakerProjects (app/views/maker_projects)
# Create index, show, new, edit views with appropriate forms and links

# Don't forget to run the server
# rails server

# Now you can visit localhost:3000 and manage community maker projects.
```
