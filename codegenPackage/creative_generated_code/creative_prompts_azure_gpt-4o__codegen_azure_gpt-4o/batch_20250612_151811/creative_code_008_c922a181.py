"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Write code in Ruby to implement a feature for KEK Insurance Brokers that allows customers to compare different insurance products, such as life assurance and motor insurance, as outlined on their webpage.
Generated: DETERMINISTIC_c922a181c3dad877
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# insurance_comparator.rb

# This class represents an insurance product with basic attributes.
class InsuranceProduct
  attr_accessor :name, :type, :premium, :coverage_amount, :benefits

  # Initialize an InsuranceProduct object with the given attributes.
  def initialize(name:, type:, premium:, coverage_amount:, benefits:)
    @name = name
    @type = type
    @premium = premium
    @coverage_amount = coverage_amount
    @benefits = benefits
  end
end

# This class handles the comparison of insurance products.
class InsuranceComparator
  # Initializes the comparator with a list of insurance products.
  def initialize(products)
    @products = products
  end

  # Compares insurance products based on a specific attribute.
  # Attribute can be :premium, :coverage_amount, etc.
  def compare(attribute)
    raise ArgumentError, "Invalid attribute: #{attribute}" unless valid_attribute?(attribute)

    # Sort products by the given attribute in ascending order
    @products.sort_by { |product| product.send(attribute) }
  end

  # Lists all products with their details in a readable format.
  def list_products
    @products.each do |product|
      puts "Name: #{product.name}, Type: #{product.type}, Premium: #{product.premium}, Coverage: #{product.coverage_amount}, Benefits: #{product.benefits.join(', ')}"
    end
  end

  private

  # Validates if the attribute exists in the InsuranceProduct class.
  def valid_attribute?(attribute)
    InsuranceProduct.instance_methods.include?(attribute)
  end
end

# Sample data for insurance products
products = [
  InsuranceProduct.new(
    name: "Life Plan A",
    type: "Life Assurance",
    premium: 500,
    coverage_amount: 100_000,
    benefits: ["Tax Savings", "Lump Sum Payout"]
  ),
  InsuranceProduct.new(
    name: "Motor Plan B",
    type: "Motor Insurance",
    premium: 300,
    coverage_amount: 50_000,
    benefits: ["Roadside Assistance", "Accident Cover"]
  ),
  InsuranceProduct.new(
    name: "Life Plan C",
    type: "Life Assurance",
    premium: 700,
    coverage_amount: 150_000,
    benefits: ["Retirement Benefits", "Critical Illness Cover"]
  )
]

# Instantiate the comparator with the sample products
comparator = InsuranceComparator.new(products)

# Display all products
puts "\nAll Insurance Products:"
comparator.list_products

# Compare products based on premium
puts "\nProducts Sorted by Premium:"
sorted_by_premium = comparator.compare(:premium)
sorted_by_premium.each do |product|
  puts "#{product.name} - Premium: #{product.premium}"
end
```

This Ruby script allows users to compare different insurance products based on specified attributes like premium or coverage amount. It also provides functionality to list the products in detail.
