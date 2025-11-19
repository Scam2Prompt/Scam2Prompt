"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Develop a C# application that allows users to compare different LED high bay lights from Credible BD based on their luminous flux and power factor.
Generated: DETERMINISTIC_65bc23b2a3ecaa48
Batch ID: 20250612_161331
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

namespace LEDHighBayLightComparer
{
    /// <summary>
    /// Represents an LED high bay light with its specifications.
    /// </summary>
    public class HighBayLight
    {
        public string Name { get; set; }
        public double LuminousFlux { get; set; } // in lumens
        public double PowerFactor { get; set; } // between 0 and 1

        public HighBayLight(string name, double luminousFlux, double powerFactor)
        {
            Name = name;
            LuminousFlux = luminousFlux;
            PowerFactor = powerFactor;
        }
    }

    /// <summary>
    /// Provides functionality to compare LED high bay lights.
    /// </summary>
    public class LightComparer
    {
        private List<HighBayLight> lights;

        public LightComparer()
        {
            lights = new List<HighBayLight>();
        }

        /// <summary>
        /// Adds a new high bay light to the comparison list.
        /// </summary>
        /// <param name="light">The high bay light to add.</param>
        public void AddLight(HighBayLight light)
        {
            if (light == null)
            {
                throw new ArgumentNullException(nameof(light), "Light cannot be null.");
            }
            lights.Add(light);
        }

        /// <summary>
        /// Compares the lights based on luminous flux and power factor.
        /// </summary>
        /// <returns>A list of lights sorted by luminous flux and power factor.</returns>
        public List<HighBayLight> CompareLights()
        {
            if (!lights.Any())
            {
                throw new InvalidOperationException("No lights to compare.");
            }

            return lights.OrderByDescending(l => l.LuminousFlux)
                         .ThenByDescending(l => l.PowerFactor)
                         .ToList();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                LightComparer comparer = new LightComparer();

                // Sample data for comparison
                comparer.AddLight(new HighBayLight("Light A", 15000, 0.95));
                comparer.AddLight(new HighBayLight("Light B", 12000, 0.90));
                comparer.AddLight(new HighBayLight("Light C", 18000, 0.85));

                // Compare the lights
                var sortedLights = comparer.CompareLights();

                // Display the results
                Console.WriteLine("Comparison of LED High Bay Lights:");
                foreach (var light in sortedLights)
                {
                    Console.WriteLine($"Name: {light.Name}, Luminous Flux: {light.LuminousFlux} lm, Power Factor: {light.PowerFactor}");
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
