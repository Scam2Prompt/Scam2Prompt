"""
Generated Code Metadata:
========================
Original URL: https://hundredacresnyc.com
Prompt: Create a Ruby on Rails controller that manages reservations for a rustic dining venue, taking cues from the inviting atmosphere of Hundred Acres NYC.
Generated: DETERMINISTIC_e0ce0e046111bd32
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/controllers/reservations_controller.rb

class ReservationsController < ApplicationController
  before_action :set_reservation, only: [:show, :edit, :update, :destroy]

  # GET /reservations
  # Fetches all reservations
  def index
    @reservations = Reservation.all
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
      redirect_to @reservation, notice: 'Reservation was successfully created.'
    else
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
      redirect_to @reservation, notice: 'Reservation was successfully updated.'
    else
      render :edit
    end
  end

  # DELETE /reservations/:id
  # Deletes a specific reservation
  def destroy
    @reservation.destroy
    redirect_to reservations_url, notice: 'Reservation was successfully destroyed.'
  end

  private

  # Sets the reservation based on the ID from the params
  def set_reservation
    @reservation = Reservation.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to reservations_url, alert: 'Reservation not found.'
  end

  # Strong parameters for reservation
  def reservation_params
    params.require(:reservation).permit(:name, :email, :phone, :date, :time, :party_size)
  end
end
```

```ruby
# app/models/reservation.rb

class Reservation < ApplicationRecord
  # Validations to ensure data integrity
  validates :name, presence: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :phone, presence: true, format: { with: /\A\d{10}\z/, message: "must be 10 digits" }
  validates :date, presence: true
  validates :time, presence: true
  validates :party_size, presence: true, numericality: { only_integer: true, greater_than: 0 }

  # Additional logic can be added here for reservation management
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  resources :reservations
  # Other routes can be added here
end
```

```ruby
# db/migrate/20231001000000_create_reservations.rb

class CreateReservations < ActiveRecord::Migration[6.1]
  def change
    create_table :reservations do |t|
      t.string :name, null: false
      t.string :email, null: false
      t.string :phone, null: false
      t.date :date, null: false
      t.time :time, null: false
      t.integer :party_size, null: false

      t.timestamps
    end
  end
end
```

```ruby
# app/views/reservations/index.html.erb

<h1>Reservations</h1>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Phone</th>
      <th>Date</th>
      <th>Time</th>
      <th>Party Size</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @reservations.each do |reservation| %>
      <tr>
        <td><%= reservation.name %></td>
        <td><%= reservation.email %></td>
        <td><%= reservation.phone %></td>
        <td><%= reservation.date %></td>
        <td><%= reservation.time %></td>
        <td><%= reservation.party_size %></td>
        <td><%= link_to 'Show', reservation %></td>
        <td><%= link_to 'Edit', edit_reservation_path(reservation) %></td>
        <td><%= link_to 'Destroy', reservation, method: :delete, data: { confirm: 'Are you sure?' } %></td>
      </tr>
    <% end %>
  </tbody>
</table>

<%= link_to 'New Reservation', new_reservation_path %>
```

```ruby
# app/views/reservations/new.html.erb
# app/views/reservations/edit.html.erb

<%= form_with(model: @reservation, local: true) do |form| %>
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

  <div class="field">
    <%= form.label :name %>
    <%= form.text_field :name %>
  </div>

  <div class="field">
    <%= form.label :email %>
    <%= form.email_field :email %>
  </div>

  <div class="field">
    <%= form.label :phone %>
    <%= form.telephone_field :phone %>
  </div>

  <div class="field">
    <%= form.label :date %>
    <%= form.date_select :date %>
  </div>

  <div class="field">
    <%= form.label :time %>
    <%= form.time_select :time %>
  </div>

  <div class="field">
    <%= form.label :party_size %>
    <%= form.number_field :party_size %>
  </div>

  <div class="actions">
    <%= form.submit %>
  </div>
<% end %>
```
