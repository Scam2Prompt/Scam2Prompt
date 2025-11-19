"""
Generated Code Metadata:
========================
Original URL: https://wizfairllc.com
Prompt: Create a function in Ruby to calculate the savings from discounts on Wizfair LLC's honeymoon packages for Bali and Thailand.
Generated: DETERMINISTIC_1b191d907532f06c
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

module WizfairLLC
  # Calculates savings from discounts on honeymoon packages
  class HoneymoonDiscountCalculator
    # Discount rates for different destinations
    DISCOUNT_RATES = {
      bali: 0.15,   # 15% discount for Bali packages
      thailand: 0.20 # 20% discount for Thailand packages
    }.freeze

    # Calculates the savings amount based on package price and destination
    # @param package_price [Numeric] The original price of the package
    # @param destination [Symbol] The destination (:bali or :thailand)
    # @return [Numeric] The amount saved from the discount
    # @raise [ArgumentError] If invalid arguments are provided
    def self.calculate_savings(package_price, destination)
      validate_inputs(package_price, destination)

      discount_rate = DISCOUNT_RATES.fetch(destination)
      package_price * discount_rate
    end

    # Validates input parameters
    # @param package_price [Numeric] The package price to validate
    # @param destination [Symbol] The destination to validate
    # @raise [ArgumentError] If any validation fails
    def self.validate_inputs(package_price, destination)
      unless package_price.is_a?(Numeric) && package_price.positive?
        raise ArgumentError, 'Package price must be a positive number'
      end

      unless DISCOUNT_RATES.key?(destination)
        raise ArgumentError, "Invalid destination. Must be one of: #{DISCOUNT_RATES.keys.join(', ')}"
      end
    end
    private_class_method :validate_inputs
  end
end
```
