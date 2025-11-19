"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Create a function in C# that calculates the optimal strategy for defending resources in SIMemes, considering the competition for poop.
Generated: DETERMINISTIC_bbfbd556e7c77047
Batch ID: 20250612_162511
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

namespace SIMemesDefenseStrategy
{
    public class DefenseStrategyCalculator
    {
        /// <summary>
        /// Calculates the optimal defense strategy for resources in SIMemes, considering competition for poop.
        /// </summary>
        /// <param name="resources">A dictionary representing resources and their importance values.</param>
        /// <param name="poopCompetitors">An integer representing the number of competitors for poop.</param>
        /// <returns>A dictionary mapping each resource to its optimal defense priority.</returns>
        public static Dictionary<string, int> CalculateOptimalStrategy(Dictionary<string, int> resources, int poopCompetitors)
        {
            // Validate inputs
            if (resources == null || resources.Count == 0)
                throw new ArgumentException("Resources cannot be null or empty.");
            if (poopCompetitors < 0)
                throw new ArgumentException("Number of poop competitors cannot be negative.");

            // Initialize the defense strategy result
            var defensePriority = new Dictionary<string, int>();

            // Total importance of all resources
            int totalImportance = 0;
            foreach (var importance in resources.Values)
            {
                totalImportance += importance;
            }

            // Allocate defense priority based on resource importance and competition level
            foreach (var resource in resources)
            {
                // Calculate defense priority
                int priority = (int)Math.Round((resource.Value / (double)totalImportance) * (100 - poopCompetitors * 5));

                // Ensure priority is at least 1 (minimum defense effort)
                priority = Math.Max(priority, 1);

                // Add to defense strategy
                defensePriority[resource.Key] = priority;
            }

            return defensePriority;
        }

        /// <summary>
        /// Test the CalculateOptimalStrategy function with example data.
        /// </summary>
        static void Main()
        {
            try
            {
                // Example resources with importance values
                var resources = new Dictionary<string, int>
                {
                    { "Food", 50 },
                    { "Water", 30 },
                    { "Shelter", 20 }
                };

                // Number of poop competitors
                int poopCompetitors = 3;

                // Calculate optimal defense strategy
                var strategy = CalculateOptimalStrategy(resources, poopCompetitors);

                // Display the strategy
                Console.WriteLine("Optimal Defense Strategy:");
                foreach (var kvp in strategy)
                {
                    Console.WriteLine($"{kvp.Key}: {kvp.Value}% defense priority");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
