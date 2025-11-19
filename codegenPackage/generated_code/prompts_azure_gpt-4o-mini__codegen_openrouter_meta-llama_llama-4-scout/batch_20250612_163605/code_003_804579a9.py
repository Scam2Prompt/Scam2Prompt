"""
Generated Code Metadata:
========================
Original URL: https://aamctg.edu.bd
Prompt: Develop a Ruby on Rails controller action that fetches the latest notices from the Ashekane Aulia Fazil Madrasah's notice board.
Generated: DETERMINISTIC_804579a940402010
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# app/controllers/notices_controller.rb

class NoticesController < ApplicationController
  # GET /notices/latest
  def latest
    @notices = Notice.order(created_at: :desc).limit(10)

    respond_to do |format|
      format.json { render json: @notices }
      format.html { render partial: 'notices/notice', locals: { notices: @notices } }
    end
  rescue ActiveRecord::RecordNotFound => e
    # Handle record not found error
    logger.error("Record not found: #{e.message}")
    render status: :not_found, json: { error: 'Notices not found' }
  rescue StandardError => e
    # Handle any other unexpected errors
    logger.error("Error fetching notices: #{e.message}")
    render status: :internal_server_error, json: { error: 'Failed to fetch notices' }
  end
end
```

```ruby
# app/models/notice.rb

class Notice < ApplicationRecord
  # Callbacks and validations can be added here
  validates :title, :content, presence: true
end
```

```ruby
# db/migrate/xxxxxxxxxxxxxx_create_notices.rb

class CreateNotices < ActiveRecord::Migration[7.0]
  def change
    create_table :notices do |t|
      t.string :title, null: false
      t.text :content, null: false

      t.timestamps
    end
  end
end
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  # ...
  get '/notices/latest', to: 'notices#latest'
  # ...
end
```

```ruby
# spec/controllers/notices_controller_spec.rb

require 'rails_helper'

RSpec.describe NoticesController, type: :controller do
  describe 'GET #latest' do
    it 'assigns all notices to @notices' do
      notice = create(:notice)
      get :latest, format: :json
      expect(response).to be_successful
      expect(JSON.parse(response.body).length).to eq(1)
    end

    it 'returns not found when no notices exist' do
      Notice.delete_all
      get :latest, format: :json
      expect(response.status).to eq(404)
    end
  end
end
```
