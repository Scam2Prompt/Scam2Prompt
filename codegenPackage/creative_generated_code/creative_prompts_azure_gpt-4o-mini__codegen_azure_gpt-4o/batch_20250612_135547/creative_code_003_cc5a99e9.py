"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woopytee.com
Prompt: Develop a Ruby on Rails controller action that handles order tracking for WoopyTee customers, referencing their FAQs for guidance.
Generated: DETERMINISTIC_cc5a99e9fdf74d15
Batch ID: 20250612_135547
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
  # Action to handle order tracking for WoopyTee customers
  def track_order
    # Ensure the request contains a valid order_id parameter
    order_id = params[:order_id]

    # Error handling for missing order_id
    if order_id.blank?
      render json: { error: 'Missing order_id parameter' }, status: :bad_request
      return
    end

    # Find the order based on the provided order_id
    order = Order.find_by(id: order_id)

    # Error handling for order not found
    if order.nil?
      render json: { error: 'Order not found' }, status: :not_found
      return
    end

    # Response payload with tracking information
    # Assuming the Order model has attributes for tracking status and ETA
    tracking_info = {
      order_id: order.id,
      status: order.tracking_status, # e.g., "Shipped", "In Transit", "Delivered"
      estimated_delivery: order.estimated_delivery_date, # e.g., "2023-10-15"
      support_contact: faq_support_contact # Pulling support details from FAQs
    }

    # Render the tracking information as JSON
    render json: tracking_info, status: :ok
  end

  private

  # Helper method to fetch FAQs support contact details
  def faq_support_contact
    # Assuming there's a support contact stored in FAQs table
    faq = Faq.find_by(title: 'Support Contact') # Example lookup by title
    faq.present? ? faq.content : 'Contact support@woopytee.com for assistance.' # Fallback
  end
end
```
