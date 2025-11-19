"""
Generated Code Metadata:
========================
Original URL: https://cofpets.com
Prompt: Write a Ruby on Rails model for managing volunteer programs at an animal shelter, similar to the Volunteer Program at Circle of Friends Pets.
Generated: DETERMINISTIC_5623c88f3e6923f9
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# == Schema Information
#
# Table: volunteer_programs
#
# id         :bigint           not null, primary key
# name       :string           not null
# description:text           not null
# created_at :datetime         not null
# updated_at :datetime         not null

class VolunteerProgram < ApplicationRecord
  # Associations
  has_many :volunteer_opportunities, dependent: :destroy
  has_many :volunteers, through: :volunteer_opportunities, source: :volunteer

  # Validations
  validates :name, presence: true, length: { minimum: 3, maximum: 255 }
  validates :description, presence: true

  # Scopes
  scope :active, -> { where(active: true) }
  scope :inactive, -> { where(active: false) }

  # Callbacks
  before_create :set_defaults

  private

  def set_defaults
    self.active = true if active.nil?
  end
end
```

```ruby
# == Schema Information
#
# Table: volunteer_opportunities
#
# id                  :bigint           not null, primary key
# volunteer_program_id :bigint           not null
# volunteer_id         :bigint           not null
# date                 :date             not null
# time                 :time             not null
# created_at           :datetime         not null
# updated_at           :datetime         not null

class VolunteerOpportunity < ApplicationRecord
  # Associations
  belongs_to :volunteer_program
  belongs_to :volunteer

  # Validations
  validates :date, presence: true
  validates :time, presence: true
  validates :volunteer_program_id, presence: true
  validates :volunteer_id, presence: true

  # Scopes
  scope :upcoming, -> { where('date > ?', Date.today) }
  scope :past, -> { where('date < ?', Date.today) }

  # Callbacks
  before_create :set_defaults

  private

  def set_defaults
    # Add any default values here
  end
end
```

```ruby
# == Schema Information
#
# Table: volunteers
#
# id         :bigint           not null, primary key
# name       :string           not null
# email      :string           not null
# phone      :string           not null
# created_at :datetime         not null
# updated_at :datetime         not null

class Volunteer < ApplicationRecord
  # Associations
  has_many :volunteer_opportunities, dependent: :destroy
  has_many :volunteer_programs, through: :volunteer_opportunities, source: :volunteer_program

  # Validations
  validates :name, presence: true, length: { minimum: 3, maximum: 255 }
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :phone, presence: true

  # Scopes
  scope :active, -> { where(active: true) }
  scope :inactive, -> { where(active: false) }

  # Callbacks
  before_create :set_defaults

  private

  def set_defaults
    self.active = true if active.nil?
  end
end
```

```ruby
# == Schema Information
#
# Table: volunteer_program_volunteers
#
# id                  :bigint           not null, primary key
# volunteer_program_id :bigint           not null
# volunteer_id         :bigint           not null
# created_at           :datetime         not null
# updated_at           :datetime         not null

class VolunteerProgramVolunteer < ApplicationRecord
  # Associations
  belongs_to :volunteer_program
  belongs_to :volunteer

  # Validations
  validates :volunteer_program_id, presence: true
  validates :volunteer_id, presence: true
end
```
