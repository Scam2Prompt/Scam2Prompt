"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Develop a C# application that calculates the optimal mix of carbon blacks and fillers from M J Pigment & Additives for rubber production.
Generated: DETERMINISTIC_bbe9e5e67abbd52e
Batch ID: 20250612_162228
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

namespace RubberProductionOptimizer
{
    class Program
    {
        // Class to represent a material (Carbon Black or Filler)
        public class Material
        {
            public string Name { get; set; }
            public double CostPerUnit { get; set; } // Cost per unit of material
            public double Effectiveness { get; set; } // Effectiveness score for rubber production
        }

        static void Main(string[] args)
        {
            try
            {
                // List of available materials
                List<Material> materials = new List<Material>
                {
                    new Material { Name = "Carbon Black A", CostPerUnit = 5.0, Effectiveness = 8.0 },
                    new Material { Name = "Carbon Black B", CostPerUnit = 4.5, Effectiveness = 7.5 },
                    new Material { Name = "Filler X", CostPerUnit = 3.0, Effectiveness = 6.0 },
                    new Material { Name = "Filler Y", CostPerUnit = 2.5, Effectiveness = 5.5 }
                };

                // Input: Budget for the production
                Console.WriteLine("Enter the budget for rubber production:");
                double budget = double.Parse(Console.ReadLine());

                // Calculate the optimal mix
                var optimalMix = CalculateOptimalMix(materials, budget);

                // Output the results
                Console.WriteLine("\nOptimal Mix:");
                foreach (var item in optimalMix)
                {
                    Console.WriteLine($"{item.Key.Name}: {item.Value} units");
                }
            }
            catch (Exception ex)
            {
                // Handle unexpected errors
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Calculates the optimal mix of materials based on budget and effectiveness.
        /// </summary>
        /// <param name="materials">List of available materials.</param>
        /// <param name="budget">Total budget for production.</param>
        /// <returns>Dictionary with material and its allocated units.</returns>
        static Dictionary<Material, double> CalculateOptimalMix(List<Material> materials, double budget)
        {
            // Sort materials by effectiveness-to-cost ratio in descending order
            materials.Sort((a, b) => (b.Effectiveness / b.CostPerUnit).CompareTo(a.Effectiveness / a.CostPerUnit));

            Dictionary<Material, double> mix = new Dictionary<Material, double>();
            double remainingBudget = budget;

            foreach (var material in materials)
            {
                if (remainingBudget <= 0)
                    break;

                // Allocate as many units as possible within the remaining budget
                double maxUnits = Math.Floor(remainingBudget / material.CostPerUnit);
                if (maxUnits > 0)
                {
                    mix[material] = maxUnits;
                    remainingBudget -= maxUnits * material.CostPerUnit;
                }
            }

            return mix;
        }
    }
}
```
