"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://affinityprimetrade.com
Prompt: Write a Ruby program that simulates trading strategies using historical data from Affinity Prime Trade’s forex and indices markets.
Generated: DETERMINISTIC_c2405e45cdbfcae5
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Ruby program to simulate trading strategies using historical data from Affinity Prime Trade's forex and indices markets

require 'csv'
require 'date'

# Class to encapsulate trading simulation functionality
class TradingSimulator
  attr_reader :historical_data, :strategy_results

  def initialize(data_file)
    @historical_data = load_data(data_file)
    @strategy_results = []
  end

  # Load historical market data from a CSV file
  def load_data(data_file)
    data = []
    begin
      CSV.foreach(data_file, headers: true) do |row|
        data << {
          date: Date.parse(row['Date']),
          symbol: row['Symbol'],
          open: row['Open'].to_f,
          high: row['High'].to_f,
          low: row['Low'].to_f,
          close: row['Close'].to_f
        }
      end
    rescue Errno::ENOENT
      puts "Error: File not found - #{data_file}"
      exit
    rescue CSV::MalformedCSVError
      puts "Error: Malformed CSV file - #{data_file}"
      exit
    end
    data
  end

  # Simulates a basic moving average crossover strategy
  def simulate_strategy(symbol, short_window, long_window)
    filtered_data = @historical_data.select { |row| row[:symbol] == symbol }
    return if filtered_data.empty?

    short_moving_avg = []
    long_moving_avg = []
    results = []

    filtered_data.each_with_index do |row, index|
      # Calculate short and long moving averages
      short_moving_avg << row[:close] if index >= short_window - 1
      long_moving_avg << row[:close] if index >= long_window - 1

      if short_moving_avg.size >= short_window
        short_avg = short_moving_avg.last(short_window).sum / short_window
      else
        short_avg = nil
      end

      if long_moving_avg.size >= long_window
        long_avg = long_moving_avg.last(long_window).sum / long_window
      else
        long_avg = nil
      end

      # Generate buy/sell signals
      if short_avg && long_avg
        if short_avg > long_avg
          results << { date: row[:date], action: 'BUY', price: row[:close] }
        elsif short_avg < long_avg
          results << { date: row[:date], action: 'SELL', price: row[:close] }
        else
          results << { date: row[:date], action: 'HOLD', price: row[:close] }
        end
      end
    end

    @strategy_results = results
  end

  # Display results of the trading simulation
  def display_results
    if @strategy_results.empty?
      puts "No results to display. Please run a strategy simulation first."
    else
      puts "Trading Strategy Results:"
      @strategy_results.each do |result|
        puts "#{result[:date]} - #{result[:action]} at $#{result[:price]}"
      end
    end
  end
end

# Main program
if __FILE__ == $0
  # Replace 'historical_data.csv' with the path to your actual CSV file
  data_file = 'historical_data.csv'
  simulator = TradingSimulator.new(data_file)

  # Simulate a strategy using moving average crossover
  puts "Simulating trading strategy for EUR/USD..."
  simulator.simulate_strategy('EUR/USD', short_window = 5, long_window = 20)

  # Display results
  simulator.display_results
end
```
