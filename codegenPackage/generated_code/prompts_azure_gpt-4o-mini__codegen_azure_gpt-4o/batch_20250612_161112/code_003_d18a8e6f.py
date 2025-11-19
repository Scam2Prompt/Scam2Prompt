"""
Generated Code Metadata:
========================
Original URL: https://cocula.gob.mx
Prompt: Develop a Ruby on Rails controller that handles user registrations for events like the "Diálogos de Red, Mujeres Ciudadanas" in Cocula, as mentioned on the official site.
Generated: DETERMINISTIC_d18a8e6f4c956e14
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/controllers/event_registrations_controller.rb

class EventRegistrationsController < ApplicationController
  # Ensure user is authenticated before allowing access to registration actions
  before_action :authenticate_user!

  # GET /event_registrations/new
  # Displays the registration form for the event
  def new
    @event_registration = EventRegistration.new
  end

  # POST /event_registrations
  # Handles the submission of the registration form
  def create
    @event_registration = EventRegistration.new(event_registration_params)
    @event_registration.user = current_user # Associate the registration with the logged-in user

    if @event_registration.save
      # Redirect to a confirmation page or show a success message
      redirect_to event_registration_path(@event_registration), notice: 'Registration successful!'
    else
      # Render the form again with error messages
      render :new, status: :unprocessable_entity
    end
  end

  # GET /event_registrations/:id
  # Displays the details of a specific registration
  def show
    @event_registration = EventRegistration.find(params[:id])
    # Ensure the user can only view their own registrations
    authorize_user!
  end

  private

  # Strong parameters to prevent mass assignment vulnerabilities
  def event_registration_params
    params.require(:event_registration).permit(:event_name, :event_date, :additional_notes)
  end

  # Ensure the user is authorized to view their registration
  def authorize_user!
    unless @event_registration.user == current_user
      redirect_to root_path, alert: 'You are not authorized to view this registration.'
    end
  end
end
```

```ruby
# app/models/event_registration.rb

class EventRegistration < ApplicationRecord
  # Associations
  belongs_to :user

  # Validations
  validates :event_name, presence: true
  validates :event_date, presence: true
  validates :additional_notes, length: { maximum: 500 }

  # Custom validation example (optional)
  validate :event_date_cannot_be_in_the_past

  private

  # Ensure the event date is not in the past
  def event_date_cannot_be_in_the_past
    if event_date.present? && event_date < Date.today
      errors.add(:event_date, "can't be in the past")
    end
  end
end
```

```ruby
# db/migrate/xxxxxx_create_event_registrations.rb

class CreateEventRegistrations < ActiveRecord::Migration[6.1]
  def change
    create_table :event_registrations do |t|
      t.string :event_name, null: false
      t.date :event_date, null: false
      t.text :additional_notes
      t.references :user, null: false, foreign_key: true

      t.timestamps
    end
  end
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  # Event registration routes
  resources :event_registrations, only: [:new, :create, :show]

  # Other routes...
end
```
