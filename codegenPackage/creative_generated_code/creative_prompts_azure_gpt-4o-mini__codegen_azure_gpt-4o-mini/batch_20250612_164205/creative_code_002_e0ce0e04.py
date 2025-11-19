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
  before_action :set_reservation, only: [:show, :edit, :update, :destroy]

  # GET /reservations
  # Retrieves and displays a list of all reservations
  def index
    @reservations = Reservation.all
  rescue StandardError => e
    flash[:alert] = "Error retrieving reservations: #{e.message}"
    redirect_to root_path
  end

  # GET /reservations/new
  # Initializes a new reservation object
  def new
    @reservation = Reservation.new
  end

  # POST /reservations
  # Creates a new reservation
  def create
    @reservation = Reservation.new(reservation_params)

    if @reservation.save
      flash[:notice] = "Reservation created successfully."
      redirect_to @reservation
    else
      flash.now[:alert] = "Error creating reservation: #{@reservation.errors.full_messages.join(', ')}"
      render :new
    end
  end

  # GET /reservations/:id
  # Displays a specific reservation
  def show
  end

  # GET /reservations/:id/edit
  # Prepares the reservation for editing
  def edit
  end

  # PATCH/PUT /reservations/:id
  # Updates an existing reservation
  def update
    if @reservation.update(reservation_params)
      flash[:notice] = "Reservation updated successfully."
      redirect_to @reservation
    else
      flash.now[:alert] = "Error updating reservation: #{@reservation.errors.full_messages.join(', ')}"
      render :edit
    end
  end

  # DELETE /reservations/:id
  # Deletes a specific reservation
  def destroy
    @reservation.destroy
    flash[:notice] = "Reservation deleted successfully."
    redirect_to reservations_path
  rescue StandardError => e
    flash[:alert] = "Error deleting reservation: #{e.message}"
    redirect_to reservations_path
  end

  private

  # Set the reservation based on the provided ID
  def set_reservation
    @reservation = Reservation.find(params[:id])
  rescue ActiveRecord::RecordNotFound => e
    flash[:alert] = "Reservation not found: #{e.message}"
    redirect_to reservations_path
  end

  # Strong parameters for reservation
  def reservation_params
    params.require(:reservation).permit(:name, :email, :phone, :party_size, :reservation_date, :special_requests)
  end
end
```

```ruby
# app/models/reservation.rb

class Reservation < ApplicationRecord
  # Validations for reservation attributes
  validates :name, presence: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :phone, presence: true, format: { with: /\A\d{10}\z/, message: "must be a 10-digit phone number" }
  validates :party_size, presence: true, numericality: { only_integer: true, greater_than: 0 }
  validates :reservation_date, presence: true
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  resources :reservations
  root 'reservations#index'
end
```

```erb
<!-- app/views/reservations/index.html.erb -->

<h1>Reservations</h1>

<%= link_to 'New Reservation', new_reservation_path %>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Phone</th>
      <th>Party Size</th>
      <th>Reservation Date</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <% @reservations.each do |reservation| %>
      <tr>
        <td><%= reservation.name %></td>
        <td><%= reservation.email %></td>
        <td><%= reservation.phone %></td>
        <td><%= reservation.party_size %></td>
        <td><%= reservation.reservation_date.strftime('%B %d, %Y %I:%M %p') %></td>
        <td>
          <%= link_to 'Show', reservation %>
          <%= link_to 'Edit', edit_reservation_path(reservation) %>
          <%= link_to 'Delete', reservation, method: :delete, data: { confirm: 'Are you sure?' } %>
        </td>
      </tr>
    <% end %>
  </tbody>
</table>
```

```erb
<!-- app/views/reservations/new.html.erb -->

<h1>New Reservation</h1>

<%= form_with model: @reservation, local: true do |form| %>
  <% if @reservation.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(@reservation.errors.count, "error") %> prohibited this reservation from being saved:</h2>
      <ul>
        <% @reservation.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div>
    <%= form.label :name %>
    <%= form.text_field :name %>
  </div>

  <div>
    <%= form.label :email %>
    <%= form.email_field :email %>
  </div>

  <div>
    <%= form.label :phone %>
    <%= form.telephone_field :phone %>
  </div>

  <div>
    <%= form.label :party_size %>
    <%= form.number_field :party_size %>
  </div>

  <div>
    <%= form.label :reservation_date %>
    <%= form.datetime_select :reservation_date %>
  </div>

  <div>
    <%= form.label :special_requests %>
    <%= form.text_area :special_requests %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>

<%= link_to 'Back', reservations_path %>
```

```erb
<!-- app/views/reservations/edit.html.erb -->

<h1>Edit Reservation</h1>

<%= form_with model: @reservation, local: true do |form| %>
  <% if @reservation.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(@reservation.errors.count, "error") %> prohibited this reservation from being saved:</h2>
      <ul>
        <% @reservation.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div>
    <%= form.label :name %>
    <%= form.text_field :name %>
  </div>

  <div>
    <%= form.label :email %>
    <%= form.email_field :email %>
  </div>

  <div>
    <%= form.label :phone %>
    <%= form.telephone_field :phone %>
  </div>

  <div>
    <%= form.label :party_size %>
    <%= form.number_field :party_size %>
  </div>

  <div>
    <%= form.label :reservation_date %>
    <%= form.datetime_select :reservation_date %>
  </div>

  <div>
    <%= form.label :special_requests %>
    <%= form.text_area :special_requests %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>

<%= link_to 'Back', reservations_path %>
```

```ruby
# db/migrate/20231010120000_create_reservations.rb

class CreateReservations < ActiveRecord::Migration[6.1]
  def change
    create_table :reservations do |t|
      t.string :name, null: false
      t.string :email, null: false
      t.string :phone, null: false
      t.integer :party_size, null: false
      t.datetime :reservation_date, null: false
      t.text :special_requests

      t.timestamps
    end
  end
end
```

```bash
# Run the database migration
rails db:migrate
```
