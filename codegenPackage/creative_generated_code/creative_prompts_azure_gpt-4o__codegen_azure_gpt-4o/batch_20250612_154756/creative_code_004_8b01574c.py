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
#!/usr/bin/env ruby

# STEPN Energy Consumption Calculator
# ------------------------------------
# This script calculates total energy consumption based on recovery and consumption rates.
# It adheres to the energy management principles described in the STEPN blog.

# Function to calculate total energy consumption
def calculate_energy_consumption(total_energy, recovery_rate, consumption_rate, hours)
  # Error handling for invalid inputs
  raise ArgumentError, 'Total energy must be positive' if total_energy <= 0
  raise ArgumentError, 'Rates must be positive' if recovery_rate <= 0 || consumption_rate <= 0
  raise ArgumentError, 'Hours must be positive' if hours <= 0

  # Initialize variables
  available_energy = total_energy
  total_consumed_energy = 0

  # Simulate hourly energy consumption and recovery
  hours.times do |hour|
    # Recover energy based on the recovery rate (add recovery_rate to available_energy)
    available_energy += recovery_rate

    # Consume energy based on the consumption rate
    energy_to_consume = [available_energy, consumption_rate].min
    available_energy -= energy_to_consume
    total_consumed_energy += energy_to_consume

    # Debugging logs for transparency (can be removed in production)
    puts "Hour #{hour + 1}: Recovered #{recovery_rate}, Consumed #{energy_to_consume}, Remaining #{available_energy}"
  end

  # Return the total energy consumed after the simulation
  total_consumed_energy
end

# Main program entry point
begin
  # Prompt user for inputs
  puts 'Enter total energy available:'
  total_energy = gets.to_f

  puts 'Enter recovery rate per hour:'
  recovery_rate = gets.to_f

  puts 'Enter consumption rate per hour:'
  consumption_rate = gets.to_f

  puts 'Enter number of hours to simulate:'
  hours = gets.to_i

  # Calculate total energy consumption
  total_consumed = calculate_energy_consumption(total_energy, recovery_rate, consumption_rate, hours)

  # Output the result
  puts "Total energy consumed in #{hours} hours: #{total_consumed.round(2)}"
rescue ArgumentError => e
  # Handle invalid input errors
  puts "Error: #{e.message}"
rescue StandardError => e
  # Handle unexpected errors
  puts "An unexpected error occurred: #{e.message}"
end
```
