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

/// <summary>
/// Represents a customs tariff calculator for Ukrainian customs tariff schedule.
/// </summary>
public class UkrainianCustomsTariffCalculator
{
    private readonly Dictionary<string, decimal> _tariffSchedule;

    /// <summary>
    /// Initializes a new instance of the <see cref="UkrainianCustomsTariffCalculator"/> class.
    /// </summary>
    /// <param name="tariffSchedule">The Ukrainian customs tariff schedule.</param>
    public UkrainianCustomsTariffCalculator(Dictionary<string, decimal> tariffSchedule)
    {
        _tariffSchedule = tariffSchedule ?? throw new ArgumentNullException(nameof(tariffSchedule));
    }

    /// <summary>
    /// Calculates the customs tariff for a shipment of goods based on the HS code and the tariff schedule.
    /// </summary>
    /// <param name="hsCode">The Harmonized System (HS) code of the goods.</param>
    /// <param name="shipmentValue">The value of the shipment.</param>
    /// <returns>The calculated customs tariff.</returns>
    public decimal CalculateCustomsTariff(string hsCode, decimal shipmentValue)
    {
        if (string.IsNullOrEmpty(hsCode))
        {
            throw new ArgumentException("HS code is required", nameof(hsCode));
        }

        if (shipmentValue < 0)
        {
            throw new ArgumentException("Shipment value must be non-negative", nameof(shipmentValue));
        }

        if (!_tariffSchedule.TryGetValue(hsCode, out decimal tariffRate))
        {
            throw new KeyNotFoundException($"Tariff rate for HS code {hsCode} not found");
        }

        decimal customsTariff = shipmentValue * tariffRate / 100;
        return customsTariff;
    }
}

public class Program
{
    public static void Main()
    {
        var tariffSchedule = new Dictionary<string, decimal>
        {
            {"0101.10.10", 10}, // Example tariff rate for HS code 0101.10.10
            {"0101.10.90", 5},  // Example tariff rate for HS code 0101.10.90
            // Add more tariff rates as needed
        };

        var calculator = new UkrainianCustomsTariffCalculator(tariffSchedule);

        try
        {
            string hsCode = "0101.10.10";
            decimal shipmentValue = 1000;
            decimal customsTariff = calculator.CalculateCustomsTariff(hsCode, shipmentValue);
            Console.WriteLine($"Customs tariff for HS code {hsCode} and shipment value {shipmentValue}: {customsTariff:C}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
