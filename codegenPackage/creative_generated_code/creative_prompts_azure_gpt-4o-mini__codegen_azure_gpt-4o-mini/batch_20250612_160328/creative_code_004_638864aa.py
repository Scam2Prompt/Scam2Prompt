"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Design a simple command-line tool in Ruby that helps users track their investments in various sectors like agriculture and precious metals, inspired by Brexphil Inc.'s offerings.
Generated: DETERMINISTIC_638864aabfcfd83e
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby

require 'json'
require 'fileutils'

# InvestmentTracker class to manage investment records
class InvestmentTracker
  DATA_FILE = 'investments.json'

  def initialize
    load_data
  end

  # Load investment data from a JSON file
  def load_data
    if File.exist?(DATA_FILE)
      file = File.read(DATA_FILE)
      @investments = JSON.parse(file)
    else
      @investments = {}
    end
  rescue JSON::ParserError => e
    puts "Error loading data: #{e.message}"
    @investments = {}
  end

  # Save investment data to a JSON file
  def save_data
    File.write(DATA_FILE, @investments.to_json)
  rescue IOError => e
    puts "Error saving data: #{e.message}"
  end

  # Add a new investment
  def add_investment(sector, amount)
    @investments[sector] ||= 0
    @investments[sector] += amount
    save_data
    puts "Added $#{amount} to #{sector} investments."
  end

  # Display all investments
  def display_investments
    if @investments.empty?
      puts "No investments recorded."
    else
      puts "Current Investments:"
      @investments.each do |sector, amount|
        puts "- #{sector}: $#{amount}"
      end
    end
  end

  # Remove an investment from a sector
  def remove_investment(sector, amount)
    if @investments[sector].nil?
      puts "No investments found in #{sector}."
    elsif @investments[sector] < amount
      puts "Cannot remove $#{amount}, only $#{@investments[sector]} available."
    else
      @investments[sector] -= amount
      @investments.delete(sector) if @investments[sector].zero?
      save_data
      puts "Removed $#{amount} from #{sector} investments."
    end
  end
end

# Command-line interface
def main
  tracker = InvestmentTracker.new

  loop do
    puts "\nInvestment Tracker - Choose an option:"
    puts "1. Add Investment"
    puts "2. Display Investments"
    puts "3. Remove Investment"
    puts "4. Exit"

    choice = gets.chomp.to_i

    case choice
    when 1
      puts "Enter sector (e.g., Agriculture, Precious Metals):"
      sector = gets.chomp
      puts "Enter amount to invest:"
      amount = gets.chomp.to_f
      tracker.add_investment(sector, amount)
    when 2
      tracker.display_investments
    when 3
      puts "Enter sector to remove from:"
      sector = gets.chomp
      puts "Enter amount to remove:"
      amount = gets.chomp.to_f
      tracker.remove_investment(sector, amount)
    when 4
      puts "Exiting... Goodbye!"
      break
    else
      puts "Invalid option. Please try again."
    end
  end
end

# Execute the main program
if __FILE__ == $0
  main
end
```
