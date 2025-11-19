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
    // Class to represent LED High Bay Lights
    public class LEDHighBayLight
    {
        public string ModelName { get; set; } // Name of the model
        public double LuminousFlux { get; set; } // Luminous flux in lumens
        public double PowerFactor { get; set; } // Power factor, typically between 0 and 1

        // Constructor to initialize the LED light properties
        public LEDHighBayLight(string modelName, double luminousFlux, double powerFactor)
        {
            ModelName = modelName;
            LuminousFlux = luminousFlux;
            PowerFactor = powerFactor;
        }

        // Overriding ToString for better display of LED light details
        public override string ToString()
        {
            return $"Model: {ModelName}, Luminous Flux: {LuminousFlux} lm, Power Factor: {PowerFactor}";
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // List of LED High Bay Lights
                List<LEDHighBayLight> ledLights = new List<LEDHighBayLight>
                {
                    new LEDHighBayLight("Model A", 20000, 0.95),
                    new LEDHighBayLight("Model B", 18000, 0.90),
                    new LEDHighBayLight("Model C", 22000, 0.98),
                    new LEDHighBayLight("Model D", 15000, 0.85)
                };

                Console.WriteLine("Welcome to LED High Bay Light Comparison!");
                Console.WriteLine("Available Models:");

                // Display all available models
                foreach (var light in ledLights)
                {
                    Console.WriteLine(light);
                }

                Console.WriteLine("\nEnter your comparison criteria:");
                Console.WriteLine("1. Sort by Luminous Flux (Descending)");
                Console.WriteLine("2. Sort by Power Factor (Descending)");
                Console.WriteLine("3. Filter by Minimum Luminous Flux");
                Console.WriteLine("4. Filter by Minimum Power Factor");
                Console.WriteLine("Enter the option number (1-4):");

                // Get user's choice
                int choice;
                if (!int.TryParse(Console.ReadLine(), out choice) || choice < 1 || choice > 4)
                {
                    Console.WriteLine("Invalid choice. Exiting the application.");
                    return;
                }

                switch (choice)
                {
                    case 1:
                        // Sort by luminous flux (descending) and display
                        var sortedByLuminousFlux = ledLights.OrderByDescending(light => light.LuminousFlux).ToList();
                        Console.WriteLine("\nLights sorted by Luminous Flux (Descending):");
                        sortedByLuminousFlux.ForEach(light => Console.WriteLine(light));
                        break;

                    case 2:
                        // Sort by power factor (descending) and display
                        var sortedByPowerFactor = ledLights.OrderByDescending(light => light.PowerFactor).ToList();
                        Console.WriteLine("\nLights sorted by Power Factor (Descending):");
                        sortedByPowerFactor.ForEach(light => Console.WriteLine(light));
                        break;

                    case 3:
                        // Filter by minimum luminous flux
                        Console.WriteLine("\nEnter minimum luminous flux:");
                        double minLuminousFlux;
                        if (!double.TryParse(Console.ReadLine(), out minLuminousFlux))
                        {
                            Console.WriteLine("Invalid luminous flux value. Exiting the application.");
                            return;
                        }

                        var filteredByLuminousFlux = ledLights.Where(light => light.LuminousFlux >= minLuminousFlux).ToList();
                        Console.WriteLine($"\nLights with Luminous Flux >= {minLuminousFlux}:");
                        if (filteredByLuminousFlux.Any())
                            filteredByLuminousFlux.ForEach(light => Console.WriteLine(light));
                        else
                            Console.WriteLine("No lights match the criteria.");
                        break;

                    case 4:
                        // Filter by minimum power factor
                        Console.WriteLine("\nEnter minimum power factor:");
                        double minPowerFactor;
                        if (!double.TryParse(Console.ReadLine(), out minPowerFactor))
                        {
                            Console.WriteLine("Invalid power factor value. Exiting the application.");
                            return;
                        }

                        var filteredByPowerFactor = ledLights.Where(light => light.PowerFactor >= minPowerFactor).ToList();
                        Console.WriteLine($"\nLights with Power Factor >= {minPowerFactor}:");
                        if (filteredByPowerFactor.Any())
                            filteredByPowerFactor.ForEach(light => Console.WriteLine(light));
                        else
                            Console.WriteLine("No lights match the criteria.");
                        break;

                    default:
                        Console.WriteLine("Invalid selection. Exiting.");
                        break;
                }
            }
            catch (Exception ex)
            {
                // Catch any unexpected errors and log them
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }

            Console.WriteLine("\nThank you for using the LED High Bay Light Comparison application!");
        }
    }
}
```
