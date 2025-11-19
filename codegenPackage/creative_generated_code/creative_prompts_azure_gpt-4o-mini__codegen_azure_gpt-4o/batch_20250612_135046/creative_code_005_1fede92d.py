"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Write a Ruby on Rails controller action that handles user registration and login for an online diving equipment store.
Generated: DETERMINISTIC_1fede92d43ef160a
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/users_controller.rb

class UsersController < ApplicationController
  # Handles user registration
  def register
    # Strong parameters to permit only required fields
    user_params = params.require(:user).permit(:name, :email, :password, :password_confirmation)

    # Create a new user
    @user = User.new(user_params)

    # Attempt to save the user to the database
    if @user.save
      # Return success response, e.g., HTTP 201 Created
      render json: { message: 'User registration successful', user: @user }, status: :created
    else
      # Return error response with validation errors
      render json: { message: 'User registration failed', errors: @user.errors.full_messages }, status: :unprocessable_entity
    end
  rescue StandardError => e
    # Catch unexpected errors and return appropriate response
    render json: { message: 'An error occurred during registration', error: e.message }, status: :internal_server_error
  end

  # Handles user login
  def login
    # Find the user based on email
    user = User.find_by(email: params[:email])

    # Authenticate user if they exist
    if user&.authenticate(params[:password])
      # Generate a token (assuming JWT or similar mechanism is used)
      token = JwtService.encode(user_id: user.id)

      # Return success response with user info and token
      render json: { message: 'Login successful', user: user, token: token }, status: :ok
    else
      # Return error response for invalid credentials
      render json: { message: 'Invalid email or password' }, status: :unauthorized
    end
  rescue StandardError => e
    # Catch unexpected errors and return appropriate response
    render json: { message: 'An error occurred during login', error: e.message }, status: :internal_server_error
  end
end

# Note:
# - `User` model is assumed to have `has_secure_password` enabled for password authentication.
# - The `JwtService` is assumed to be a helper module that handles JWT token generation.
```
