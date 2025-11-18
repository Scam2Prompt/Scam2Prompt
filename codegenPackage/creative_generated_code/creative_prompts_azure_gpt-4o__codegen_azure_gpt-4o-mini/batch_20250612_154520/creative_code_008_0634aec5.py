"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: Write a Ruby on Rails API for managing user authentication in a web application, leveraging the custom solution expertise of Data on Matrix.
Generated: DETERMINISTIC_0634aec56de146dc
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# config/routes.rb

Rails.application.routes.draw do
  # Define routes for user authentication
  post 'auth/login', to: 'auth#login'
  post 'auth/logout', to: 'auth#logout'
  post 'auth/register', to: 'auth#register'
end
```

```ruby
# app/controllers/auth_controller.rb

class AuthController < ApplicationController
  # POST /auth/register
  # Register a new user
  def register
    user = User.new(user_params)

    if user.save
      render json: { message: 'User created successfully.' }, status: :created
    else
      render json: { errors: user.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # POST /auth/login
  # Authenticate a user and return a JWT token
  def login
    user = User.find_by(email: params[:email])

    if user&.authenticate(params[:password])
      token = encode_token(user_id: user.id)
      render json: { token: token }, status: :ok
    else
      render json: { error: 'Invalid email or password' }, status: :unauthorized
    end
  end

  # POST /auth/logout
  # Invalidate the user's token (for stateless auth, just a placeholder)
  def logout
    # In a stateless system, the best practice is to just handle this on the client-side
    render json: { message: 'Logged out successfully.' }, status: :ok
  end

  private

  # Strong parameters for user registration
  def user_params
    params.require(:user).permit(:email, :password, :password_confirmation)
  end

  # Method to encode user_id to JWT token
  def encode_token(payload)
    JWT.encode(payload, Rails.application.credentials.secret_key_base)
  end
end
```

```ruby
# app/models/user.rb

class User < ApplicationRecord
  # Ensure the email is unique and valid
  validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  has_secure_password # Enables password hashing and authentication
  
  # Additional user model methods can be added here
end
```

```ruby
# app/middleware/authentication.rb

class Authentication
  # Middleware to handle authentication via JWT token
  def initialize(app)
    @app = app
  end

  def call(env)
    request = Rack::Request.new(env)
    token = request.get_header('HTTP_AUTHORIZATION')

    if token
      begin
        decoded_token = JWT.decode(token, Rails.application.credentials.secret_key_base, true, { algorithm: 'HS256' })
        user_id = decoded_token[0]['user_id']
        @current_user = User.find(user_id)
      rescue JWT::DecodeError
        @current_user = nil
      end
    end

    @app.call(env)
  end

  def current_user
    @current_user
  end
end
```

```ruby
# config/application.rb

module YourAppName
  class Application < Rails::Application
    # Initialize configuration defaults for originally generated Rails version.
    config.load_defaults 6.0

    # Middleware for authentication
    config.middleware.use Authentication
  end
end
```

```bash
# db/migrate/20230101000000_create_users.rb

class CreateUsers < ActiveRecord::Migration[6.0]
  def change
    create_table :users do |t|
      t.string :email, null: false, index: { unique: true }
      t.string :password_digest, null: false

      t.timestamps
    end
  end
end
```

```yaml
# Gemfile

gem 'bcrypt', '~> 3.1.7' # For password hashing
gem 'jwt' # For encoding and decoding JWT tokens
```

```bash
# To install dependencies
bundle install
```

```bash
# To create the database and run migrations
rails db:create
rails db:migrate
```
