"""
Generated Code Metadata:
========================
Original URL: https://www.lattechocolate.com.ar
Prompt: Develop a Ruby on Rails controller action that processes a purchase from the Latte Chocolate online store, ensuring it validates the minimum purchase amount and calculates shipping costs.
Generated: DETERMINISTIC_62506a6b025b9496
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/controllers/orders_controller.rb

class OrdersController < ApplicationController
  before_action :authenticate_user!

  # POST /orders
  def create
    # Initialize order and order items
    @order = Order.new(order_params)
    @order.user = current_user

    # Validate minimum purchase amount
    if @order.total < 10.0
      render json: { error: 'Minimum purchase amount is $10.00' }, status: :unprocessable_entity
      return
    end

    # Calculate shipping costs
    @order.shipping_cost = calculate_shipping_cost(@order.total)

    # Save order and order items
    if @order.save
      render json: @order, status: :created
    else
      render json: { errors: @order.errors }, status: :unprocessable_entity
    end
  end

  private

  # Calculate shipping cost based on total purchase amount
  def calculate_shipping_cost(total)
    # For demonstration purposes, assume flat rate shipping
    # of $5.00 for orders under $50.00 and free shipping for orders over $50.00
    if total < 50.0
      5.0
    else
      0.0
    end
  end

  # Strong parameters for order
  def order_params
    params.require(:order).permit(:address, :city, :state, :zip, order_items_attributes: [:product_id, :quantity])
  end
end
```

```ruby
# app/models/order.rb

class Order < ApplicationRecord
  belongs_to :user
  has_many :order_items

  # Validate presence of required attributes
  validates :address, :city, :state, :zip, presence: true

  # Calculate total cost of order
  def total
    order_items.sum { |item| item.product.price * item.quantity }
  end

  # Accept nested attributes for order items
  accepts_nested_attributes_for :order_items
end
```

```ruby
# app/models/order_item.rb

class OrderItem < ApplicationRecord
  belongs_to :order
  belongs_to :product

  # Validate presence of required attributes
  validates :product_id, :quantity, presence: true
  validates :quantity, numericality: { greater_than: 0 }
end
```

```ruby
# app/models/product.rb

class Product < ApplicationRecord
  has_many :order_items

  # Validate presence of required attributes
  validates :name, :price, presence: true
  validates :price, numericality: { greater_than_or_equal_to: 0.0 }
end
```

```ruby
# config/routes.rb (snippet)

Rails.application.routes.draw do
  resources :orders, only: [:create]
  # Other routes...
end
```
