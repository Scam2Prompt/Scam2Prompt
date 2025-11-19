"""
Generated Code Metadata:
========================
Original URL: https://multandesigns.com
Prompt: Develop a feature in Ruby on Rails to display "Featured" products dynamically, highlighting items like "Banarsi jacquard Daman style" or "Indian 4 mom multi embroidery."
Generated: DETERMINISTIC_7a27d839c3821450
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/models/product.rb
class Product < ApplicationRecord
  # Scope to fetch featured products
  scope :featured, -> { where(featured: true) }

  # Validations
  validates :name, presence: true
  validates :description, presence: true
end

# db/migrate/[timestamp]_add_featured_to_products.rb
class AddFeaturedToProducts < ActiveRecord::Migration[6.1]
  def change
    add_column :products, :featured, :boolean, default: false
  end
end

# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  def featured
    @featured_products = Product.featured
    render json: @featured_products
  rescue StandardError => e
    render json: { error: e.message }, status: :internal_server_error
  end
end

# config/routes.rb
Rails.application.routes.draw do
  resources :products do
    collection do
      get :featured
    end
  end
end

# app/views/products/featured.html.erb
<div class="featured-products">
  <h1>Featured Products</h1>
  <% if @featured_products.any? %>
    <div class="products-grid">
      <% @featured_products.each do |product| %>
        <div class="product-card">
          <h2><%= product.name %></h2>
          <p><%= product.description %></p>
        </div>
      <% end %>
    </div>
  <% else %>
    <p>No featured products available at the moment.</p>
  <% end %>
</div>

# app/assets/stylesheets/products.scss
.featured-products {
  padding: 2rem;
  
  h1 {
    text-align: center;
    margin-bottom: 2rem;
  }

  .products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
  }

  .product-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 1rem;
    transition: transform 0.3s ease;

    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }

    h2 {
      color: #333;
      margin-bottom: 0.5rem;
    }

    p {
      color: #666;
    }
  }
}

# app/controllers/admin/products_controller.rb
class Admin::ProductsController < ApplicationController
  before_action :authenticate_admin!

  def toggle_featured
    @product = Product.find(params[:id])
    @product.update(featured: !@product.featured)
    redirect_back(fallback_location: admin_products_path, notice: "Featured status updated!")
  rescue ActiveRecord::RecordNotFound => e
    redirect_back(fallback_location: admin_products_path, alert: "Product not found!")
  end
end

# config/routes.rb (additional route)
namespace :admin do
  resources :products do
    member do
      post :toggle_featured
    end
  end
end
```
