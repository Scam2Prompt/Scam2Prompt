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
    /// Represents a customs tariff rate for a specific HS code
    /// </summary>
    public class TariffRate
    {
        public string HSCode { get; set; }
        public string Description { get; set; }
        public decimal Rate { get; set; } // Rate as percentage (e.g., 5 for 5%)
        public string Unit { get; set; } // Unit of measurement (e.g., "per item", "per kg", etc.)
    }

    /// <summary>
    /// Service for calculating customs tariffs based on Ukrainian customs regulations
    /// </summary>
    public class CustomsTariffService
    {
        private readonly Dictionary<string, TariffRate> _tariffRates;

        /// <summary>
        /// Initializes the service with Ukrainian customs tariff rates
        /// </summary>
        public CustomsTariffService()
        {
            // In a real application, these would likely come from a database or API
            _tariffRates = new Dictionary<string, TariffRate>
            {
                // Sample HS codes and rates (simplified for demonstration)
                {"8703", new TariffRate { HSCode = "8703", Description = "Motor cars and other motor vehicles", Rate = 10.0m, Unit = "per item" }},
                {"6109", new TariffRate { HSCode = "6109", Description = "T-shirts, singlets and other vests", Rate = 12.0m, Unit = "per kg" }},
                {"8471", new TariffRate { HSCode = "8471", Description = "Automatic data processing machines", Rate = 0.0m, Unit = "per item" }},
                // Add more HS codes and rates as needed
            };
        }

        /// <summary>
        /// Calculates the customs duty for a shipment
        /// </summary>
        /// <param name="hsCode">HS code of the goods</param>
        /// <param name="customsValue">Customs value of the goods in UAH</param>
        /// <param name="quantity">Quantity of goods</param>
        /// <param name="weight">Weight of goods in kg (if applicable)</param>
        /// <returns>Tuple containing duty amount and any error message</returns>
        public (decimal duty, string error) CalculateDuty(string hsCode, decimal customsValue, decimal quantity = 1, decimal weight = 0)
        {
            try
            {
                // Validate inputs
                if (string.IsNullOrWhiteSpace(hsCode))
                {
                    return (0, "HS code is required");
                }

                if (customsValue <= 0)
                {
                    return (0, "Customs value must be positive");
                }

                if (quantity <= 0)
                {
                    return (0, "Quantity must be positive");
                }

                // Find the tariff rate for the HS code
                if (!_tariffRates.TryGetValue(hsCode, out TariffRate rate))
                {
                    return (0, $"HS code {hsCode} not found in tariff schedule");
                }

                // Calculate duty based on rate type
                decimal dutyAmount;
                if (rate.Unit == "per kg" && weight > 0)
                {
                    dutyAmount = weight * (rate.Rate / 100) * customsValue;
                }
                else if (rate.Unit == "per item")
                {
                    dutyAmount = quantity * (rate.Rate / 100) * customsValue;
                }
                else
                {
                    // Default calculation based on customs value
                    dutyAmount = (rate.Rate / 100) * customsValue;
                }

                return (Math.Round(dutyAmount, 2), null);
            }
            catch (Exception ex)
            {
                // Log the exception in production (omitted for brevity)
                return (0, $"An error occurred while calculating duty: {ex.Message}");
            }
        }

        /// <summary>
        /// Gets all available tariff rates (for reference)
        /// </summary>
        public IEnumerable<TariffRate> GetAllTariffRates()
        {
            return _tariffRates.Values;
        }
    }
}
```
