"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytrustasset.com
Prompt: Develop a Ruby script that evaluates the profitability of different tariff plans from Sky Trust Ltd based on user input for investment amounts.
Generated: DETERMINISTIC_63ea455eabc6648c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# sky_trust_profitability.rb

# This script evaluates the profitability of different tariff plans from Sky Trust Ltd
# based on user input for investment amounts.

# Define Tariff Plans
TARIFF_PLANS = {
  "Basic" => { rate: 0.05, min_investment: 100, max_investment: 1000 },
  "Standard" => { rate: 0.07, min_investment: 1001, max_investment: 5000 },
  "Premium" => { rate: 0.1, min_investment: 5001, max_investment: 10000 }
}

# Method to calculate profitability
def calculate_profit(investment, rate)
  investment * rate
end

# Method to validate investment amount
def validate_investment(amount)
  raise ArgumentError, "Investment amount must be a positive number." unless amount.is_a?(Numeric) && amount > 0
end

# Main Execution Block
begin
  # Prompt user for investment amount
  print "Enter your investment amount: "
  investment_amount = gets.chomp.to_f

  # Validate investment amount
  validate_investment(investment_amount)

  # Evaluate profitability for each plan
  puts "\nProfitability for each tariff plan:"
  TARIFF_PLANS.each do |plan_name, details|
    if investment_amount >= details[:min_investment] && investment_amount <= details[:max_investment]
      profit = calculate_profit(investment_amount, details[:rate])
      puts "#{plan_name} Plan - Rate: #{details[:rate] * 100}% | Profit: $#{'%.2f' % profit}"
    else
      puts "#{plan_name} Plan - Not applicable for your investment amount."
    end
  end

rescue ArgumentError => e
  puts "Error: #{e.message}"
rescue StandardError => e
  puts "An unexpected error occurred: #{e.message}"
end

# End of the script
```
