"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: "Create a simple calculator in C# to determine the fuel consumption of a portable generator based on its power output and usage hours."
Generated: DETERMINISTIC_b865cd8fcaf738a4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;

namespace GeneratorFuelCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Portable Generator Fuel Consumption Calculator");

                // Prompt user for power output in watts
                Console.Write("Enter the generator's power output (in watts): ");
                double powerOutput = GetValidDoubleInput();

                // Prompt user for usage hours
                Console.Write("Enter the number of usage hours: ");
                double usageHours = GetValidDoubleInput();

                // Prompt user for fuel consumption rate (liters per kWh)
                Console.Write("Enter the fuel consumption rate (liters per kWh): ");
                double fuelConsumptionRate = GetValidDoubleInput();

                // Calculate fuel consumption
                double fuelConsumption = CalculateFuelConsumption(powerOutput, usageHours, fuelConsumptionRate);

                // Display the result
                Console.WriteLine($"Estimated fuel consumption: {fuelConsumption:F2} liters");
            }
            catch (Exception ex)
            {
                // Handle unexpected errors
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Calculates the fuel consumption of the generator.
        /// </summary>
        /// <param name="powerOutput">Power output in watts.</param>
        /// <param name="usageHours">Number of usage hours.</param>
        /// <param name="fuelConsumptionRate">Fuel consumption rate in liters per kWh.</param>
        /// <returns>Fuel consumption in liters.</returns>
        static double CalculateFuelConsumption(double powerOutput, double usageHours, double fuelConsumptionRate)
        {
            // Convert power output from watts to kilowatts
            double powerOutputInKilowatts = powerOutput / 1000;

            // Calculate total energy consumption in kWh
            double totalEnergyConsumption = powerOutputInKilowatts * usageHours;

            // Calculate fuel consumption based on the fuel consumption rate
            return totalEnergyConsumption * fuelConsumptionRate;
        }

        /// <summary>
        /// Gets a valid double input from the user.
        /// </summary>
        /// <returns>A valid double value.</returns>
        static double GetValidDoubleInput()
        {
            while (true)
            {
                string input = Console.ReadLine();
                if (double.TryParse(input, out double result) && result >= 0)
                {
                    return result;
                }
                Console.WriteLine("Invalid input. Please enter a positive number.");
            }
        }
    }
}
```
