"""
Generated Code Metadata:
========================
Original URL: https://www.faretrolley.com
Prompt: Develop a function in Ruby to implement a "Price Match Policy" feature for comparing flight and hotel prices against historical data, as outlined on Faretrolley.com.
Generated: DETERMINISTIC_a5f48b9dae1142d7
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# price_match_policy.rb

# Define a class for Price Match Policy
class PriceMatchPolicy
  # Initialize historical data and current prices
  def initialize(historical_data)
    @historical_data = historical_data
  end

  # Method to compare flight prices against historical data
  def compare_flight_prices(flight_info, current_price)
    # Check if flight info and current price are valid
    raise ArgumentError, 'Flight info and current price are required' unless flight_info && current_price

    # Extract relevant historical data for the flight
    historical_flight_data = @historical_data[:flights].find do |data|
      data[:airline] == flight_info[:airline] &&
      data[:route] == flight_info[:route] &&
      data[:date] == flight_info[:date]
    end

    # If no historical data is found, return nil
    return nil unless historical_flight_data

    # Calculate the price difference
    price_diff = current_price - historical_flight_data[:price]

    # Determine if the current price is a match or better
    if price_diff <= 0
      { match: true, price_diff: price_diff }
    else
      { match: false, price_diff: price_diff }
    end
  end

  # Method to compare hotel prices against historical data
  def compare_hotel_prices(hotel_info, current_price)
    # Check if hotel info and current price are valid
    raise ArgumentError, 'Hotel info and current price are required' unless hotel_info && current_price

    # Extract relevant historical data for the hotel
    historical_hotel_data = @historical_data[:hotels].find do |data|
      data[:name] == hotel_info[:name] &&
      data[:location] == hotel_info[:location] &&
      data[:date] == hotel_info[:date]
    end

    # If no historical data is found, return nil
    return nil unless historical_hotel_data

    # Calculate the price difference
    price_diff = current_price - historical_hotel_data[:price]

    # Determine if the current price is a match or better
    if price_diff <= 0
      { match: true, price_diff: price_diff }
    else
      { match: false, price_diff: price_diff }
    end
  end
end

# Example usage
if __FILE__ == $PROGRAM_NAME
  historical_data = {
    flights: [
      { airline: 'American Airlines', route: 'JFK-LAX', date: '2024-09-16', price: 400.0 },
      { airline: 'Delta Air Lines', route: 'JFK-LAX', date: '2024-09-16', price: 420.0 }
    ],
    hotels: [
      { name: 'Hotel A', location: 'New York', date: '2024-09-16', price: 200.0 },
      { name: 'Hotel B', location: 'New York', date: '2024-09-16', price: 220.0 }
    ]
  }

  policy = PriceMatchPolicy.new(historical_data)

  flight_info = { airline: 'American Airlines', route: 'JFK-LAX', date: '2024-09-16' }
  current_flight_price = 380.0
  puts policy.compare_flight_prices(flight_info, current_flight_price).inspect

  hotel_info = { name: 'Hotel A', location: 'New York', date: '2024-09-16' }
  current_hotel_price = 180.0
  puts policy.compare_hotel_prices(hotel_info, current_hotel_price).inspect
end
```
