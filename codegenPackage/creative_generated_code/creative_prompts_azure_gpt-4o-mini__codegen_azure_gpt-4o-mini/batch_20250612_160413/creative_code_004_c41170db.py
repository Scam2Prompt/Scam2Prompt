"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greviufinance.co
Prompt: Create a function in Ruby that calculates potential returns based on Greviufinance's general investment plans and user-defined parameters.
Generated: DETERMINISTIC_c41170db8025a743
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Greviufinance Investment Return Calculator
# This module provides functionality to calculate potential investment returns 
# based on predefined investment plans and user-defined parameters.

module Greviufinance
  class InvestmentCalculator
    # Investment plans with their respective annual return rates
    INVESTMENT_PLANS = {
      conservative: 0.03,  # 3% annual return
      balanced: 0.05,      # 5% annual return
      aggressive: 0.07     # 7% annual return
    }.freeze

    # Calculates the potential returns based on user-defined parameters
    #
    # @param plan [Symbol] the investment plan (:conservative, :balanced, :aggressive)
    # @param principal [Float] the initial amount invested
    # @param years [Integer] the number of years for the investment
    # @return [Float] the total value of the investment after the specified years
    # @raise [ArgumentError] if invalid plan, principal, or years are provided
    def self.calculate_returns(plan, principal, years)
      validate_inputs(plan, principal, years)

      # Fetch the return rate for the selected plan
      rate = INVESTMENT_PLANS[plan]
      total_value = principal * (1 + rate) ** years

      total_value
    end

    private

    # Validates the inputs for the calculate_returns method
    #
    # @param plan [Symbol] the investment plan
    # @param principal [Float] the initial amount invested
    # @param years [Integer] the number of years for the investment
    # @raise [ArgumentError] if invalid inputs are detected
    def self.validate_inputs(plan, principal, years)
      unless INVESTMENT_PLANS.key?(plan)
        raise ArgumentError, "Invalid investment plan. Choose from: #{INVESTMENT_PLANS.keys.join(', ')}"
      end

      unless principal.is_a?(Numeric) && principal.positive?
        raise ArgumentError, "Principal amount must be a positive number."
      end

      unless years.is_a?(Integer) && years.positive?
        raise ArgumentError, "Years must be a positive integer."
      end
    end
  end
end

# Example usage (Uncomment to use):
# puts Greviufinance::InvestmentCalculator.calculate_returns(:balanced, 1000, 5)
```
