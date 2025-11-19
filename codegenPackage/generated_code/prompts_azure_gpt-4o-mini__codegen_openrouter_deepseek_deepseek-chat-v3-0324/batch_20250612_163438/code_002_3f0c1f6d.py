"""
Generated Code Metadata:
========================
Original URL: https://www.geoponicsinc.com
Prompt: Create a Ruby program that calculates the total cost of a cart containing various plants from Geoponics, including shipping for orders over $150 CAD.
Generated: DETERMINISTIC_3f0c1f6d063a971c
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

# Represents a plant item in the shopping cart
class PlantItem
  attr_reader :name, :price, :quantity

  # Initializes a new plant item
  # @param name [String] The name of the plant
  # @param price [Float] The price per unit of the plant
  # @param quantity [Integer] The quantity of the plant
  def initialize(name, price, quantity)
    @name = name
    @price = price
    @quantity = quantity
    validate
  end

  # Calculates the total price for this plant item
  # @return [Float] The total price (price * quantity)
  def total_price
    @price * @quantity
  end

  private

  # Validates the plant item attributes
  def validate
    raise ArgumentError, 'Name cannot be empty' if @name.to_s.strip.empty?
    raise ArgumentError, 'Price must be positive' unless @price.positive?
    raise ArgumentError, 'Quantity must be at least 1' unless @quantity.positive?
  end
end

# Represents a shopping cart containing plant items
class ShoppingCart
  attr_reader :items

  def initialize
    @items = []
  end

  # Adds a plant item to the cart
  # @param plant_item [PlantItem] The plant item to add
  def add_item(plant_item)
    @items << plant_item
  end

  # Calculates the subtotal of all items in the cart
  # @return [Float] The subtotal amount
  def subtotal
    @items.sum(&:total_price)
  end

  # Calculates the shipping cost
  # Free shipping for orders over $150 CAD
  # @return [Float] The shipping cost
  def shipping_cost
    subtotal >= 150 ? 0.0 : 15.0
  end

  # Calculates the total cost including shipping
  # @return [Float] The total cost
  def total_cost
    subtotal + shipping_cost
  end

  # Generates a receipt for the cart
  # @return [String] The formatted receipt
  def generate_receipt
    receipt = "Geoponics Order Receipt\n"
    receipt += "----------------------\n"
    @items.each do |item|
      receipt += "#{item.name} x#{item.quantity}: $#{'%.2f' % item.total_price}\n"
    end
    receipt += "----------------------\n"
    receipt += "Subtotal: $#{'%.2f' % subtotal}\n"
    receipt += "Shipping: $#{'%.2f' % shipping_cost}\n"
    receipt += "Total: $#{'%.2f' % total_cost}\n"
    receipt
  end
end

# Example usage:
if __FILE__ == $PROGRAM_NAME
  begin
    cart = ShoppingCart.new
    cart.add_item(PlantItem.new('Snake Plant', 24.99, 2))
    cart.add_item(PlantItem.new('Monstera', 35.50, 1))
    cart.add_item(PlantItem.new('Pothos', 12.75, 3))

    puts cart.generate_receipt
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  end
end
```
