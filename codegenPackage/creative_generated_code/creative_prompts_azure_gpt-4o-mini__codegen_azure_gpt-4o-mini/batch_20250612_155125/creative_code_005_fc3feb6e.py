"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futuresourcelimited.com
Prompt: Write a Ruby script that calculates potential returns based on the investment plans offered by futuresourcelimited.com, including the referral bonus structure.
Generated: DETERMINISTIC_fc3feb6efdb5f565
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# investment_calculator.rb

# InvestmentCalculator class to handle investment returns calculation
class InvestmentCalculator
  # Initialize the calculator with required parameters
  def initialize(investment_amount, referral_bonus_rate, plan_details)
    @investment_amount = investment_amount
    @referral_bonus_rate = referral_bonus_rate
    @plan_details = plan_details
  end

  # Method to calculate total returns based on the selected plan
  def calculate_returns(plan_name, referral_count = 0)
    plan = @plan_details[plan_name]
    
    raise ArgumentError, "Invalid investment plan: #{plan_name}" unless plan

    # Calculate returns based on the selected plan
    potential_return = @investment_amount * (1 + plan[:return_rate] / 100.0)
    
    # Calculate referral bonus if applicable
    referral_bonus = referral_count * @investment_amount * @referral_bonus_rate / 100.0
    total_return = potential_return + referral_bonus

    {
      potential_return: potential_return.round(2),
      referral_bonus: referral_bonus.round(2),
      total_return: total_return.round(2)
    }
  end
end

# Example investment plans offered by the company
investment_plans = {
  "Basic" => { return_rate: 5.0 },
  "Standard" => { return_rate: 10.0 },
  "Premium" => { return_rate: 15.0 }
}

# Constants for the investment scenario
INVESTMENT_AMOUNT = 1000.00 # The amount to be invested
REFERRAL_BONUS_RATE = 2.0    # Percentage of referral bonus

# Create an instance of InvestmentCalculator
calculator = InvestmentCalculator.new(INVESTMENT_AMOUNT, REFERRAL_BONUS_RATE, investment_plans)

# Example usage of the InvestmentCalculator
begin
  plan_name = "Standard"          # Selected investment plan
  referral_count = 3              # Number of successful referrals

  # Calculate and display results
  results = calculator.calculate_returns(plan_name, referral_count)

  puts "Investment Plan: #{plan_name}"
  puts "Potential Return: $#{results[:potential_return]}"
  puts "Referral Bonus: $#{results[:referral_bonus]}"
  puts "Total Return: $#{results[:total_return]}"
rescue ArgumentError => e
  puts "Error: #{e.message}"
rescue StandardError => e
  puts "An unexpected error occurred: #{e.message}"
end
```
