"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Develop a Ruby on Rails model to manage student registrations for short-term courses in brokerage, specifically for the Kigali Institute's offerings.
Generated: DETERMINISTIC_98c7667faabec7f3
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/models/student_registration.rb

class StudentRegistration < ApplicationRecord
  # Associations
  # Assuming there are models such as `Student` and `Course` linked to registrations
  belongs_to :student
  belongs_to :course

  # Validations
  validates :student_id, presence: true
  validates :course_id, presence: true
  validates :registration_date, presence: true
  validate :course_availability

  # Callbacks
  before_create :check_duplicate_registration

  # Scopes
  scope :recent, -> { order(registration_date: :desc) }

  # Custom methods

  # Check if the course has available slots
  def course_availability
    if course.present? && course.remaining_slots <= 0
      errors.add(:course, "is fully booked")
    end
  end

  # Ensure a student cannot register for the same course twice
  def check_duplicate_registration
    existing_registration = StudentRegistration.where(student_id: student_id, course_id: course_id).exists?
    if existing_registration
      errors.add(:base, "Student is already registered for this course")
      throw(:abort)
    end
  end
end

# db/migrate/<timestamp>_create_student_registrations.rb

class CreateStudentRegistrations < ActiveRecord::Migration[6.1]
  def change
    create_table :student_registrations do |t|
      t.references :student, null: false, foreign_key: true
      t.references :course, null: false, foreign_key: true
      t.date :registration_date, null: false

      t.timestamps
    end
  end
end

# app/models/student.rb

class Student < ApplicationRecord
  # Associations
  has_many :student_registrations
  has_many :courses, through: :student_registrations

  # Validations
  validates :name, presence: true
  validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }
end

# app/models/course.rb

class Course < ApplicationRecord
  # Associations
  has_many :student_registrations
  has_many :students, through: :student_registrations

  # Validations
  validates :title, presence: true
  validates :description, presence: true
  validates :max_slots, presence: true, numericality: { only_integer: true, greater_than: 0 }

  # Custom methods

  # Calculate remaining slots
  def remaining_slots
    max_slots - student_registrations.count
  end
end
```
