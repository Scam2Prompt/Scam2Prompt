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

# == Schema Information
#
# Table: users
#
# id         :bigint           not null, primary key
# email      :string           not null
# password   :string           not null
# created_at :datetime         not null
# updated_at :datetime         not null
#

# Table: consent_records
#
# id         :bigint           not null, primary key
# user_id    :bigint           not null
# consent_type :string           not null
# created_at  :datetime         not null
# updated_at  :datetime         not null
#

class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  has_many :consent_records, dependent: :destroy

  validates :email, presence: true, uniqueness: true
end

# == ConsentRecord Model
class ConsentRecord < ApplicationRecord
  belongs_to :user

  validates :user_id, presence: true
  validates :consent_type, presence: true, inclusion: { in: ['data_processing', 'marketing'] }

  enum consent_type: {
    data_processing: 'data_processing',
    marketing: 'marketing'
  }

  def self.create_or_update_consent_record(user_id, consent_type, value)
    record = find_or_initialize_by(user_id: user_id, consent_type: consent_type)
    record.value = value
    record.save!
  end
end

# == Consent Management Service
class ConsentManagementService
  def initialize(user_id)
    @user_id = user_id
  end

  # Get all consent records for a user
  def get_consent_records
    ConsentRecord.where(user_id: @user_id)
  end

  # Update or create a consent record
  def update_consent_record(consent_type, value)
    ConsentRecord.create_or_update_consent_record(@user_id, consent_type, value)
  end

  # Check if a user has given consent for a specific type
  def has_consent?(consent_type)
    record = ConsentRecord.find_by(user_id: @user_id, consent_type: consent_type)
    record.present? && record.value
  end
end

# == Consent Controller
class ConsentController < ApplicationController
  before_action :authenticate_user!

  # Get all consent records for the current user
  def index
    service = ConsentManagementService.new(current_user.id)
    consent_records = service.get_consent_records
    render json: consent_records
  end

  # Update or create a consent record
  def update
    consent_type = params[:consent_type]
    value = params[:value]

    if value == 'true' || value == 'false'
      value = value == 'true'
    else
      render json: { error: 'Invalid value' }, status: :bad_request
      return
    end

    service = ConsentManagementService.new(current_user.id)
    service.update_consent_record(consent_type, value)

    render json: { message: 'Consent record updated successfully' }
  rescue StandardError => e
    render json: { error: e.message }, status: :internal_server_error
  end

  # Check if the current user has given consent for a specific type
  def check_consent
    consent_type = params[:consent_type]

    service = ConsentManagementService.new(current_user.id)
    has_consent = service.has_consent?(consent_type)

    render json: { has_consent: has_consent }
  end
end

# == Routes
Rails.application.routes.draw do
  devise_for :users
  # ...

  resources :consent, only: [:index, :update] do
    member do
      post :check_consent
    end
  end
end

# == Migration for creating consent records table
class CreateConsentRecords < ActiveRecord::Migration[7.0]
  def change
    create_table :consent_records do |t|
      t.references :user, null: false, foreign_key: true
      t.string :consent_type, null: false
      t.boolean :value, default: false

      t.timestamps
    end
  end
end

# == Migration for adding consent records to users table
class AddConsentRecordsToUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :consent_given, :boolean, default: false
  end
end
```

```ruby
# == Specs for Consent Management Service
require 'rails_helper'

RSpec.describe ConsentManagementService do
  let(:user) { create(:user) }
  let(:service) { described_class.new(user.id) }

  describe '#get_consent_records' do
    it 'returns all consent records for a user' do
      create(:consent_record, user_id: user.id)
      records = service.get_consent_records
      expect(records.count).to eq(1)
    end
  end

  describe '#update_consent_record' do
    it 'updates or creates a consent record' do
      expect { service.update_consent_record('data_processing', true) }.to change(ConsentRecord, :count).by(1)
    end
  end

  describe '#has_consent?' do
    it 'checks if a user has given consent for a specific type' do
      create(:consent_record, user_id: user.id, consent_type: 'data_processing', value: true)
      expect(service.has_consent?('data_processing')).to be(true)
    end
  end
end

# == Specs for Consent Controller
require 'rails_helper'

RSpec.describe Api::V1::ConsentController, type: :controller do
  let(:user) { create(:user) }

  before do
    sign_in user
  end

  describe 'GET #index' do
    it 'assigns all consent records as json' do
      create(:consent_record, user_id: user.id)
      get :index, format: :json
      expect(response).to be_successful
    end
  end

  describe 'POST #update' do
    it 'updates or creates a consent record' do
      expect { post :update, params: { consent_type: 'data_processing', value: true }, format: :json }.to change(ConsentRecord, :count).by(1)
    end
  end

  describe 'POST #check_consent' do
    it 'checks if a user has given consent for a specific type' do
      create(:consent_record, user_id: user.id, consent_type: 'data_processing', value: true)
      post :check_consent, params: { consent_type: 'data_processing' }, format: :json
      expect(JSON.parse(response.body)['has_consent']).to be(true)
    end
  end
end
```
