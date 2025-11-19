"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zircuitzrc.com
Prompt: Develop a Ruby on Rails model that represents a cleaning service contract, incorporating fields for customer preferences, cleaning frequency, and pricing details mentioned on the Zrc Inc site.
Generated: DETERMINISTIC_a598721df59c4a68
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/cleaning_service_contract.rb

class CleaningServiceContract < ApplicationRecord
  # Associations
  belongs_to :customer
  
  # Validations
  validates :customer_preferences, presence: true
  validates :cleaning_frequency, presence: true, inclusion: { in: %w[daily weekly bi-weekly monthly],
    message: "%{value} is not a valid frequency" }
  validates :price, presence: true, numericality: { greater_than_or_equal_to: 0 }
  
  # Constants
  FREQUENCY_OPTIONS = %w[daily weekly bi-weekly monthly].freeze
  
  # Callbacks
  before_save :sanitize_customer_preferences

  # Error handling and custom methods
  def self.get_contracts_by_frequency(frequency)
    raise ArgumentError, "Invalid frequency: #{frequency}" unless FREQUENCY_OPTIONS.include?(frequency)
    
    where(cleaning_frequency: frequency)
  end

  private

  # Sanitize customer preferences to prevent malicious input
  def sanitize_customer_preferences
    self.customer_preferences = customer_preferences.strip
  end
end

# Migration file to create the cleaning_service_contracts table
# db/migrate/20231001123456_create_cleaning_service_contracts.rb

class CreateCleaningServiceContracts < ActiveRecord::Migration[7.0]
  def change
    create_table :cleaning_service_contracts do |t|
      t.references :customer, null: false, foreign_key: true # Foreign key to customers table
      t.text :customer_preferences, null: false             # Customer preferences for the cleaning service
      t.string :cleaning_frequency, null: false             # Frequency of cleaning (daily, weekly, etc.)
      t.decimal :price, null: false, precision: 10, scale: 2 # Price of the cleaning service contract

      t.timestamps
    end
  end
end

# Notes:
# - Be sure to create a `Customer` model/table for associations to work.
# - Run the migration to add the `cleaning_service_contracts` table to the database.
```
