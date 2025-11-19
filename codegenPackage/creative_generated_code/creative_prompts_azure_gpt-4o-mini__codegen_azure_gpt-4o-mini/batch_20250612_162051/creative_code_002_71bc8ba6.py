"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Create a Ruby on Rails controller action that handles user login for ShopeeWise, ensuring it checks for existing accounts and redirects to the cart page.
Generated: DETERMINISTIC_71bc8ba6c1ca2589
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/sessions_controller.rb

class SessionsController < ApplicationController
  # POST /login
  # Handles user login for ShopeeWise.
  # Checks for existing accounts and redirects to the cart page on successful login.
  def create
    # Find the user by the provided email
    @user = User.find_by(email: params[:email])

    # Check if the user exists and if the password is correct
    if @user && @user.authenticate(params[:password])
      # Log the user in by setting the user_id in the session
      session[:user_id] = @user.id
      
      # Redirect to the cart page
      redirect_to cart_path, notice: 'Successfully logged in!'
    else
      # Handle invalid login attempts
      flash.now[:alert] = 'Invalid email or password. Please try again.'
      render :new
    end
  rescue StandardError => e
    # Log the error for further investigation
    logger.error "Login error: #{e.message}"
    flash.now[:alert] = 'An error occurred while trying to log you in. Please try again later.'
    render :new
  end

  # DELETE /logout
  # Logs out the user by clearing the session
  def destroy
    session[:user_id] = nil
    redirect_to root_path, notice: 'Successfully logged out.'
  end
end
```

```ruby
# app/models/user.rb

class User < ApplicationRecord
  # Include default devise modules if using Devise, or use bcrypt for password handling
  has_secure_password

  # Validations for user attributes
  validates :email, presence: true, uniqueness: true
  validates :password, presence: true, length: { minimum: 6 }
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  # Define routes for sessions (login and logout)
  get 'login', to: 'sessions#new'
  post 'login', to: 'sessions#create'
  delete 'logout', to: 'sessions#destroy'
  
  # Define route for cart
  get 'cart', to: 'cart#index'
  
  # Root path
  root 'home#index'
end
```

```erb
<!-- app/views/sessions/new.html.erb -->

<h1>Login</h1>

<%= form_with(url: login_path, local: true) do |form| %>
  <% if flash[:alert] %>
    <div class="alert alert-danger"><%= flash[:alert] %></div>
  <% end %>

  <div class="form-group">
    <%= form.label :email %>
    <%= form.email_field :email, class: 'form-control', required: true %>
  </div>

  <div class="form-group">
    <%= form.label :password %>
    <%= form.password_field :password, class: 'form-control', required: true %>
  </div>

  <%= form.submit 'Login', class: 'btn btn-primary' %>
<% end %>
```
