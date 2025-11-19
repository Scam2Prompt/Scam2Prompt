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
# Investment Comparison Program
# This program compares the risks and benefits of investing in antique coins, real estate, and stocks.
# It provides a summary based on user input and general investment principles.

# Define a class for investments
class Investment
  attr_reader :name, :risk_level, :average_return

  # Constructor method to initialize investment properties
  def initialize(name, risk_level, average_return)
    @name = name
    @risk_level = risk_level
    @average_return = average_return
  end

  # Method to display the summary of an investment
  def summary
    <<~SUMMARY
      Investment: #{@name}
      Risk Level: #{@risk_level}
      Average Return: #{@average_return}%
    SUMMARY
  end
end

# Error handling for invalid user inputs
class InvalidInputError < StandardError; end

# Main program logic
class InvestmentComparison
  # Initialize investments with preset data
  def initialize
    @investments = [
      Investment.new("Antique Coins", "Medium", 6.0), # Example values
      Investment.new("Real Estate", "Low", 4.5),
      Investment.new("Stocks", "High", 8.0)
    ]
  end

  # Display all investments
  def display_investments
    puts "\nAvailable Investments:"
    @investments.each_with_index do |investment, index|
      puts "#{index + 1}. #{investment.name}"
    end
  end

  # Compare investments and return details for user-selected choices
  def compare_investments
    display_investments

    # Prompt user for comparison selection
    print "\nEnter the numbers of the investments you want to compare (comma-separated): "
    input = gets.chomp

    # Validate and process user input
    begin
      indices = input.split(",").map { |i| Integer(i.strip) - 1 }
      validate_indices(indices)
      show_comparison(indices)
    rescue InvalidInputError => e
      puts "\nError: #{e.message}. Please try again."
      compare_investments
    rescue ArgumentError
      puts "\nError: Invalid input format. Please enter numbers separated by commas."
      compare_investments
    end
  end

  private

  # Validate user input indices
  def validate_indices(indices)
    indices.each do |index|
      raise InvalidInputError, "Index #{index + 1} is out of range" unless index.between?(0, @investments.size - 1)
    end
  end

  # Display comparison of selected investments
  def show_comparison(indices)
    puts "\nComparison Summary:"
    indices.each do |index|
      puts @investments[index].summary
    end

    puts "\nGeneral Guidance:"
    puts "1. Antique Coins: Collectible items that can appreciate due to rarity but may require expertise."
    puts "2. Real Estate: Tangible asset offering stable returns, suitable for risk-averse investors."
    puts "3. Stocks: High potential returns but involve volatility; requires careful market analysis."
  end
end

# Entry point for the program
if __FILE__ == $0
  puts "Investment Risks and Benefits Comparison Tool"
  comparison_tool = InvestmentComparison.new
  comparison_tool.compare_investments
end
```
