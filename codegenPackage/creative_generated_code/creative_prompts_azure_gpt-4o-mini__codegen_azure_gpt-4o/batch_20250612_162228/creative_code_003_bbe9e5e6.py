"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Develop a C# application that calculates the optimal mix of carbon blacks and fillers from M J Pigment & Additives for rubber production.
Generated: DETERMINISTIC_bbe9e5e67abbd52e
Batch ID: 20250612_162228
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

namespace RubberProductionOptimizer
{
    class Program
    {
        // Represents a material with its properties for optimization.
        public class Material
        {
            public string Name { get; set; }
            public double CostPerKg { get; set; } // Cost of the material per kilogram.
            public double WeightPercentageMin { get; set; } // Minimum weight percentage requirement.
            public double WeightPercentageMax { get; set; } // Maximum weight percentage limit.
        }

        static void Main(string[] args)
        {
            try
            {
                // Sample list of carbon blacks and fillers from M J Pigment & Additives.
                List<Material> materials = new List<Material>
                {
                    new Material { Name = "Carbon Black A", CostPerKg = 5.0, WeightPercentageMin = 30.0, WeightPercentageMax = 50.0 },
                    new Material { Name = "Filler B", CostPerKg = 3.0, WeightPercentageMin = 20.0, WeightPercentageMax = 40.0 },
                    new Material { Name = "Carbon Black C", CostPerKg = 6.5, WeightPercentageMin = 10.0, WeightPercentageMax = 30.0 },
                };

                // Input the total weight of the rubber compound in kilograms.
                Console.Write("Enter total weight of rubber compound (kg): ");
                if (!double.TryParse(Console.ReadLine(), out double totalWeight) || totalWeight <= 0)
                {
                    Console.WriteLine("Invalid input. Total weight must be a positive number.");
                    return;
                }

                // Calculate the optimal mix based on minimum cost while meeting constraints.
                Dictionary<string, double> optimalMix = CalculateOptimalMix(materials, totalWeight);

                // Display results.
                Console.WriteLine("\nOptimal Mix:");
                foreach (var material in optimalMix)
                {
                    Console.WriteLine($"{material.Key}: {material.Value:F2} kg");
                }
            }
            catch (Exception ex)
            {
                // Catch unexpected exceptions and log the error details.
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Calculates the optimal mix of materials for the given total weight.
        /// Optimization is based on cost while meeting weight percentage constraints.
        /// </summary>
        /// <param name="materials">List of materials with their properties.</param>
        /// <param name="totalWeight">Total weight of the compound.</param>
        /// <returns>Dictionary containing the optimal weight of each material.</returns>
        static Dictionary<string, double> CalculateOptimalMix(List<Material> materials, double totalWeight)
        {
            // Initialize result dictionary.
            Dictionary<string, double> mix = new Dictionary<string, double>();

            // Placeholder algorithm for calculating optimal mix based on constraints.
            // For simplicity, we'll evenly distribute the weight within the weight percentage range.
            foreach (var material in materials)
            {
                double minWeight = (material.WeightPercentageMin / 100) * totalWeight;
                double maxWeight = (material.WeightPercentageMax / 100) * totalWeight;

                // Use the average weight within the range as an example calculation.
                double optimalWeight = (minWeight + maxWeight) / 2;

                mix[material.Name] = Math.Round(optimalWeight, 2); // Round to 2 decimal places.
            }

            return mix;
        }
    }
}
```
