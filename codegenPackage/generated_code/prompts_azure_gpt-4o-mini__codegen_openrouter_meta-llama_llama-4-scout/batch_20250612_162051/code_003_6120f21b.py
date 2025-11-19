"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: Develop a Ruby on Rails application that tracks dietary habits and provides feedback on managing diabetes, inspired by the diabetes care strategies outlined on the Green Apples e-Rx Clinic page.
Generated: DETERMINISTIC_6120f21bba9d0bea
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**config/application.rb**
```ruby
module DietaryHabitsTracker
  class Application < Rails::Application
    # Configure the default encoding used in templates for Ruby files.
    config.encoding = 'utf-8'

    # Configure sensitive parameters which will be filtered from the log file.
    config.filter_parameters += [:password, :password_confirmation]

    # Use the lowest rank log level to ensure that even prod-like deploys
    # don't create unexpected issues.
    config.log_level = :info

    # Precompile additional assets.
    # application.js, application.css, and all non-JS/CSS in app/assets folder are already added.
    # config.assets.precompile += %w( admin.js admin.css )

    # Enable serving of images, stylesheets, and JavaScript files from an assets pipeline.
    config.assets.enabled = true

    # Version of your assets, change this if you want to expire all your assets.
    config.assets.version = '1.0'

    # Configure generators
    config.generators do |g|
      g.orm :active_record
      g.test_framework :rspec
    end
  end
end
```

**config/database.yml**
```yml
default: &default
  adapter: postgresql
  encoding: unicode
  host: localhost
  username: dietary_habits_tracker
  password: dietary_habits_tracker

development:
  <<: *default
  database: dietary_habits_tracker_development

test:
  <<: *default
  database: dietary_habits_tracker_test

production:
  <<: *default
  database: dietary_habits_tracker_production
  username: dietary_habits_tracker
  password: <%= ENV['DIETARY_HABITS_TRACKER_DATABASE_PASSWORD'] %>
```

**config/routes.rb**
```ruby
Rails.application.routes.draw do
  resources :users do
    resources :food_intakes
  end

  resources :foods

  get '/dashboard', to: 'users#dashboard'
  get '/feedback', to: 'users#feedback'

  root 'welcome#index'
end
```

**app/models/user.rb**
```ruby
class User < ApplicationRecord
  has_many :food_intakes
  has_many :foods, through: :food_intakes

  validates :name, :email, presence: true
  validates :email, uniqueness: true

  def dashboard
    # Display user's food intake and feedback
  end

  def feedback
    # Provide feedback based on user's dietary habits
  end
end
```

**app/models/food.rb**
```ruby
class Food < ApplicationRecord
  has_many :food_intakes
  has_many :users, through: :food_intakes

  validates :name, :carbohydrates, :protein, :fat, presence: true

  def carb_ratio
    carbohydrates / (carbohydrates + protein + fat).to_f
  end
end
```

**app/models/food_intake.rb**
```ruby
class FoodIntake < ApplicationRecord
  belongs_to :user
  belongs_to :food

  validates :user_id, :food_id, :consumption_time, presence: true

  def calculate_carb_load
    food.carb_ratio * food.carbohydrates
  end
end
```

**app/controllers/users_controller.rb**
```ruby
class UsersController < ApplicationController
  before_action :set_user, only: [:show, :edit, :update, :destroy]

  def index
    @users = User.all
  end

  def show
    @user = User.find(params[:id])
  end

  def new
    @user = User.new
  end

  def edit; end

  def create
    @user = User.new(user_params)

    if @user.save
      redirect_to @user, notice: 'User was successfully created.'
    else
      render :new
    end
  end

  def update
    if @user.update(user_params)
      redirect_to @user, notice: 'User was successfully updated.'
    else
      render :edit
    end
  end

  def destroy
    @user.destroy
    redirect_to users_url, notice: 'User was successfully destroyed.'
  end

  def dashboard
    @user = current_user
    @food_intakes = @user.food_intakes
  end

  def feedback
    @user = current_user
    # Provide feedback based on user's dietary habits
  end

  private

  def set_user
    @user = User.find(params[:id])
  end

  def user_params
    params.require(:user).permit(:name, :email)
  end
end
```

**app/controllers/food_intakes_controller.rb**
```ruby
class FoodIntakesController < ApplicationController
  before_action :set_food_intake, only: [:show, :edit, :update, :destroy]

  def index
    @food_intakes = FoodIntake.all
  end

  def show; end

  def new
    @food_intake = FoodIntake.new
  end

  def edit; end

  def create
    @food_intake = FoodIntake.new(food_intake_params)

    if @food_intake.save
      redirect_to @food_intake, notice: 'Food intake was successfully created.'
    else
      render :new
    end
  end

  def update
    if @food_intake.update(food_intake_params)
      redirect_to @food_intake, notice: 'Food intake was successfully updated.'
    else
      render :edit
    end
  end

  def destroy
    @food_intake.destroy
    redirect_to food_intakes_url, notice: 'Food intake was successfully destroyed.'
  end

  private

  def set_food_intake
    @food_intake = FoodIntake.find(params[:id])
  end

  def food_intake_params
    params.require(:food_intake).permit(:user_id, :food_id, :consumption_time)
  end
end
```

**db/migrate/20230916134758_create_users.rb**
```ruby
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :name
      t.string :email

      t.timestamps
    end
  end
end
```

**db/migrate/20230916134801_create_foods.rb**
```ruby
class CreateFoods < ActiveRecord::Migration[7.0]
  def change
    create_table :foods do |t|
      t.string :name
      t.float :carbohydrates
      t.float :protein
      t.float :fat

      t.timestamps
    end
  end
end
```

**db/migrate/20230916134804_create_food_intakes.rb**
```ruby
class CreateFoodIntakes < ActiveRecord::Migration[7.0]
  def change
    create_table :food_intakes do |t|
      t.references :user, null: false, foreign_key: true
      t.references :food, null: false, foreign_key: true
      t.datetime :consumption_time

      t.timestamps
    end
  end
end
```
