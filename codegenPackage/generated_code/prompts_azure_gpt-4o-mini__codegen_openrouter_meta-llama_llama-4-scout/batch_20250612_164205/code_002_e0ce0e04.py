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
# reservations_controller.rb

class ReservationsController < ApplicationController
  # Before actions
  before_action :set_reservation, only [:show, :edit, :update, :destroy]
  before_action :authenticate_user!, except: [:index, :show]

  # GET /reservations
  def index
    @reservations = Reservation.all
    render json: @reservations
  end

  # GET /reservations/1
  def show
    render json: @reservation
  end

  # GET /reservations/new
  def new
    @reservation = Reservation.new
  end

  # GET /reservations/1/edit
  def edit; end

  # POST /reservations
  def create
    @reservation = Reservation.new(reservation_params)

    if @reservation.save
      render json: @reservation, status: :created, location: @reservation
    else
      render json: @reservation.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /reservations/1
  def update
    if @reservation.update(reservation_params)
      render json: @reservation
    else
      render json: @reservation.errors, status: :unprocessable_entity
    end
  end

  # DELETE /reservations/1
  def destroy
    @reservation.destroy
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_reservation
    @reservation = Reservation.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Reservation not found' }, status: :not_found
  end

  # Only allow a trusted parameter "white list" through.
  def reservation_params
    params.require(:reservation).permit(:date, :time, :party_size, :user_id, :table_id)
  end
end
```

```ruby
# reservation.rb

class Reservation < ApplicationRecord
  # Associations
  belongs_to :user
  belongs_to :table

  # Validations
  validates :date, :time, :party_size, :user_id, :table_id, presence: true
  validates :party_size, numericality: { greater_than: 0 }

  # Date and time validation
  validate :valid_date_and_time

  private

  def valid_date_and_time
    if date && time
      datetime = DateTime.new(date.year, date.month, date.day, time.hour, time.min)
      errors.add(:date, 'is in the past') if datetime < DateTime.now
    end
  end
end
```

```ruby
# tables_controller.rb

class TablesController < ApplicationController
  # Before actions
  before_action :set_table, only [:show, :edit, :update, :destroy]
  before_action :authenticate_user!, except: [:index, :show]

  # GET /tables
  def index
    @tables = Table.all
    render json: @tables
  end

  # GET /tables/1
  def show
    render json: @table
  end

  # GET /tables/new
  def new
    @table = Table.new
  end

  # GET /tables/1/edit
  def edit; end

  # POST /tables
  def create
    @table = Table.new(table_params)

    if @table.save
      render json: @table, status: :created, location: @table
    else
      render json: @table.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /tables/1
  def update
    if @table.update(table_params)
      render json: @table
    else
      render json: @table.errors, status: :unprocessable_entity
    end
  end

  # DELETE /tables/1
  def destroy
    @table.destroy
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_table
    @table = Table.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Table not found' }, status: :not_found
  end

  # Only allow a trusted parameter "white list" through.
  def table_params
    params.require(:table).permit(:table_number, :seating_capacity)
  end
end
```

```ruby
# tables.rb

class Table < ApplicationRecord
  # Associations
  has_many :reservations

  # Validations
  validates :table_number, :seating_capacity, presence: true
  validates :table_number, uniqueness: true
  validates :seating_capacity, numericality: { greater_than: 0 }
end
```

```ruby
# users_controller.rb

class UsersController < ApplicationController
  # Before actions
  before_action :set_user, only [:show, :edit, :update, :destroy]
  before_action :authenticate_user!, except: [:index, :show]

  # GET /users
  def index
    @users = User.all
    render json: @users
  end

  # GET /users/1
  def show
    render json: @user
  end

  # GET /users/new
  def new
    @user = User.new
  end

  # GET /users/1/edit
  def edit; end

  # POST /users
  def create
    @user = User.new(user_params)

    if @user.save
      render json: @user, status: :created, location: @user
    else
      render json: @user.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /users/1
  def update
    if @user.update(user_params)
      render json: @user
    else
      render json: @user.errors, status: :unprocessable_entity
    end
  end

  # DELETE /users/1
  def destroy
    @user.destroy
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_user
    @user = User.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'User not found' }, status: :not_found
  end

  # Only allow a trusted parameter "white list" through.
  def user_params
    params.require(:user).permit(:name, :email, :password)
  end
end
```

```ruby
# application_controller.rb

class ApplicationController < ActionController::API
  include Devise::Controllers::Helpers

  # Handle errors
  rescue_from ActiveRecord::RecordNotFound, with: :not_found
  rescue_from Exception, with: :internal_server_error

  private

  def not_found
    render json: { error: 'Not found' }, status: :not_found
  end

  def internal_server_error
    render json: { error: 'Internal server error' }, status: :internal_server_error
  end
end
```
