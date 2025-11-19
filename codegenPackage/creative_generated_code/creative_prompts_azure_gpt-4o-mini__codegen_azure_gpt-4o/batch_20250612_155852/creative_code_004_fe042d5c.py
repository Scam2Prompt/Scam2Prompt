"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Design a financial calculator in Ruby that helps users evaluate the potential dividends they can earn from different investment plans on Centraltraderz.
Generated: DETERMINISTIC_fe042d5cf7e3fe18
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# financial_calculator.rb

# Financial Calculator for Centraltraderz
# This script calculates potential dividends for various investment plans.
# Adheres to best practices and is production-ready.

# Utility class for the financial calculator
class FinancialCalculator
  # Initialize the calculator with investment details
  def initialize(principal, annual_rate, years)
    @principal = principal  # Initial investment amount
    @annual_rate = annual_rate  # Annual percentage rate (as a decimal)
    @years = years  # Investment duration in years
  end

  # Method to calculate simple annual dividends
  # Formula: Dividends = Principal * Annual Rate * Years
  def calculate_simple_dividends
    (@principal * @annual_rate * @years).round(2)
  end

  # Method to calculate compound annual dividends
  # Formula: Dividends = Principal * (1 + Annual Rate) ** Years - Principal
  def calculate_compound_dividends
    ((@principal * (1 + @annual_rate)**@years) - @principal).round(2)
  end

  # Method to display formatted results for the user
  def display_results
    simple_dividends = calculate_simple_dividends
    compound_dividends = calculate_compound_dividends

    puts "Investment Summary:"
    puts "--------------------"
    puts "Principal Amount: $#{@principal}"
    puts "Annual Rate: #{@annual_rate * 100}%"
    puts "Investment Duration: #{@years} years"
    puts "--------------------"
    puts "Potential Dividends (Simple Interest): $#{simple_dividends}"
    puts "Potential Dividends (Compound Interest): $#{compound_dividends}"
    puts "--------------------"
  rescue StandardError => e
    puts "An error occurred while displaying results: #{e.message}"
  end
end

# Main script execution
begin
  puts "Welcome to the Centraltraderz Financial Calculator!"
  print "Enter the principal investment amount (e.g., 1000): "
  principal = Float(gets.chomp)

  print "Enter the annual rate as a percentage (e.g., 5 for 5%): "
  annual_rate = Float(gets.chomp) / 100

  print "Enter the investment duration in years (e.g., 10): "
  years = Integer(gets.chomp)

  # Instantiate the financial calculator
  calculator = FinancialCalculator.new(principal, annual_rate, years)

  # Display results to the user
  calculator.display_results
rescue ArgumentError => e
  puts "Invalid input: Please ensure you enter numbers for all fields."
rescue StandardError => e
  puts "An unexpected error occurred: #{e.message}"
end
```

Save this script as `financial_calculator.rb` and execute it using Ruby to interact with the calculator. Ensure Ruby is installed and the script is run in a console environment to capture user inputs.
