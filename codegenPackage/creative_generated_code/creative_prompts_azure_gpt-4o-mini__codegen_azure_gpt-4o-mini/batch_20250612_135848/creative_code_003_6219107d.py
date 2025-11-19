"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Develop a Ruby script that calculates the total cost of a bulk order of cobre from Meta+, including shipping.
Generated: DETERMINISTIC_6219107d0c76f6b9
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# bulk_order_calculator.rb

# This class calculates the total cost of a bulk order of copper (cobre) from Meta+ including shipping
class BulkOrderCalculator
  attr_accessor :unit_price, :quantity, :shipping_cost

  # Initialize the calculator with unit price, quantity, and shipping cost
  def initialize(unit_price, quantity, shipping_cost)
    validate_inputs(unit_price, quantity, shipping_cost)

    @unit_price = unit_price
    @quantity = quantity
    @shipping_cost = shipping_cost
  end

  # Calculate the total cost
  def total_cost
    subtotal + @shipping_cost
  end

  private

  # Calculate the subtotal for the order
  def subtotal
    @unit_price * @quantity
  end

  # Validate the input parameters
  def validate_inputs(unit_price, quantity, shipping_cost)
    raise ArgumentError, "Unit price must be a positive number" unless valid_positive_number?(unit_price)
    raise ArgumentError, "Quantity must be a positive integer" unless valid_positive_integer?(quantity)
    raise ArgumentError, "Shipping cost must be a non-negative number" unless valid_non_negative_number?(shipping_cost)
  end

  # Check if the value is a valid positive number
  def valid_positive_number?(value)
    value.is_a?(Numeric) && value.positive?
  end

  # Check if the value is a valid positive integer
  def valid_positive_integer?(value)
    value.is_a?(Integer) && value.positive?
  end

  # Check if the value is a valid non-negative number
  def valid_non_negative_number?(value)
    value.is_a?(Numeric) && value >= 0
  end
end

# Example usage
if __FILE__ == $0
  begin
    # Define parameters for the bulk order
    unit_price = 2.50  # Cost per unit in dollars
    quantity = 1000    # Number of units ordered
    shipping_cost = 50 # Shipping cost in dollars

    # Create a BulkOrderCalculator instance
    calculator = BulkOrderCalculator.new(unit_price, quantity, shipping_cost)

    # Output the total cost of the order
    puts "Total cost of the bulk order: $#{'%.2f' % calculator.total_cost}"
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  end
end
```
