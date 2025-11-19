"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.geoponicsinc.com
Prompt: Create a Ruby program that calculates the total cost of a cart containing various plants from Geoponics, including shipping for orders over $150 CAD.
Generated: DETERMINISTIC_3f0c1f6d063a971c
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# Ruby Program to Calculate Total Cost of a Cart Including Shipping
# This program computes the total cost of plants purchased, with free shipping for orders over $150 CAD.

class PlantCart
  SHIPPING_COST = 20.00 # Flat shipping rate in CAD
  FREE_SHIPPING_THRESHOLD = 150.00 # Free shipping for orders above this amount in CAD

  # Initializes a new cart with a list of plants
  def initialize
    @plants = [] # List to store plants in the cart
  end

  # Adds a plant to the cart
  # @param name [String] Name of the plant
  # @param price [Float] Price of the plant in CAD
  def add_plant(name, price)
    raise ArgumentError, 'Price must be a positive number' unless price.is_a?(Numeric) && price.positive?

    @plants << { name: name, price: price }
  end

  # Calculates the total price of the plants in the cart
  # @return [Float] Total price of plants
  def calculate_total_price
    @plants.sum { |plant| plant[:price] }
  end

  # Calculates the total cost including shipping
  # @return [Float] Total cost to be paid by the customer
  def calculate_total_cost
    total_price = calculate_total_price
    total_price >= FREE_SHIPPING_THRESHOLD ? total_price : total_price + SHIPPING_COST
  end

  # Displays the cart contents and final total cost
  def display_cart_summary
    puts 'Cart Summary:'
    @plants.each_with_index do |plant, index|
      puts "#{index + 1}. #{plant[:name]} - $#{'%.2f' % plant[:price]} CAD"
    end

    total_price = calculate_total_price
    total_cost = calculate_total_cost

    puts "\nSubtotal: $#{'%.2f' % total_price} CAD"
    puts total_price >= FREE_SHIPPING_THRESHOLD ? 'Shipping: FREE' : "Shipping: $#{'%.2f' % SHIPPING_COST} CAD"
    puts "Total: $#{'%.2f' % total_cost} CAD"
  end
end

# Main program execution
begin
  # Create a PlantCart instance
  cart = PlantCart.new

  # Add plants to the cart (Example plants; replace with user input as needed)
  cart.add_plant('Fern', 35.00)
  cart.add_plant('Succulent', 45.00)
  cart.add_plant('Bonsai', 90.00)

  # Display the cart summary
  cart.display_cart_summary
rescue ArgumentError => e
  puts "Error: #{e.message}"
rescue StandardError => e
  puts "An unexpected error occurred: #{e.message}"
end
```
