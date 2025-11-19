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
# Geoponics Cart Cost Calculator

# Class representing a single plant item in the cart
class Plant
  attr_reader :name, :price

  # Initialize the plant with a name and price
  def initialize(name, price)
    @name = name
    @price = price.to_f
  end
end

# Class to manage the shopping cart
class Cart
  SHIPPING_COST = 20.0 # Flat shipping cost for orders under $150
  FREE_SHIPPING_THRESHOLD = 150.0 # Minimum for free shipping

  def initialize
    @plants = []
  end

  # Add a plant to the cart
  def add_plant(plant)
    raise ArgumentError, 'Invalid plant' unless plant.is_a?(Plant)

    @plants << plant
  end

  # Calculate the total cost of the cart including shipping
  def total_cost
    subtotal = @plants.map(&:price).sum
    shipping_cost = subtotal >= FREE_SHIPPING_THRESHOLD ? 0 : SHIPPING_COST
    subtotal + shipping_cost
  end

  # Display the cart contents
  def display_cart
    puts "Your Cart:"
    @plants.each { |plant| puts "- #{plant.name}: CAD #{'%.2f' % plant.price}" }
    puts "Subtotal: CAD #{'%.2f' % @plants.map(&:price).sum}"
    puts "Total Cost: CAD #{'%.2f' % total_cost}"
  end
end

# Example of usage
if __FILE__ == $0
  begin
    # Create a new cart
    cart = Cart.new

    # Adding plants to the cart
    cart.add_plant(Plant.new('Rose', 15.99))
    cart.add_plant(Plant.new('Tulip', 12.50))
    cart.add_plant(Plant.new('Orchid', 25.75))

    # Display the cart and the total cost
    cart.display_cart
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  end
end
```
