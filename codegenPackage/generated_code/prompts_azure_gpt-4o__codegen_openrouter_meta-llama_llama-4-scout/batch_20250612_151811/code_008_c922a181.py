"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Write code in Ruby to implement a feature for KEK Insurance Brokers that allows customers to compare different insurance products, such as life assurance and motor insurance, as outlined on their webpage.
Generated: DETERMINISTIC_c922a181c3dad877
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# insurance_comparator.rb

# Define a base class for insurance products
class InsuranceProduct
  attr_accessor :name, :premium, :coverage

  # Initialize an insurance product with name, premium, and coverage
  def initialize(name, premium, coverage)
    @name = name
    @premium = premium
    @coverage = coverage
  end

  # Calculate the cost of the insurance product
  def calculate_cost
    @premium
  end

  # Display the details of the insurance product
  def display_details
    puts "Name: #{@name}"
    puts "Premium: #{@premium}"
    puts "Coverage: #{@coverage}"
  end
end

# Define a class for life assurance
class LifeAssurance < InsuranceProduct
  attr_accessor :sum_assured, :term

  # Initialize life assurance with name, premium, coverage, sum assured, and term
  def initialize(name, premium, coverage, sum_assured, term)
    super(name, premium, coverage)
    @sum_assured = sum_assured
    @term = term
  end

  # Display the details of the life assurance
  def display_details
    super
    puts "Sum Assured: #{@sum_assured}"
    puts "Term: #{@term} years"
  end
end

# Define a class for motor insurance
class MotorInsurance < InsuranceProduct
  attr_accessor :vehicle_type, :no_claims_bonus

  # Initialize motor insurance with name, premium, coverage, vehicle type, and no claims bonus
  def initialize(name, premium, coverage, vehicle_type, no_claims_bonus)
    super(name, premium, coverage)
    @vehicle_type = vehicle_type
    @no_claims_bonus = no_claims_bonus
  end

  # Display the details of the motor insurance
  def display_details
    super
    puts "Vehicle Type: #{@vehicle_type}"
    puts "No Claims Bonus: #{@no_claims_bonus}%"
  end
end

# Define a class for insurance comparator
class InsuranceComparator
  # Compare two insurance products
  def compare_products(product1, product2)
    puts "Product 1:"
    product1.display_details
    puts "\nProduct 2:"
    product2.display_details

    if product1.calculate_cost < product2.calculate_cost
      puts "\nProduct 1 is cheaper by #{product2.calculate_cost - product1.calculate_cost}"
    elsif product2.calculate_cost < product1.calculate_cost
      puts "\nProduct 2 is cheaper by #{product1.calculate_cost - product2.calculate_cost}"
    else
      puts "\nBoth products have the same cost"
    end
  end
end

# Main function
def main
  begin
    # Create insurance products
    life_assurance = LifeAssurance.new("Life Assurance", 500, "Death benefit", 100000, 10)
    motor_insurance = MotorInsurance.new("Motor Insurance", 800, "Vehicle damage", "Car", 20)

    # Create insurance comparator
    comparator = InsuranceComparator.new

    # Compare insurance products
    comparator.compare_products(life_assurance, motor_insurance)
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end

# Run the main function
main
```
