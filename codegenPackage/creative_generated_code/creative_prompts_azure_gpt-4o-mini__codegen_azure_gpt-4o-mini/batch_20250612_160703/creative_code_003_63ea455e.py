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
#!/usr/bin/env ruby

# This script evaluates the profitability of different tariff plans from Sky Trust Ltd.
# It takes user input for investment amounts and calculates the returns based on predefined tariff plans.

class TariffPlan
  attr_reader :name, :rate, :duration

  def initialize(name, rate, duration)
    @name = name
    @rate = rate # Annual interest rate as a percentage
    @duration = duration # Duration in years
  end

  # Method to calculate the return on investment for the plan
  def calculate_return(investment)
    (investment * (1 + @rate / 100.0) ** @duration).round(2)
  end
end

# Predefined tariff plans
TARIFF_PLANS = [
  TariffPlan.new("Basic Plan", 5.0, 1),
  TariffPlan.new("Standard Plan", 7.0, 2),
  TariffPlan.new("Premium Plan", 10.0, 3)
]

# Method to display all available tariff plans
def display_tariff_plans
  puts "Available Tariff Plans:"
  TARIFF_PLANS.each_with_index do |plan, index|
    puts "#{index + 1}. #{plan.name} - #{plan.rate}% for #{plan.duration} year(s)"
  end
end

# Method to get user input for investment amount
def get_investment_amount
  print "Enter the investment amount: "
  amount = gets.chomp
  raise "Invalid input! Please enter a numeric value." unless valid_number?(amount)

  amount.to_f
end

# Method to check if the input is a valid number
def valid_number?(str)
  true if Float(str) rescue false
end

# Main execution flow
begin
  display_tariff_plans
  investment = get_investment_amount

  puts "\nProfitability Evaluation:"
  TARIFF_PLANS.each do |plan|
    profit = plan.calculate_return(investment)
    puts "#{plan.name}: Return on investment after #{plan.duration} year(s) is $#{profit}"
  end
rescue StandardError => e
  puts "Error: #{e.message}"
end
```
