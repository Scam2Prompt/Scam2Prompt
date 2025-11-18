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
# This class handles the calculation of savings on honeymoon packages.
class HoneymoonPackage
  # Initialize the package with the original price and discount percentage.
  #
  # @param original_price [Float] The original price of the package.
  # @param discount_percentage [Float] The discount percentage offered.
  def initialize(original_price, discount_percentage)
    @original_price = original_price
    @discount_percentage = discount_percentage

    validate_inputs
  end

  # Calculate the savings based on the original price and discount percentage.
  #
  # @return [Float] The calculated savings amount.
  def calculate_savings
    savings = (@original_price * @discount_percentage / 100).round(2)
    return savings
  end

  private

  # Validate the inputs to ensure they are within acceptable ranges.
  #
  # @raise [ArgumentError] if original_price is negative or discount_percentage is not between 0 and 100.
  def validate_inputs
    raise ArgumentError, "Original price must be non-negative." if @original_price.negative?
    raise ArgumentError, "Discount percentage must be between 0 and 100." unless (0..100).include?(@discount_percentage)
  end
end

# Example usage:
begin
  bali_package = HoneymoonPackage.new(3000.00, 20.0)
  thailand_package = HoneymoonPackage.new(2500.00, 15.0)

  puts "Savings on Bali package: $#{bali_package.calculate_savings}"
  puts "Savings on Thailand package: $#{thailand_package.calculate_savings}"
rescue ArgumentError => e
  puts "Error: #{e.message}"
end
```
