"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Develop a Ruby on Rails application that allows users to order custom ojotas with their logo, based on the customization options provided by Surff Ojotas.
Generated: DETERMINISTIC_af54c068ef680a46
Batch ID: 20250612_160804
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

# Rails application dependencies
gem 'rails', '~> 6.1'
gem 'sqlite3'
gem 'puma'
gem 'sass-rails', '>= 6'
gem 'webpacker', '~> 5.0'
gem 'turbolinks', '~> 5'
gem 'jbuilder', '~> 2.7'
gem 'devise' # For user authentication
gem 'figaro' # For environment variables management

# Run bundle install to install dependencies

# Run `rails new ojotas_app --database=sqlite3` to create the app

# Generate the User model with Devise
# rails generate devise User
# rails db:migrate

# Generate the Order model
rails generate model Order user:references logo:string size:string color:string custom_text:string
rails db:migrate

# app/models/user.rb
class User < ApplicationRecord
  # Devise modules for authentication
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  has_many :orders, dependent: :destroy
end

# app/models/order.rb
class Order < ApplicationRecord
  belongs_to :user

  validates :logo, presence: true
  validates :size, presence: true
  validates :color, presence: true
  validates :custom_text, length: { maximum: 100 }, allow_blank: true
end

# app/controllers/orders_controller.rb
class OrdersController < ApplicationController
  before_action :authenticate_user!

  # GET /orders/new
  def new
    @order = Order.new
  end

  # POST /orders
  def create
    @order = current_user.orders.build(order_params)

    if @order.save
      redirect_to @order, notice: 'Order was successfully created.'
    else
      render :new
    end
  end

  # GET /orders/:id
  def show
    @order = Order.find(params[:id])
  end

  private

  # Strong parameters for order creation
  def order_params
    params.require(:order).permit(:logo, :size, :color, :custom_text)
  rescue ActionController::ParameterMissing
    {}
  end
end

# app/views/orders/new.html.erb
<%= form_with(model: @order, local: true) do |form| %>
  <% if @order.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(@order.errors.count, "error") %> prohibited this order from being saved:</h2>
      <ul>
        <% @order.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= form.label :logo %>
    <%= form.text_field :logo %>
  </div>

  <div class="field">
    <%= form.label :size %>
    <%= form.select :size, ['S', 'M', 'L', 'XL'] %>
  </div>

  <div class="field">
    <%= form.label :color %>
    <%= form.text_field :color %>
  </div>

  <div class="field">
    <%= form.label :custom_text %>
    <%= form.text_field :custom_text %>
  </div>

  <div class="actions">
    <%= form.submit %>
  </div>
<% end %>

# config/routes.rb
Rails.application.routes.draw do
  devise_for :users
  resources :orders, only: [:new, :create, :show]
  root 'orders#new' # Set the root path to the new order page
end

# To run the application, use the following commands:
# rails server
# Visit http://localhost:3000 in your web browser
```
This code provides a basic Ruby on Rails application for ordering custom ojotas, including user authentication and order management. Make sure to run the necessary migrations and install required gems before running the application.
