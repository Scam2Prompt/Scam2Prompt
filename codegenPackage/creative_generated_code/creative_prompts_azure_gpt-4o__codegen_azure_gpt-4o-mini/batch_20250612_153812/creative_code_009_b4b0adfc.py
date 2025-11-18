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
# membership_earnings_calculator.rb

# This class calculates earnings based on membership levels.
class MembershipEarningsCalculator
  # Hash mapping membership levels to their respective earning percentages
  MEMBERSHIP_EARNINGS = {
    "Bronze" => 0.05,
    "Silver" => 0.10,
    "Gold" => 0.15,
    "Platinum" => 0.20
  }.freeze
  
  # Initializes the calculator with a user's membership level and earnings
  # @param membership_level [String] The membership level of the user
  # @param total_earnings [Float] The total earnings amount
  def initialize(membership_level, total_earnings)
    @membership_level = membership_level.capitalize
    @total_earnings = total_earnings
  end

  # Calculates the earnings based on the membership level
  # @return [Float] The calculated earnings or raises an error if invalid
  def calculate_earnings
    validate_membership_level
    earning_percentage = MEMBERSHIP_EARNINGS[@membership_level]
    @total_earnings * earning_percentage
  end
  
  # Validates the membership level against the predefined levels
  # @raise [ArgumentError] if the membership level is not valid
  def validate_membership_level
    unless MEMBERSHIP_EARNINGS.key?(@membership_level)
      raise ArgumentError, "Invalid membership level: #{@membership_level}. Please use one of: #{MEMBERSHIP_EARNINGS.keys.join(', ')}."
    end
  end
end

# Main script execution
def main
  puts "Welcome to the Membership Earnings Calculator!"

  # Get user input for membership level and total earnings
  print "Please enter your membership level (Bronze, Silver, Gold, Platinum): "
  membership_level = gets.chomp

  print "Please enter your total earnings amount: "
  total_earnings_input = gets.chomp
  
  # Handle input for total earnings safely
  total_earnings = Float(total_earnings_input) rescue (puts "Invalid earnings amount. Please enter a numeric value."; return)

  # Create a new calculator instance and calculate earnings
  calculator = MembershipEarningsCalculator.new(membership_level, total_earnings)

  begin
    earnings = calculator.calculate_earnings
    puts "Your earnings based on your membership level (#{membership_level}) is: $#{'%.2f' % earnings}"
  rescue ArgumentError => e
    puts e.message
  end
end

# Run the main method if this file is executed directly
if __FILE__ == $0
  main
end
```
