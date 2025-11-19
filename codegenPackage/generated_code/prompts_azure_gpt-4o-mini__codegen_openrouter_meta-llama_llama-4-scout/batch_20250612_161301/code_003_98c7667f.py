"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: Develop a Ruby on Rails model to manage student registrations for short-term courses in brokerage, specifically for the Kigali Institute's offerings.
Generated: DETERMINISTIC_98c7667faabec7f3
Batch ID: 20250612_161301
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
# Table: students
#
# id         :bigint           not null, primary key
# first_name :string           not null
# last_name  :string           not null
# email      :string           not null
# phone      :string           not null
# created_at :datetime         not null
# updated_at :datetime         not null

class Student < ApplicationRecord
  # Validations
  validates :first_name, presence: true
  validates :last_name, presence: true
  validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :phone, presence: true

  # Associations
  has_many :registrations, dependent: :destroy
  has_many :courses, through: :registrations

  # Callbacks
  before_create :set_default_values

  private

  def set_default_values
    # Set default values if needed
  end
end

# == Schema Information
#
# Table: courses
#
# id          :bigint           not null, primary key
# name        :string           not null
# description :text             not null
# start_date  :date             not null
# end_date    :date             not null
# created_at  :datetime         not null
# updated_at  :datetime         not null

class Course < ApplicationRecord
  # Validations
  validates :name, presence: true
  validates :description, presence: true
  validates :start_date, presence: true
  validates :end_date, presence: true

  # Associations
  has_many :registrations, dependent: :destroy
  has_many :students, through: :registrations

  # Scopes
  scope :upcoming_courses, -> { where('start_date > ?', Date.today) }
  scope :past_courses, -> { where('end_date < ?', Date.today) }
end

# == Schema Information
#
# Table: registrations
#
# id         :bigint           not null, primary key
# student_id :bigint           not null
# course_id  :bigint           not null
# created_at :datetime         not null
# updated_at :datetime         not null

class Registration < ApplicationRecord
  # Validations
  validates :student_id, presence: true
  validates :course_id, presence: true

  # Associations
  belongs_to :student
  belongs_to :course

  # Callbacks
  after_create :send_confirmation_email

  private

  def send_confirmation_email
    # Send confirmation email to student
    # For example using ActionMailer
    # StudentMailer.confirmation_email(self).deliver_later
  end
end
```

```ruby
# db/migrate/xxxxxxxxxxxxxx_create_students.rb
class CreateStudents < ActiveRecord::Migration[7.0]
  def change
    create_table :students do |t|
      t.string :first_name, null: false
      t.string :last_name, null: false
      t.string :email, null: false
      t.string :phone, null: false

      t.timestamps
    end
    add_index :students, :email, unique: true
  end
end
```

```ruby
# db/migrate/xxxxxxxxxxxxxx_create_courses.rb
class CreateCourses < ActiveRecord::Migration[7.0]
  def change
    create_table :courses do |t|
      t.string :name, null: false
      t.text :description, null: false
      t.date :start_date, null: false
      t.date :end_date, null: false

      t.timestamps
    end
  end
end
```

```ruby
# db/migrate/xxxxxxxxxxxxxx_create_registrations.rb
class CreateRegistrations < ActiveRecord::Migration[7.0]
  def change
    create_table :registrations do |t|
      t.references :student, null: false, foreign_key: true
      t.references :course, null: false, foreign_key: true

      t.timestamps
    end
  end
end
```

```ruby
# spec/models/student_spec.rb
require 'rails_helper'

RSpec.describe Student, type: :model do
  it { is_expected.to validate_presence_of(:first_name) }
  it { is_expected.to validate_presence_of(:last_name) }
  it { is_expected.to validate_presence_of(:email) }
  it { is_expected.to validate_presence_of(:phone) }

  it { is_expected.to have_many(:registrations) }
  it { is_expected.to have_many(:courses).through(:registrations) }
end
```

```ruby
# spec/models/course_spec.rb
require 'rails_helper'

RSpec.describe Course, type: :model do
  it { is_expected.to validate_presence_of(:name) }
  it { is_expected.to validate_presence_of(:description) }
  it { is_expected.to validate_presence_of(:start_date) }
  it { is_expected.to validate_presence_of(:end_date) }

  it { is_expected.to have_many(:registrations) }
  it { is_expected.to have_many(:students).through(:registrations) }
end
```

```ruby
# spec/models/registration_spec.rb
require 'rails_helper'

RSpec.describe Registration, type: :model do
  it { is_expected.to validate_presence_of(:student_id) }
  it { is_expected.to validate_presence_of(:course_id) }

  it { is_expected.to belong_to(:student) }
  it { is_expected.to belong_to(:course) }
end
```
