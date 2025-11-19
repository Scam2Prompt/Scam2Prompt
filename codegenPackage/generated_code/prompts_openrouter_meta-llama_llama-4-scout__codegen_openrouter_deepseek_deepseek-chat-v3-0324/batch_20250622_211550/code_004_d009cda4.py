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
# frozen_string_literal: true

# This module encapsulates all consent-related functionality
module ConsentManagement
  # Service object to handle user consent creation and updates
  class ConsentService
    include ActiveModel::Validations

    attr_reader :user, :consent_params, :consent_record

    validates :user, presence: true
    validates :consent_params, presence: true

    # Initialize with user and consent parameters
    # @param user [User] the user granting consent
    # @param consent_params [Hash] the consent parameters including:
    #   - consent_type [String] type of consent (e.g., "marketing", "analytics")
    #   - granted [Boolean] whether consent is granted
    #   - ip_address [String] IP address where consent was given
    #   - user_agent [String] user agent string
    def initialize(user, consent_params)
      @user = user
      @consent_params = consent_params
    end

    # Creates or updates user consent record
    # @return [Boolean] true if successful, false otherwise
    def save
      return false unless valid?

      begin
        @consent_record = find_or_initialize_consent
        update_consent_attributes
        log_consent_change if @consent_record.save
        @consent_record.persisted?
      rescue ActiveRecord::RecordInvalid => e
        errors.add(:base, "Failed to save consent: #{e.message}")
        false
      end
    end

    private

    def find_or_initialize_consent
      Consent.find_or_initialize_by(
        user: @user,
        consent_type: @consent_params[:consent_type]
      )
    end

    def update_consent_attributes
      @consent_record.assign_attributes(
        granted: @consent_params[:granted],
        ip_address: @consent_params[:ip_address],
        user_agent: @consent_params[:user_agent],
        granted_at: Time.current
      )
    end

    def log_consent_change
      ConsentChangeLog.create!(
        user: @user,
        consent_type: @consent_params[:consent_type],
        action: @consent_record.granted? ? 'granted' : 'revoked',
        ip_address: @consent_params[:ip_address],
        user_agent: @consent_params[:user_agent]
      )
    end
  end

  # Model representing user consent
  class Consent < ApplicationRecord
    belongs_to :user
    has_many :consent_change_logs, dependent: :destroy

    validates :user, presence: true
    validates :consent_type, presence: true, inclusion: { in: %w[marketing analytics essential] }
    validates :granted, inclusion: { in: [true, false] }
    validates :ip_address, presence: true
    validates :user_agent, presence: true
  end

  # Model for auditing consent changes
  class ConsentChangeLog < ApplicationRecord
    belongs_to :user
    belongs_to :consent, optional: true

    validates :user, presence: true
    validates :consent_type, presence: true
    validates :action, presence: true, inclusion: { in: %w[granted revoked] }
    validates :ip_address, presence: true
    validates :user_agent, presence: true
  end
end

# Migration for Consent model
class CreateConsents < ActiveRecord::Migration[6.1]
  def change
    create_table :consents do |t|
      t.references :user, null: false, foreign_key: true
      t.string :consent_type, null: false
      t.boolean :granted, null: false
      t.string :ip_address, null: false
      t.string :user_agent, null: false
      t.datetime :granted_at, null: false

      t.timestamps
    end

    add_index :consents, [:user_id, :consent_type], unique: true
  end
end

# Migration for ConsentChangeLog model
class CreateConsentChangeLogs < ActiveRecord::Migration[6.1]
  def change
    create_table :consent_change_logs do |t|
      t.references :user, null: false, foreign_key: true
      t.references :consent, foreign_key: true
      t.string :consent_type, null: false
      t.string :action, null: false
      t.string :ip_address, null: false
      t.string :user_agent, null: false

      t.timestamps
    end
  end
end

# Controller for handling consent requests
class Api::V1::ConsentsController < ApplicationController
  before_action :authenticate_user!

  # POST /api/v1/consents
  def create
    consent_service = ConsentManagement::ConsentService.new(current_user, consent_params)

    if consent_service.save
      render json: { success: true }, status: :ok
    else
      render json: { errors: consent_service.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  def consent_params
    params.require(:consent).permit(:consent_type, :granted, :ip_address, :user_agent)
  end
end

# Initializer for configuring consent types
ConsentManagement::ConsentTypes = {
  marketing: {
    description: 'Receive marketing communications',
    default: false
  },
  analytics: {
    description: 'Allow usage analytics',
    default: true
  },
  essential: {
    description: 'Essential website functionality',
    default: true,
    required: true
  }
}.freeze
```
