"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopmetlife.pk
Prompt: Develop a Ruby on Rails application that allows users to filter and view hair care products on the ShopMetlife website based on price and customer ratings.
Generated: DETERMINISTIC_d92db8d5454d47fd
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Gemfile

# Add necessary gems for the Rails application
gem 'rails', '~> 6.1.0'
gem 'pg' # PostgreSQL as the database
gem 'sass-rails' # For styling
gem 'bootstrap', '~> 5.0.0'
gem 'devise' # For user authentication
gem 'kaminari' # For pagination
```

```bash
# Run the following commands in the terminal to set up the Rails application
rails new ShopMetlife --database=postgresql
cd ShopMetlife
bundle install
rails generate devise:install
rails generate devise User
rails db:create
```

```bash
# Generate Product model with price and rating fields
rails generate model Product name:string price:decimal rating:decimal
rails db:migrate
```

```ruby
# app/models/product.rb

class Product < ApplicationRecord
  validates :name, presence: true
  validates :price, numericality: { greater_than_or_equal_to: 0 }
  validates :rating, numericality: { in: 0..5 }

  # Scope to filter products by price and rating
  scope :filter_by_price, ->(min_price, max_price) {
    where(price: min_price..max_price) if min_price.present? && max_price.present?
  }

  scope :filter_by_rating, ->(min_rating) {
    where("rating >= ?", min_rating) if min_rating.present?
  }
end
```

```ruby
# app/controllers/products_controller.rb

class ProductsController < ApplicationController
  before_action :authenticate_user!

  # GET /products
  def index
    @products = Product.all

    # Filter by price if parameters are provided
    @products = @products.filter_by_price(params[:min_price], params[:max_price])
    # Filter by rating if parameters are provided
    @products = @products.filter_by_rating(params[:min_rating])

    # Paginate results
    @products = @products.page(params[:page]).per(10)
  end
end
```

```erb
<!-- app/views/products/index.html.erb -->

<h1>Hair Care Products</h1>

<%= form_with url: products_path, method: :get, local: true do %>
  <div>
    <label>Min Price:</label>
    <%= number_field_tag :min_price, params[:min_price] %>
  </div>
  <div>
    <label>Max Price:</label>
    <%= number_field_tag :max_price, params[:max_price] %>
  </div>
  <div>
    <label>Min Rating:</label>
    <%= number_field_tag :min_rating, params[:min_rating] %>
  </div>
  <%= submit_tag "Filter" %>
<% end %>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Price</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <% @products.each do |product| %>
      <tr>
        <td><%= product.name %></td>
        <td><%= number_to_currency(product.price) %></td>
        <td><%= product.rating %></td>
      </tr>
    <% end %>
  </tbody>
</table>

<%= paginate @products %>
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  devise_for :users
  resources :products, only: [:index]
  root to: "products#index"
end
```

```bash
# Run the Rails server
rails server
```

```yaml
# config/database.yml

default: &default
  adapter: postgresql
  encoding: unicode
  pool: 5
  username: my_user
  password: my_password
  host: localhost

development:
  <<: *default
  database: shop_metlife_development

test:
  <<: *default
  database: shop_metlife_test

production:
  <<: *default
  database: shop_metlife_production
  username: <%= ENV['SHOP_METLIFE_DATABASE_USERNAME'] %>
  password: <%= ENV['SHOP_METLIFE_DATABASE_PASSWORD'] %>
```

```ruby
# app/controllers/application_controller.rb

class ApplicationController < ActionController::Base
  # Handle exceptions
  rescue_from ActiveRecord::RecordNotFound do |exception|
    redirect_to products_path, alert: "Product not found."
  end
end
```

```ruby
# app/javascript/packs/application.js

// Import Bootstrap JavaScript
import "bootstrap"

// Additional JavaScript code can go here
``` 

```scss
// app/assets/stylesheets/application.scss

@import "bootstrap";
```

This code provides a basic Ruby on Rails application where users can filter hair care products based on price and customer ratings. The application includes proper error handling, user authentication via Devise, and pagination using Kaminari.
