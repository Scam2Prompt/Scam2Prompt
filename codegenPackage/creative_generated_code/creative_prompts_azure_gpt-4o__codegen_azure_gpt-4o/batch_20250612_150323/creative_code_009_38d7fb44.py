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
# Ruby script to manage customer inquiries for HVAC services

require 'sqlite3'

# Initialize or connect to the SQLite database
class InquiryDatabase
  def initialize(db_file = 'hvac_inquiries.db')
    @db = SQLite3::Database.new(db_file)
    create_table
  end

  # Create the inquiries table if it doesn't exist
  def create_table
    @db.execute <<-SQL
      CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        subject TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    SQL
  end

  # Insert a new inquiry into the table
  def add_inquiry(name:, email:, subject:, message:)
    begin
      @db.execute("INSERT INTO inquiries (name, email, subject, message) VALUES (?, ?, ?, ?)", [name, email, subject, message])
      puts "Inquiry successfully added."
    rescue SQLite3::Exception => e
      puts "Failed to add inquiry: #{e.message}"
    end
  end

  # Filter inquiries by subject
  def filter_inquiries_by_subject(subject)
    begin
      rows = @db.execute("SELECT * FROM inquiries WHERE subject = ?", [subject])
      rows.map do |row|
        {
          id: row[0],
          name: row[1],
          email: row[2],
          subject: row[3],
          message: row[4],
          created_at: row[5]
        }
      end
    rescue SQLite3::Exception => e
      puts "Failed to filter inquiries: #{e.message}"
      []
    end
  end

  # Close the database connection
  def close_connection
    @db.close
  end
end

# Helper class for user interaction
class InquiryManager
  def initialize
    @db = InquiryDatabase.new
  end

  # Record a new inquiry
  def record_inquiry
    puts "Enter name:"
    name = gets.chomp
    puts "Enter email:"
    email = gets.chomp
    puts "Enter subject (e.g., installation, maintenance, financing):"
    subject = gets.chomp
    puts "Enter message:"
    message = gets.chomp

    @db.add_inquiry(name: name, email: email, subject: subject, message: message)
  end

  # Display filtered inquiries
  def display_inquiries_by_subject
    puts "Enter subject to filter by (e.g., installation, maintenance, financing):"
    subject = gets.chomp
    inquiries = @db.filter_inquiries_by_subject(subject)

    if inquiries.empty?
      puts "No inquiries found for subject: #{subject}"
    else
      puts "Inquiries for subject '#{subject}':"
      inquiries.each do |inquiry|
        puts "ID: #{inquiry[:id]}, Name: #{inquiry[:name]}, Email: #{inquiry[:email]}, Message: #{inquiry[:message]}, Created At: #{inquiry[:created_at]}"
      end
    end
  end

  # Close the database connection
  def close_manager
    @db.close_connection
  end
end

# Main script for user interaction
puts "Welcome to the HVAC Inquiry Manager"
manager = InquiryManager.new

loop do
  puts "\nSelect an option:"
  puts "1. Record a new inquiry"
  puts "2. Display inquiries by subject"
  puts "3. Exit"
  choice = gets.chomp.to_i

  case choice
  when 1
    manager.record_inquiry
  when 2
    manager.display_inquiries_by_subject
  when 3
    manager.close_manager
    puts "Goodbye!"
    break
  else
    puts "Invalid option. Please try again."
  end
end
```
