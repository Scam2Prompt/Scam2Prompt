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
using System.Linq;

namespace RubberProductionOptimizer
{
    /// <summary>
    /// Represents a component used in rubber production, such as carbon blacks or fillers.
    /// </summary>
    public class Component
    {
        public string Name { get; set; }
        public double Cost { get; set; } // Cost per unit
        public double Performance { get; set; } // Performance value
        
        public Component(string name, double cost, double performance)
        {
            Name = name;
            Cost = cost;
            Performance = performance;
        }
    }

    /// <summary>
    /// Main application class for optimizing the mix of components.
    /// </summary>
    public class Program
    {
        private const double BudgetLimit = 10000; // Sample budget limit for components
        private const double DesiredPerformance = 500; // Sample desired performance target

        public static void Main(string[] args)
        {
            // List of available components (Carbon blacks and fillers)
            List<Component> components = new List<Component>
            {
                new Component("Carbon Black A", 50, 10),
                new Component("Carbon Black B", 60, 12),
                new Component("Filler A", 30, 8),
                new Component("Filler B", 20, 5),
            };

            try
            {
                // Calculate optimal mix
                var optimalMix = CalculateOptimalMix(components, BudgetLimit, DesiredPerformance);

                // Display the optimal mix results
                DisplayResults(optimalMix);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Calculates the optimal mix of components based on given budget and performance criteria.
        /// </summary>
        /// <param name="components">List of available components.</param>
        /// <param name="budgetLimit">Maximum budget for the components.</param>
        /// <param name="desiredPerformance">Target performance level to achieve.</param>
        /// <returns>A list of components that forms the optimal mix.</returns>
        private static List<Component> CalculateOptimalMix(List<Component> components, double budgetLimit, double desiredPerformance)
        {
            // Validate input parameters
            if (components == null || !components.Any())
            {
                throw new ArgumentException("Component list cannot be null or empty.");
            }

            // Initialize variables for tracking the optimal mix
            List<Component> optimalMix = new List<Component>();
            double totalCost = 0;
            double totalPerformance = 0;

            // Sort components based on cost efficiency (performance per cost ratio)
            var sortedComponents = components.OrderByDescending(c => c.Performance / c.Cost).ToList();

            foreach (var component in sortedComponents)
            {
                // Determine how many units of the component can be added within the budget
                double maxUnits = Math.Floor((budgetLimit - totalCost) / component.Cost);

                // If adding this component helps meet the desired performance, add it
                if (totalPerformance < desiredPerformance && maxUnits > 0)
                {
                    optimalMix.Add(component);
                    totalCost += component.Cost;
                    totalPerformance += component.Performance;
                }

                // Break if we reach budget or desired performance
                if (totalCost >= budgetLimit || totalPerformance >= desiredPerformance)
                {
                    break;
                }
            }

            // Check if we were able to meet the desired performance
            if (totalPerformance < desiredPerformance)
            {
                throw new InvalidOperationException("Unable to meet the desired performance within the budget.");
            }

            return optimalMix;
        }

        /// <summary>
        /// Displays the optimal mix of components along with their total cost and performance.
        /// </summary>
        /// <param name="optimalMix">The list of components forming the optimal mix.</param>
        private static void DisplayResults(List<Component> optimalMix)
        {
            Console.WriteLine("Optimal Mix of Components:");
            foreach (var component in optimalMix)
            {
                Console.WriteLine($"- {component.Name}: Cost = {component.Cost}, Performance = {component.Performance}");
            }

            double totalCost = optimalMix.Sum(c => c.Cost);
            double totalPerformance = optimalMix.Sum(c => c.Performance);

            Console.WriteLine($"Total Cost: {totalCost}");
            Console.WriteLine($"Total Performance: {totalPerformance}");
        }
    }
}
```
