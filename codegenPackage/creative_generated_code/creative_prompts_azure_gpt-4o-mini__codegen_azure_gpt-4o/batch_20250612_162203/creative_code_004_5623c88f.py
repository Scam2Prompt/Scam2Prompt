"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cofpets.com
Prompt: Write a Ruby on Rails model for managing volunteer programs at an animal shelter, similar to the Volunteer Program at Circle of Friends Pets.
Generated: DETERMINISTIC_5623c88f3e6923f9
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/volunteer_program.rb

class VolunteerProgram < ApplicationRecord
  # Associations
  has_many :volunteers, dependent: :destroy
  has_many :events, dependent: :destroy

  # Validations
  validates :name, presence: true, length: { maximum: 100 }
  validates :description, presence: true, length: { maximum: 1000 }
  validates :start_date, presence: true
  validates :end_date, presence: true
  validate :end_date_after_start_date

  # Callbacks
  before_save :sanitize_description

  # Scope for fetching active programs
  scope :active, -> { where("start_date <= ? AND end_date >= ?", Date.current, Date.current) }

  # Instance Methods

  # Check if the program is currently active
  def active?
    start_date <= Date.current && end_date >= Date.current
  end

  private

  # Ensure end_date is after start_date
  def end_date_after_start_date
    if end_date.present? && start_date.present? && end_date <= start_date
      errors.add(:end_date, "must be after the start date")
    end
  end

  # Sanitize description to remove any unwanted characters or scripts
  def sanitize_description
    self.description = ActionController::Base.helpers.sanitize(description)
  end
end
```

```ruby
# db/migrate/20231010120000_create_volunteer_programs.rb

class CreateVolunteerPrograms < ActiveRecord::Migration[6.1]
  def change
    create_table :volunteer_programs do |t|
      t.string :name, null: false, limit: 100
      t.text :description, null: false, limit: 1000
      t.date :start_date, null: false
      t.date :end_date, null: false

      t.timestamps
    end
  end
end
```
