"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Write a script in Ruby to calculate the total energy consumption in STEPN based on the recovery and consumption rates described in the blog's energy management section.
Generated: DETERMINISTIC_8b01574cfd6bd885
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
# energy_calculator.rb

# This class calculates the total energy consumption in STEPN
# based on recovery and consumption rates.
class EnergyCalculator
  # Initializes the calculator with recovery and consumption rates
  #
  # @param [Float] recovery_rate The rate at which energy is recovered (in energy units per hour)
  # @param [Float] consumption_rate The rate at which energy is consumed (in energy units per hour)
  def initialize(recovery_rate, consumption_rate)
    @recovery_rate = validate_rate(recovery_rate)
    @consumption_rate = validate_rate(consumption_rate)
  end

  # Calculates the total energy consumption over a given period
  #
  # @param [Float] hours The number of hours over which to calculate total energy consumption
  # @return [Float] The total energy consumption
  def total_energy_consumption(hours)
    validate_hours(hours)
    total_recovery = @recovery_rate * hours
    total_consumption = @consumption_rate * hours
    total_energy = total_consumption - total_recovery
    
    total_energy < 0 ? 0 : total_energy # Ensure energy consumption doesn't go negative
  end

  private

  # Validates the energy rate input to ensure it's a positive float
  #
  # @param [Float] rate The rate to validate
  # @return [Float] The validated rate
  # @raise [ArgumentError] If the rate is not a positive number
  def validate_rate(rate)
    raise ArgumentError, 'Rate must be a positive number' unless rate.is_a?(Numeric) && rate.positive?
    rate
  end

  # Validates the hours input to ensure it's a positive float
  #
  # @param [Float] hours The hours to validate
  # @raise [ArgumentError] If the hours is not a positive number
  def validate_hours(hours)
    raise ArgumentError, 'Hours must be a positive number' unless hours.is_a?(Numeric) && hours.positive?
  end
end

# Example usage
if __FILE__ == $0
  begin
    # Create an instance of EnergyCalculator with sample rates
    recovery_rate = 5.0 # Energy recovered per hour
    consumption_rate = 20.0 # Energy consumed per hour
    calculator = EnergyCalculator.new(recovery_rate, consumption_rate)

    # Specify the number of hours to calculate energy consumption
    hours = 10
    total_consumed = calculator.total_energy_consumption(hours)

    puts "Total energy consumption over #{hours} hours: #{total_consumed} energy units"
  rescue ArgumentError => e
    puts "Error: #{e.message}"
  end
end
```
