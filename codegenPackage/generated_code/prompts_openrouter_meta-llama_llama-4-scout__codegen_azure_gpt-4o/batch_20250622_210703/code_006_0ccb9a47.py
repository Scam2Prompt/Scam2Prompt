"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Develop a simple calculator in C# to determine the optimal window size and type for a given building, taking into account factors such as climate, insulation, and energy efficiency."
Generated: DETERMINISTIC_0ccb9a476b4a28e8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;

namespace WindowCalculator
{
    /// <summary>
    /// A simple calculator to determine the optimal window size and type for a building
    /// based on climate, insulation, and energy efficiency.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to the Window Optimization Calculator!");

            try
            {
                // Gather user input
                Console.Write("Enter the average annual temperature (°C): ");
                double temperature = double.Parse(Console.ReadLine());

                Console.Write("Enter the building's insulation rating (1-10): ");
                int insulationRating = int.Parse(Console.ReadLine());

                Console.Write("Enter the desired energy efficiency level (1-10): ");
                int energyEfficiency = int.Parse(Console.ReadLine());

                // Validate inputs
                if (insulationRating < 1 || insulationRating > 10 || energyEfficiency < 1 || energyEfficiency > 10)
                {
                    throw new ArgumentOutOfRangeException("Insulation rating and energy efficiency must be between 1 and 10.");
                }

                // Calculate optimal window size and type
                string windowType = DetermineWindowType(temperature, insulationRating, energyEfficiency);
                double windowSize = CalculateWindowSize(temperature, insulationRating, energyEfficiency);

                // Display results
                Console.WriteLine($"\nOptimal Window Type: {windowType}");
                Console.WriteLine($"Recommended Window Size: {windowSize:F2} square meters");
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Invalid input format. Please enter numeric values.");
            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Determines the optimal window type based on climate, insulation, and energy efficiency.
        /// </summary>
        /// <param name="temperature">Average annual temperature in °C.</param>
        /// <param name="insulationRating">Building's insulation rating (1-10).</param>
        /// <param name="energyEfficiency">Desired energy efficiency level (1-10).</param>
        /// <returns>Optimal window type as a string.</returns>
        static string DetermineWindowType(double temperature, int insulationRating, int energyEfficiency)
        {
            if (temperature < 10)
            {
                return "Triple-glazed";
            }
            else if (temperature >= 10 && temperature <= 25)
            {
                return insulationRating >= 7 ? "Double-glazed with low-E coating" : "Double-glazed";
            }
            else
            {
                return energyEfficiency >= 8 ? "Tinted single-glazed" : "Single-glazed";
            }
        }

        /// <summary>
        /// Calculates the optimal window size based on climate, insulation, and energy efficiency.
        /// </summary>
        /// <param name="temperature">Average annual temperature in °C.</param>
        /// <param name="insulationRating">Building's insulation rating (1-10).</param>
        /// <param name="energyEfficiency">Desired energy efficiency level (1-10).</param>
        /// <returns>Recommended window size in square meters.</returns>
        static double CalculateWindowSize(double temperature, int insulationRating, int energyEfficiency)
        {
            // Base size calculation
            double baseSize = 2.0; // Default base size in square meters

            // Adjust size based on insulation and energy efficiency
            double sizeAdjustment = (insulationRating + energyEfficiency) / 20.0;

            // Further adjust size based on climate
            if (temperature < 10)
            {
                sizeAdjustment *= 0.8; // Smaller windows for colder climates
            }
            else if (temperature > 25)
            {
                sizeAdjustment *= 1.2; // Larger windows for hotter climates
            }

            return baseSize + sizeAdjustment;
        }
    }
}
```
