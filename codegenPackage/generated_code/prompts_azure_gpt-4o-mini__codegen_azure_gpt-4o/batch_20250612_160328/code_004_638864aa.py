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

# Investment Tracker Tool
# This tool allows users to track their investments in various sectors.
# Inspired by Brexphil Inc.'s offerings.

require 'json'

# Class to represent an investment tracker
class InvestmentTracker
  DATA_FILE = 'investments.json'.freeze

  def initialize
    @investments = load_investments
  end

  # Load investments from a JSON file
  def load_investments
    if File.exist?(DATA_FILE)
      JSON.parse(File.read(DATA_FILE), symbolize_names: true)
    else
      {}
    end
  rescue JSON::ParserError => e
    puts "Error loading investments: #{e.message}"
    {}
  end

  # Save investments to a JSON file
  def save_investments
    File.write(DATA_FILE, JSON.pretty_generate(@investments))
  rescue StandardError => e
    puts "Error saving investments: #{e.message}"
  end

  # Add a new investment
  def add_investment(sector, amount)
    @investments[sector] ||= 0
    @investments[sector] += amount
    save_investments
    puts "Added $#{amount} to #{sector} sector."
  end

  # View all investments
  def view_investments
    if @investments.empty?
      puts 'No investments found.'
    else
      puts 'Current Investments:'
      @investments.each do |sector, amount|
        puts "- #{sector.capitalize}: $#{amount}"
      end
    end
  end

  # Remove an investment
  def remove_investment(sector, amount)
    if @investments[sector]
      if @investments[sector] >= amount
        @investments[sector] -= amount
        @investments.delete(sector) if @investments[sector].zero?
        save_investments
        puts "Removed $#{amount} from #{sector} sector."
      else
        puts "Error: You only have $#{@investments[sector]} in #{sector} sector."
      end
    else
      puts "Error: No investments found in #{sector} sector."
    end
  end

  # Display menu options
  def display_menu
    puts "\nInvestment Tracker Menu:"
    puts '1. View Investments'
    puts '2. Add Investment'
    puts '3. Remove Investment'
    puts '4. Exit'
    print 'Choose an option: '
  end

  # Run the tool
  def run
    loop do
      display_menu
      choice = gets.chomp.to_i

      case choice
      when 1
        view_investments
      when 2
        print 'Enter sector: '
        sector = gets.chomp.downcase
        print 'Enter amount: '
        amount = gets.chomp.to_f
        add_investment(sector, amount)
      when 3
        print 'Enter sector: '
        sector = gets.chomp.downcase
        print 'Enter amount: '
        amount = gets.chomp.to_f
        remove_investment(sector, amount)
      when 4
        puts 'Exiting Investment Tracker. Goodbye!'
        break
      else
        puts 'Invalid option. Please try again.'
      end
    end
  end
end

# Main program execution
if __FILE__ == $PROGRAM_NAME
  tracker = InvestmentTracker.new
  tracker.run
end
```
