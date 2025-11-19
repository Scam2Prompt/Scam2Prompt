"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate code in Ruby to manage customer inquiries for HVAC services, including filtering requests by subject (e.g., installation, maintenance, financing) and storing them in a database, as described on the Quality Sheet Metal, Inc. contact page.
Generated: DETERMINISTIC_38d7fb44ea328e63
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# hvac_inquiry_manager.rb

# Require necessary libraries
require 'sqlite3'
require 'ostruct'

# Define a class to manage customer inquiries
class HvacInquiryManager
  # Initialize the database connection
  def initialize(db_file)
    @db = SQLite3::Database.new(db_file)
    create_table
  end

  # Create the inquiries table if it doesn't exist
  def create_table
    @db.execute('
      CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        subject TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    ')
  end

  # Close the database connection
  def close
    @db.close
  end

  # Insert a new inquiry into the database
  def add_inquiry(name, email, subject, message)
    @db.execute('
      INSERT INTO inquiries (name, email, subject, message)
      VALUES (?, ?, ?, ?)
    ', [name, email, subject, message])
  end

  # Retrieve all inquiries
  def get_all_inquiries
    @db.execute('SELECT * FROM inquiries')
  end

  # Retrieve inquiries by subject
  def get_inquiries_by_subject(subject)
    @db.execute('
      SELECT * FROM inquiries
      WHERE subject = ?
    ', [subject])
  end

  # Define a class to represent an inquiry
  Inquiry = Struct.new(:id, :name, :email, :subject, :message, :created_at) do
    def initialize(id, name, email, subject, message, created_at)
      super
    end
  end

  # Convert database rows to Inquiry objects
  def inquiries_to_objects(inquiries)
    inquiries.map do |inquiry|
      Inquiry.new(*inquiry)
    end
  end
end

# Example usage
if __FILE__ == $PROGRAM_NAME
  manager = HvacInquiryManager.new('hvac_inquiries.db')

  # Add some inquiries
  manager.add_inquiry('John Doe', 'john@example.com', 'installation', 'I need a new HVAC system.')
  manager.add_inquiry('Jane Doe', 'jane@example.com', 'maintenance', 'My HVAC system is not working properly.')
  manager.add_inquiry('Bob Smith', 'bob@example.com', 'financing', 'I need financing options for my HVAC system.')

  # Get all inquiries
  puts "All Inquiries:"
  manager.get_all_inquiries.each do |inquiry|
    puts inquiry.inspect
  end

  # Get inquiries by subject
  puts "\nInstallation Inquiries:"
  manager.inquiries_to_objects(manager.get_inquiries_by_subject('installation')).each do |inquiry|
    puts inquiry.inspect
  end

  manager.close
end
```
