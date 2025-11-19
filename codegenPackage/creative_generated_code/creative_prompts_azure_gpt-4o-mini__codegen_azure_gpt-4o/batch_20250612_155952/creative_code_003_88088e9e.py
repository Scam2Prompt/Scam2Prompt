"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makerfinance.org
Prompt: Develop a Ruby on Rails application that connects to the Amazon API to allow users to browse and filter grocery items based on discounts.
Generated: DETERMINISTIC_88088e9ebd4112fe
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Gemfile

# Add the necessary gem for Amazon API integration
gem 'amazon_paapi', '~> 1.0'

# Install all gems by running `bundle install`

---

# config/initializers/amazon_api.rb

# This file initializes the Amazon API client with credentials.
AmazonAPIConfig = {
  access_key: ENV['AMAZON_ACCESS_KEY'],
  secret_key: ENV['AMAZON_SECRET_KEY'],
  region: ENV['AMAZON_API_REGION'],
  partner_tag: ENV['AMAZON_PARTNER_TAG']
}

---

# app/controllers/grocery_items_controller.rb

class GroceryItemsController < ApplicationController
  before_action :validate_filters, only: :index

  # GET /grocery_items
  # Fetches and filters grocery items from Amazon API
  def index
    begin
      # Initialize Amazon API client
      client = AmazonPaapi::Client.new(AmazonAPIConfig)

      # Search for grocery items
      response = client.search_items(
        keywords: 'grocery',
        search_index: 'Grocery',
        item_page: params[:item_page] || 1
      )

      # Filter items based on discounts if applicable
      filtered_items = filter_items_by_discount(response.items, params[:discount_threshold])

      render json: { grocery_items: filtered_items }
    rescue StandardError => e
      # Handle errors gracefully
      Rails.logger.error("Failed to fetch grocery items: #{e.message}")
      render json: { error: 'Failed to fetch grocery items' }, status: :internal_server_error
    end
  end

  private

  # Validates incoming filter parameters
  def validate_filters
    if params[:discount_threshold].present? && !valid_discount_threshold?
      render json: { error: 'Invalid discount threshold' }, status: :unprocessable_entity
    end
  end

  # Checks if discount_threshold is a valid number between 0 and 100
  def valid_discount_threshold?
    params[:discount_threshold].to_i.between?(0, 100)
  end

  # Filters items by discount threshold
  def filter_items_by_discount(items, discount_threshold)
    return items unless discount_threshold.present?

    items.select do |item|
      item.offers&.discount_percentage.to_i >= discount_threshold.to_i
    end
  end
end

---

# config/routes.rb

Rails.application.routes.draw do
  # Route for browsing grocery items
  resources :grocery_items, only: [:index]
end

---

# .env (Add this file to .gitignore)

# Environment variables for Amazon API credentials
AMAZON_ACCESS_KEY=your_amazon_access_key
AMAZON_SECRET_KEY=your_amazon_secret_key
AMAZON_API_REGION=your_amazon_api_region
AMAZON_PARTNER_TAG=your_amazon_partner_tag

---

# app/views/grocery_items/index.json.jbuilder

# JSON response structure for grocery items
json.array! @grocery_items do |item|
  json.name item.title
  json.price item.offers&.price&.formatted_amount
  json.discount item.offers&.discount_percentage
  json.link item.detail_page_url
end

---

# Specifying required tasks
# 1. Run `rails db:migrate` to configure the database if necessary.
# 2. Run `rails server` and access the endpoint `/grocery_items?discount_threshold=20` to test.
# Note:
# Replace `your_amazon_access_key`, `your_amazon_secret_key`, etc., with actual credentials.
```
