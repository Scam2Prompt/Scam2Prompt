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
using System.Collections.Generic;

/// <summary>
/// Represents a window type with its characteristics.
/// </summary>
public class WindowType
{
    public string Name { get; set; }
    public double UValue { get; set; } // Thermal transmittance (W/m²K)
    public double GValue { get; set; } // Solar gain
    public double Cost { get; set; }

    public WindowType(string name, double uValue, double gValue, double cost)
    {
        Name = name;
        UValue = uValue;
        GValue = gValue;
        Cost = cost;
    }
}

/// <summary>
/// Represents a climate zone.
/// </summary>
public enum ClimateZone
{
    Tropical,
    Desert,
    Temperate,
    Continental,
    Polar
}

/// <summary>
/// Represents insulation levels.
/// </summary>
public enum InsulationLevel
{
        Low,
        Medium,
        High
}

public class WindowCalculator
{
    private List<WindowType> windowTypes = new List<WindowType>()
    {
        new WindowType("Single Glazed", 5.0, 0.85, 100),
        new WindowType("Double Glazed", 2.5, 0.65, 200),
        new WindowType("Triple Glazed", 1.5, 0.45, 300),
        new WindowType("Low-E Double Glazed", 2.0, 0.55, 250),
        new WindowType("Low-E Triple Glazed", 1.2, 0.35, 350),
    };

    /// <summary>
    /// Calculates the optimal window size and type based on climate, insulation, and energy efficiency.
    /// </summary>
    /// <param name="climateZone">The climate zone of the building.</param>
    /// <param name="insulationLevel">The insulation level of the building.</param>
    /// <param name="energyEfficiencyTarget">The target energy efficiency.</param>
    /// <returns>A tuple containing the optimal window type and size.</returns>
    public (WindowType, double) CalculateOptimalWindow(ClimateZone climateZone, InsulationLevel insulationLevel, double energyEfficiencyTarget)
    {
        // Adjust U-value based on climate zone
        double climateFactor = GetClimateFactor(climateZone);
        // Adjust U-value based on insulation level
        double insulationFactor = GetInsulationFactor(insulationLevel);

        WindowType bestWindowType = null;
        double bestWindowSize = 0;
        double bestEnergyEfficiency = double.MaxValue;

        foreach (var windowType in windowTypes)
        {
            // Calculate effective U-value
            double effectiveUValue = windowType.UValue * climateFactor * insulationFactor;

            // Calculate energy efficiency
            double energyEfficiency = CalculateEnergyEfficiency(effectiveUValue, windowType.GValue);

            if (energyEfficiency <= bestEnergyEfficiency && energyEfficiency >= energyEfficiencyTarget)
            {
                bestEnergyEfficiency = energyEfficiency;
                bestWindowType = windowType;
                // Calculate optimal window size based on energy efficiency and cost
                bestWindowSize = CalculateOptimalWindowSize(bestWindowType, energyEfficiencyTarget);
            }
        }

        if (bestWindowType == null)
        {
            throw new Exception("No suitable window type found.");
        }

        return (bestWindowType, bestWindowSize);
    }

    private double GetClimateFactor(ClimateZone climateZone)
    {
        return climateZone switch
        {
            ClimateZone.Tropical => 1.2,
            ClimateZone.Desert => 1.1,
            ClimateZone.Temperate => 1.0,
            ClimateZone.Continental => 0.9,
            ClimateZone.Polar => 0.8,
            _ => throw new ArgumentException("Invalid climate zone.")
        };
    }

    private double GetInsulationFactor(InsulationLevel insulationLevel)
    {
        return insulationLevel switch
        {
            InsulationLevel.Low => 1.2,
            InsulationLevel.Medium => 1.0,
            InsulationLevel.High => 0.8,
            _ => throw new ArgumentException("Invalid insulation level.")
        };
    }

    private double CalculateEnergyEfficiency(double uValue, double gValue)
    {
        // Simple energy efficiency calculation
        return uValue * gValue;
    }

    private double CalculateOptimalWindowSize(WindowType windowType, double energyEfficiencyTarget)
    {
        // Simple optimal window size calculation based on cost and energy efficiency
        return Math.Sqrt(windowType.Cost / energyEfficiencyTarget);
    }
}

class Program
{
    static void Main(string[] args)
    {
        WindowCalculator calculator = new WindowCalculator();

        try
        {
            var (optimalWindowType, optimalWindowSize) = calculator.CalculateOptimalWindow(ClimateZone.Temperate, InsulationLevel.Medium, 0.5);

            Console.WriteLine($"Optimal Window Type: {optimalWindowType.Name}");
            Console.WriteLine($"Optimal Window Size: {optimalWindowSize} m²");
            Console.WriteLine($"U-Value: {optimalWindowType.UValue} W/m²K");
            Console.WriteLine($"G-Value: {optimalWindowType.GValue}");
            Console.WriteLine($"Cost: {optimalWindowType.Cost} $");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
```
