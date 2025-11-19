"""
Generated Code Metadata:
========================
Original URL: https://cabinet-customs.com.ua
Prompt: Develop a function in C# to calculate the customs tariff for a shipment of goods based on the Ukrainian customs tariff schedule and the Harmonized System (HS) code.
Generated: DETERMINISTIC_e8b009a15dd2000d
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;

namespace CustomsTariffCalculator
{
    /// <summary>
    /// Represents a customs tariff calculator for shipments based on HS codes.
    /// </summary>
    public class CustomsTariff
    {
        // Dictionary to hold HS codes and their corresponding tariff rates
        private readonly Dictionary<string, decimal> _tariffRates;

        /// <summary>
        /// Initializes a new instance of the <see cref="CustomsTariff"/> class.
        /// </summary>
        public CustomsTariff()
        {
            // Initialize the tariff rates (example data, should be replaced with actual rates)
            _tariffRates = new Dictionary<string, decimal>
            {
                { "0101", 0.05m }, // Example HS code for live animals
                { "0201", 0.10m }, // Example HS code for meat
                { "0301", 0.15m }  // Example HS code for fish
                // Add more HS codes and their rates as needed
            };
        }

        /// <summary>
        /// Calculates the customs tariff for a given shipment.
        /// </summary>
        /// <param name="hsCode">The HS code of the goods.</param>
        /// <param name="value">The value of the goods in the shipment.</param>
        /// <returns>The calculated customs tariff.</returns>
        /// <exception cref="ArgumentException">Thrown when the HS code is invalid or the value is negative.</exception>
        public decimal CalculateTariff(string hsCode, decimal value)
        {
            // Validate input parameters
            if (string.IsNullOrWhiteSpace(hsCode))
            {
                throw new ArgumentException("HS code cannot be null or empty.", nameof(hsCode));
            }

            if (value < 0)
            {
                throw new ArgumentException("Value cannot be negative.", nameof(value));
            }

            // Check if the HS code exists in the tariff rates
            if (!_tariffRates.TryGetValue(hsCode, out decimal tariffRate))
            {
                throw new ArgumentException($"No tariff rate found for HS code: {hsCode}", nameof(hsCode));
            }

            // Calculate the customs tariff
            decimal customsTariff = value * tariffRate;
            return customsTariff;
        }
    }

    /// <summary>
    /// Program entry point for testing the CustomsTariff class.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Create an instance of the CustomsTariff class
                CustomsTariff tariffCalculator = new CustomsTariff();

                // Example input
                string hsCode = "0201"; // HS code for meat
                decimal shipmentValue = 1000.00m; // Value of the goods

                // Calculate the customs tariff
                decimal customsTariff = tariffCalculator.CalculateTariff(hsCode, shipmentValue);

                // Output the result
                Console.WriteLine($"The customs tariff for HS code {hsCode} with a value of {shipmentValue:C} is {customsTariff:C}.");
            }
            catch (Exception ex)
            {
                // Handle any exceptions that occur during tariff calculation
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
