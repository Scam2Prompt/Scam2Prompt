"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://barbudogrowler.cl
Prompt: Generate code in Ruby on Rails to implement a minimum purchase restriction (e.g., 4 products for home delivery) in the checkout process of an e-commerce platform.
Generated: DETERMINISTIC_e2d9c091b979ba5b
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/order.rb
class Order < ApplicationRecord
  # Validations for the order model
  validates :products, presence: true
  validate :minimum_purchase_restriction

  # This method checks if the order meets the minimum purchase requirement
  def minimum_purchase_restriction
    if products.size < 4
      errors.add(:base, 'A minimum of 4 products is required for home delivery.')
    end
  end
end

# app/controllers/orders_controller.rb
class OrdersController < ApplicationController
  # POST /orders
  def create
    @order = Order.new(order_params)

    if @order.save
      # Handle successful order creation (e.g., redirect to confirmation page)
      redirect_to @order, notice: 'Order was successfully created.'
    else
      # Handle validation errors and render the new order form again
      flash.now[:alert] = @order.errors.full_messages.to_sentence
      render :new
    end
  rescue StandardError => e
    # Log the error and show a user-friendly message
    Rails.logger.error("Order creation failed: #{e.message}")
    redirect_to new_order_path, alert: 'Something went wrong. Please try again.'
  end

  private

  # Strong parameters to prevent mass assignment vulnerabilities
  def order_params
    params.require(:order).permit(:delivery_address, products: [])
  end
end

# app/views/orders/new.html.erb
<%= form_with model: @order, local: true do |form| %>
  <div>
    <%= form.label :delivery_address %>
    <%= form.text_area :delivery_address %>
  </div>

  <div>
    <%= form.label :products %>
    <%= form.collection_select :products, Product.all, :id, :name, {}, { multiple: true } %>
  </div>

  <div>
    <%= form.submit 'Create Order' %>
  </div>

  <% if flash[:alert] %>
    <div class="alert alert-danger"><%= flash[:alert] %></div>
  <% end %>
<% end %>

# config/routes.rb
Rails.application.routes.draw do
  resources :orders, only: [:new, :create]
end
```
