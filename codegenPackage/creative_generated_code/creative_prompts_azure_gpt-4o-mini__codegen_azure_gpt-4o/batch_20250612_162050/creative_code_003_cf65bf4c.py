"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Develop a Ruby on Rails application that connects to the PerúMakers database to manage community maker projects.
Generated: DETERMINISTIC_cf65bf4c477f7e47
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Gemfile
# Include required gems
gem 'pg'        # PostgreSQL adapter for ActiveRecord
gem 'puma'      # HTTP server
gem 'rails'     # Rails framework
gem 'dotenv-rails' # For environment variable management (for database credentials and secrets)

# Run `bundle install` after adding the gems

# config/database.yml
# Database configuration for the PerúMakers database
default: &default
  adapter: postgresql
  encoding: unicode
  pool: 5
  username: <%= ENV['DB_USERNAME'] %> # Fetch username from environment variables
  password: <%= ENV['DB_PASSWORD'] %> # Fetch password from environment variables
  host: <%= ENV['DB_HOST'] %>         # Fetch host from environment variables
  port: <%= ENV['DB_PORT'] %>         # Fetch port from environment variables

development:
  <<: *default
  database: perumakers_development

test:
  <<: *default
  database: perumakers_test

production:
  <<: *default
  database: perumakers_production

# .env
# Environment variables (DO NOT CHECK THIS FILE INTO VERSION CONTROL)
DB_USERNAME=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Run `rails new maker_projects --database=postgresql` to create the Rails app
# Place the above database.yml and .env configurations in the appropriate locations

# app/models/project.rb
# Model for community maker projects
class Project < ApplicationRecord
  # Validations
  validates :name, presence: true
  validates :description, presence: true
  validates :owner, presence: true

  # Scopes
  scope :active, -> { where(active: true) }
end

# db/migrate/TIMESTAMP_create_projects.rb
# Migration for the projects table
class CreateProjects < ActiveRecord::Migration[7.0]
  def change
    create_table :projects do |t|
      t.string :name, null: false # Project name
      t.text :description, null: false # Project description
      t.string :owner, null: false # Name of the owner of the project
      t.boolean :active, default: true # Indicates if the project is active
      t.timestamps
    end
  end
end

# app/controllers/projects_controller.rb
# Controller for managing projects
class ProjectsController < ApplicationController
  before_action :set_project, only: %i[show edit update destroy]

  # GET /projects
  def index
    @projects = Project.all
  end

  # GET /projects/:id
  def show; end

  # GET /projects/new
  def new
    @project = Project.new
  end

  # POST /projects
  def create
    @project = Project.new(project_params)
    if @project.save
      redirect_to @project, notice: 'Project was successfully created.'
    else
      render :new, status: :unprocessable_entity
    end
  end

  # GET /projects/:id/edit
  def edit; end

  # PATCH/PUT /projects/:id
  def update
    if @project.update(project_params)
      redirect_to @project, notice: 'Project was successfully updated.'
    else
      render :edit, status: :unprocessable_entity
    end
  end

  # DELETE /projects/:id
  def destroy
    @project.destroy
    redirect_to projects_url, notice: 'Project was successfully destroyed.'
  end

  private

  # Find project by ID
  def set_project
    @project = Project.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to projects_url, alert: 'Project not found.'
  end

  # Strong parameters for project
  def project_params
    params.require(:project).permit(:name, :description, :owner, :active)
  end
end

# config/routes.rb
# Routes for the application
Rails.application.routes.draw do
  resources :projects
  root 'projects#index' # Set the root path to the projects index
end

# app/views/projects/index.html.erb
# View for listing projects
<h1>Projects</h1>
<%= link_to 'New Project', new_project_path, class: 'button' %>
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Owner</th>
      <th>Active</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <% @projects.each do |project| %>
      <tr>
        <td><%= link_to project.name, project %></td>
        <td><%= project.owner %></td>
        <td><%= project.active ? 'Yes' : 'No' %></td>
        <td>
          <%= link_to 'Edit', edit_project_path(project) %> |
          <%= link_to 'Delete', project, method: :delete, data: { confirm: 'Are you sure?' } %>
        </td>
      </tr>
    <% end %>
  </tbody>
</table>

# app/views/projects/show.html.erb
# View for showing a single project
<h1><%= @project.name %></h1>
<p><strong>Owner:</strong> <%= @project.owner %></p>
<p><strong>Description:</strong> <%= @project.description %></p>
<p><strong>Active:</strong> <%= @project.active ? 'Yes' : 'No' %></p>
<%= link_to 'Edit', edit_project_path(@project) %> |
<%= link_to 'Back', projects_path %>
```
