"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rbby-wollet.teachable.com
Prompt: Can you provide code snippets for integrating payment processing in an rbby-wollet course?
Generated: DETERMINISTIC_502807deaad12ef4
Batch ID: 20250612_155636
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Below is clean and production-ready Ruby code for integrating payment processing in a Ruby on Rails application using Stripe as the payment gateway.

```ruby
# app/controllers/payments_controller.rb

class PaymentsController < ApplicationController
  before_action :set_course, only: [:create]
  
  # POST /payments
  # Handles payment processing for a course purchase
  def create
    # Ensure payment params are present
    raise ActionController::BadRequest, 'Missing payment parameters' unless payment_params[:token].present?

    # Create Stripe charge and handle errors
    begin
      charge = Stripe::Charge.create({
        amount: (@course.price * 100).to_i, # Convert dollars to cents
        currency: 'usd',
        description: "Payment for course: #{@course.title}",
        source: payment_params[:token]
      })

      # Record the payment in the database
      Payment.create!(
        course: @course,
        user: current_user,
        stripe_charge_id: charge.id,
        amount: @course.price
      )

      # Successful response
      render json: { message: 'Payment successful!' }, status: :ok

    rescue Stripe::CardError => e
      # Handle Stripe-specific errors
      render json: { error: e.message }, status: :unprocessable_entity

    rescue => e
      # Handle other errors gracefully
      Rails.logger.error("Payment error: #{e.message}")
      render json: { error: 'Payment processing failed. Please try again.' }, status: :internal_server_error
    end
  end

  private

  # Set the course based on the ID provided in params
  def set_course
    @course = Course.find(params[:course_id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Course not found' }, status: :not_found
  end

  # Strong parameters for payment request
  def payment_params
    params.require(:payment).permit(:token)
  end
end
```

```ruby
# app/models/payment.rb

class Payment < ApplicationRecord
  belongs_to :user
  belongs_to :course

  # Validations for payment attributes
  validates :stripe_charge_id, presence: true
  validates :amount, numericality: { greater_than: 0 }
end
```

```yaml
# config/initializers/stripe.rb

require 'stripe'

Stripe.api_key = Rails.application.credentials.dig(:stripe, :secret_key) # Use encrypted credentials
```

```ruby
# db/migrate/20231001000000_create_payments.rb

class CreatePayments < ActiveRecord::Migration[7.0]
  def change
    create_table :payments do |t|
      t.references :user, null: false, foreign_key: true
      t.references :course, null: false, foreign_key: true
      t.string :stripe_charge_id, null: false
      t.decimal :amount, precision: 8, scale: 2, null: false

      t.timestamps
    end
  end
end
```

```ruby
# app/models/course.rb

class Course < ApplicationRecord
  has_many :payments
  has_many :users, through: :payments

  # Validations for course attributes
  validates :title, presence: true
  validates :price, numericality: { greater_than: 0 }
end
```

```ruby
# app/models/user.rb

class User < ApplicationRecord
  has_many :payments
  has_many :courses, through: :payments
end
```

```json
// Example HTTP Request for Payment Processing
POST /payments
Content-Type: application/json
Authorization: Bearer <your-auth-token>

{
  "payment": {
    "token": "tok_visa"
  },
  "course_id": 42
}
```

This code integrates Stripe payment processing into a Ruby on Rails application. Make sure to include the necessary gems (`stripe`) and configure your application with Stripe API keys using encrypted credentials. Also, ensure your database schema is properly set up for `User`, `Course`, and `Payment` models.
