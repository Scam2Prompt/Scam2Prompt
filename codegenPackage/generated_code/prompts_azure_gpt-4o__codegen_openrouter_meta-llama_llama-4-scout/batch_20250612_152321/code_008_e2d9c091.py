"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Generate code in Ruby on Rails to implement a minimum purchase restriction (e.g., 4 products for home delivery) in the checkout process of an e-commerce platform.
Generated: DETERMINISTIC_e2d9c091b979ba5b
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Minimum Purchase Restriction Implementation in Ruby on Rails**

### Models

```ruby
# app/models/order.rb
class Order < ApplicationRecord
  has_many :order_items

  validates :user_id, presence: true

  def total_items
    order_items.sum(:quantity)
  end

  def minimum_purchase_restriction_met?
    # Assuming the minimum purchase restriction is 4 products for home delivery
    # and that home delivery is the default delivery method
    # You can adjust this logic according to your requirements
    total_items >= 4 || delivery_method != 'home_delivery'
  end
end

# app/models/order_item.rb
class OrderItem < ApplicationRecord
  belongs_to :order
  belongs_to :product

  validates :order_id, :product_id, :quantity, presence: true
end
```

### Controllers

```ruby
# app/controllers/orders_controller.rb
class OrdersController < ApplicationController
  before_action :authenticate_user!

  def create
    @order = current_user.orders.new(order_params)

    if @order.save
      # Process payment and complete order
      if @order.minimum_purchase_restriction_met?
        # Complete order processing
        redirect_to @order, notice: 'Order created successfully'
      else
        # Handle minimum purchase restriction error
        @order.destroy
        redirect_to cart_path, alert: 'Minimum purchase restriction not met. Please add more items to your cart.'
      end
    else
      render :new
    end
  rescue StandardError => e
    # Handle any unexpected errors
    logger.error e.message
    redirect_to cart_path, alert: 'An error occurred while processing your order.'
  end

  private

  def order_params
    params.require(:order).permit(:delivery_method)
  end
end
```

### Services

```ruby
# app/services/order_service.rb
class OrderService
  def self.create_order(user, order_params)
    order = user.orders.new(order_params)

    if order.save
      if order.minimum_purchase_restriction_met?
        # Complete order processing
        return order
      else
        order.destroy
        raise 'Minimum purchase restriction not met'
      end
    else
      raise 'Failed to create order'
    end
  rescue StandardError => e
    # Handle any unexpected errors
    logger.error e.message
    raise
  end
end
```

### Validators

```ruby
# app/validators/minimum_purchase_validator.rb
class MinimumPurchaseValidator < ActiveModel::Validator
  def validate(record)
    if record.delivery_method == 'home_delivery' && record.total_items < 4
      record.errors[:base] << 'Minimum purchase restriction not met'
    end
  end
end
```

### Usage

```ruby
# In your order creation logic
# Use OrderService to create an order
# order = OrderService.create_order(current_user, order_params)

# Or use OrdersController#create action
```

### Migration

```ruby
# db/migrate/xxxxxxxxxxxxxx_add_delivery_method_to_orders.rb
class AddDeliveryMethodToOrders < ActiveRecord::Migration[7.0]
  def change
    add_column :orders, :delivery_method, :string, default: 'home_delivery'
  end
end
```
