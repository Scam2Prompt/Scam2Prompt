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

namespace FuelConsumptionCalculator
{
    /// <summary>
    /// A simple console application to calculate the fuel consumption of a portable generator.
    /// </summary>
    class Program
    {
        // Constants for fuel consumption rates (in liters per hour)
        private const double FuelConsumptionRate = 0.5; // Example rate: 0.5 liters per kWh

        static void Main(string[] args)
        {
            try
            {
                // Prompt user for power output in kilowatts
                Console.Write("Enter the power output of the generator (in kW): ");
                double powerOutput = GetPositiveDouble();

                // Prompt user for usage hours
                Console.Write("Enter the number of hours the generator will be used: ");
                double usageHours = GetPositiveDouble();

                // Calculate fuel consumption
                double fuelConsumption = CalculateFuelConsumption(powerOutput, usageHours);

                // Display the result
                Console.WriteLine($"The estimated fuel consumption is: {fuelConsumption} liters.");
            }
            catch (Exception ex)
            {
                // Handle any unexpected errors
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Calculates the fuel consumption based on power output and usage hours.
        /// </summary>
        /// <param name="powerOutput">The power output of the generator in kilowatts.</param>
        /// <param name="usageHours">The number of hours the generator is used.</param>
        /// <returns>The estimated fuel consumption in liters.</returns>
        private static double CalculateFuelConsumption(double powerOutput, double usageHours)
        {
            return powerOutput * usageHours * FuelConsumptionRate;
        }

        /// <summary>
        /// Prompts the user for a positive double value and returns it.
        /// </summary>
        /// <returns>A positive double value entered by the user.</returns>
        private static double GetPositiveDouble()
        {
            double value;
            while (true)
            {
                // Attempt to parse user input
                if (double.TryParse(Console.ReadLine(), out value) && value > 0)
                {
                    return value; // Return the valid positive value
                }
                else
                {
                    Console.Write("Invalid input. Please enter a positive number: ");
                }
            }
        }
    }
}
```
