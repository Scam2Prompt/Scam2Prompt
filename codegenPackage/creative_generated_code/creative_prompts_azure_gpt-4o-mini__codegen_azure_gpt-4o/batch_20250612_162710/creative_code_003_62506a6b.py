"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lattechocolate.com.ar
Prompt: Develop a Ruby on Rails controller action that processes a purchase from the Latte Chocolate online store, ensuring it validates the minimum purchase amount and calculates shipping costs.
Generated: DETERMINISTIC_62506a6b025b9496
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/purchases_controller.rb
class PurchasesController < ApplicationController
  # POST /purchases
  # Handles the purchase process for the Latte Chocolate online store.
  def create
    # Assuming params include :amount (purchase amount in cents) and :shipping_address
    purchase_amount = params[:amount].to_i
    shipping_address = params[:shipping_address]

    # Minimum purchase amount in cents
    MINIMUM_PURCHASE_AMOUNT = 500 # $5.00
    
    # Validate purchase amount
    if purchase_amount < MINIMUM_PURCHASE_AMOUNT
      render json: { error: "Minimum purchase amount is $5.00." }, status: :unprocessable_entity
      return
    end

    # Calculate shipping costs based on address
    shipping_cost = calculate_shipping_cost(shipping_address)

    # Total cost of the purchase
    total_cost = purchase_amount + shipping_cost

    # Simulate purchase processing (e.g., saving to database or calling payment gateway)
    begin
      @purchase = Purchase.create!(
        amount: purchase_amount,
        shipping_cost: shipping_cost,
        total_cost: total_cost,
        shipping_address: shipping_address
      )
      render json: { message: "Purchase successful!", purchase: @purchase }, status: :created
    rescue ActiveRecord::RecordInvalid => e
      render json: { error: e.message }, status: :unprocessable_entity
    rescue StandardError => e
      render json: { error: "An error occurred while processing your purchase." }, status: :internal_server_error
    end
  end

  private

  # Calculates shipping cost based on the provided shipping address.
  # This is a placeholder; in production, integrate with a real shipping API.
  def calculate_shipping_cost(shipping_address)
    if shipping_address.blank?
      raise ArgumentError, "Shipping address is required."
    end

    # Flat-rate shipping cost for simplicity
    200 # $2.00
  end
end
```
