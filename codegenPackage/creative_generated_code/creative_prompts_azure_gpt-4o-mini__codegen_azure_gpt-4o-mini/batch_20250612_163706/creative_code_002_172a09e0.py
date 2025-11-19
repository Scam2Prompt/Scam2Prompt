"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: How can I implement a simple budgeting tool in Ruby that aligns with the budgeting strategies outlined by Cashflow Routine?
Generated: DETERMINISTIC_172a09e04d46b7e2
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Simple Budgeting Tool in Ruby
# This tool allows users to manage their budget based on Cashflow Routine strategies.

class Budget
  attr_accessor :income, :expenses, :savings, :debt

  # Initializes the Budget instance with income, expenses, savings, and debt.
  def initialize(income, expenses = 0, savings = 0, debt = 0)
    @income = income
    @expenses = expenses
    @savings = savings
    @debt = debt
  end

  # Calculate the net income after expenses, savings, and debt payments
  def net_income
    @income - @expenses - @savings - @debt
  end

  # Add a new expense
  def add_expense(amount)
    raise ArgumentError, 'Amount must be greater than zero' if amount <= 0
    @expenses += amount
  end

  # Record a saving amount
  def add_saving(amount)
    raise ArgumentError, 'Amount must be greater than zero' if amount <= 0
    @savings += amount
  end

  # Pay off a debt amount
  def pay_debt(amount)
    raise ArgumentError, 'Amount must be greater than zero' if amount <= 0
    raise ArgumentError, 'Insufficient debt to pay' if amount > @debt
    @debt -= amount
  end

  # Generate a summary of the budget
  def summary
    {
      income: @income,
      expenses: @expenses,
      savings: @savings,
      debt: @debt,
      net_income: net_income
    }
  end
end

# Example usage:
begin
  # Create a new budget
  my_budget = Budget.new(5000)

  # Adding expenses, savings, and payments
  my_budget.add_expense(1500)   # Rent
  my_budget.add_expense(300)     # Utilities
  my_budget.add_saving(500)      # Savings Contribution
  my_budget.pay_debt(200)        # Debt Payment

  # Print budget summary
  puts "Budget Summary:"
  puts my_budget.summary
rescue ArgumentError => e
  puts "Error: #{e.message}"
end
```
