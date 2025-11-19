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
# Ruby script to calculate the total cost of a bulk order of cobre from Meta+, including shipping.

# Constants
PRICE_PER_UNIT = 50.0       # Price per unit of cobre in dollars
SHIPPING_COST_PER_UNIT = 5.0 # Shipping cost per unit in dollars
BULK_DISCOUNT_THRESHOLD = 100 # Number of units required for a bulk discount
BULK_DISCOUNT_RATE = 0.10    # Bulk discount rate (10%)

# Function to calculate the total cost
def calculate_total_cost(units_ordered)
  raise ArgumentError, "Units ordered must be a positive integer" unless units_ordered.is_a?(Integer) && units_ordered > 0
  
  # Calculate cost breakdown
  base_cost = units_ordered * PRICE_PER_UNIT
  shipping_cost = units_ordered * SHIPPING_COST_PER_UNIT
  
  # Apply bulk discount if applicable
  if units_ordered >= BULK_DISCOUNT_THRESHOLD
    discount = base_cost * BULK_DISCOUNT_RATE
  else
    discount = 0.0
  end
  
  # Total cost calculation
  total_cost = base_cost + shipping_cost - discount
  
  # Return a detailed breakdown
  {
    units_ordered: units_ordered,
    base_cost: base_cost,
    shipping_cost: shipping_cost,
    discount: discount,
    total_cost: total_cost
  }
end

# Main script
begin
  # Prompt user for input
  print "Enter the number of units to order: "
  units_ordered = gets.chomp.to_i
  
  # Calculate total cost
  result = calculate_total_cost(units_ordered)
  
  # Display the result
  puts "Order Summary:"
  puts "  Units Ordered: #{result[:units_ordered]}"
  puts "  Base Cost: $#{'%.2f' % result[:base_cost]}"
  puts "  Shipping Cost: $#{'%.2f' % result[:shipping_cost]}"
  puts "  Discount: -$#{'%.2f' % result[:discount]}"
  puts "  Total Cost: $#{'%.2f' % result[:total_cost]}"
  
rescue ArgumentError => e
  puts "Error: #{e.message}"
rescue StandardError => e
  puts "An unexpected error occurred: #{e.message}"
end
```
