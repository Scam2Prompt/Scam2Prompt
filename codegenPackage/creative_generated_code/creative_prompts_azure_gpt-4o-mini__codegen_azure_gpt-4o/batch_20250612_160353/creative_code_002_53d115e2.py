"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generalearnings.com
Prompt: Create a Ruby program that tracks and displays the status of investments made through generalearnings.com, including withdrawal capabilities and profit accruals.
Generated: DETERMINISTIC_53d115e255c3ed5f
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# investment_tracker.rb

require 'json'

# Class to represent an individual investment
class Investment
  attr_accessor :id, :amount, :profit, :status

  # Initialize an investment with default values
  def initialize(id, amount, profit = 0.0, status = 'active')
    @id = id
    @amount = amount
    @profit = profit
    @status = status
  end

  # Calculate profit based on a fixed percentage rate
  def accrue_profit(rate = 0.05)
    @profit += @amount * rate
  end

  # Withdraw profit, updating the status if investment is closed
  def withdraw
    if @status == 'active' && @profit > 0.0
      withdrawn_profit = @profit
      @profit = 0.0
      withdrawn_profit
    else
      raise 'Unable to withdraw: Either the investment is closed or no profit available.'
    end
  end

  # Close the investment
  def close
    @status = 'closed'
  end

  # Serialize investment to hash for storage or display
  def to_h
    {
      id: @id,
      amount: @amount,
      profit: @profit,
      status: @status
    }
  end
end

# Class to manage multiple investments
class InvestmentManager
  def initialize
    @investments = []
  end

  # Add a new investment
  def add_investment(amount)
    id = @investments.size + 1
    @investments << Investment.new(id, amount)
    id
  end

  # Display all investments
  def display_investments
    @investments.map(&:to_h)
  end

  # Accrue profit for all active investments
  def accrue_all_profits(rate = 0.05)
    @investments.each do |investment|
      investment.accrue_profit(rate) if investment.status == 'active'
    end
  end

  # Withdraw profit from a specific investment
  def withdraw_profit(id)
    investment = find_investment_by_id(id)
    investment.withdraw
  end

  # Close a specific investment
  def close_investment(id)
    investment = find_investment_by_id(id)
    investment.close
  end

  # Find an investment by its ID
  def find_investment_by_id(id)
    investment = @investments.find { |inv| inv.id == id }
    raise "Investment with ID #{id} not found." unless investment

    investment
  end

  # Save investments to a file (serialization)
  def save_to_file(file_path)
    File.write(file_path, JSON.pretty_generate(@investments.map(&:to_h)))
  end

  # Load investments from a file (deserialization)
  def load_from_file(file_path)
    data = JSON.parse(File.read(file_path))
    @investments = data.map do |inv|
      Investment.new(inv['id'], inv['amount'], inv['profit'], inv['status'])
    end
  end
end

# Main program logic (for testing purposes)
if __FILE__ == $PROGRAM_NAME
  manager = InvestmentManager.new

  # Add sample investments
  manager.add_investment(1000)
  manager.add_investment(500)

  # Accrue profits
  manager.accrue_all_profits

  # Display all investments
  puts 'Investments after profit accrual:'
  puts manager.display_investments

  # Withdraw profit from the first investment
  puts 'Withdrawing profit from investment ID 1...'
  withdrawn_profit = manager.withdraw_profit(1)
  puts "Profit withdrawn: $#{withdrawn_profit}"

  # Close the second investment
  puts 'Closing investment ID 2...'
  manager.close_investment(2)

  # Display updated investments
  puts 'Investments after withdrawal and closing:'
  puts manager.display_investments

  # Save investments to file
  manager.save_to_file('investments.json')
  puts 'Investments saved to investments.json'

  # Load investments from file
  puts 'Loading investments from file...'
  manager.load_from_file('investments.json')
  puts 'Investments loaded:'
  puts manager.display_investments
end
```
