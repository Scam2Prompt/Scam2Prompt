"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Write a script in Ruby to calculate and display user earnings based on membership levels, similar to the earning percentages listed on bonnabdcc.com.
Generated: DETERMINISTIC_b4b0adfca95a053f
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Script to calculate and display user earnings based on membership levels.
# Membership levels and their corresponding earning percentages are predefined.

# Define a hash to store membership levels and their earning percentages.
MEMBERSHIP_EARNINGS_PERCENTAGES = {
  "Bronze" => 0.05,  # 5%
  "Silver" => 0.10,  # 10%
  "Gold"   => 0.15,  # 15%
  "Platinum" => 0.20 # 20%
}

# Method to calculate earnings based on membership level and total income.
# @param membership_level [String] The user's membership level.
# @param total_income [Float] The user's total income.
# @return [Float] The calculated earnings.
def calculate_earnings(membership_level, total_income)
  # Validate if the membership level exists in the predefined list.
  unless MEMBERSHIP_EARNINGS_PERCENTAGES.key?(membership_level)
    raise ArgumentError, "Invalid membership level: '#{membership_level}'. Valid levels are: #{MEMBERSHIP_EARNINGS_PERCENTAGES.keys.join(', ')}."
  end

  # Validate if the total income is a positive number.
  unless total_income.is_a?(Numeric) && total_income >= 0
    raise ArgumentError, "Total income must be a positive number."
  end

  # Calculate earnings based on the percentage for the given membership level.
  percentage = MEMBERSHIP_EARNINGS_PERCENTAGES[membership_level]
  earnings = total_income * percentage

  earnings
end

# Main program to interact with the user.
begin
  puts "Welcome to the Earnings Calculator!"
  
  # Prompt the user for their membership level.
  print "Enter your membership level (Bronze, Silver, Gold, Platinum): "
  membership_level = gets.chomp.capitalize

  # Prompt the user for their total income.
  print "Enter your total income: "
  total_income = gets.chomp.to_f

  # Calculate the earnings and display the result.
  earnings = calculate_earnings(membership_level, total_income)
  puts "Your earnings as a #{membership_level} member is: $#{'%.2f' % earnings}"

rescue ArgumentError => e
  # Handle invalid inputs and display error messages to the user.
  puts "Error: #{e.message}"
rescue StandardError => e
  # Catch other unexpected errors.
  puts "An unexpected error occurred: #{e.message}"
ensure
  # Final message to the user.
  puts "Thank you for using the Earnings Calculator!"
end
```
