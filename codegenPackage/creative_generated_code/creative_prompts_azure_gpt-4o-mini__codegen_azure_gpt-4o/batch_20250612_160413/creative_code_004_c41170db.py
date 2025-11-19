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
# This module encapsulates functionality related to calculating investment returns
module GreviuFinance
  # Calculates potential investment returns based on GreviuFinance's general plans
  #
  # @param principal [Float] the initial amount invested
  # @param rate [Float] the annual interest rate in percentage (e.g., 5.0 for 5%)
  # @param years [Integer] the investment period in years
  # @param compounding_frequency [Integer] the number of times interest is compounded per year (e.g., 12 for monthly)
  # @return [Hash] a hash containing the total returns and the breakdown
  def self.calculate_returns(principal:, rate:, years:, compounding_frequency: 1)
    # Validate input
    raise ArgumentError, "Principal must be a positive number." unless principal.is_a?(Numeric) && principal > 0
    raise ArgumentError, "Rate must be a positive number." unless rate.is_a?(Numeric) && rate > 0
    raise ArgumentError, "Years must be a positive integer." unless years.is_a?(Integer) && years > 0
    raise ArgumentError, "Compounding frequency must be a positive integer." unless compounding_frequency.is_a?(Integer) && compounding_frequency > 0

    # Convert rate to a decimal (e.g., 5% -> 0.05)
    annual_rate = rate / 100.0

    # Formula for compound interest: A = P * (1 + r/n)^(n*t)
    total_amount = principal * (1 + annual_rate / compounding_frequency)**(compounding_frequency * years)

    # Calculate interest earned
    interest_earned = total_amount - principal

    # Return results as a hash
    {
      principal: principal,
      total_amount: total_amount.round(2),
      interest_earned: interest_earned.round(2),
      years: years,
      compounding_frequency: compounding_frequency
    }
  end
end

# Example usage:
# begin
#   result = GreviuFinance.calculate_returns(principal: 1000, rate: 5, years: 10, compounding_frequency: 12)
#   puts "Investment Details: #{result}"
# rescue ArgumentError => e
#   puts "Error: #{e.message}"
# end
```
