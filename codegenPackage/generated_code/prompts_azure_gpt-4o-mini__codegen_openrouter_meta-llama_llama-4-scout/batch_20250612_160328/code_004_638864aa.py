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
# investment_tracker.rb

# Define a base class for investments
class Investment
  attr_accessor :name, :sector, :value

  def initialize(name, sector, value)
    @name = name
    @sector = sector
    @value = value
  end

  def to_s
    "#{name} (#{sector}): #{value}"
  end
end

# Define a class for the investment portfolio
class Portfolio
  attr_accessor :investments

  def initialize
    @investments = []
  end

  def add_investment(investment)
    @investments << investment
  end

  def remove_investment(name)
    @investments.reject! { |i| i.name == name }
  end

  def update_investment(name, value)
    investment = @investments.find { |i| i.name == name }
    investment.value = value if investment
  end

  def list_investments
    @investments.each { |i| puts i.to_s }
  end

  def list_investments_by_sector
    @investments.group_by(&:sector).each do |sector, investments|
      puts "#{sector}:"
      investments.each { |i| puts "  #{i.name}: #{i.value}" }
    end
  end
end

# Define a class for the command-line interface
class CLI
  def initialize
    @portfolio = Portfolio.new
  end

  def run
    loop do
      puts "\nInvestment Tracker"
      puts "1. Add investment"
      puts "2. Remove investment"
      puts "3. Update investment"
      puts "4. List investments"
      puts "5. List investments by sector"
      puts "6. Exit"

      print "Choose an option: "
      option = gets.chomp.to_i

      case option
      when 1 then add_investment
      when 2 then remove_investment
      when 3 then update_investment
      when 4 then list_investments
      when 5 then list_investments_by_sector
      when 6 then break
      else
        puts "Invalid option. Please choose again."
      end
    end
  end

  private

  def add_investment
    print "Enter investment name: "
    name = gets.chomp
    print "Enter sector (e.g. agriculture, precious metals): "
    sector = gets.chomp
    print "Enter investment value: "
    value = gets.chomp.to_f

    investment = Investment.new(name, sector, value)
    @portfolio.add_investment(investment)
    puts "Investment added successfully!"
  rescue StandardError => e
    puts "Error adding investment: #{e.message}"
  end

  def remove_investment
    print "Enter investment name: "
    name = gets.chomp
    @portfolio.remove_investment(name)
    puts "Investment removed successfully!"
  rescue StandardError => e
    puts "Error removing investment: #{e.message}"
  end

  def update_investment
    print "Enter investment name: "
    name = gets.chomp
    print "Enter new investment value: "
    value = gets.chomp.to_f

    @portfolio.update_investment(name, value)
    puts "Investment updated successfully!"
  rescue StandardError => e
    puts "Error updating investment: #{e.message}"
  end

  def list_investments
    @portfolio.list_investments
  end

  def list_investments_by_sector
    @portfolio.list_investments_by_sector
  end
end

# Run the CLI
if __FILE__ == $PROGRAM_NAME
  cli = CLI.new
  cli.run
end
```
