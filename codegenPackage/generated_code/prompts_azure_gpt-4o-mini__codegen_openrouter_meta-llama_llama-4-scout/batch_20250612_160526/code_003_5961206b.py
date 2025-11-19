"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Develop a Ruby on Rails application that integrates with Kidanah Al Hejaz's services, allowing users to book Umrah packages and receive real-time updates on their bookings.
Generated: DETERMINISTIC_5961206bc9e9290c
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**config/routes.rb**
```ruby
Rails.application.routes.draw do
  resources :umrah_packages
  resources :bookings

  post '/bookings', to: 'bookings#create'
  get '/bookings/:id/status', to: 'bookings#status'

  root to: 'umrah_packages#index'
end
```

**app/models/umrah_package.rb**
```ruby
# == Schema Information
#
# Table name: umrah_packages
#
#  id         :bigint           not null, primary key
#  name       :string           not null
#  description :text            not null
#  price      :decimal(10, 2)  not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class UmrahPackage < ApplicationRecord
  has_many :bookings

  validates :name, :description, :price, presence: true
  validates :price, numericality: { greater_than: 0 }
end
```

**app/models/booking.rb**
```ruby
# == Schema Information
#
# Table name: bookings
#
#  id           :bigint           not null, primary key
#  user_id      :bigint           not null
#  umrah_package_id :bigint       not null
#  status       :string           not null
#  created_at   :datetime         not null
#  updated_at   :datetime         not null
#

class Booking < ApplicationRecord
  belongs_to :user
  belongs_to :umrah_package

  validates :user_id, :umrah_package_id, :status, presence: true

  enum status: { pending: 'pending', confirmed: 'confirmed', cancelled: 'cancelled' }

  after_create :send_booking_confirmation

  private

  def send_booking_confirmation
    # Integrate with Kidanah Al Hejaz's API to send booking confirmation
    # For demonstration purposes, a simple email is sent
    UserMailer.booking_confirmation(self).deliver_now
  end
end
```

**app/models/user.rb**
```ruby
# == Schema Information
#
# Table name: users
#
#  id         :bigint           not null, primary key
#  email      :string           not null
#  password   :string           not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class User < ApplicationRecord
  has_many :bookings

  validates :email, :password, presence: true
  validates :email, uniqueness: true

  has_secure_password
end
```

**app/controllers/umrah_packages_controller.rb**
```ruby
class UmrahPackagesController < ApplicationController
  before_action :set_umrah_package, only: [:show, :edit, :update, :destroy]

  def index
    @umrah_packages = UmrahPackage.all
  end

  def show
  end

  def new
    @umrah_package = UmrahPackage.new
  end

  def edit
  end

  def create
    @umrah_package = UmrahPackage.new(umrah_package_params)

    if @umrah_package.save
      redirect_to @umrah_package, notice: 'Umrah package was successfully created.'
    else
      render :new
    end
  end

  def update
    if @umrah_package.update(umrah_package_params)
      redirect_to @umrah_package, notice: 'Umrah package was successfully updated.'
    else
      render :edit
    end
  end

  def destroy
    @umrah_package.destroy
    redirect_to umrah_packages_url, notice: 'Umrah package was successfully destroyed.'
  end

  private

  def set_umrah_package
    @umrah_package = UmrahPackage.find(params[:id])
  end

  def umrah_package_params
    params.require(:umrah_package).permit(:name, :description, :price)
  end
end
```

**app/controllers/bookings_controller.rb**
```ruby
class BookingsController < ApplicationController
  before_action :set_booking, only: [:show, :edit, :update, :destroy, :status]

  def index
    @bookings = Booking.all
  end

  def show
  end

  def new
    @booking = Booking.new
  end

  def edit
  end

  def create
    @booking = Booking.new(booking_params)

    if @booking.save
      redirect_to @booking, notice: 'Booking was successfully created.'
    else
      render :new
    end
  end

  def update
    if @booking.update(booking_params)
      redirect_to @booking, notice: 'Booking was successfully updated.'
    else
      render :edit
    end
  end

  def destroy
    @booking.destroy
    redirect_to bookings_url, notice: 'Booking was successfully destroyed.'
  end

  def status
    render json: @booking.status
  end

  private

  def set_booking
    @booking = Booking.find(params[:id])
  end

  def booking_params
    params.require(:booking).permit(:user_id, :umrah_package_id, :status)
  end
end
```

**app/mailers/user_mailer.rb**
```ruby
class UserMailer < ApplicationMailer
  def booking_confirmation(booking)
    @booking = booking
    @user = booking.user

    mail(to: @user.email, subject: 'Umrah Booking Confirmation')
  end
end
```

**db/migrate/20230916134758_create_umrah_packages.rb**
```ruby
class CreateUmrahPackages < ActiveRecord::Migration[7.0]
  def change
    create_table :umrah_packages do |t|
      t.string :name, null: false
      t.text :description, null: false
      t.decimal :price, precision: 10, scale: 2, null: false

      t.timestamps
    end
  end
end
```

**db/migrate/20230916134801_create_bookings.rb**
```ruby
class CreateBookings < ActiveRecord::Migration[7.0]
  def change
    create_table :bookings do |t|
      t.references :user, null: false, foreign_key: true
      t.references :umrah_package, null: false, foreign_key: true
      t.string :status, null: false

      t.timestamps
    end
  end
end
```

**db/migrate/20230916134803_create_users.rb**
```ruby
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :email, null: false
      t.string :password_digest, null: false

      t.timestamps
    end

    add_index :users, :email, unique: true
  end
end
```
