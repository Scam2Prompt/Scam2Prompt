"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naimatabbasind.com
Prompt: Develop a Ruby on Rails controller action that processes user input for ordering sports gloves from Naimat Abbas Industries, ensuring compliance with their quality standards.
Generated: DETERMINISTIC_57610842dd74cd56
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/orders_controller.rb
class OrdersController < ApplicationController
  # POST /orders
  # This action processes user input for ordering sports gloves
  def create
    # Strong parameters for order creation
    order_params = params.require(:order).permit(:user_id, :glove_type, :quantity, :size, :address)

    # Validate user input against quality standards
    if valid_order?(order_params)
      @order = Order.new(order_params)

      if @order.save
        render json: { message: 'Order successfully created', order: @order }, status: :created
      else
        render json: { error: @order.errors.full_messages }, status: :unprocessable_entity
      end
    else
      render json: { error: 'Invalid order input. Please check the glove type, quantity, and size.' }, status: :unprocessable_entity
    end
  end

  private

  # Validate the order input against quality standards
  def valid_order?(order_params)
    # Example validation rules
    valid_glove_types = ['leather', 'synthetic', 'mesh'] # Allowed glove types
    valid_sizes = ['small', 'medium', 'large'] # Allowed sizes
    quantity_valid = order_params[:quantity].to_i > 0 # Quantity must be greater than 0

    valid_glove_types.include?(order_params[:glove_type]) && 
      valid_sizes.include?(order_params[:size]) && 
      quantity_valid
  end
end
```

```ruby
# app/models/order.rb
class Order < ApplicationRecord
  # Associations
  belongs_to :user

  # Validations
  validates :glove_type, presence: true
  validates :quantity, numericality: { greater_than: 0 }
  validates :size, presence: true
  validates :address, presence: true
end
```

```ruby
# config/routes.rb
Rails.application.routes.draw do
  resources :orders, only: [:create]
end
```

```ruby
# db/migrate/xxxxxx_create_orders.rb
class CreateOrders < ActiveRecord::Migration[6.1]
  def change
    create_table :orders do |t|
      t.references :user, null: false, foreign_key: true
      t.string :glove_type, null: false
      t.integer :quantity, null: false
      t.string :size, null: false
      t.string :address, null: false

      t.timestamps
    end
  end
end
```
