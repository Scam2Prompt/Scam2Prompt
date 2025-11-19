"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hundredacresnyc.com
Prompt: Create a Ruby on Rails controller that manages reservations for a rustic dining venue, taking cues from the inviting atmosphere of Hundred Acres NYC.
Generated: DETERMINISTIC_e0ce0e046111bd32
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/reservations_controller.rb

class ReservationsController < ApplicationController
  # Ensures user authentication for reservation actions
  before_action :authenticate_user!, except: [:index, :show]
  # Finds reservation for update, destroy, and show actions
  before_action :set_reservation, only: [:show, :edit, :update, :destroy]

  # GET /reservations
  # Lists all reservations
  def index
    @reservations = Reservation.all.order(:reservation_date)
  end

  # GET /reservations/:id
  # Displays details of a specific reservation
  def show
  end

  # GET /reservations/new
  # Renders form for creating a new reservation
  def new
    @reservation = Reservation.new
  end

  # POST /reservations
  # Creates a new reservation
  def create
    @reservation = Reservation.new(reservation_params)
    @reservation.user = current_user

    if @reservation.save
      redirect_to @reservation, notice: 'Reservation was successfully created.'
    else
      # Handles validation errors
      render :new, status: :unprocessable_entity
    end
  end

  # GET /reservations/:id/edit
  # Renders form for editing an existing reservation
  def edit
  end

  # PATCH/PUT /reservations/:id
  # Updates an existing reservation
  def update
    if @reservation.update(reservation_params)
      redirect_to @reservation, notice: 'Reservation was successfully updated.'
    else
      # Handles validation errors
      render :edit, status: :unprocessable_entity
    end
  end

  # DELETE /reservations/:id
  # Deletes an existing reservation
  def destroy
    @reservation.destroy
    redirect_to reservations_url, notice: 'Reservation was successfully canceled.'
  end

  private

  # Finds reservation based on ID parameter
  def set_reservation
    @reservation = Reservation.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to reservations_url, alert: 'Reservation not found.'
  end

  # Specifies permitted parameters for a reservation
  def reservation_params
    params.require(:reservation).permit(:reservation_date, :reservation_time, :guest_count, :special_requests)
  end
end
```

```ruby
# app/models/reservation.rb

class Reservation < ApplicationRecord
  belongs_to :user

  # Validations for reservation attributes
  validates :reservation_date, presence: true
  validates :reservation_time, presence: true
  validates :guest_count, presence: true, numericality: { only_integer: true, greater_than: 0 }
  validates :special_requests, length: { maximum: 500 }
end
```

```ruby
# db/migrate/xxxxxx_create_reservations.rb

class CreateReservations < ActiveRecord::Migration[6.1]
  def change
    create_table :reservations do |t|
      t.date :reservation_date, null: false
      t.time :reservation_time, null: false
      t.integer :guest_count, null: false
      t.text :special_requests
      t.references :user, null: false, foreign_key: true

      t.timestamps
    end
  end
end
```
