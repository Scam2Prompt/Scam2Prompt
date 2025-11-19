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
  # Ensure that only authenticated users can register for events
  before_action :authenticate_user!

  # GET /event_registrations/new
  # This action renders the registration form for the event
  def new
    @event_registration = EventRegistration.new
  end

  # POST /event_registrations
  # This action handles the registration submission
  def create
    @event_registration = EventRegistration.new(event_registration_params)

    if @event_registration.save
      # Send a confirmation email after successful registration
      EventRegistrationMailer.with(registration: @event_registration).confirmation.deliver_later
      redirect_to event_registration_path(@event_registration), notice: 'Registration was successfully created.'
    else
      # If validation fails, re-render the new template with errors
      render :new
    end
  rescue StandardError => e
    # Log the error and display a friendly message to the user
    logger.error "Error creating registration: #{e.message}"
    redirect_to new_event_registration_path, alert: 'There was an error processing your registration. Please try again.'
  end

  # GET /event_registrations/:id
  # This action shows the details of a specific registration
  def show
    @event_registration = EventRegistration.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to new_event_registration_path, alert: 'Registration not found.'
  end

  private

  # Strong parameters to prevent mass assignment vulnerabilities
  def event_registration_params
    params.require(:event_registration).permit(:user_id, :event_id, :comments)
  end
end
```

```ruby
# app/mailers/event_registration_mailer.rb

class EventRegistrationMailer < ApplicationMailer
  # Sends a confirmation email for the event registration
  def confirmation
    @registration = params[:registration]
    mail(to: @registration.user.email, subject: 'Registration Confirmation')
  end
end
```

```ruby
# app/models/event_registration.rb

class EventRegistration < ApplicationRecord
  # Associations
  belongs_to :user
  belongs_to :event

  # Validations
  validates :user_id, presence: true
  validates :event_id, presence: true
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  resources :event_registrations, only: [:new, :create, :show]
end
```
