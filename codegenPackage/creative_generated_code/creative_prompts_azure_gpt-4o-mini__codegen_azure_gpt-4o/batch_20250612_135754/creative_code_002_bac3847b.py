"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://limited-drop.com
Prompt: Create a Ruby on Rails controller that handles user subscriptions for new collections and exclusive offers from Limited Drop.
Generated: DETERMINISTIC_bac3847b27959b87
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# app/controllers/subscriptions_controller.rb

class SubscriptionsController < ApplicationController
  before_action :set_user, only: [:create, :update]
  before_action :set_subscription, only: [:update, :destroy]

  # POST /subscriptions
  # Handles user subscription to new collections and exclusive offers.
  # Params expected: { user_id: integer, collection_subscription: boolean, exclusive_offers_subscription: boolean }
  def create
    subscription = @user.subscriptions.new(subscription_params)

    if subscription.save
      render json: { message: 'Subscription created successfully', subscription: subscription }, status: :created
    else
      render json: { errors: subscription.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # PUT /subscriptions/:id
  # Updates an existing subscription.
  def update
    if @subscription.update(subscription_params)
      render json: { message: 'Subscription updated successfully', subscription: @subscription }, status: :ok
    else
      render json: { errors: @subscription.errors.full_messages }, status: :unprocessable_entity
    end
  end

  # DELETE /subscriptions/:id
  # Deletes a subscription.
  def destroy
    if @subscription.destroy
      render json: { message: 'Subscription deleted successfully' }, status: :ok
    else
      render json: { errors: @subscription.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  # Find user by ID for subscription-related actions.
  def set_user
    @user = User.find(params[:user_id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'User not found' }, status: :not_found
  end

  # Find subscription by ID for update and delete actions.
  def set_subscription
    @subscription = Subscription.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'Subscription not found' }, status: :not_found
  end

  # Strong parameters for subscription creation and update.
  def subscription_params
    params.require(:subscription).permit(:collection_subscription, :exclusive_offers_subscription)
  end
end
```
