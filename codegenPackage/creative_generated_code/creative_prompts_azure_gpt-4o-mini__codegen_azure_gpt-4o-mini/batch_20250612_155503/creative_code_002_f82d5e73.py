"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thresholdsummer.org
Prompt: Create a Ruby on Rails API endpoint to manage room bookings for the Threshold Summer Meeting, including email notifications to the hotel and the event organizer.
Generated: DETERMINISTIC_f82d5e7356229aa8
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/api/v1/bookings_controller.rb
class Api::V1::BookingsController < ApplicationController
  before_action :set_booking, only: [:show, :update, :destroy]

  # GET /api/v1/bookings
  # Fetch all bookings
  def index
    @bookings = Booking.all
    render json: @bookings, status: :ok
  end

  # POST /api/v1/bookings
  # Create a new booking
  def create
    @booking = Booking.new(booking_params)

    if @booking.save
      send_email_notifications(@booking)
      render json: @booking, status: :created
    else
      render json: @booking.errors, status: :unprocessable_entity
    end
  end

  # GET /api/v1/bookings/:id
  # Fetch a specific booking
  def show
    render json: @booking, status: :ok
  end

  # PATCH/PUT /api/v1/bookings/:id
  # Update a specific booking
  def update
    if @booking.update(booking_params)
      render json: @booking, status: :ok
    else
      render json: @booking.errors, status: :unprocessable_entity
    end
  end

  # DELETE /api/v1/bookings/:id
  # Delete a specific booking
  def destroy
    @booking.destroy
    head :no_content
  end

  private

  # Set booking for show, update and destroy actions
  def set_booking
    @booking = Booking.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Booking not found' }, status: :not_found
  end

  # Strong parameters for booking
  def booking_params
    params.require(:booking).permit(:name, :email, :room_type, :check_in_date, :check_out_date)
  end

  # Send email notifications for new bookings
  def send_email_notifications(booking)
    # Notify the hotel
    HotelMailer.with(booking: booking).new_booking_email.deliver_later

    # Notify the event organizer
    EventOrganizerMailer.with(booking: booking).new_booking_notification.deliver_later
  end
end
```

```ruby
# app/models/booking.rb
class Booking < ApplicationRecord
  validates :name, presence: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :room_type, presence: true
  validates :check_in_date, presence: true
  validates :check_out_date, presence: true
  validate :check_in_before_check_out

  private

  # Custom validation to ensure check-in date is before check-out date
  def check_in_before_check_out
    if check_in_date >= check_out_date
      errors.add(:check_in_date, 'must be before check-out date')
    end
  end
end
```

```ruby
# app/mailers/hotel_mailer.rb
class HotelMailer < ApplicationMailer
  default from: 'notifications@thresholdsummermeeting.com'

  # Send a new booking email to the hotel
  def new_booking_email
    @booking = params[:booking]
    mail(to: 'hotel@thresholdsummermeeting.com', subject: 'New Room Booking')
  end
end
```

```ruby
# app/mailers/event_organizer_mailer.rb
class EventOrganizerMailer < ApplicationMailer
  default from: 'notifications@thresholdsummermeeting.com'

  # Send a new booking notification to the event organizer
  def new_booking_notification
    @booking = params[:booking]
    mail(to: 'organizer@thresholdsummermeeting.com', subject: 'New Room Booking Notification')
  end
end
```

```ruby
# config/routes.rb
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :bookings
    end
  end
end
```

```ruby
# db/migrate/20230101000000_create_bookings.rb
class CreateBookings < ActiveRecord::Migration[6.1]
  def change
    create_table :bookings do |t|
      t.string :name, null: false
      t.string :email, null: false
      t.string :room_type, null: false
      t.date :check_in_date, null: false
      t.date :check_out_date, null: false

      t.timestamps
    end
  end
end
```

```ruby
# config/environments/development.rb
config.action_mailer.delivery_method = :letter_opener
```

```ruby
# config/environments/production.rb
config.action_mailer.delivery_method = :smtp
config.action_mailer.smtp_settings = {
  address: 'smtp.example.com',
  port: 587,
  user_name: 'user@example.com',
  password: 'password',
  authentication: 'plain',
  enable_starttls_auto: true
}
```

```ruby
# Gemfile
gem 'rails', '~> 6.0'
gem 'bcrypt', '~> 3.1.7'
gem 'letter_opener', group: :development
```
