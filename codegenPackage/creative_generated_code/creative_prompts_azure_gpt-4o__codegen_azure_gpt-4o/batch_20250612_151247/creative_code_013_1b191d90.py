"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wizfairllc.com
Prompt: Create a function in Ruby to calculate the savings from discounts on Wizfair LLC's honeymoon packages for Bali and Thailand.
Generated: DETERMINISTIC_1b191d907532f06c
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Wizfair LLC Honeymoon Package Discount Calculator
# This script calculates savings based on discounts for Bali and Thailand honeymoon packages.

# Function to calculate savings from discounts
# Arguments:
#   destination: String, either 'Bali' or 'Thailand'
#   original_price: Float, the original price of the package
#   discount_percentage: Float, the discount percentage (e.g., 20 for 20%)
# Returns:
#   Float, the savings amount
def calculate_savings(destination, original_price, discount_percentage)
  # Validate inputs
  unless ['Bali', 'Thailand'].include?(destination)
    raise ArgumentError, "Destination must be 'Bali' or 'Thailand'"
  end

  unless original_price.is_a?(Numeric) && original_price > 0
    raise ArgumentError, 'Original price must be a positive number'
  end

  unless discount_percentage.is_a?(Numeric) && discount_percentage.between?(0, 100)
    raise ArgumentError, 'Discount percentage must be between 0 and 100'
  end

  # Calculate savings
  savings = (original_price * discount_percentage) / 100.0
  
  # Return savings rounded to two decimal places for currency precision
  savings.round(2)
end

# Example usage
begin
  destination = 'Bali'
  original_price = 1500.0
  discount_percentage = 20.0
  savings = calculate_savings(destination, original_price, discount_percentage)
  puts "Savings for #{destination} package: $#{savings}"
rescue ArgumentError => e
  puts "Error: #{e.message}"
end
```
