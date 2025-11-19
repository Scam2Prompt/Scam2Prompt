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
using System.Linq;

namespace RubberProductionOptimizer
{
    /// <summary>
    /// Represents a pigment or additive with its properties
    /// </summary>
    public class Material
    {
        public string Name { get; set; }
        public double CostPerKg { get; set; }
        public double PerformanceIndex { get; set; } // Higher is better
        public double Density { get; set; } // kg/m³
        public double MaxPercentage { get; set; } // Maximum allowed in mix (0-1)
    }

    /// <summary>
    /// Represents a rubber compound formulation
    /// </summary>
    public class RubberCompound
    {
        public Dictionary<Material, double> Composition { get; set; } // Material -> percentage (0-1)
        public double TotalCost { get; set; }
        public double TotalPerformance { get; set; }
    }

    /// <summary>
    /// Optimizes the mix of carbon blacks and fillers for rubber production
    /// </summary>
    public class RubberOptimizer
    {
        private List<Material> _availableMaterials;
        private double _totalWeight;
        private double _minPerformance;
        private double _maxCost;

        /// <summary>
        /// Initialize the optimizer with available materials and constraints
        /// </summary>
        public RubberOptimizer(List<Material> materials, double totalWeight, double minPerformance, double maxCost)
        {
            if (materials == null || !materials.Any())
                throw new ArgumentException("Materials list cannot be empty", nameof(materials));

            if (totalWeight <= 0)
                throw new ArgumentException("Total weight must be positive", nameof(totalWeight));

            _availableMaterials = materials;
            _totalWeight = totalWeight;
            _minPerformance = minPerformance;
            _maxCost = maxCost;
        }

        /// <summary>
        /// Finds the optimal mix of materials
        /// </summary>
        public RubberCompound Optimize()
        {
            // Filter materials that are too expensive to possibly meet cost constraints
            var feasibleMaterials = _availableMaterials
                .Where(m => m.CostPerKg <= _maxCost)
                .OrderBy(m => m.CostPerKg / m.PerformanceIndex)
                .ToList();

            if (!feasibleMaterials.Any())
                throw new InvalidOperationException("No feasible materials found within cost constraints");

            var compound = new RubberCompound { Composition = new Dictionary<Material, double>() };
            double remainingWeight = _totalWeight;
            double remainingPerformance = _minPerformance;

            // Greedy algorithm: select materials with best cost/performance ratio first
            foreach (var material in feasibleMaterials)
            {
                if (remainingPerformance <= 0 && Math.Abs(remainingWeight) < 0.0001)
                    break;

                double maxPossible = Math.Min(material.MaxPercentage * _totalWeight, remainingWeight);
                if (maxPossible <= 0) continue;

                double neededForPerformance = remainingPerformance / material.PerformanceIndex;
                double amountToUse = Math.Min(maxPossible, neededForPerformance);

                if (amountToUse > 0)
                {
                    double percentage = amountToUse / _totalWeight;
                    compound.Composition[material] = percentage;
                    remainingWeight -= amountToUse;
                    remainingPerformance -= amountToUse * material.PerformanceIndex;
                }
            }

            // If we couldn't meet performance requirements with the given materials
            if (remainingPerformance > 0)
                throw new InvalidOperationException("Could not meet performance requirements with available materials");

            // Calculate totals
            compound.TotalCost = compound.Composition.Sum(x => x.Key.CostPerKg * x.Value * _totalWeight);
            compound.TotalPerformance = compound.Composition.Sum(x => x.Key.PerformanceIndex * x.Value * _totalWeight);

            // Verify constraints
            if (compound.TotalCost > _maxCost)
                throw new InvalidOperationException("Optimization failed to meet cost constraints");

            if (compound.TotalPerformance < _minPerformance)
                throw new InvalidOperationException("Optimization failed to meet performance constraints");

            return compound;
        }
    }

    /// <summary>
    /// Main application class
    /// </summary>
    public class Program
    {
        public static void Main(string[] args)
        {
            try
            {
                // Sample materials from M J Pigment & Additives
                var materials = new List<Material>
                {
                    new Material { Name = "N110 Carbon Black", CostPerKg = 1.20, PerformanceIndex = 95, Density = 1800, MaxPercentage = 0.30 },
                    new Material { Name = "N220 Carbon Black", CostPerKg = 1.10, PerformanceIndex = 85, Density = 1850, MaxPercentage = 0.35 },
                    new Material { Name = "N330 Carbon Black", CostPerKg = 1.00, PerformanceIndex = 75, Density = 1900, MaxPercentage = 0.40 },
                    new Material { Name = "Silica Filler", CostPerKg = 0.90, PerformanceIndex = 65, Density = 2100, MaxPercentage = 0.25 },
                    new Material { Name = "Clay Filler", CostPerKg = 0.60, PerformanceIndex = 50, Density = 2200, MaxPercentage = 0.20 }
                };

                Console.WriteLine("Rubber Production Optimizer");
                Console.WriteLine("----------------------------");

                Console.Write("Enter total batch weight (kg): ");
                double totalWeight = double.Parse(Console.ReadLine());

                Console.Write("Enter minimum required performance index: ");
                double minPerformance = double.Parse(Console.ReadLine());

                Console.Write("Enter maximum allowed cost per kg: ");
                double maxCost = double.Parse(Console.ReadLine());

                var optimizer = new RubberOptimizer(materials, totalWeight, minPerformance, maxCost);
                var optimalMix = optimizer.Optimize();

                Console.WriteLine("\nOptimal Mix:");
                Console.WriteLine($"Total Cost: {optimalMix.TotalCost:C2}");
                Console.WriteLine($"Total Performance: {optimalMix.TotalPerformance:F2}");
                Console.WriteLine("\nComposition:");

                foreach (var item in optimalMix.Composition.OrderByDescending(x => x.Value))
                {
                    Console.WriteLine($"{item.Key.Name}: {item.Value * 100:F2}% ({item.Value * totalWeight:F2} kg)");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
