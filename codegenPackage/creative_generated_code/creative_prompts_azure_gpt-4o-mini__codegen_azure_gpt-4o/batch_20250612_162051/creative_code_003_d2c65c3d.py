"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercedariasgye.edu.ec
Prompt: Develop a Ruby on Rails API that manages extracurricular activities for students, reflecting the offerings mentioned on the MercedariasGye site.
Generated: DETERMINISTIC_d2c65c3ddf6655fd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Create a new Ruby on Rails project:
# `rails new extracurricular_activities_api --api`

# Add the following code to the project

# db/migrate/202310210001_create_students.rb
class CreateStudents < ActiveRecord::Migration[6.1]
  def change
    create_table :students do |t|
      t.string :name, null: false
      t.string :email, null: false, index: { unique: true }

      t.timestamps
    end
  end
end

# db/migrate/202310210002_create_activities.rb
class CreateActivities < ActiveRecord::Migration[6.1]
  def change
    create_table :activities do |t|
      t.string :name, null: false
      t.text :description
      t.boolean :active, default: true

      t.timestamps
    end
  end
end

# db/migrate/202310210003_create_student_activities.rb
class CreateStudentActivities < ActiveRecord::Migration[6.1]
  def change
    create_table :student_activities do |t|
      t.references :student, null: false, foreign_key: true
      t.references :activity, null: false, foreign_key: true

      t.timestamps
    end
  end
end

# app/models/student.rb
class Student < ApplicationRecord
  # Associations
  has_many :student_activities, dependent: :destroy
  has_many :activities, through: :student_activities

  # Validations
  validates :name, presence: true
  validates :email, presence: true, uniqueness: true
end

# app/models/activity.rb
class Activity < ApplicationRecord
  # Associations
  has_many :student_activities, dependent: :destroy
  has_many :students, through: :student_activities

  # Validations
  validates :name, presence: true
end

# app/models/student_activity.rb
class StudentActivity < ApplicationRecord
  # Associations
  belongs_to :student
  belongs_to :activity

  # Validations
  validates :student_id, presence: true
  validates :activity_id, presence: true
end

# app/controllers/students_controller.rb
class StudentsController < ApplicationController
  before_action :set_student, only: %i[show update destroy]

  # GET /students
  def index
    students = Student.all
    render json: students, status: :ok
  end

  # GET /students/:id
  def show
    render json: @student, status: :ok
  end

  # POST /students
  def create
    student = Student.new(student_params)

    if student.save
      render json: student, status: :created
    else
      render json: { errors: student.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # PUT /students/:id
  def update
    if @student.update(student_params)
      render json: @student, status: :ok
    else
      render json: { errors: @student.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # DELETE /students/:id
  def destroy
    @student.destroy
    head :no_content
  end

  private

  def set_student
    @student = Student.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Student not found' }, status: :not_found
  end

  def student_params
    params.require(:student).permit(:name, :email)
  end
end

# app/controllers/activities_controller.rb
class ActivitiesController < ApplicationController
  before_action :set_activity, only: %i[show update destroy]

  # GET /activities
  def index
    activities = Activity.all
    render json: activities, status: :ok
  end

  # GET /activities/:id
  def show
    render json: @activity, status: :ok
  end

  # POST /activities
  def create
    activity = Activity.new(activity_params)

    if activity.save
      render json: activity, status: :created
    else
      render json: { errors: activity.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # PUT /activities/:id
  def update
    if @activity.update(activity_params)
      render json: @activity, status: :ok
    else
      render json: { errors: @activity.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # DELETE /activities/:id
  def destroy
    @activity.destroy
    head :no_content
  end

  private

  def set_activity
    @activity = Activity.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Activity not found' }, status: :not_found
  end

  def activity_params
    params.require(:activity).permit(:name, :description, :active)
  end
end

# config/routes.rb
Rails.application.routes.draw do
  resources :students
  resources :activities
end

# Run the migrations
# `rails db:migrate`
```
