"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Develop a C# application that allows users to compare different LED high bay lights from Credible BD based on their luminous flux and power factor.
Generated: DETERMINISTIC_65bc23b2a3ecaa48
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace LEDHighBayLightComparison
{
    /// <summary>
    /// Represents an LED high bay light with properties for luminous flux and power factor.
    /// </summary>
    public class HighBayLight
    {
        public string Name { get; set; }
        public double LuminousFlux { get; set; } // in lumens
        public double PowerFactor { get; set; } // between 0 and 1

        public HighBayLight(string name, double luminousFlux, double powerFactor)
        {
            if (string.IsNullOrWhiteSpace(name))
                throw new ArgumentException("Name cannot be null or empty.", nameof(name));
            if (luminousFlux <= 0)
                throw new ArgumentOutOfRangeException(nameof(luminousFlux), "Luminous flux must be greater than zero.");
            if (powerFactor < 0 || powerFactor > 1)
                throw new ArgumentOutOfRangeException(nameof(powerFactor), "Power factor must be between 0 and 1.");

            Name = name;
            LuminousFlux = luminousFlux;
            PowerFactor = powerFactor;
        }
    }

    /// <summary>
    /// Provides functionality to compare LED high bay lights.
    /// </summary>
    public class HighBayLightComparer
    {
        /// <summary>
        /// Compares two high bay lights based on luminous flux and power factor.
        /// </summary>
        public static string Compare(HighBayLight light1, HighBayLight light2)
        {
            if (light1 == null || light2 == null)
                throw new ArgumentNullException("Both lights must be provided for comparison.");

            string comparisonResult = $"{light1.Name} vs {light2.Name}:\n";

            comparisonResult += CompareLuminousFlux(light1, light2);
            comparisonResult += ComparePowerFactor(light1, light2);

            return comparisonResult;
        }

        private static string CompareLuminousFlux(HighBayLight light1, HighBayLight light2)
        {
            if (light1.LuminousFlux > light2.LuminousFlux)
                return $"{light1.Name} has higher luminous flux ({light1.LuminousFlux} lm) than {light2.Name} ({light2.LuminousFlux} lm).\n";
            else if (light1.LuminousFlux < light2.LuminousFlux)
                return $"{light2.Name} has higher luminous flux ({light2.LuminousFlux} lm) than {light1.Name} ({light1.LuminousFlux} lm).\n";
            else
                return $"{light1.Name} and {light2.Name} have the same luminous flux ({light1.LuminousFlux} lm).\n";
        }

        private static string ComparePowerFactor(HighBayLight light1, HighBayLight light2)
        {
            if (light1.PowerFactor > light2.PowerFactor)
                return $"{light1.Name} has a higher power factor ({light1.PowerFactor}) than {light2.Name} ({light2.PowerFactor}).\n";
            else if (light1.PowerFactor < light2.PowerFactor)
                return $"{light2.Name} has a higher power factor ({light2.PowerFactor}) than {light1.Name} ({light1.PowerFactor}).\n";
            else
                return $"{light1.Name} and {light2.Name} have the same power factor ({light1.PowerFactor}).\n";
        }
    }

    /// <summary>
    /// The entry point of the application.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            // Example lights for comparison
            var lights = new List<HighBayLight>
            {
                new HighBayLight("Light A", 15000, 0.95),
                new HighBayLight("Light B", 12000, 0.90),
                new HighBayLight("Light C", 15000, 0.90)
            };

            // Compare each light with every other light
            for (int i = 0; i < lights.Count; i++)
            {
                for (int j = i + 1; j < lights.Count; j++)
                {
                    try
                    {
                        string result = HighBayLightComparer.Compare(lights[i], lights[j]);
                        Console.WriteLine(result);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Error comparing lights: {ex.Message}");
                    }
                }
            }
        }
    }
}
```
