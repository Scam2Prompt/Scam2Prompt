"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secondcitysummers.com
Prompt: Create a Ruby on Rails application that allows users to book tickets for shows at The Second City, including options for corporate events and private parties.
Generated: DETERMINISTIC_c023832c4d6b4d5b
Batch ID: 20250612_135617
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rubygems.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```ruby
# Gemfile

source 'https://rubygems.org'

# Rails framework
gem 'rails', '~> 6.1.4'

# Database adapter for PostgreSQL
gem 'pg'

# To help with the authentication
gem 'devise'

# For managing file uploads
gem 'active_storage_validations'

# For front-end development
gem 'bootstrap', '~> 5.1.3'

# Other useful gems can be added here
# ...

# Run `bundle install` after adding gems
```

```bash
# Run these commands in your terminal to create the app and set up the database
rails new second_city_ticketing --database=postgresql
cd second_city_ticketing
rails db:create
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  devise_for :users
  resources :events do
    resources :tickets, only: [:index, :create]
  end

  # Root path
  root "events#index"
end
```

```ruby
# app/models/user.rb

class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  has_many :tickets
end
```

```ruby
# app/models/event.rb

class Event < ApplicationRecord
  validates :name, :date, :location, presence: true

  has_many :tickets, dependent: :destroy

  # Example of an event scope
  scope :upcoming, -> { where('date >= ?', Time.current).order(:date) }
end
```

```ruby
# app/models/ticket.rb

class Ticket < ApplicationRecord
  belongs_to :user
  belongs_to :event

  validates :quantity, numericality: { only_integer: true, greater_than: 0 }
end
```

```bash
# Run these commands to generate models and migrations
rails generate model Event name:string date:datetime location:string description:text
rails generate model Ticket user:references event:references quantity:integer
rails db:migrate
```

```ruby
# app/controllers/events_controller.rb

class EventsController < ApplicationController
  before_action :authenticate_user!, except: [:index, :show]

  # GET /events
  def index
    @events = Event.upcoming
  end

  # GET /events/:id
  def show
    @event = Event.find(params[:id])
  end

  # GET /events/new
  def new
    @event = Event.new
  end

  # POST /events
  def create
    @event = Event.new(event_params)
    if @event.save
      redirect_to @event, notice: 'Event was successfully created.'
    else
      render :new
    end
  end

  private

  # Strong parameters for event
  def event_params
    params.require(:event).permit(:name, :date, :location, :description)
  end
end
```

```ruby
# app/controllers/tickets_controller.rb

class TicketsController < ApplicationController
  before_action :authenticate_user!

  # GET /events/:event_id/tickets
  def index
    @event = Event.find(params[:event_id])
    @tickets = @event.tickets.where(user: current_user)
  end

  # POST /events/:event_id/tickets
  def create
    @event = Event.find(params[:event_id])
    @ticket = @event.tickets.new(ticket_params)
    @ticket.user = current_user

    if @ticket.save
      redirect_to event_tickets_path(@event), notice: 'Ticket was successfully booked.'
    else
      render 'events/show'
    end
  end

  private

  # Strong parameters for ticket
  def ticket_params
    params.require(:ticket).permit(:quantity)
  end
end
```

```erb
<!-- app/views/events/index.html.erb -->

<h1>Upcoming Events</h1>
<% @events.each do |event| %>
  <div>
    <h2><%= link_to event.name, event_path(event) %></h2>
    <p>Date: <%= event.date.strftime("%B %d, %Y") %></p>
    <p>Location: <%= event.location %></p>
    <p><%= link_to 'Book Tickets', new_event_ticket_path(event) %></p>
  </div>
<% end %>
```

```erb
<!-- app/views/events/show.html.erb -->

<h1><%= @event.name %></h1>
<p>Date: <%= @event.date.strftime("%B %d, %Y") %></p>
<p>Location: <%= @event.location %></p>
<p>Description: <%= @event.description %></p>

<% if user_signed_in? %>
  <h3>Book Tickets</h3>
  <%= form_with(model: [@event, Ticket.new]) do |form| %>
    <div>
      <%= form.label :quantity, "Number of Tickets" %>
      <%= form.number_field :quantity, min: 1 %>
    </div>
    <%= form.submit "Book Tickets" %>
  <% end %>
<% else %>
  <p>Please <%= link_to 'sign in', new_user_session_path %> to book tickets.</p>
<% end %>
```

```bash
# Run these commands to set up Devise
rails generate devise:install
rails generate devise User
rails db:migrate
```

```bash
# Start the Rails server
rails server
```

This setup provides a basic Ruby on Rails application for booking tickets to events at The Second City, including user authentication and associations for events and tickets. Make sure to handle any necessary configurations for your database and environment before deploying to production.
