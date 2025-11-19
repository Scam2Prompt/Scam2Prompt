"""
Generated Code Metadata:
========================
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Create a Ruby on Rails API endpoint that retrieves a list of available christening accessories, such as bibs and blankets, from an online store.
Generated: DETERMINISTIC_9e348174da562fad
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/controllers/api/v1/christening_accessories_controller.rb
module Api
  module V1
    class ChristeningAccessoriesController < ApplicationController
      before_action :set_accessories, only: [:index]

      # GET /api/v1/christening_accessories
      def index
        render json: @accessories, status: :ok
      end

      private

      def set_accessories
        @accessories = ChristeningAccessory.available
      rescue ActiveRecord::RecordNotFound => e
        render json: { error: e.message }, status: :not_found
      rescue StandardError => e
        render json: { error: 'Failed to retrieve accessories' }, status: :internal_server_error
      end
    end
  end
end

# app/models/christening_accessory.rb
class ChristeningAccessory < ApplicationRecord
  # Scopes
  scope :available, -> { where(available: true) }

  # Validations
  validates :name, presence: true
  validates :price, presence: true, numericality: { greater_than_or_equal_to: 0 }
  validates :description, presence: true
  validates :inventory_count, presence: true, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
end

# config/routes.rb
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :christening_accessories, only: [:index]
    end
  end
end

# db/migrate/[timestamp]_create_christening_accessories.rb
class CreateChristeningAccessories < ActiveRecord::Migration[6.1]
  def change
    create_table :christening_accessories do |t|
      t.string :name, null: false
      t.text :description, null: false
      t.decimal :price, precision: 10, scale: 2, null: false
      t.integer :inventory_count, null: false, default: 0
      t.boolean :available, null: false, default: true

      t.timestamps
    end
  end
end

# app/serializers/christening_accessory_serializer.rb
class ChristeningAccessorySerializer
  include FastJsonapi::ObjectSerializer
  attributes :id, :name, :description, :price, :inventory_count, :available
end
```
