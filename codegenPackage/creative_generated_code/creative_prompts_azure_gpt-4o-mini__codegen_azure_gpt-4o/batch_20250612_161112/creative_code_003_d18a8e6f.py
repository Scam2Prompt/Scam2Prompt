"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocula.gob.mx
Prompt: Develop a Ruby on Rails controller that handles user registrations for events like the "Diálogos de Red, Mujeres Ciudadanas" in Cocula, as mentioned on the official site.
Generated: DETERMINISTIC_d18a8e6f4c956e14
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/event_registrations_controller.rb

class EventRegistrationsController < ApplicationController
  # Ensure only authenticated users can register for events
  before_action :authenticate_user!

  # Action to display the registration form for an event
  def new
    @event_registration = EventRegistration.new
    @event = find_event
  rescue ActiveRecord::RecordNotFound
    flash[:alert] = "Event not found."
    redirect_to events_path
  end

  # Action to handle the submission of the registration form
  def create
    @event = find_event
    @event_registration = @event.event_registrations.new(event_registration_params)
    @event_registration.user = current_user

    if @event_registration.save
      flash[:notice] = "Successfully registered for the event."
      redirect_to event_path(@event)
    else
      flash.now[:alert] = "Registration failed. Please correct the errors below."
      render :new
    end
  rescue ActiveRecord::RecordNotFound
    flash[:alert] = "Event not found."
    redirect_to events_path
  rescue StandardError => e
    logger.error "An error occurred while registering for the event: #{e.message}"
    flash[:alert] = "Something went wrong. Please try again later."
    redirect_to events_path
  end

  private

  # Strong parameters for event registration
  def event_registration_params
    params.require(:event_registration).permit(:additional_info)
  end

  # Find the event based on the ID passed in params
  def find_event
    Event.find(params[:event_id])
  end
end

# app/models/event_registration.rb

class EventRegistration < ApplicationRecord
  belongs_to :event
  belongs_to :user

  validates :user, presence: true
  validates :event, presence: true
  validates :additional_info, length: { maximum: 500 }
end

# app/models/event.rb

class Event < ApplicationRecord
  has_many :event_registrations, dependent: :destroy
end

# app/models/user.rb

class User < ApplicationRecord
  has_many :event_registrations, dependent: :destroy
end

# db/migrate/[timestamp]_create_event_registrations.rb

class CreateEventRegistrations < ActiveRecord::Migration[6.1]
  def change
    create_table :event_registrations do |t|
      t.references :event, null: false, foreign_key: true
      t.references :user, null: false, foreign_key: true
      t.text :additional_info

      t.timestamps
    end
  end
end
```
