"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blog.firstflytravel.com
Prompt: Generate a script in Ruby that fetches flight options for group travel and military travel from First Fly Travel's database, prioritizing affordable deals.
Generated: DETERMINISTIC_1ff8348790b66f15
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'pg'
require 'logger'

# Logger to track errors and script execution
logger = Logger.new('flight_fetcher.log')

begin
  # Connect to the database (Update with correct credentials)
  db_connection = PG.connect(
    dbname: 'first_fly_travel_db',
    user: 'your_username',
    password: 'your_password',
    host: 'localhost',
    port: 5432
  )

  logger.info("Database connection established.")

  # Fetch group travel and military travel flight options
  query = <<-SQL
    SELECT 
      flight_id, 
      airline, 
      origin, 
      destination, 
      departure_time, 
      arrival_time, 
      price, 
      travel_type 
    FROM 
      flights 
    WHERE 
      travel_type IN ('group', 'military') 
    ORDER BY 
      price ASC; -- Prioritize cheaper (affordable) deals
  SQL

  # Execute query
  result = db_connection.exec(query)

  # Check if any flights were found
  if result.ntuples.zero?
    logger.warn("No flight options found for group or military travel.")
    puts "No flight options available for the requested travel types."
  else
    logger.info("Flight options fetched successfully.")

    # Display results in a readable format
    puts "Available Flight Options (Prioritized by Affordability):"
    result.each do |row|
      puts "----------------------------------------"
      puts "Flight ID: #{row['flight_id']}"
      puts "Airline: #{row['airline']}"
      puts "Origin: #{row['origin']}"
      puts "Destination: #{row['destination']}"
      puts "Departure Time: #{row['departure_time']}"
      puts "Arrival Time: #{row['arrival_time']}"
      puts "Price: $#{row['price']}"
      puts "Travel Type: #{row['travel_type']}"
    end
  end

rescue PG::Error => e
  # Log database errors
  logger.error("Database error: #{e.message}")
  puts "An error occurred while fetching flight options. Please try again later."

ensure
  # Ensure the database connection is closed
  if db_connection
    db_connection.close
    logger.info("Database connection closed.")
  end
end
```
