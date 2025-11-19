"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmetromile-investment.com
Prompt: Write a Ruby program that calculates potential returns based on the investment plans offered by globalmetromile-investment.com, including Gold and Forex trading options.
Generated: DETERMINISTIC_ed505a9ec9aeb349
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# investment_calculator.rb
# This Ruby program calculates potential returns for investment plans.
# It supports Gold and Forex trading options based on user input.

# Define a class for Investment
class Investment
  attr_reader :plan_name, :principal, :rate_of_return, :duration

  # Initialize the investment attributes
  def initialize(plan_name, principal, rate_of_return, duration)
    @plan_name = plan_name
    @principal = principal
    @rate_of_return = rate_of_return
    @duration = duration
  end

  # Method to calculate potential return
  def calculate_return
    begin
      # Formula: Total Return = Principal * (1 + Rate of Return) ** Duration
      @principal * ((1 + @rate_of_return) ** @duration)
    rescue StandardError => e
      puts "Error calculating return: #{e.message}"
      nil
    end
  end
end

# Define available investment plans
INVESTMENT_PLANS = {
  "Gold" => { rate_of_return: 0.05 }, # 5% annual return
  "Forex" => { rate_of_return: 0.08 } # 8% annual return
}.freeze

# Display menu for user
def display_menu
  puts "Welcome to Global MetroMile Investment Calculator!"
  puts "Available Investment Plans:"
  INVESTMENT_PLANS.each_with_index do |(plan, details), index|
    puts "#{index + 1}. #{plan} (Annual Return Rate: #{(details[:rate_of_return] * 100).round(2)}%)"
  end
  puts "\nPlease select an investment plan (1 or 2):"
end

# Main program execution
def main
  display_menu

  # Get user input for plan selection
  plan_choice = gets.chomp.to_i
  selected_plan = INVESTMENT_PLANS.keys[plan_choice - 1]

  if selected_plan.nil?
    puts "Invalid choice. Please restart the program and select a valid option."
    return
  end

  # Get user input for principal amount and investment duration
  begin
    print "Enter your principal investment amount ($): "
    principal = Float(gets.chomp)

    print "Enter the duration of the investment (in years): "
    duration = Integer(gets.chomp)

    # Create an instance of the Investment class
    investment = Investment.new(
      selected_plan,
      principal,
      INVESTMENT_PLANS[selected_plan][:rate_of_return],
      duration
    )

    # Calculate and display the potential return
    potential_return = investment.calculate_return
    if potential_return
      puts "\nYour potential return after #{duration} years with the #{selected_plan} plan:"
      puts "$#{potential_return.round(2)}"
    else
      puts "Unable to compute potential return due to an error."
    end
  rescue ArgumentError => e
    puts "Invalid input: #{e.message}. Please restart the program and provide valid values."
  rescue StandardError => e
    puts "An unexpected error occurred: #{e.message}"
  end
end

# Run the main program
main
```
