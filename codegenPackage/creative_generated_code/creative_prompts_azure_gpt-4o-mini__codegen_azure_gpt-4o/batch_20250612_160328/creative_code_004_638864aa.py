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

# InvestmentTracker: A command-line tool to track investments across multiple sectors.
class InvestmentTracker
  attr_accessor :investments

  def initialize
    @investments = load_investments
  end

  # Load investments from a JSON file or initialize an empty hash if the file doesn't exist.
  def load_investments
    if File.exist?('investments.json')
      JSON.parse(File.read('investments.json'))
    else
      {}
    end
  rescue JSON::ParserError => e
    puts "Error loading investments file: #{e.message}"
    {}
  end

  # Save investments to a JSON file.
  def save_investments
    File.write('investments.json', JSON.pretty_generate(@investments))
  rescue IOError => e
    puts "Error saving investments file: #{e.message}"
  end

  # Add a new investment.
  def add_investment(sector, amount)
    @investments[sector] ||= 0
    @investments[sector] += amount
    puts "Added $#{amount} to the #{sector} sector."
    save_investments
  end

  # Display all investments.
  def display_investments
    if @investments.empty?
      puts 'No investments to display.'
    else
      puts 'Your investments:'
      @investments.each do |sector, amount|
        puts "- #{sector.capitalize}: $#{amount}"
      end
    end
  end

  # Remove an investment from a sector.
  def remove_investment(sector, amount)
    if @investments[sector]
      if @investments[sector] >= amount
        @investments[sector] -= amount
        @investments.delete(sector) if @investments[sector] == 0
        puts "Removed $#{amount} from the #{sector} sector."
        save_investments
      else
        puts "Error: You don't have enough funds in the #{sector} sector to remove $#{amount}."
      end
    else
      puts "Error: No investments found in the #{sector} sector."
    end
  end

  # Command-line menu for user interaction.
  def menu
    loop do
      puts "\nInvestment Tracker Menu:"
      puts "1. View Investments"
      puts "2. Add Investment"
      puts "3. Remove Investment"
      puts "4. Exit"
      print "Choose an option: "

      case gets.chomp
      when '1'
        display_investments
      when '2'
        print 'Enter sector (e.g., agriculture, precious metals): '
        sector = gets.chomp.downcase
        print 'Enter amount to invest: '
        amount = gets.chomp.to_f
        add_investment(sector, amount)
      when '3'
        print 'Enter sector to remove investment from: '
        sector = gets.chomp.downcase
        print 'Enter amount to remove: '
        amount = gets.chomp.to_f
        remove_investment(sector, amount)
      when '4'
        puts 'Exiting Investment Tracker. Goodbye!'
        break
      else
        puts 'Invalid option. Please try again.'
      end
    end
  end
end

# Start the application.
if __FILE__ == $0
  tracker = InvestmentTracker.new
  tracker.menu
end
```
