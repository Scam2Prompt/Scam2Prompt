"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stether.us
Prompt: Create a function in Ruby that calculates the investment returns based on historical price data from JD.com’s financial reports.
Generated: DETERMINISTIC_6ce835ce96b00e56
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
require 'csv'

# Function to calculate investment returns based on historical price data from JD.com
# Input: file_path - Path to the CSV file containing historical price data
#        initial_investment - Amount of initial investment
# Output: Hash containing investment returns and percentage change
def calculate_investment_returns(file_path, initial_investment)
  begin
    # Read and parse the historical price data from the CSV file
    data = CSV.read(file_path, headers: true)

    # Validate that the CSV file has the required data
    raise ArgumentError, "CSV file must contain 'Date' and 'Close Price' columns" unless data.headers.include?('Date') && data.headers.include?('Close Price')

    # Extract the closing prices for the first and last trading days
    first_day_price = data[0]['Close Price'].to_f
    last_day_price = data[-1]['Close Price'].to_f

    # Validate that the closing prices are valid numbers
    raise ArgumentError, "Closing prices must be valid numeric values" if first_day_price <= 0 || last_day_price <= 0

    # Calculate the investment returns
    ending_balance = (initial_investment / first_day_price) * last_day_price
    profit_or_loss = ending_balance - initial_investment
    percentage_change = ((profit_or_loss / initial_investment) * 100).round(2)

    # Return the calculated results
    {
      initial_investment: initial_investment.round(2),
      ending_balance: ending_balance.round(2),
      profit_or_loss: profit_or_loss.round(2),
      percentage_change: percentage_change
    }
  rescue Errno::ENOENT
    # Handle file not found error
    raise "The file at '#{file_path}' could not be found. Please check the path and try again."
  rescue CSV::MalformedCSVError
    # Handle malformed CSV file error
    raise "The file provided is not a valid CSV file. Please check the format and try again."
  rescue ArgumentError => e
    # Handle argument-related errors
    raise e.message
  rescue StandardError => e
    # Catch any other unexpected errors
    raise "An unexpected error occurred: #{e.message}"
  end
end

# Example usage:
# file_path = 'jd_historical_prices.csv'
# initial_investment = 1000.0
# result = calculate_investment_returns(file_path, initial_investment)
# puts result
```
