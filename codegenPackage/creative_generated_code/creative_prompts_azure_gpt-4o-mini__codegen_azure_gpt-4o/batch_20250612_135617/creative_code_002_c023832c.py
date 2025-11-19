"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secondcitysummers.com
Prompt: Create a Ruby on Rails application that allows users to book tickets for shows at The Second City, including options for corporate events and private parties.
Generated: DETERMINISTIC_c023832c4d6b4d5b
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Gemfile
# Add necessary gems
gem 'rails', '~> 7.0'
gem 'pg', '~> 1.1' # PostgreSQL for production database
gem 'puma', '~> 5.0'
gem 'devise', '~> 4.8' # User authentication
gem 'simple_form', '~> 5.1' # Form builder

# Run `bundle install` to install gems

# Create the Rails application and configure the database
# Command: rails new second_city_booking --database=postgresql

# app/models/user.rb
class User < ApplicationRecord
  # Include Devise modules
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  # Associations
  has_many :bookings, dependent: :destroy
end

# app/models/show.rb
class Show < ApplicationRecord
  # Validations
  validates :title, :description, :show_date, :available_seats, presence: true
  validates :available_seats, numericality: { greater_than_or_equal_to: 0 }

  # Associations
  has_many :bookings, dependent: :destroy
end

# app/models/booking.rb
class Booking < ApplicationRecord
  # Associations
  belongs_to :user
  belongs_to :show

  # Validations
  validates :number_of_seats, presence: true, numericality: { greater_than: 0 }
  validate :seats_availability

  # Custom validation to ensure seats are available
  def seats_availability
    if show.available_seats < number_of_seats
      errors.add(:number_of_seats, "are not available.")
    end
  end

  # Callback to reduce available seats after booking
  after_create :reduce_seats

  private

  def reduce_seats
    show.update(available_seats: show.available_seats - number_of_seats)
  end
end

# db/migrate/xxxx_create_users.rb
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :email, null: false, default: ""
      t.string :encrypted_password, null: false, default: ""

      t.timestamps
    end

    add_index :users, :email, unique: true
  end
end

# db/migrate/xxxx_create_shows.rb
class CreateShows < ActiveRecord::Migration[7.0]
  def change
    create_table :shows do |t|
      t.string :title, null: false
      t.text :description
      t.date :show_date, null: false
      t.integer :available_seats, null: false, default: 0

      t.timestamps
    end
  end
end

# db/migrate/xxxx_create_bookings.rb
class CreateBookings < ActiveRecord::Migration[7.0]
  def change
    create_table :bookings do |t|
      t.references :user, null: false, foreign_key: true
      t.references :show, null: false, foreign_key: true
      t.integer :number_of_seats, null: false

      t.timestamps
    end
  end
end

# config/routes.rb
Rails.application.routes.draw do
  devise_for :users

  resources :shows do
    resources :bookings, only: [:new, :create]
  end

  root "shows#index"
end

# app/controllers/shows_controller.rb
class ShowsController < ApplicationController
  before_action :authenticate_user!, except: [:index, :show]
  before_action :set_show, only: [:show, :edit, :update, :destroy]

  def index
    @shows = Show.all
  end

  def show; end

  def new
    @show = Show.new
  end

  def create
    @show = Show.new(show_params)

    if @show.save
      redirect_to @show, notice: "Show successfully created."
    else
      render :new, status: :unprocessable_entity
    end
  end

  def edit; end

  def update
    if @show.update(show_params)
      redirect_to @show, notice: "Show successfully updated."
    else
      render :edit, status: :unprocessable_entity
    end
  end

  def destroy
    @show.destroy
    redirect_to shows_path, notice: "Show successfully deleted."
  end

  private

  def set_show
    @show = Show.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to shows_path, alert: "Show not found."
  end

  def show_params
    params.require(:show).permit(:title, :description, :show_date, :available_seats)
  end
end

# app/controllers/bookings_controller.rb
class BookingsController < ApplicationController
  before_action :authenticate_user!
  before_action :set_show

  def new
    @booking = Booking.new
  end

  def create
    @booking = current_user.bookings.build(booking_params)
    @booking.show = @show

    if @booking.save
      redirect_to show_path(@show), notice: "Booking successfully created."
    else
      render :new, status: :unprocessable_entity
    end
  end

  private

  def set_show
    @show = Show.find(params[:show_id])
  rescue ActiveRecord::RecordNotFound
    redirect_to shows_path, alert: "Show not found."
  end

  def booking_params
    params.require(:booking).permit(:number_of_seats)
  end
end

# app/views/shows/index.html.erb
<h1>Shows</h1>
<%= link_to "New Show", new_show_path if user_signed_in? %>
<ul>
  <% @shows.each do |show| %>
    <li>
      <%= link_to show.title, show_path(show) %>
      (Available Seats: <%= show.available_seats %>)
    </li>
  <% end %>
</ul>

# app/views/shows/show.html.erb
<h1><%= @show.title %></h1>
<p><%= @show.description %></p>
<p>Show Date: <%= @show.show_date %></p>
<p>Available Seats: <%= @show.available_seats %></p>

<%= link_to "Book Tickets", new_show_booking_path(@show) if user_signed_in? %>
<%= link_to "Edit Show", edit_show_path(@show) if user_signed_in? %>
<%= link_to "Delete Show", show_path(@show), method: :delete, data: { confirm: "Are you sure?" } if user_signed_in? %>

# app/views/bookings/new.html.erb
<h1>Book Tickets for <%= @show.title %></h1>
<%= simple_form_for([@show, @booking]) do |f| %>
  <%= f.input :number_of_seats, label: "Number of Seats" %>
  <%= f.submit "Book Tickets" %>
<% end %>

# Run migrations
# Command: rails db:create db:migrate

# To use Devise for authentication:
# Command: rails generate devise:install
# Command: rails generate devise User

# Start the server
# Command: rails server
```
