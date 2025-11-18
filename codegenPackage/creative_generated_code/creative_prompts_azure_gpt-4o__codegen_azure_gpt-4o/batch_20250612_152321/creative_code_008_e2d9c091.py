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
# app/controllers/checkout_controller.rb

class CheckoutController < ApplicationController
  before_action :ensure_minimum_purchase, only: :create

  def create
    # Code for handling the checkout process (e.g., creating an order)
    # Assuming `cart_items` is available through current user's session or similar
    @order = Order.new(order_params)

    if @order.save
      # Redirect to order confirmation or success page
      redirect_to order_confirmation_path(@order), notice: 'Order successfully placed!'
    else
      # Render the checkout page with errors
      render :new, status: :unprocessable_entity
    end
  end

  private

  # Ensure minimum purchase restriction for home delivery
  def ensure_minimum_purchase
    # Assuming `cart_items` is a method that retrieves all items in the user's cart
    if cart_items.count < 4
      flash[:alert] = 'You must purchase at least 4 products for home delivery.'
      redirect_to cart_path # Redirect back to the cart page
    end
  end

  # Strong parameters for order creation
  def order_params
    params.require(:order).permit(:user_id, :address, :payment_method, :delivery_type, :total_price)
  end

  # Assuming cart_items is a helper that fetches all items in the user's cart
  def cart_items
    current_user.cart.items
  end
end
```

```ruby
# app/models/user.rb

class User < ApplicationRecord
  has_one :cart
  
  # Additional user-related methods
end
```

```ruby
# app/models/cart.rb

class Cart < ApplicationRecord
  belongs_to :user
  has_many :items, class_name: 'CartItem'

  # Additional cart-related methods
end
```

```ruby
# app/models/cart_item.rb

class CartItem < ApplicationRecord
  belongs_to :cart

  # Additional cart item-related methods
end
```
