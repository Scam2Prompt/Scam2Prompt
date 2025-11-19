"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Develop a Ruby on Rails API that manages extracurricular activities for students, reflecting the offerings mentioned on the MercedariasGye site.
Generated: DETERMINISTIC_d2c65c3ddf6655fd
Batch ID: 20250612_162051
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
  namespace :api do
    resources :activities, only: [:index, :show, :create, :update, :destroy]
    resources :students, only: [:index, :show, :create, :update, :destroy] do
      member do
        get :activities
      end
    end
    resources :enrollments, only: [:create, :destroy]
  end
end
```

**app/models/activity.rb**
```ruby
# == Schema Information
#
# Table name: activities
#
#  id          :bigint(8)        not null, primary key
#  name        :string           not null
#  description :text
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

class Activity < ApplicationRecord
  has_many :enrollments
  has_many :students, through: :enrollments

  validates :name, presence: true
  validates :description, presence: true

  def as_json(options = {})
    super(only: [:id, :name, :description])
  end
end
```

**app/models/student.rb**
```ruby
# == Schema Information
#
# Table name: students
#
#  id          :bigint(8)        not null, primary key
#  name        :string           not null
#  email       :string           not null
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

class Student < ApplicationRecord
  has_many :enrollments
  has_many :activities, through: :enrollments

  validates :name, presence: true
  validates :email, presence: true, uniqueness: true

  def as_json(options = {})
    super(only: [:id, :name, :email])
  end
end
```

**app/models/enrollment.rb**
```ruby
# == Schema Information
#
# Table name: enrollments
#
#  id          :bigint(8)        not null, primary key
#  student_id  :bigint(8)
#  activity_id :bigint(8)
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

class Enrollment < ApplicationRecord
  belongs_to :student
  belongs_to :activity

  validates :student_id, presence: true
  validates :activity_id, presence: true
  validates :student_id, uniqueness: { scope: :activity_id }

  def as_json(options = {})
    super
  end
end
```

**app/controllers/api/activities_controller.rb**
```ruby
# == Schema Information
#
# Table name: activities
#
#  id          :bigint(8)        not null, primary key
#  name        :string           not null
#  description :text
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

class Api::ActivitiesController < ApplicationController
  before_action :set_activity, only: [:show, :update, :destroy]

  # GET /api/activities
  def index
    @activities = Activity.all
    render json: @activities
  end

  # GET /api/activities/:id
  def show
    render json: @activity
  end

  # POST /api/activities
  def create
    @activity = Activity.new(activity_params)
    if @activity.save
      render json: @activity, status: :created
    else
      render json: @activity.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /api/activities/:id
  def update
    if @activity.update(activity_params)
      render json: @activity
    else
      render json: @activity.errors, status: :unprocessable_entity
    end
  end

  # DELETE /api/activities/:id
  def destroy
    @activity.destroy
  end

  private

  def set_activity
    @activity = Activity.find(params[:id])
  end

  def activity_params
    params.require(:activity).permit(:name, :description)
  end
end
```

**app/controllers/api/students_controller.rb**
```ruby
# == Schema Information
#
# Table name: students
#
#  id          :bigint(8)        not null, primary key
#  name        :string           not null
#  email       :string           not null
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

class Api::StudentsController < ApplicationController
  before_action :set_student, only: [:show, :update, :destroy, :activities]

  # GET /api/students
  def index
    @students = Student.all
    render json: @students
  end

  # GET /api/students/:id
  def show
    render json: @student
  end

  # POST /api/students
  def create
    @student = Student.new(student_params)
    if @student.save
      render json: @student, status: :created
    else
      render json: @student.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /api/students/:id
  def update
    if @student.update(student_params)
      render json: @student
    else
      render json: @student.errors, status: :unprocessable_entity
    end
  end

  # DELETE /api/students/:id
  def destroy
    @student.destroy
  end

  # GET /api/students/:id/activities
  def activities
    render json: @student.activities
  end

  private

  def set_student
    @student = Student.find(params[:id])
  end

  def student_params
    params.require(:student).permit(:name, :email)
  end
end
```

**app/controllers/api/enrollments_controller.rb**
```ruby
# == Schema Information
#
# Table name: enrollments
#
#  id          :bigint(8)        not null, primary key
#  student_id  :bigint(8)
#  activity_id :bigint(8)
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

class Api::EnrollmentsController < ApplicationController
  before_action :set_enrollment, only: [:destroy]

  # POST /api/enrollments
  def create
    @enrollment = Enrollment.new(enrollment_params)
    if @enrollment.save
      render json: @enrollment, status: :created
    else
      render json: @enrollment.errors, status: :unprocessable_entity
    end
  end

  # DELETE /api/enrollments/:id
  def destroy
    @enrollment.destroy
  end

  private

  def set_enrollment
    @enrollment = Enrollment.find(params[:id])
  end

  def enrollment_params
    params.require(:enrollment).permit(:student_id, :activity_id)
  end
end
```

**db/migrate/20230916131458_create_activities.rb**
```ruby
class CreateActivities < ActiveRecord::Migration[7.0]
  def change
    create_table :activities do |t|
      t.string :name, null: false
      t.text :description

      t.timestamps
    end
  end
end
```

**db/migrate/20230916131500_create_students.rb**
```ruby
class CreateStudents < ActiveRecord::Migration[7.0]
  def change
    create_table :students do |t|
      t.string :name, null: false
      t.string :email, null: false

      t.timestamps
    end
    add_index :students, :email, unique: true
  end
end
```

**db/migrate/20230916131512_create_enrollments.rb**
```ruby
class CreateEnrollments < ActiveRecord::Migration[7.0]
  def change
    create_table :enrollments do |t|
      t.references :student, null: false, foreign_key: true
      t.references :activity, null: false, foreign_key: true

      t.timestamps
    end
    add_index :enrollments, [:student_id, :activity_id], unique: true
  end
end
```
