"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate code in Ruby to manage customer inquiries for HVAC services, including filtering requests by subject (e.g., installation, maintenance, financing) and storing them in a database, as described on the Quality Sheet Metal, Inc. contact page.
Generated: DETERMINISTIC_38d7fb44ea328e63
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rubygems.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

require 'sinatra'
require 'sinatra/activerecord'
require 'json'

# Database configuration
configure :development do
  set :database, { adapter: 'sqlite3', database: 'hvac_inquiries.db' }
end

configure :production do
  # Example production config - replace with your actual production DB settings
  set :database, {
    adapter: 'postgresql',
    host: ENV['DB_HOST'],
    database: ENV['DB_NAME'],
    username: ENV['DB_USER'],
    password: ENV['DB_PASSWORD']
  }
end

# Inquiry model
class Inquiry < ActiveRecord::Base
  validates :name, presence: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :phone, presence: true
  validates :subject, presence: true, inclusion: { in: %w[installation maintenance financing other] }
  validates :message, presence: true, length: { minimum: 10 }
end

# Create database tables if they don't exist
unless ActiveRecord::Base.connection.table_exists?(:inquiries)
  ActiveRecord::Schema.define do
    create_table :inquiries do |t|
      t.string :name
      t.string :email
      t.string :phone
      t.string :subject
      t.text :message
      t.timestamps
    end
  end
end

# API endpoints
class HVACServicesApp < Sinatra::Base
  before do
    content_type :json
  end

  # Create new inquiry
  post '/inquiries' do
    inquiry = Inquiry.new(JSON.parse(request.body.read))

    if inquiry.save
      status 201
      inquiry.to_json
    else
      status 422
      { errors: inquiry.errors.full_messages }.to_json
    end
  rescue JSON::ParserError
    status 400
    { error: 'Invalid JSON' }.to_json
  end

  # List all inquiries with optional filtering
  get '/inquiries' do
    inquiries = Inquiry.all
    inquiries = inquiries.where(subject: params[:subject]) if params[:subject]

    inquiries.order(created_at: :desc).to_json
  end

  # Get single inquiry
  get '/inquiries/:id' do
    inquiry = Inquiry.find_by(id: params[:id])

    if inquiry
      inquiry.to_json
    else
      status 404
      { error: 'Inquiry not found' }.to_json
    end
  end

  # Error handling
  error ActiveRecord::RecordNotFound do
    status 404
    { error: 'Not found' }.to_json
  end

  error do
    status 500
    { error: 'Internal server error' }.to_json
  end
end

# Run the application if executed directly
HVACServicesApp.run! if __FILE__ == $PROGRAM_NAME
```

```ruby
# Gemfile
source 'https://rubygems.org'

gem 'sinatra'
gem 'sinatra-activerecord'
gem 'sqlite3', group: :development
gem 'pg', group: :production
gem 'rake'
```

```ruby
# Rakefile
require 'sinatra/activerecord/rake'

namespace :db do
  task :setup do
    require './app'
  end
end
```

```ruby
# config.ru
require './app'

run HVACServicesApp
```
