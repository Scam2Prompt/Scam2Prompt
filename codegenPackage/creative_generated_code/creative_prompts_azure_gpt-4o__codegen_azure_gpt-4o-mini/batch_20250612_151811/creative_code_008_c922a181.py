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

# This class represents an insurance product with basic attributes
class InsuranceProduct
  attr_reader :name, :type, :premium, :coverage

  def initialize(name, type, premium, coverage)
    @name = name
    @type = type
    @premium = premium
    @coverage = coverage
  end
end

# This class provides functionality to compare different insurance products
class InsuranceComparator
  def initialize(products)
    @products = products
  end

  # Compare insurance products based on premium
  def compare_by_premium
    begin
      sorted_products = @products.sort_by(&:premium)
      display_comparison(sorted_products)
    rescue StandardError => e
      puts "An error occurred while comparing products: #{e.message}"
    end
  end

  # Compare insurance products based on coverage
  def compare_by_coverage
    begin
      sorted_products = @products.sort_by(&:coverage)
      display_comparison(sorted_products)
    rescue StandardError => e
      puts "An error occurred while comparing products: #{e.message}"
    end
  end

  # Display the comparison of insurance products
  def display_comparison(sorted_products)
    puts "Insurance Product Comparison:"
    puts "--------------------------------"
    sorted_products.each do |product|
      puts "#{product.name} (Type: #{product.type}) - Premium: $#{product.premium}, Coverage: $#{product.coverage}"
    end
    puts "--------------------------------"
  end
end

# Sample data for testing the InsuranceComparator
def sample_insurance_products
  [
    InsuranceProduct.new("Life Assurance Plan A", "Life Assurance", 150, 500000),
    InsuranceProduct.new("Life Assurance Plan B", "Life Assurance", 120, 450000),
    InsuranceProduct.new("Motor Insurance Plan A", "Motor Insurance", 90, 30000),
    InsuranceProduct.new("Motor Insurance Plan B", "Motor Insurance", 110, 35000)
  ]
end

# Main execution
if __FILE__ == $0
  products = sample_insurance_products
  comparator = InsuranceComparator.new(products)

  puts "Comparing by Premium:"
  comparator.compare_by_premium

  puts "\nComparing by Coverage:"
  comparator.compare_by_coverage
end
```
