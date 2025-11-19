"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exclusiveaffilateonline.com
Prompt: Construct a Ruby script that simulates trading with a £500 minimum deposit and calculates the expected profit based on the trading conditions provided by Exclusive Affiliate Marketing.
Generated: DETERMINISTIC_095953583103209c
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# trading_simulator.rb

# A Ruby script simulating trading with a £500 minimum deposit
# and calculates the expected profit based on provided conditions.

class TradingSimulator
  attr_reader :initial_deposit, :profit_percentage

  def initialize(initial_deposit, profit_percentage)
    @initial_deposit = initial_deposit
    @profit_percentage = profit_percentage
    validate_initial_deposit
  end

  # Validate the deposit to ensure it meets the minimum requirement of £500
  def validate_initial_deposit
    if @initial_deposit < 500
      raise ArgumentError, "Initial deposit must be at least £500."
    end
  end

  # Calculate expected profit based on deposit and profit percentage
  def calculate_profit
    (@initial_deposit * @profit_percentage / 100).round(2)
  end

  # Print trading summary
  def trading_summary
    profit = calculate_profit
    puts "Trading Summary:"
    puts "Initial Deposit: £#{@initial_deposit}"
    puts "Profit Percentage: #{@profit_percentage}%"
    puts "Expected Profit: £#{profit}"
  end
end

# Error handling for user input
begin
  # Collect user input for deposit amount
  print "Enter your initial deposit amount (minimum £500): "
  initial_deposit = gets.chomp.to_f

  # Collect user input for profit percentage
  print "Enter the expected profit percentage: "
  profit_percentage = gets.chomp.to_f

  # Create a new trading simulator instance
  simulator = TradingSimulator.new(initial_deposit, profit_percentage)

  # Display the trading summary
  simulator.trading_summary

rescue ArgumentError => e
  puts e.message # Display specific error message for invalid deposit
rescue => e
  puts "An error occurred: #{e.message}" # Display generic error message
end
```

To execute the script, save it to a file named `trading_simulator.rb` and run it with Ruby (`ruby trading_simulator.rb`).
