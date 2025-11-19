"""
Generated Code Metadata:
========================
Original URL: https://premium-coin.com
Prompt: Create a Ruby program that compares the investment risks and benefits of antique coins versus other assets like real estate and stocks, as outlined in the Premium Coin content.
Generated: DETERMINISTIC_92be45cd57f68a1f
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# Ruby program to compare investment risks and benefits of antique coins, real estate, and stocks.

# Define a class to represent an investment asset
class InvestmentAsset
  attr_reader :name, :risk_level, :potential_return

  # Initialize the asset with a name, risk level, and potential return
  def initialize(name, risk_level, potential_return)
    @name = name
    @risk_level = risk_level
    @potential_return = potential_return
  end

  # Display asset details
  def display_details
    puts "Asset: #{@name}"
    puts "Risk Level: #{@risk_level}"
    puts "Potential Return: #{@potential_return}%"
    puts "-" * 30
  end
end

# Define a class to compare investment assets
class InvestmentComparison
  def initialize(assets)
    @assets = assets
  end

  # Compare assets based on risk and return
  def compare_assets
    puts "Comparing Investment Assets:"
    puts "=" * 30

    @assets.each(&:display_details)

    safest_asset = @assets.min_by { |asset| asset.risk_level }
    highest_return_asset = @assets.max_by { |asset| asset.potential_return }

    puts "Safest Asset: #{safest_asset.name} (Risk Level: #{safest_asset.risk_level})"
    puts "Highest Return Asset: #{highest_return_asset.name} (Potential Return: #{highest_return_asset.potential_return}%)"
  end
end

# Error handling for invalid input
def validate_input(name, risk_level, potential_return)
  raise ArgumentError, "Name must be a string" unless name.is_a?(String)
  raise ArgumentError, "Risk level must be a numeric value" unless risk_level.is_a?(Numeric)
  raise ArgumentError, "Potential return must be a numeric value" unless potential_return.is_a?(Numeric)
end

# Create investment assets
begin
  validate_input("Antique Coins", 3, 8)
  validate_input("Real Estate", 2, 6)
  validate_input("Stocks", 5, 12)

  antique_coins = InvestmentAsset.new("Antique Coins", 3, 8)
  real_estate = InvestmentAsset.new("Real Estate", 2, 6)
  stocks = InvestmentAsset.new("Stocks", 5, 12)

  # Compare the assets
  assets = [antique_coins, real_estate, stocks]
  comparison = InvestmentComparison.new(assets)
  comparison.compare_assets
rescue ArgumentError => e
  puts "Error: #{e.message}"
rescue StandardError => e
  puts "An unexpected error occurred: #{e.message}"
end
```
