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
  # Validations to ensure data integrity
  validates :name, presence: true, uniqueness: true
  validates :description, presence: true
  validates :schedule, presence: true
  validates :capacity, presence: true, numericality: { greater_than: 0 }

  # Associations
  has_many :volunteers, dependent: :destroy
  has_many :assignments, dependent: :destroy

  # Scopes for common queries
  scope :active, -> { where(active: true) }
  scope :full, -> { where("capacity <= (SELECT COUNT(*) FROM volunteers WHERE volunteer_program_id = volunteer_programs.id)") }

  # Instance method to check if the program is full
  def full?
    volunteers.count >= capacity
  end

  # Instance method to add a volunteer to the program
  def add_volunteer(volunteer)
    if full?
      errors.add(:base, "Volunteer program is full")
      false
    else
      volunteers << volunteer
    end
  end

  # Instance method to remove a volunteer from the program
  def remove_volunteer(volunteer)
    if volunteers.include?(volunteer)
      volunteers.delete(volunteer)
    else
      errors.add(:base, "Volunteer not found in this program")
      false
    end
  end

  # Method to retrieve a list of volunteers in the program
  def volunteer_list
    volunteers.includes(:user).map(&:user)
  end
end
```

```ruby
# app/models/volunteer.rb

class Volunteer < ApplicationRecord
  # Validations to ensure volunteer data integrity
  validates :name, presence: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }

  # Associations
  belongs_to :volunteer_program

  # Instance method to get the volunteer's program status
  def status
    volunteer_program.active? ? "Active" : "Inactive"
  end
end
```

```ruby
# app/models/assignment.rb

class Assignment < ApplicationRecord
  # Validations to ensure assignment data integrity
  validates :date, presence: true
  validates :task, presence: true

  # Associations
  belongs_to :volunteer
  belongs_to :volunteer_program

  # Method to mark the assignment as completed
  def complete
    update(completed: true)
  end
end
```

```ruby
# db/migrate/XXXX_create_volunteer_programs.rb

class CreateVolunteerPrograms < ActiveRecord::Migration[6.1]
  def change
    create_table :volunteer_programs do |t|
      t.string :name, null: false
      t.text :description, null: false
      t.string :schedule, null: false
      t.integer :capacity, null: false
      t.boolean :active, default: true

      t.timestamps
    end
    add_index :volunteer_programs, :name, unique: true
  end
end
```

```ruby
# db/migrate/XXXX_create_volunteers.rb

class CreateVolunteers < ActiveRecord::Migration[6.1]
  def change
    create_table :volunteers do |t|
      t.string :name, null: false
      t.string :email, null: false
      t.references :volunteer_program, null: false, foreign_key: true

      t.timestamps
    end
  end
end
```

```ruby
# db/migrate/XXXX_create_assignments.rb

class CreateAssignments < ActiveRecord::Migration[6.1]
  def change
    create_table :assignments do |t|
      t.references :volunteer, null: false, foreign_key: true
      t.references :volunteer_program, null: false, foreign_key: true
      t.date :date, null: false
      t.string :task, null: false
      t.boolean :completed, default: false

      t.timestamps
    end
  end
end
```

```ruby
# app/controllers/volunteer_programs_controller.rb

class VolunteerProgramsController < ApplicationController
  before_action :set_volunteer_program, only: [:show, :update, :destroy]

  # GET /volunteer_programs
  def index
    @volunteer_programs = VolunteerProgram.all
    render json: @volunteer_programs
  end

  # GET /volunteer_programs/:id
  def show
    render json: @volunteer_program
  end

  # POST /volunteer_programs
  def create
    @volunteer_program = VolunteerProgram.new(volunteer_program_params)
    if @volunteer_program.save
      render json: @volunteer_program, status: :created
    else
      render json: @volunteer_program.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /volunteer_programs/:id
  def update
    if @volunteer_program.update(volunteer_program_params)
      render json: @volunteer_program
    else
      render json: @volunteer_program.errors, status: :unprocessable_entity
    end
  end

  # DELETE /volunteer_programs/:id
  def destroy
    @volunteer_program.destroy
    head :no_content
  end

  private

  def set_volunteer_program
    @volunteer_program = VolunteerProgram.find(params[:id])
  end

  def volunteer_program_params
    params.require(:volunteer_program).permit(:name, :description, :schedule, :capacity, :active)
  end
end
```
