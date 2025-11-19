"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Develop a Ruby on Rails model that represents the Armourers & Brasiers' Company’s charitable activities, including attributes for funding amounts and project descriptions.
Generated: DETERMINISTIC_5fbe1c58de851730
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/charitable_activity.rb

class CharitableActivity < ApplicationRecord
  # Validations
  validates :project_name, presence: true, length: { maximum: 255 }
  validates :description, presence: true, length: { maximum: 1000 }
  validates :funding_amount, presence: true, numericality: { greater_than_or_equal_to: 0 }

  # Scopes
  scope :recent, -> { order(created_at: :desc) }
  scope :high_funding, ->(threshold) { where("funding_amount > ?", threshold) }

  # Instance Methods
  def formatted_funding_amount
    ActionController::Base.helpers.number_to_currency(funding_amount)
  end

  def summary
    "#{project_name}: #{description.truncate(100)}"
  end
end

# Database migration: This should be generated separately via Rails migrations
# Example migration file: db/migrate/20231016120000_create_charitable_activities.rb

class CreateCharitableActivities < ActiveRecord::Migration[6.1]
  def change
    create_table :charitable_activities do |t|
      # Columns for the model
      t.string :project_name, null: false, limit: 255
      t.text :description, null: false, limit: 1000
      t.decimal :funding_amount, precision: 15, scale: 2, null: false, default: 0.0

      t.timestamps # Adds created_at and updated_at fields
    end
  end
end
```
