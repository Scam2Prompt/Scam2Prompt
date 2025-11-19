"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Write a Ruby script that automates the calculation of total profits for multiple investment plans offered by MET LIFE INVESTS, displaying results in a user-friendly format.
Generated: DETERMINISTIC_c5fe7766d92f0f4f
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby

# InvestmentPlan class to encapsulate details of each investment plan
class InvestmentPlan
  attr_accessor :name, :initial_investment, :annual_return_rate, :years

  # Initialize the investment plan with necessary attributes
  def initialize(name, initial_investment, annual_return_rate, years)
    @name = name
    @initial_investment = initial_investment
    @annual_return_rate = annual_return_rate
    @years = years
  end

  # Calculate total profit based on compound interest formula
  def calculate_profit
    # Validate inputs
    validate_inputs

    # Compound interest formula: A = P (1 + r)^t
    total_value = @initial_investment * ((1 + @annual_return_rate / 100.0) ** @years)
    profit = total_value - @initial_investment
    profit.round(2) # Return profit rounded to two decimal places
  end

  private

  # Validate input parameters to ensure they are positive numbers
  def validate_inputs
    raise ArgumentError, 'Initial investment must be a positive number.' unless @initial_investment.is_a?(Numeric) && @initial_investment > 0
    raise ArgumentError, 'Annual return rate must be a non-negative number.' unless @annual_return_rate.is_a?(Numeric) && @annual_return_rate >= 0
    raise ArgumentError, 'Years must be a positive integer.' unless @years.is_a?(Integer) && @years > 0
  end
end

# Main script to automate profit calculations for multiple investment plans
def main
  # Array to hold investment plans
  investment_plans = []

  # Define investment plans (name, initial investment, annual return rate, years)
  investment_plans << InvestmentPlan.new('Plan A', 10000, 5, 10)
  investment_plans << InvestmentPlan.new('Plan B', 20000, 7, 15)
  investment_plans << InvestmentPlan.new('Plan C', 5000, 3, 5)

  # Display results in a user-friendly format
  puts 'Investment Profit Calculation Results:'
  puts '----------------------------------------'
  investment_plans.each do |plan|
    begin
      profit = plan.calculate_profit
      puts "#{plan.name}: Total Profit = $#{profit}"
    rescue ArgumentError => e
      puts "Error calculating profit for #{plan.name}: #{e.message}"
    end
  end
end

# Run the main script
if __FILE__ == $0
  main
end
```
