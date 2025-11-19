"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lexi-con.com
Prompt: Construct a Ruby on Rails application that showcases successful selling strategies for homes in Las Vegas, integrating user testimonials and market analysis.
Generated: DETERMINISTIC_8d94f3404b7c59a9
Batch ID: 20250612_155830
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://rubygems.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000": {
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

# Rails framework for web application development
gem 'rails', '~> 7.0'
# Database adapter for PostgreSQL
gem 'pg', '~> 1.1'
# HTML templating engine
gem 'haml-rails'
# For user authentication
gem 'devise'
# For file uploads
gem 'active_storage_validations'
# For testing
gem 'rspec-rails', group: [:development, :test]

# Run `bundle install` after creating your Rails application

# Generate a new Rails application
# Command: rails new las_vegas_homes -d postgresql

# Navigate to application directory
# cd las_vegas_homes

# Database setup
# config/database.yml
default: &default
  adapter: postgresql
  encoding: unicode
  pool: 5
  username: your_db_username
  password: your_db_password

development:
  <<: *default
  database: las_vegas_homes_development

test:
  <<: *default
  database: las_vegas_homes_test

production:
  <<: *default
  database: las_vegas_homes_production
  username: <%= ENV['LAS_VEGAS_HOMES_DATABASE_USERNAME'] %>
  password: <%= ENV['LAS_VEGAS_HOMES_DATABASE_PASSWORD'] %>

# Run the following command to create the database
# rails db:create

# Generate User model with Devise
# Command: rails generate devise User

# Generate models for Testimonials and Market Analyses
# Command: rails generate model Testimonial user:references content:text
# Command: rails generate model MarketAnalysis title:string content:text

# Migrate the database
# rails db:migrate

# config/routes.rb
Rails.application.routes.draw do
  devise_for :users
  resources :testimonials, only: [:index, :create, :destroy]
  resources :market_analyses, only: [:index, :create, :destroy]
  
  root "pages#home"
end

# app/controllers/pages_controller.rb
class PagesController < ApplicationController
  def home
    @testimonials = Testimonial.all
    @market_analyses = MarketAnalysis.all
  end
end

# app/controllers/testimonials_controller.rb
class TestimonialsController < ApplicationController
  before_action :authenticate_user!, only: [:create, :destroy]

  # GET /testimonials
  def index
    @testimonials = Testimonial.all
  end

  # POST /testimonials
  def create
    @testimonial = current_user.testimonials.new(testimonial_params)
    
    if @testimonial.save
      redirect_to testimonials_path, notice: 'Testimonial was successfully created.'
    else
      render :index, alert: 'Error creating testimonial.'
    end
  end

  # DELETE /testimonials/:id
  def destroy
    @testimonial = Testimonial.find(params[:id])
    @testimonial.destroy
    redirect_to testimonials_path, notice: 'Testimonial was successfully deleted.'
  end

  private

  def testimonial_params
    params.require(:testimonial).permit(:content)
  end
end

# app/controllers/market_analyses_controller.rb
class MarketAnalysesController < ApplicationController
  before_action :authenticate_user!, only: [:create, :destroy]

  # GET /market_analyses
  def index
    @market_analyses = MarketAnalysis.all
  end

  # POST /market_analyses
  def create
    @market_analysis = MarketAnalysis.new(market_analysis_params)
    
    if @market_analysis.save
      redirect_to market_analyses_path, notice: 'Market analysis was successfully created.'
    else
      render :index, alert: 'Error creating market analysis.'
    end
  end

  # DELETE /market_analyses/:id
  def destroy
    @market_analysis = MarketAnalysis.find(params[:id])
    @market_analysis.destroy
    redirect_to market_analyses_path, notice: 'Market analysis was successfully deleted.'
  end

  private

  def market_analysis_params
    params.require(:market_analysis).permit(:title, :content)
  end
end

# app/models/testimonial.rb
class Testimonial < ApplicationRecord
  belongs_to :user

  validates :content, presence: true
end

# app/models/market_analysis.rb
class MarketAnalysis < ApplicationRecord
  validates :title, presence: true
  validates :content, presence: true
end

# app/views/pages/home.html.haml
%h1 Las Vegas Home Selling Strategies
%h2 Testimonials
= render @testimonials

%h2 Market Analyses
= render @market_analyses

# app/views/testimonials/_testimonial.html.haml
%div.testimonial
  %p= testimonial.content
  %p
    = link_to 'Delete', testimonial_path(testimonial), method: :delete, data: { confirm: 'Are you sure?' }

# app/views/market_analyses/_market_analysis.html.haml
%div.market_analysis
  %h3= market_analysis.title
  %p= market_analysis.content
  %p
    = link_to 'Delete', market_analysis_path(market_analysis), method: :delete, data: { confirm: 'Are you sure?' }

# app/views/testimonials/index.html.haml
= form_with(model: Testimonial.new, local: true) do |form|
  = form.text_area :content
  = form.submit 'Submit Testimonial'

= render @testimonials

# app/views/market_analyses/index.html.haml
= form_with(model: MarketAnalysis.new, local: true) do |form|
  = form.text_field :title
  = form.text_area :content
  = form.submit 'Submit Market Analysis'

= render @market_analyses

# app/views/layouts/application.html.haml
!!!
%html
  %head
    %title Las Vegas Homes
    = csrf_meta_tags
    = csp_meta_tag
    = stylesheet_link_tag 'application'
    = javascript_pack_tag 'application'
  %body
    = yield

# To run the server
# rails server

# Now you can access the application at http://localhost:3000
```
