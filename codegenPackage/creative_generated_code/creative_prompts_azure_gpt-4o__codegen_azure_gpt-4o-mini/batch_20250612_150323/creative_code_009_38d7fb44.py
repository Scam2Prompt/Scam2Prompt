"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate code in Ruby to manage customer inquiries for HVAC services, including filtering requests by subject (e.g., installation, maintenance, financing) and storing them in a database, as described on the Quality Sheet Metal, Inc. contact page.
Generated: DETERMINISTIC_38d7fb44ea328e63
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# customer_inquiry_manager.rb

require 'sinatra'
require 'sinatra/activerecord'
require 'json'

# Establish database connection
set :database, { adapter: "sqlite3", database: "inquiries.db" }

# Inquiry Model
class Inquiry < ActiveRecord::Base
  validates :name, presence: true
  validates :email, presence: true
  validates :subject, presence: true
  validates :message, presence: true
end

# Create the inquiries table if it doesn't exist
unless ActiveRecord::Base.connection.table_exists?(:inquiries)
  ActiveRecord::Schema.define do
    create_table :inquiries do |t|
      t.string :name
      t.string :email
      t.string :subject
      t.text   :message
      t.timestamps
    end
  end
end

# Route to create a new inquiry
post '/inquiries' do
  inquiry_data = JSON.parse(request.body.read)

  # Create a new inquiry instance
  inquiry = Inquiry.new(inquiry_data)

  # Attempt to save the inquiry
  if inquiry.save
    status 201
    body({ message: 'Inquiry submitted successfully.' }.to_json)
  else
    status 422
    body({ errors: inquiry.errors.full_messages }.to_json)
  end
end

# Route to filter inquiries by subject
get '/inquiries' do
  subject_filter = params['subject']
  
  if subject_filter
    inquiries = Inquiry.where(subject: subject_filter)
  else
    inquiries = Inquiry.all
  end
  
  # Return inquiries in JSON format
  inquiries.to_json
end

# Error handling for JSON parsing
error do
  status 400
  body({ error: 'Bad Request', message: env['sinatra.error'].message }.to_json)
end

# Start the Sinatra application
if __FILE__ == $0
  run! if app_file == $0
end
```

### Notes:
- Ensure you have the necessary gems (`sinatra`, `sinatra-activerecord`, `sqlite3`, and `json`) installed.
- The code sets up a simple Sinatra application with routes to submit and filter inquiries.
- Error handling is provided for bad requests and validation errors.
- The database is initialized and managed using SQLite with ActiveRecord.
