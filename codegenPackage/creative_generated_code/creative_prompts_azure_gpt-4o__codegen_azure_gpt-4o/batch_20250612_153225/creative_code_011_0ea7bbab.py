"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Write a script in Ruby on Rails to implement a "Refund & Return Policy" system for an e-commerce store selling Travis Scott merchandise.
Generated: DETERMINISTIC_0ea7bbab0d267eeb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/refunds_controller.rb
class RefundsController < ApplicationController
  before_action :set_order, only: [:create]
  before_action :validate_refund_eligibility, only: [:create]

  # POST /refunds
  def create
    refund = Refund.new(refund_params)
    refund.order = @order

    if refund.save
      @order.update(status: 'refunded') # Update order status
      render json: { message: 'Refund processed successfully.', refund: refund }, status: :created
    else
      render json: { errors: refund.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  # Find the order associated with the refund request
  def set_order
    @order = Order.find_by(id: params[:order_id])
    unless @order
      render json: { error: 'Order not found.' }, status: :not_found
    end
  end

  # Validate refund eligibility based on business rules
  def validate_refund_eligibility
    return if @order && @order.eligible_for_refund?

    render json: { error: 'Order is not eligible for a refund.' }, status: :unprocessable_entity
  end

  # Strong parameters for the refund model
  def refund_params
    params.require(:refund).permit(:reason, :amount)
  end
end

# app/models/order.rb
class Order < ApplicationRecord
  has_many :refunds

  # Check if the order is eligible for a refund
  def eligible_for_refund?
    # Business rule: Refunds allowed within 30 days of purchase if order status is 'completed'
    completed? && (Time.zone.now <= created_at + 30.days)
  end

  # Determine if the order is completed
  def completed?
    status == 'completed'
  end
end

# app/models/refund.rb
class Refund < ApplicationRecord
  belongs_to :order

  validates :reason, presence: true
  validates :amount, presence: true, numericality: { greater_than: 0 }
end

# db/migrate/xxxxxx_create_refunds.rb
class CreateRefunds < ActiveRecord::Migration[6.1]
  def change
    create_table :refunds do |t|
      t.references :order, null: false, foreign_key: true
      t.string :reason, null: false
      t.decimal :amount, null: false, precision: 10, scale: 2
      t.timestamps
    end
  end
end

# app/controllers/returns_controller.rb
class ReturnsController < ApplicationController
  before_action :set_order, only: [:create]
  before_action :validate_return_eligibility, only: [:create]

  # POST /returns
  def create
    return_request = ReturnRequest.new(return_params)
    return_request.order = @order

    if return_request.save
      @order.update(status: 'returned') # Update order status
      render json: { message: 'Return initiated successfully.', return_request: return_request }, status: :created
    else
      render json: { errors: return_request.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  # Find the order associated with the return request
  def set_order
    @order = Order.find_by(id: params[:order_id])
    unless @order
      render json: { error: 'Order not found.' }, status: :not_found
    end
  end

  # Validate return eligibility based on business rules
  def validate_return_eligibility
    return if @order && @order.eligible_for_return?

    render json: { error: 'Order is not eligible for return.' }, status: :unprocessable_entity
  end

  # Strong parameters for the return request model
  def return_params
    params.require(:return_request).permit(:reason, :condition_note)
  end
end

# app/models/return_request.rb
class ReturnRequest < ApplicationRecord
  belongs_to :order

  validates :reason, presence: true
  validates :condition_note, presence: true
end

# db/migrate/xxxxxx_create_return_requests.rb
class CreateReturnRequests < ActiveRecord::Migration[6.1]
  def change
    create_table :return_requests do |t|
      t.references :order, null: false, foreign_key: true
      t.string :reason, null: false
      t.text :condition_note, null: false
      t.timestamps
    end
  end
end

# app/models/order.rb (additional method for return eligibility)
class Order < ApplicationRecord
  has_many :refunds
  has_many :return_requests

  # Check if the order is eligible for a return
  def eligible_for_return?
    # Business rule: Returns allowed within 15 days of delivery if order status is 'delivered'
    delivered? && (Time.zone.now <= delivered_at + 15.days)
  end

  # Determine if the order is delivered
  def delivered?
    status == 'delivered'
  end
end
```
