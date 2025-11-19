"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Develop a Ruby on Rails controller action that handles donations for the Amir International Charity Organization, ensuring it validates donor input and updates the database accordingly.
Generated: DETERMINISTIC_d4508e76bb57ce7e
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/donations_controller.rb

class DonationsController < ApplicationController
  # POST /donations
  # Handles the creation of a new donation
  def create
    @donation = Donation.new(donation_params)

    # Validate the donation and save it to the database
    if @donation.save
      # Respond with a success message and the created donation
      render json: { message: 'Donation successfully created', donation: @donation }, status: :created
    else
      # Respond with error messages if validation fails
      render json: { errors: @donation.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  # Strong parameters to prevent mass assignment vulnerability
  def donation_params
    params.require(:donation).permit(:donor_name, :amount, :email, :message)
  end
end
```

```ruby
# app/models/donation.rb

class Donation < ApplicationRecord
  # Validations for the Donation model
  validates :donor_name, presence: true
  validates :amount, presence: true, numericality: { greater_than: 0 }
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :message, length: { maximum: 500 }, allow_blank: true
end
```

```ruby
# db/migrate/20230101000000_create_donations.rb

class CreateDonations < ActiveRecord::Migration[6.1]
  def change
    create_table :donations do |t|
      t.string :donor_name, null: false
      t.decimal :amount, precision: 10, scale: 2, null: false
      t.string :email, null: false
      t.text :message

      t.timestamps
    end
    
    # Index for faster lookups by email
    add_index :donations, :email
  end
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  # Define the route for creating a donation
  resources :donations, only: [:create]
end
```
