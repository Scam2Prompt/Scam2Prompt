"""
Generated Code Metadata:
========================
Original URL: https://apexdiginvcompany.com
Prompt: Create a function in Ruby that simulates the investment process for the Gold Design plan from Apex Digital Limited, including daily returns and capital return.
Generated: DETERMINISTIC_c8229592dd9d7644
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# This Ruby script simulates the investment process for the Gold Design plan from Apex Digital Limited.
# The plan includes daily returns and capital return after a specified investment period.

# Function to simulate the investment process
def simulate_gold_design_investment(initial_investment, daily_return_rate, investment_period)
  # Validate input parameters
  raise ArgumentError, "Initial investment must be a positive number." unless initial_investment.is_a?(Numeric) && initial_investment > 0
  raise ArgumentError, "Daily return rate must be a positive number." unless daily_return_rate.is_a?(Numeric) && daily_return_rate > 0
  raise ArgumentError, "Investment period must be a positive integer." unless investment_period.is_a?(Integer) && investment_period > 0

  # Initialize variables
  total_returns = 0
  daily_returns = []

  # Simulate daily returns
  investment_period.times do |day|
    daily_return = initial_investment * (daily_return_rate / 100.0)
    daily_returns << daily_return
    total_returns += daily_return
    puts "Day #{day + 1}: Daily Return = $#{'%.2f' % daily_return}"
  end

  # Calculate total payout (capital + returns)
  total_payout = initial_investment + total_returns

  # Display summary
  puts "\nInvestment Summary:"
  puts "Initial Investment: $#{'%.2f' % initial_investment}"
  puts "Total Returns: $#{'%.2f' % total_returns}"
  puts "Total Payout (Capital + Returns): $#{'%.2f' % total_payout}"

  # Return detailed results as a hash
  {
    initial_investment: initial_investment,
    daily_return_rate: daily_return_rate,
    investment_period: investment_period,
    daily_returns: daily_returns,
    total_returns: total_returns,
    total_payout: total_payout
  }
end

# Example usage:
begin
  # Simulate an investment with $1000 initial capital, 2% daily return rate, and a 30-day period
  result = simulate_gold_design_investment(1000, 2, 30)
  puts "\nDetailed Results: #{result}"
rescue ArgumentError => e
  puts "Error: #{e.message}"
end
```
