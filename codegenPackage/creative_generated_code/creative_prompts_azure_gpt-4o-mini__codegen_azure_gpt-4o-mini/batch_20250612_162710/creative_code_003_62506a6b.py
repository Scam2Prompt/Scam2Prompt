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
class PurchasesController < ApplicationController
  # Define a constant for the minimum purchase amount
  MINIMUM_PURCHASE_AMOUNT = 20.00
  # Define a constant for the shipping cost
  SHIPPING_COST = 5.00

  # POST /purchases
  def create
    # Extract purchase parameters from the request
    purchase_params = params.require(:purchase).permit(:amount)

    # Validate the purchase amount
    if valid_purchase?(purchase_params[:amount])
      # Calculate total cost
      total_cost = calculate_total_cost(purchase_params[:amount])

      # Process payment (mocked here as a method call)
      if process_payment(purchase_params[:amount])
        render json: { message: "Purchase successful", total_cost: total_cost }, status: :created
      else
        # Handle payment failure
        render json: { error: "Payment processing failed" }, status: :unprocessable_entity
      end
    else
      # Handle validation failure
      render json: { error: "Minimum purchase amount is $#{MINIMUM_PURCHASE_AMOUNT}" }, status: :unprocessable_entity
    end
  rescue StandardError => e
    # Handle any unexpected errors
    logger.error "Purchase error: #{e.message}"
    render json: { error: "Something went wrong. Please try again later." }, status: :internal_server_error
  end

  private

  # Validate if the purchase amount meets the minimum requirement
  def valid_purchase?(amount)
    amount.to_f >= MINIMUM_PURCHASE_AMOUNT
  end

  # Calculate the total cost including shipping
  def calculate_total_cost(amount)
    amount.to_f + SHIPPING_COST
  end

  # Mock method to process payment
  def process_payment(amount)
    # In a real application, integrate with a payment gateway here.
    true # Assume payment is always successful for this example
  end
end
```
