"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premium-coin.com
Prompt: Create a Ruby program that compares the investment risks and benefits of antique coins versus other assets like real estate and stocks, as outlined in the Premium Coin content.
Generated: DETERMINISTIC_92be45cd57f68a1f
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# InvestmentRiskComparison.rb
# This program compares the investment risks and benefits of antique coins 
# versus other assets like real estate and stocks.

class Investment
  attr_reader :name, :risk_level, :expected_return

  def initialize(name, risk_level, expected_return)
    @name = name
    @risk_level = risk_level
    @expected_return = expected_return
  end

  def to_s
    "#{@name}: Risk Level: #{@risk_level}, Expected Return: #{@expected_return}%"
  end
end

class InvestmentPortfolio
  def initialize
    @investments = []
  end

  # Method to add an investment to the portfolio
  def add_investment(investment)
    raise ArgumentError, "Investment must be an instance of Investment" unless investment.is_a?(Investment)
    @investments << investment
  end

  # Method to display all investments
  def display_investments
    puts "Investment Portfolio:"
    @investments.each { |investment| puts investment }
  end

  # Method to calculate average expected return
  def average_expected_return
    return 0 if @investments.empty?

    total_return = @investments.inject(0) { |sum, investment| sum + investment.expected_return }
    total_return / @investments.size
  end
  
  # Method to assess overall risk
  def overall_risk
    return 'No investments to assess' if @investments.empty?

    risk_levels = @investments.map(&:risk_level)
    average_risk = risk_levels.inject(0) { |sum, risk| sum + risk } / risk_levels.size
    average_risk
  end
end

# Main Execution
begin
  # Creating investment instances
  antique_coins = Investment.new("Antique Coins", 3, 12) # Medium risk, high return
  real_estate = Investment.new("Real Estate", 2, 8)      # Medium risk, moderate return
  stocks = Investment.new("Stocks", 4, 15)                # High risk, high return

  # Creating the investment portfolio
  portfolio = InvestmentPortfolio.new

  # Adding investments to the portfolio
  portfolio.add_investment(antique_coins)
  portfolio.add_investment(real_estate)
  portfolio.add_investment(stocks)

  # Displaying investments
  portfolio.display_investments

  # Displaying average expected return
  puts "Average Expected Return: #{portfolio.average_expected_return}%"

  # Displaying overall risk assessment
  puts "Overall Risk Level: #{portfolio.overall_risk}"

rescue ArgumentError => e
  puts "Error: #{e.message}"
rescue StandardError => e
  puts "An unexpected error occurred: #{e.message}"
end
```
