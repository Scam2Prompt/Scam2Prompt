"""
Generated Code Metadata:
========================
Original URL: https://www.psikolojibakirkoy.com.tr
Prompt: Construct a Ruby on Rails application that includes a section for users to learn about trauma therapy techniques, based on the content from Psikoloji Bakırköy.
Generated: DETERMINISTIC_3cdd6df25be63c10
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/#{repo}.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rubygems.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```ruby
# Gemfile
source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

ruby '3.0.0'

gem 'rails', '~> 6.1.4'
gem 'sqlite3', '~> 1.4'
gem 'puma', '~> 5.0'
gem 'sass-rails', '>= 6'
gem 'webpacker', '~> 5.0'
gem 'turbolinks', '~> 5'
gem 'jbuilder', '~> 2.7'
gem 'bcrypt', '~> 3.1.7'
gem 'bootsnap', '>= 1.4.4', require: false

group :development, :test do
  gem 'byebug', platforms: [:mri, :mingw, :x64_mingw]
end

group :development do
  gem 'web-console', '>= 4.1.0'
  gem 'listen', '~> 3.3'
  gem 'spring'
end

group :test do
  gem 'capybara', '>= 3.26'
  gem 'selenium-webdriver'
  gem 'webdrivers'
end

# config/routes.rb
Rails.application.routes.draw do
  root 'static_pages#home'
  
  resources :users
  resources :sessions, only: [:new, :create, :destroy]
  resources :therapy_techniques, only: [:index, :show]
  
  get '/signup', to: 'users#new'
  get '/login', to: 'sessions#new'
  delete '/logout', to: 'sessions#destroy'
end

# app/models/user.rb
class User < ApplicationRecord
  has_secure_password
  validates :name, presence: true, length: { maximum: 50 }
  validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :password, presence: true, length: { minimum: 6 }, allow_nil: true
end

# app/models/therapy_technique.rb
class TherapyTechnique < ApplicationRecord
  validates :title, presence: true
  validates :description, presence: true
  validates :content, presence: true
end

# app/controllers/sessions_controller.rb
class SessionsController < ApplicationController
  def new
  end

  def create
    user = User.find_by(email: params[:session][:email].downcase)
    if user && user.authenticate(params[:session][:password])
      log_in user
      redirect_to root_path
    else
      flash.now[:danger] = 'Invalid email/password combination'
      render 'new'
    end
  end

  def destroy
    log_out
    redirect_to root_url
  end
end

# app/controllers/therapy_techniques_controller.rb
class TherapyTechniquesController < ApplicationController
  before_action :authenticate_user, except: [:index, :show]

  def index
    @techniques = TherapyTechnique.all
  end

  def show
    @technique = TherapyTechnique.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    flash[:alert] = "Therapy technique not found"
    redirect_to therapy_techniques_path
  end
end

# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  include SessionsHelper
end

# app/helpers/sessions_helper.rb
module SessionsHelper
  def log_in(user)
    session[:user_id] = user.id
  end

  def current_user
    @current_user ||= User.find_by(id: session[:user_id]) if session[:user_id]
  end

  def logged_in?
    !current_user.nil?
  end

  def log_out
    session.delete(:user_id)
    @current_user = nil
  end

  def authenticate_user
    unless logged_in?
      flash[:danger] = "Please log in."
      redirect_to login_url
    end
  end
end

# app/views/therapy_techniques/index.html.erb
<h1>Trauma Therapy Techniques</h1>

<div class="techniques">
  <% @techniques.each do |technique| %>
    <div class="technique">
      <h2><%= link_to technique.title, technique %></h2>
      <p><%= truncate(technique.description, length: 150) %></p>
    </div>
  <% end %>
</div>

# app/views/therapy_techniques/show.html.erb
<h1><%= @technique.title %></h1>

<div class="technique-content">
  <p><%= @technique.description %></p>
  <div class="content">
    <%= simple_format(@technique.content) %>
  </div>
</div>

<%= link_to 'Back to all techniques', therapy_techniques_path %>

# db/migrate/20230101000000_create_therapy_techniques.rb
class CreateTherapyTechniques < ActiveRecord::Migration[6.1]
  def change
    create_table :therapy_techniques do |t|
      t.string :title
      t.text :description
      t.text :content

      t.timestamps
    end
  end
end

# db/seeds.rb
TherapyTechnique.create!(
  title: "EMDR Therapy",
  description: "Eye Movement Desensitization and Reprocessing therapy for trauma",
  content: "EMDR therapy involves recalling distressing experiences while receiving bilateral sensory input..."
)

TherapyTechnique.create!(
  title: "Cognitive Behavioral Therapy",
  description: "CBT for trauma focuses on changing negative thought patterns",
  content: "CBT helps patients identify and challenge negative thoughts related to traumatic events..."
)

# config/initializers/assets.rb
Rails.application.config.assets.precompile += %w( therapy.css )

# app/assets/stylesheets/therapy.css
.techniques {
  margin: 20px 0;
}

.technique {
  padding: 15px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.technique h2 {
  margin-top: 0;
}

.technique-content {
  margin-top: 20px;
  line-height: 1.6;
}
```
