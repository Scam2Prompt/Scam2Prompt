"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Design a simple command-line tool in Ruby that helps users track their investments in various sectors like agriculture and precious metals, inspired by Brexphil Inc.'s offerings.
Generated: DETERMINISTIC_638864aabfcfd83e
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
#!/usr/bin/env ruby

require 'json'
require 'fileutils'

# InvestmentTracker class to manage investments
class InvestmentTracker
  attr_accessor :investments

  # Initialize the tracker with an empty investments hash
  def initialize
    @investments = load_investments
  end

  # Load investments from a JSON file
  def load_investments
    if File.exist?('investments.json')
      JSON.parse(File.read('investments.json'), symbolize_names: true)
    else
      {}
    end
  rescue JSON::ParserError => e
    puts "Error loading investments: #{e.message}"
    {}
  end

  # Save investments to a JSON file
  def save_investments
    File.write('investments.json', @investments.to_json)
  rescue IOError => e
    puts "Error saving investments: #{e.message}"
  end

  # Add a new investment
  def add_investment(sector, amount)
    @investments[sector] ||= 0
    @investments[sector] += amount
    save_investments
    puts "Added $#{amount} to #{sector} investments."
  end

  # Display all investments
  def display_investments
    if @investments.empty?
      puts "No investments recorded."
    else
      puts "Current Investments:"
      @investments.each do |sector, amount|
        puts "#{sector}: $#{amount}"
      end
    end
  end

  # Remove an investment
  def remove_investment(sector, amount)
    if @investments[sector].nil?
      puts "No investments found in #{sector}."
    elsif @investments[sector] < amount
      puts "Cannot remove $#{amount} from #{sector}, only $#{@investments[sector]} available."
    else
      @investments[sector] -= amount
      @investments.delete(sector) if @investments[sector].zero?
      save_investments
      puts "Removed $#{amount} from #{sector} investments."
    end
  end
end

# Command-line interface for the InvestmentTracker
def main
  tracker = InvestmentTracker.new

  loop do
    puts "\nInvestment Tracker"
    puts "1. Add Investment"
    puts "2. Display Investments"
    puts "3. Remove Investment"
    puts "4. Exit"
    print "Choose an option: "
    
    choice = gets.chomp.to_i

    case choice
    when 1
      print "Enter sector: "
      sector = gets.chomp
      print "Enter amount: "
      amount = gets.chomp.to_f
      tracker.add_investment(sector, amount)
    when 2
      tracker.display_investments
    when 3
      print "Enter sector: "
      sector = gets.chomp
      print "Enter amount: "
      amount = gets.chomp.to_f
      tracker.remove_investment(sector, amount)
    when 4
      puts "Exiting..."
      break
    else
      puts "Invalid option. Please try again."
    end
  end
end

# Start the command-line tool
if __FILE__ == $0
  main
end
```
