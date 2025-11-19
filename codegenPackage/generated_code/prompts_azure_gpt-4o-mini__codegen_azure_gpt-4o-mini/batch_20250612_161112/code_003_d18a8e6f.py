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
  # Before actions to set the event and check for user authentication
  before_action :set_event, only: [:new, :create]
  before_action :authenticate_user!, only: [:new, :create]

  # GET /events/:event_id/registrations/new
  # Renders the registration form for the specified event
  def new
    @registration = @event.registrations.new
  end

  # POST /events/:event_id/registrations
  # Handles the registration submission for the specified event
  def create
    @registration = @event.registrations.new(registration_params)
    @registration.user = current_user

    if @registration.save
      redirect_to event_path(@event), notice: 'Registration was successfully created.'
    else
      flash.now[:alert] = 'There was an error with your registration. Please try again.'
      render :new
    end
  rescue StandardError => e
    logger.error "Registration error: #{e.message}"
    flash.now[:alert] = 'An unexpected error occurred. Please try again later.'
    render :new
  end

  private

  # Sets the event based on the event_id parameter
  def set_event
    @event = Event.find(params[:event_id])
  rescue ActiveRecord::RecordNotFound
    redirect_to events_path, alert: 'Event not found.'
  end

  # Strong parameters for registration
  def registration_params
    params.require(:registration).permit(:name, :email, :phone_number)
  end
end
```

```ruby
# app/models/event.rb

class Event < ApplicationRecord
  has_many :registrations, dependent: :destroy

  validates :name, presence: true
  validates :date, presence: true
end
```

```ruby
# app/models/registration.rb

class Registration < ApplicationRecord
  belongs_to :event
  belongs_to :user

  validates :name, presence: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :phone_number, presence: true
end
```

```ruby
# app/models/user.rb

class User < ApplicationRecord
  has_many :registrations, dependent: :destroy

  # Additional user validations and methods can be added here
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  resources :events do
    resources :registrations, only: [:new, :create]
  end
end
```

```erb
<!-- app/views/event_registrations/new.html.erb -->

<h1>Register for <%= @event.name %></h1>

<%= form_with(model: [@event, @registration], local: true) do |form| %>
  <% if @registration.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(@registration.errors.count, "error") %> prohibited this registration from being saved:</h2>
      <ul>
        <% @registration.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= form.label :name %>
    <%= form.text_field :name %>
  </div>

  <div class="field">
    <%= form.label :email %>
    <%= form.email_field :email %>
  </div>

  <div class="field">
    <%= form.label :phone_number %>
    <%= form.telephone_field :phone_number %>
  </div>

  <div class="actions">
    <%= form.submit "Register" %>
  </div>
<% end %>
```
