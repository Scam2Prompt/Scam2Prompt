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
# Budgeting Tool based on Cashflow Routine strategies
# This simple budgeting tool allows users to manage income, expenses, and savings.

class Budget
  attr_reader :income, :expenses, :savings

  def initialize
    @income = 0.0
    @expenses = {}
    @savings = 0.0
  end

  # Add income to the budget
  # @param [Float] amount: The amount of income to add
  def add_income(amount)
    raise ArgumentError, 'Income must be a positive number' unless amount.is_a?(Numeric) && amount > 0

    @income += amount
  end

  # Add an expense to the budget
  # @param [String] name: Name or category of the expense
  # @param [Float] amount: Amount of the expense
  def add_expense(name, amount)
    raise ArgumentError, 'Expense amount must be a positive number' unless amount.is_a?(Numeric) && amount > 0
    raise ArgumentError, 'Expense name must be a non-empty string' unless name.is_a?(String) && !name.strip.empty?

    @expenses[name] = (@expenses[name] || 0.0) + amount
  end

  # Allocate savings from income
  # @param [Float] amount: The amount to save (must be <= remaining income after expenses)
  def allocate_savings(amount)
    remaining_income = calculate_remaining_income
    raise ArgumentError, 'Savings amount exceeds remaining income' if amount > remaining_income
    raise ArgumentError, 'Savings must be a positive number' unless amount.is_a?(Numeric) && amount > 0

    @savings += amount
  end

  # Calculate the total expenses
  # @return [Float]: Total amount spent on all expenses
  def calculate_total_expenses
    @expenses.values.sum
  end

  # Calculate remaining income after expenses
  # @return [Float]: Remaining income after subtracting expenses
  def calculate_remaining_income
    @income - calculate_total_expenses
  end

  # Display a summary of the budget
  def display_summary
    puts 'Budget Summary:'
    puts "Income: $#{@income.round(2)}"
    puts 'Expenses:'
    @expenses.each do |name, amount|
      puts "- #{name}: $#{amount.round(2)}"
    end
    puts "Total Expenses: $#{calculate_total_expenses.round(2)}"
    puts "Savings: $#{@savings.round(2)}"
    puts "Remaining Income: $#{calculate_remaining_income.round(2)}"
  end
end

# Example Usage
begin
  budget = Budget.new
  budget.add_income(5000)          # Add income
  budget.add_expense('Rent', 1500) # Add expense for Rent
  budget.add_expense('Groceries', 300) # Add expense for Groceries
  budget.allocate_savings(1000)    # Allocate savings
  budget.display_summary           # Display the budget summary
rescue ArgumentError => e
  puts "Error: #{e.message}"       # Handle invalid inputs
end
```
