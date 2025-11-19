"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Develop a Ruby on Rails controller action that processes product returns for Baazaars, implementing the 30-day return policy mentioned on the site.
Generated: DETERMINISTIC_454eb15a89b391e0
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/returns_controller.rb
class ReturnsController < ApplicationController
  before_action :find_order, only: [:create]
  
  # POST /returns
  def create
    # Check if the order exists and is eligible for return
    if @order.nil?
      render json: { error: 'Order not found' }, status: :not_found
      return
    end
    
    if return_eligible?
      begin
        # Process the return
        ActiveRecord::Base.transaction do
          create_return_record
          refund_order
        end
        render json: { message: 'Return processed successfully' }, status: :ok
      rescue => e
        # Handle any errors during transaction
        render json: { error: 'Failed to process return', details: e.message }, status: :unprocessable_entity
      end
    else
      render json: { error: 'Order not eligible for return' }, status: :unprocessable_entity
    end
  end
  
  private
  
  # Find the order by ID
  def find_order
    @order = Order.find_by(id: params[:order_id])
  end
  
  # Check if the order is eligible for return based on the 30-day policy
  def return_eligible?
    return false unless @order.completed_at.present?
    @order.completed_at >= 30.days.ago
  end
  
  # Create a record for the return
  def create_return_record
    Return.create!(
      order_id: @order.id,
      user_id: @order.user_id,
      returned_at: Time.current
    )
  end
  
  # Process the refund for the order
  def refund_order
    @order.update!(status: 'refunded')
    # TODO: Integrate payment gateway refund logic here
  end
end
```

Make sure to replace `Order` and `Return` with your application-specific models and ensure proper fields exist in the database schema.
