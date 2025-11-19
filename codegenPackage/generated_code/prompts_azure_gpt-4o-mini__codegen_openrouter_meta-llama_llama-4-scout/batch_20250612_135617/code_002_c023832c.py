"""
Generated Code Metadata:
========================
Original URL: https://secondcitysummers.com
Prompt: Create a Ruby on Rails application that allows users to book tickets for shows at The Second City, including options for corporate events and private parties.
Generated: DETERMINISTIC_c023832c4d6b4d5b
Batch ID: 20250612_135617
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
  resources :shows do
    member do
      get :book_ticket
    end
  end

  resources :bookings do
    member do
      get :cancel
    end
  end

  resources :corporate_events do
    member do
      get :book
    end
  end

  resources :private_parties do
    member do
      get :book
    end
  end

  root 'shows#index'
end
```

**app/models/show.rb**
```ruby
# == Schema Information
#
# Table name: shows
#
#  id          :bigint(8)        not null, primary key
#  name        :string           not null
#  date        :date             not null
#  time        :time             not null
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#  description :text
#

class Show < ApplicationRecord
  has_many :bookings, dependent: :destroy
  has_many :corporate_events, dependent: :destroy
  has_many :private_parties, dependent: :destroy

  validates :name, :date, :time, presence: true

  def book_ticket(user)
    bookings.create(user: user, show: self)
  end
end
```

**app/models/booking.rb**
```ruby
# == Schema Information
#
# Table name: bookings
#
#  id         :bigint(8)        not null, primary key
#  user_id    :bigint(8)
#  show_id    :bigint(8)
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class Booking < ApplicationRecord
  belongs_to :user
  belongs_to :show

  validates :user_id, :show_id, presence: true

  def cancel
    destroy
  end
end
```

**app/models/user.rb**
```ruby
# == Schema Information
#
# Table name: users
#
#  id         :bigint(8)        not null, primary key
#  email      :string           not null
#  password   :string           not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class User < ApplicationRecord
  has_many :bookings, dependent: :destroy

  validates :email, :password, presence: true

  has_secure_password
end
```

**app/models/corporate_event.rb**
```ruby
# == Schema Information
#
# Table name: corporate_events
#
#  id         :bigint(8)        not null, primary key
#  show_id    :bigint(8)
#  company    :string           not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class CorporateEvent < ApplicationRecord
  belongs_to :show

  validates :show_id, :company, presence: true

  def book
    # implement booking logic for corporate events
  end
end
```

**app/models/private_party.rb**
```ruby
# == Schema Information
#
# Table name: private_parties
#
#  id         :bigint(8)        not null, primary key
#  show_id    :bigint(8)
#  guest_name :string           not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class PrivateParty < ApplicationRecord
  belongs_to :show

  validates :show_id, :guest_name, presence: true

  def book
    # implement booking logic for private parties
  end
end
```

**app/controllers/shows_controller.rb**
```ruby
class ShowsController < ApplicationController
  before_action :set_show, only: [:book_ticket]

  def index
    @shows = Show.all
  end

  def book_ticket
    if @show.book_ticket(current_user)
      redirect_to @show, notice: 'Ticket booked successfully!'
    else
      render :show
    end
  end

  private

  def set_show
    @show = Show.find(params[:id])
  end
end
```

**app/controllers/bookings_controller.rb**
```ruby
class BookingsController < ApplicationController
  before_action :set_booking, only: [:cancel]

  def cancel
    if @booking.cancel
      redirect_to root_path, notice: 'Booking cancelled successfully!'
    else
      render :show
    end
  end

  private

  def set_booking
    @booking = Booking.find(params[:id])
  end
end
```

**app/controllers/corporate_events_controller.rb**
```ruby
class CorporateEventsController < ApplicationController
  before_action :set_corporate_event, only: [:book]

  def book
    if @corporate_event.book
      redirect_to @corporate_event.show, notice: 'Corporate event booked successfully!'
    else
      render :show
    end
  end

  private

  def set_corporate_event
    @corporate_event = CorporateEvent.find(params[:id])
  end
end
```

**app/controllers/private_parties_controller.rb**
```ruby
class PrivatePartiesController < ApplicationController
  before_action :set_private_party, only: [:book]

  def book
    if @private_party.book
      redirect_to @private_party.show, notice: 'Private party booked successfully!'
    else
      render :show
    end
  end

  private

  def set_private_party
    @private_party = PrivateParty.find(params[:id])
  end
end
```

**db/migrate/2023xxxxxxx_create_shows.rb**
```ruby
class CreateShows < ActiveRecord::Migration[7.0]
  def change
    create_table :shows do |t|
      t.string :name, null: false
      t.date :date, null: false
      t.time :time, null: false
      t.text :description

      t.timestamps
    end
  end
end
```

**db/migrate/2023xxxxxxx_create_users.rb**
```ruby
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :email, null: false
      t.string :password_digest, null: false

      t.timestamps
    end
  end
end
```

**db/migrate/2023xxxxxxx_create_bookings.rb**
```ruby
class CreateBookings < ActiveRecord::Migration[7.0]
  def change
    create_table :bookings do |t|
      t.references :user, null: false, foreign_key: true
      t.references :show, null: false, foreign_key: true

      t.timestamps
    end
  end
end
```

**db/migrate/2023xxxxxxx_create_corporate_events.rb**
```ruby
class CreateCorporateEvents < ActiveRecord::Migration[7.0]
  def change
    create_table :corporate_events do |t|
      t.references :show, null: false, foreign_key: true
      t.string :company, null: false

      t.timestamps
    end
  end
end
```

**db/migrate/2023xxxxxxx_create_private_parties.rb**
```ruby
class CreatePrivateParties < ActiveRecord::Migration[7.0]
  def change
    create_table :private_parties do |t|
      t.references :show, null: false, foreign_key: true
      t.string :guest_name, null: false

      t.timestamps
    end
  end
end
```
