"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Develop a Ruby on Rails application that connects to the PerúMakers database to manage community maker projects.
Generated: DETERMINISTIC_cf65bf4c477f7e47
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**PerúMakers Community Maker Projects Application**

### Database Configuration

```ruby
# config/database.yml
default: &default
  adapter: postgresql
  encoding: unicode
  host: localhost
  username: peru_makers_user
  password: peru_makers_password

development:
  <<: *default
  database: peru_makers_development

test:
  <<: *default
  database: peru_makers_test

production:
  <<: *default
  database: peru_makers_production
  username: peru_makers
  password: <%= ENV['PERU_MAKERS_DATABASE_PASSWORD'] %>
```

### Project Model

```ruby
# app/models/project.rb
class Project < ApplicationRecord
  # Associations
  has_many :makers, through: :project_makers
  has_many :project_makers, dependent: :destroy

  # Validations
  validates :name, presence: true
  validates :description, presence: true

  # Scopes
  scope :active, -> { where(active: true) }
end
```

### Maker Model

```ruby
# app/models/maker.rb
class Maker < ApplicationRecord
  # Associations
  has_many :projects, through: :project_makers
  has_many :project_makers, dependent: :destroy

  # Validations
  validates :name, presence: true
  validates :email, presence: true, uniqueness: true

  # Scopes
  scope :verified, -> { where(verified: true) }
end
```

### Project Maker Model

```ruby
# app/models/project_maker.rb
class ProjectMaker < ApplicationRecord
  # Associations
  belongs_to :project
  belongs_to :maker

  # Validations
  validates :project_id, presence: true
  validates :maker_id, presence: true
  validates :role, presence: true

  # Enum for role
  enum role: { leader: 1, member: 2 }
end
```

### Projects Controller

```ruby
# app/controllers/projects_controller.rb
class ProjectsController < ApplicationController
  before_action :set_project, only: [:show, :edit, :update, :destroy]

  # GET /projects
  def index
    @projects = Project.active
  end

  # GET /projects/:id
  def show
    @makers = @project.makers
  end

  # GET /projects/new
  def new
    @project = Project.new
  end

  # GET /projects/:id/edit
  def edit; end

  # POST /projects
  def create
    @project = Project.new(project_params)

    if @project.save
      redirect_to @project, notice: 'Project was successfully created.'
    else
      render :new
    end
  end

  # PATCH/PUT /projects/:id
  def update
    if @project.update(project_params)
      redirect_to @project, notice: 'Project was successfully updated.'
    else
      render :edit
    end
  end

  # DELETE /projects/:id
  def destroy
    @project.destroy
    redirect_to projects_url, notice: 'Project was successfully destroyed.'
  end

  private

  def set_project
    @project = Project.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to projects_url, notice: 'Project not found.'
  end

  def project_params
    params.require(:project).permit(:name, :description, :active)
  end
end
```

### Makers Controller

```ruby
# app/controllers/makers_controller.rb
class MakersController < ApplicationController
  before_action :set_maker, only: [:show, :edit, :update, :destroy]

  # GET /makers
  def index
    @makers = Maker.verified
  end

  # GET /makers/:id
  def show
    @projects = @maker.projects
  end

  # GET /makers/new
  def new
    @maker = Maker.new
  end

  # GET /makers/:id/edit
  def edit; end

  # POST /makers
  def create
    @maker = Maker.new(maker_params)

    if @maker.save
      redirect_to @maker, notice: 'Maker was successfully created.'
    else
      render :new
    end
  end

  # PATCH/PUT /makers/:id
  def update
    if @maker.update(maker_params)
      redirect_to @maker, notice: 'Maker was successfully updated.'
    else
      render :edit
    end
  end

  # DELETE /makers/:id
  def destroy
    @maker.destroy
    redirect_to makers_url, notice: 'Maker was successfully destroyed.'
  end

  private

  def set_maker
    @maker = Maker.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to makers_url, notice: 'Maker not found.'
  end

  def maker_params
    params.require(:maker).permit(:name, :email, :verified)
  end
end
```

### Routes

```ruby
# config/routes.rb
Rails.application.routes.draw do
  resources :projects
  resources :makers

  root 'projects#index'
end
```

### Migration

```ruby
# db/migrate/20230916134758_create_projects.rb
class CreateProjects < ActiveRecord::Migration[7.0]
  def change
    create_table :projects do |t|
      t.string :name
      t.text :description
      t.boolean :active, default: true

      t.timestamps
    end
  end
end
```

```ruby
# db/migrate/20230916134801_create_makers.rb
class CreateMakers < ActiveRecord::Migration[7.0]
  def change
    create_table :makers do |t|
      t.string :name
      t.string :email
      t.boolean :verified, default: false

      t.timestamps
    end

    add_index :makers, :email, unique: true
  end
end
```

```ruby
# db/migrate/20230916134804_create_project_makers.rb
class CreateProjectMakers < ActiveRecord::Migration[7.0]
  def change
    create_table :project_makers do |t|
      t.references :project, null: false, foreign_key: true
      t.references :maker, null: false, foreign_key: true
      t.integer :role

      t.timestamps
    end
  end
end
```

### Seeds

```ruby
# db/seeds.rb
Project.create(name: 'Project 1', description: 'Description 1')
Maker.create(name: 'Maker 1', email: 'maker1@example.com', verified: true)

project = Project.first
maker = Maker.first

ProjectMaker.create(project: project, maker: maker, role: :leader)
```
