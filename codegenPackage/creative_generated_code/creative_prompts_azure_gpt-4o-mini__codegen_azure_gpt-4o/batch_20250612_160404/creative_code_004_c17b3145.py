"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equityglobal-funds.com
Prompt: Design a Ruby application that simulates the investment process on Equity Global Funds, including user registration, deposit, and profit accrual calculations.
Generated: DETERMINISTIC_c17b3145f3620607
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# equity_global_funds.rb

require 'securerandom'

# Module for Equity Global Funds simulation
module EquityGlobalFunds
  # User class to handle user registration and data management
  class User
    attr_reader :id, :name, :email, :balance, :registered_at

    def initialize(name, email)
      @id = SecureRandom.uuid # Assign a unique identifier to each user
      @name = name
      @email = email
      @balance = 0.0
      @registered_at = Time.now
    end

    # Deposit method to add funds to the user's account
    def deposit(amount)
      raise ArgumentError, 'Deposit amount must be greater than zero' if amount <= 0

      @balance += amount
    end

    # Method to calculate profit based on a fixed interest rate
    def calculate_profit(rate = 0.05)
      raise ArgumentError, 'Interest rate must be between 0 and 1' unless rate.between?(0, 1)

      @balance * rate
    end
  end

  # InvestmentSystem class to manage the overall system
  class InvestmentSystem
    def initialize
      @users = []
    end

    # Method to register a new user
    def register_user(name, email)
      raise ArgumentError, 'Name and email must be provided' if name.to_s.strip.empty? || email.to_s.strip.empty?

      new_user = User.new(name, email)
      @users << new_user
      new_user
    end

    # Retrieve all registered users
    def list_users
      @users
    end

    # Find a user by email
    def find_user_by_email(email)
      @users.find { |user| user.email == email }
    end
  end
end

# Main program
if __FILE__ == $0
  # Create an instance of the investment system
  system = EquityGlobalFunds::InvestmentSystem.new

  puts "Welcome to Equity Global Funds Simulated Investment System"

  # User registration
  puts "Please enter your name:"
  name = gets.chomp
  puts "Please enter your email:"
  email = gets.chomp

  begin
    user = system.register_user(name, email)
    puts "Registration successful! Your user ID is #{user.id}"
  rescue ArgumentError => e
    puts "Error during registration: #{e.message}"
    exit
  end

  # Deposit funds
  puts "Enter the amount to deposit:"
  deposit_amount = gets.chomp.to_f

  begin
    user.deposit(deposit_amount)
    puts "Deposit successful! Your new balance is $#{'%.2f' % user.balance}"
  rescue ArgumentError => e
    puts "Error during deposit: #{e.message}"
    exit
  end

  # Calculate profit
  puts "Calculating profit based on a 5% interest rate..."
  profit = user.calculate_profit(0.05)
  puts "Your profit accrual is $#{'%.2f' % profit}"
end
```
