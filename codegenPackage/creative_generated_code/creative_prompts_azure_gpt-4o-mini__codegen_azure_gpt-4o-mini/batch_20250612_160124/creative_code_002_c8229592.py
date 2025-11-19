"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Create a function in Ruby that simulates the investment process for the Gold Design plan from Apex Digital Limited, including daily returns and capital return.
Generated: DETERMINISTIC_c8229592dd9d7644
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# InvestmentSimulator class simulates the investment process for the Gold Design plan.
class InvestmentSimulator
  # Initializes the simulator with the investment amount and daily return rate.
  #
  # @param [Float] initial_investment The amount invested initially.
  # @param [Float] daily_return_rate The daily return rate as a decimal (e.g., 0.01 for 1%).
  def initialize(initial_investment, daily_return_rate)
    @initial_investment = initial_investment
    @daily_return_rate = daily_return_rate
    @total_investment = initial_investment
    @total_return = 0.0
  end

  # Simulates daily returns for a specified number of days.
  #
  # @param [Integer] days The number of days to simulate.
  def simulate(days)
    raise ArgumentError, 'Days must be a positive integer' unless days.is_a?(Integer) && days > 0

    days.times do |day|
      daily_profit = @total_investment * @daily_return_rate
      @total_return += daily_profit
      @total_investment += daily_profit

      # Log daily status (optional, can be removed in production)
      puts "Day #{day + 1}: Total Investment: $#{'%.2f' % @total_investment}, Daily Profit: $#{'%.2f' % daily_profit}"
    end
  end

  # Returns the total profit after the simulation.
  #
  # @return [Float] The total profit earned.
  def total_profit
    @total_return
  end

  # Returns the total amount after the simulation.
  #
  # @return [Float] The total amount including initial investment and profit.
  def total_amount
    @total_investment
  end
end

# Example usage:
begin
  investment = InvestmentSimulator.new(1000.0, 0.01) # $1000 initial investment, 1% daily return
  investment.simulate(30) # Simulate for 30 days

  puts "Total Profit: $#{'%.2f' % investment.total_profit}" # Display total profit
  puts "Total Amount: $#{'%.2f' % investment.total_amount}" # Display total amount
rescue ArgumentError => e
  puts "Error: #{e.message}" # Handle argument errors
end
```
