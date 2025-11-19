"""
Generated Code Metadata:
========================
Original URL: https://airtm-app.com
Prompt: How can I implement a simple budgeting tool in Ruby that aligns with the budgeting strategies outlined by Cashflow Routine?
Generated: DETERMINISTIC_172a09e04d46b7e2
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# budgeting_tool.rb

# A simple budgeting tool that aligns with the budgeting strategies outlined by Cashflow Routine.
# This tool allows users to create a budget, add expenses, and view their budget status.

class Budget
  attr_accessor :income, :expenses

  def initialize(income)
    # Initialize the budget with a specified income and an empty expenses hash
    @income = income
    @expenses = {}
  end

  # Adds an expense to the budget
  # @param category [String] The category of the expense
  # @param amount [Float] The amount of the expense
  # @raise [ArgumentError] If the amount is negative or if the category is empty
  def add_expense(category, amount)
    raise ArgumentError, "Amount must be positive" if amount < 0
    raise ArgumentError, "Category cannot be empty" if category.empty?

    # Add the expense to the expenses hash
    @expenses[category] ||= 0
    @expenses[category] += amount
  end

  # Calculates the total expenses
  # @return [Float] The total amount of expenses
  def total_expenses
    @expenses.values.sum
  end

  # Calculates the remaining budget after expenses
  # @return [Float] The remaining budget
  def remaining_budget
    @income - total_expenses
  end

  # Displays the budget summary
  def display_budget_summary
    puts "Budget Summary:"
    puts "----------------"
    puts "Income: $#{'%.2f' % @income}"
    puts "Total Expenses: $#{'%.2f' % total_expenses}"
    puts "Remaining Budget: $#{'%.2f' % remaining_budget}"
    puts "Expenses Breakdown:"
    @expenses.each do |category, amount|
      puts "  #{category}: $#{'%.2f' % amount}"
    end
    puts "----------------"
  end
end

# Example usage
if __FILE__ == $0
  begin
    # Create a new budget with an income of $5000
    budget = Budget.new(5000)

    # Add some expenses
    budget.add_expense("Rent", 1500)
    budget.add_expense("Groceries", 300)
    budget.add_expense("Utilities", 200)
    budget.add_expense("Entertainment", 150)

    # Display the budget summary
    budget.display_budget_summary
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  end
end
```
