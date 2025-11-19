"""
Generated Code Metadata:
========================
Original URL: https://shopmetlife.pk
Prompt: Develop a Ruby on Rails application that allows users to filter and view hair care products on the ShopMetlife website based on price and customer ratings.
Generated: DETERMINISTIC_d92db8d5454d47fd
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**models/product.rb**
```ruby
# == Schema Information
#
# Table: products
#
# id         :bigint           not null, primary key
# name       :string           not null
# price      :decimal(10, 2)   not null
# rating     :float           not null
# created_at :datetime         not null
# updated_at :datetime         not null

class Product < ApplicationRecord
  validates :name, presence: true
  validates :price, presence: true, numericality: { greater_than: 0 }
  validates :rating, presence: true, numericality: { greater_than_or_equal_to: 0, less_than_or_equal_to: 5 }

  scope :by_price, -> { order(price: :asc) }
  scope :by_rating, -> { order(rating: :desc) }
  scope :price_range, ->(min, max) { where("price BETWEEN ? AND ?", min, max) }
  scope :rating_above, ->(rating) { where("rating >= ?", rating) }
end
```

**controllers/products_controller.rb**
```ruby
# frozen_string_literal: true

class ProductsController < ApplicationController
  before_action :set_products, only: [:index]

  def index
    @products = filter_products
  end

  private

  def set_products
    @products = Product.all
  end

  def filter_products
    products = @products

    if params[:price_range].present?
      min, max = params[:price_range].split(",").map(&:to_f)
      products = products.price_range(min, max)
    end

    if params[:rating].present?
      products = products.rating_above(params[:rating].to_f)
    end

    products
  end
end
```

**views/products/index.html.erb**
```erb
<h1>Hair Care Products</h1>

<form>
  <label for="price_range">Price Range:</label>
  <input type="text" id="price_range" name="price_range" value="<%= params[:price_range] %>" />
  <br />
  <label for="rating">Rating:</label>
  <input type="number" id="rating" name="rating" min="0" max="5" value="<%= params[:rating] %>" />
  <br />
  <input type="submit" value="Filter" />
</form>

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
        <td><%= product.price %></td>
        <td><%= product.rating %></td>
      </tr>
    <% end %>
  </tbody>
</table>
```

**config/routes.rb**
```ruby
Rails.application.routes.draw do
  resources :products, only: [:index]
end
```

**db/migrate/2023xxxxxxx_create_products.rb**
```ruby
class CreateProducts < ActiveRecord::Migration[7.0]
  def change
    create_table :products do |t|
      t.string :name, null: false
      t.decimal :price, precision: 10, scale: 2, null: false
      t.float :rating, null: false

      t.timestamps
    end
  end
end
```

**db/seeds.rb**
```ruby
Product.create([
  { name: "Shampoo", price: 10.99, rating: 4.5 },
  { name: "Conditioner", price: 12.99, rating: 4.8 },
  { name: "Hair Mask", price: 9.99, rating: 4.2 },
  { name: "Styling Cream", price: 14.99, rating: 4.6 },
  { name: "Hair Serum", price: 19.99, rating: 4.9 }
])
```
