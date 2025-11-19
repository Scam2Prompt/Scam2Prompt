"""
Generated Code Metadata:
========================
Original URL: https://doctorvitaly.pro
Prompt: What are some best practices for storing and managing user consent for personal data processing on a website focused on health and wellness, and how can these be implemented in a backend service using Ruby on Rails?
Generated: DETERMINISTIC_d009cda4906cc275
Batch ID: 20250622_211550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/models/user_consent.rb
class UserConsent < ApplicationRecord
  # Validations to ensure data integrity
  validates :user_id, presence: true
  validates :consent_given, inclusion: { in: [true, false] }
  validates :consent_type, presence: true, inclusion: { in: %w[marketing analytics service] }
  validates :consent_date, presence: true

  # Associations
  belongs_to :user

  # Scopes for querying consents
  scope :given, -> { where(consent_given: true) }
  scope :revoked, -> { where(consent_given: false) }
end

# db/migrate/20231001000000_create_user_consents.rb
class CreateUserConsents < ActiveRecord::Migration[6.1]
  def change
    create_table :user_consents do |t|
      t.references :user, null: false, foreign_key: true
      t.boolean :consent_given, null: false
      t.string :consent_type, null: false
      t.datetime :consent_date, null: false

      t.timestamps
    end
  end
end

# app/controllers/user_consents_controller.rb
class UserConsentsController < ApplicationController
  before_action :set_user_consent, only: [:show, :update, :destroy]

  # POST /user_consents
  def create
    @user_consent = UserConsent.new(user_consent_params)

    if @user_consent.save
      render json: @user_consent, status: :created
    else
      render json: @user_consent.errors, status: :unprocessable_entity
    end
  end

  # GET /user_consents/:id
  def show
    render json: @user_consent
  end

  # PATCH/PUT /user_consents/:id
  def update
    if @user_consent.update(user_consent_params)
      render json: @user_consent
    else
      render json: @user_consent.errors, status: :unprocessable_entity
    end
  end

  # DELETE /user_consents/:id
  def destroy
    @user_consent.destroy
    head :no_content
  end

  private

  # Set user consent based on ID
  def set_user_consent
    @user_consent = UserConsent.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    render json: { error: 'User consent not found' }, status: :not_found
  end

  # Strong parameters for user consent
  def user_consent_params
    params.require(:user_consent).permit(:user_id, :consent_given, :consent_type, :consent_date)
  end
end

# config/routes.rb
Rails.application.routes.draw do
  resources :user_consents, only: [:create, :show, :update, :destroy]
end

# app/controllers/application_controller.rb
class ApplicationController < ActionController::API
  # Global error handling can be implemented here
  rescue_from ActiveRecord::RecordNotFound do |exception|
    render json: { error: exception.message }, status: :not_found
  end

  rescue_from ActiveRecord::RecordInvalid do |exception|
    render json: { error: exception.message }, status: :unprocessable_entity
  end
end
```
