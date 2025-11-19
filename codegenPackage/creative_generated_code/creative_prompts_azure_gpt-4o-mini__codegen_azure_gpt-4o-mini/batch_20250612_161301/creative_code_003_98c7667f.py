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
  belongs_to :student
  belongs_to :course

  # Validations
  validates :student_id, presence: true
  validates :course_id, presence: true
  validates :registration_date, presence: true
  validates :status, inclusion: { in: ['pending', 'confirmed', 'cancelled'] }

  # Default status for new registrations
  before_create :set_default_status

  # Scopes for querying registrations
  scope :confirmed, -> { where(status: 'confirmed') }
  scope :pending, -> { where(status: 'pending') }
  scope :cancelled, -> { where(status: 'cancelled') }

  # Instance methods

  # Set default registration status to 'pending'
  def set_default_status
    self.status ||= 'pending'
  end

  # Class methods

  # Fetch all registrations for a specific course
  def self.for_course(course_id)
    where(course_id: course_id)
  end

  # Fetch all registrations for a specific student
  def self.for_student(student_id)
    where(student_id: student_id)
  end
end
```

```ruby
# db/migrate/20230301000000_create_student_registrations.rb

class CreateStudentRegistrations < ActiveRecord::Migration[6.0]
  def change
    create_table :student_registrations do |t|
      t.references :student, null: false, foreign_key: true
      t.references :course, null: false, foreign_key: true
      t.datetime :registration_date, null: false
      t.string :status, default: 'pending'

      t.timestamps
    end
  end
end
```

```ruby
# app/models/student.rb

class Student < ApplicationRecord
  # Associations
  has_many :student_registrations, dependent: :destroy
  has_many :courses, through: :student_registrations

  # Validations
  validates :name, presence: true
  validates :email, presence: true, uniqueness: true
end
```

```ruby
# app/models/course.rb

class Course < ApplicationRecord
  # Associations
  has_many :student_registrations, dependent: :destroy
  has_many :students, through: :student_registrations

  # Validations
  validates :title, presence: true
  validates :description, presence: true
  validates :start_date, presence: true
  validates :end_date, presence: true
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  resources :students do
    resources :student_registrations
  end

  resources :courses do
    resources :student_registrations
  end
end
```

```ruby
# app/controllers/student_registrations_controller.rb

class StudentRegistrationsController < ApplicationController
  before_action :set_student_registration, only: [:show, :update, :destroy]

  # GET /students/:student_id/student_registrations
  def index
    @student_registrations = StudentRegistration.where(student_id: params[:student_id])
    render json: @student_registrations
  end

  # POST /students/:student_id/student_registrations
  def create
    @student_registration = StudentRegistration.new(student_registration_params)
    @student_registration.student_id = params[:student_id]
    @student_registration.registration_date = Time.current

    if @student_registration.save
      render json: @student_registration, status: :created
    else
      render json: @student_registration.errors, status: :unprocessable_entity
    end
  end

  # GET /students/:student_id/student_registrations/:id
  def show
    render json: @student_registration
  end

  # PATCH/PUT /students/:student_id/student_registrations/:id
  def update
    if @student_registration.update(student_registration_params)
      render json: @student_registration
    else
      render json: @student_registration.errors, status: :unprocessable_entity
    end
  end

  # DELETE /students/:student_id/student_registrations/:id
  def destroy
    @student_registration.destroy
    head :no_content
  end

  private

  # Set the student registration based on the ID
  def set_student_registration
    @student_registration = StudentRegistration.find(params[:id])
  end

  # Strong parameters for student registration
  def student_registration_params
    params.require(:student_registration).permit(:course_id, :status)
  end
end
```
