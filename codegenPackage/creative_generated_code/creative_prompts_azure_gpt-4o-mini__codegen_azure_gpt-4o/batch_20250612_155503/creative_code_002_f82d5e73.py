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
# app/controllers/room_bookings_controller.rb

class RoomBookingsController < ApplicationController
  before_action :set_room_booking, only: %i[show update destroy]

  # GET /room_bookings
  # Fetch all room bookings
  def index
    @room_bookings = RoomBooking.all
    render json: @room_bookings
  end

  # GET /room_bookings/:id
  # Fetch a specific room booking by ID
  def show
    render json: @room_booking
  end

  # POST /room_bookings
  # Create a new room booking
  def create
    @room_booking = RoomBooking.new(room_booking_params)
    if @room_booking.save
      send_email_notifications(@room_booking)
      render json: @room_booking, status: :created
    else
      render json: @room_booking.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /room_bookings/:id
  # Update an existing room booking
  def update
    if @room_booking.update(room_booking_params)
      render json: @room_booking, status: :ok
    else
      render json: @room_booking.errors, status: :unprocessable_entity
    end
  end

  # DELETE /room_bookings/:id
  # Delete a room booking
  def destroy
    @room_booking.destroy
    head :no_content
  end

  private

  # Use callbacks to share common setup or constraints between actions
  def set_room_booking
    @room_booking = RoomBooking.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Room booking not found' }, status: :not_found
  end

  # Allowed parameters for room booking
  def room_booking_params
    params.require(:room_booking).permit(:room_number, :guest_name, :check_in_date, :check_out_date, :email)
  end

  # Send email notifications for new room bookings
  def send_email_notifications(room_booking)
    HotelMailer.room_booking_notification(room_booking).deliver_now
    OrganizerMailer.room_booking_notification(room_booking).deliver_now
  rescue StandardError => e
    Rails.logger.error("Failed to send email notifications: #{e.message}")
  end
end

# app/mailers/hotel_mailer.rb

class HotelMailer < ApplicationMailer
  default from: 'no-reply@thresholdmeeting.com'

  # Notification email to the hotel
  def room_booking_notification(room_booking)
    @room_booking = room_booking
    mail(
      to: 'hotel@example.com',
      subject: "New Room Booking: ##{@room_booking.room_number}"
    )
  end
end

# app/mailers/organizer_mailer.rb

class OrganizerMailer < ApplicationMailer
  default from: 'no-reply@thresholdmeeting.com'

  # Notification email to the event organizer
  def room_booking_notification(room_booking)
    @room_booking = room_booking
    mail(
      to: 'organizer@example.com',
      subject: "New Room Booking by #{@room_booking.guest_name}"
    )
  end
end

# app/models/room_booking.rb

class RoomBooking < ApplicationRecord
  # Validations
  validates :room_number, presence: true
  validates :guest_name, presence: true
  validates :check_in_date, presence: true
  validates :check_out_date, presence: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }

  # Custom validation for date range
  validate :check_out_after_check_in

  private

  def check_out_after_check_in
    return if check_out_date.blank? || check_in_date.blank?

    if check_out_date <= check_in_date
      errors.add(:check_out_date, 'must be after check-in date')
    end
  end
end

# config/routes.rb

Rails.application.routes.draw do
  resources :room_bookings
end

# db/migrate/YYYYMMDDHHMMSS_create_room_bookings.rb

class CreateRoomBookings < ActiveRecord::Migration[6.1]
  def change
    create_table :room_bookings do |t|
      t.string :room_number, null: false
      t.string :guest_name, null: false
      t.date :check_in_date, null: false
      t.date :check_out_date, null: false
      t.string :email, null: false

      t.timestamps
    end
  end
end
```
