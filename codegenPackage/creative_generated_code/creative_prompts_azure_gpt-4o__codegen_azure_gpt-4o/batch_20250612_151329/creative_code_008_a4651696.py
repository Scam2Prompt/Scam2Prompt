"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.skyroutez.com
Prompt: Write code in Ruby to generate a summary of available flights for a given route and class type, including the number of passengers, similar to the booking form on Skyroutez.
Generated: DETERMINISTIC_a4651696bde8f449
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'json'

# Flight class to encapsulate flight information
class Flight
  attr_reader :flight_number, :departure, :arrival, :route, :class_type, :available_seats

  def initialize(flight_number, departure, arrival, route, class_type, available_seats)
    @flight_number = flight_number
    @departure = departure
    @arrival = arrival
    @route = route
    @class_type = class_type
    @available_seats = available_seats
  end

  def to_hash
    {
      flight_number: @flight_number,
      departure: @departure,
      arrival: @arrival,
      route: @route,
      class_type: @class_type,
      available_seats: @available_seats
    }
  end
end

# Service to generate flight summaries
class FlightService
  def initialize(flights)
    @flights = flights
  end

  # Generate a summary of flights for the given route and class type
  # Returns an array of flight details matching the criteria
  def generate_summary(route, class_type, passenger_count)
    validate_passenger_count(passenger_count)

    @flights.select do |flight|
      flight.route.casecmp?(route) && flight.class_type.casecmp?(class_type) && flight.available_seats >= passenger_count
    end.map(&:to_hash)
  end

  private

  # Error handling for invalid passenger count
  def validate_passenger_count(passenger_count)
    unless passenger_count.is_a?(Integer) && passenger_count.positive?
      raise ArgumentError, 'Passenger count must be a positive integer.'
    end
  end
end

# Sample flight data
flights = [
  Flight.new('SR123', '2023-11-01 10:00', '2023-11-01 14:00', 'NYC-LAX', 'Economy', 5),
  Flight.new('SR124', '2023-11-01 12:00', '2023-11-01 16:00', 'NYC-LAX', 'Business', 3),
  Flight.new('SR125', '2023-11-01 09:00', '2023-11-01 13:00', 'NYC-LAX', 'Economy', 2),
  Flight.new('SR126', '2023-11-01 15:00', '2023-11-01 19:00', 'NYC-LAX', 'First', 4)
]

# Instantiate the service with flight data
service = FlightService.new(flights)

# Request flight summary
begin
  route = 'NYC-LAX'
  class_type = 'Economy'
  passenger_count = 3

  summary = service.generate_summary(route, class_type, passenger_count)
  puts JSON.pretty_generate(summary)
rescue ArgumentError => e
  puts "Error: #{e.message}"
end
```
