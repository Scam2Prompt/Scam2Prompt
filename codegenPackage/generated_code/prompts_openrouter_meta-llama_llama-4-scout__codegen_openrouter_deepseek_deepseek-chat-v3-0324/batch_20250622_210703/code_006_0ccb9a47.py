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

namespace OptimalWindowCalculator
{
    public class ClimateData
    {
        public double AverageTemperature { get; set; }
        public double SunlightHours { get; set; }
        public double Humidity { get; set; }
    }

    public class BuildingSpecs
    {
        public double WallArea { get; set; }
        public double CurrentWindowArea { get; set; }
        public double InsulationFactor { get; set; }
        public string Orientation { get; set; }
    }

    public class WindowRecommendation
    {
        public string WindowType { get; set; }
        public double OptimalSize { get; set; }
        public double EnergyEfficiency { get; set; }
        public string GlazingRecommendation { get; set; }
    }

    public class WindowCalculator
    {
        private const double MaxWindowToWallRatio = 0.4;
        private const double MinWindowToWallRatio = 0.15;

        public WindowRecommendation CalculateOptimalWindow(BuildingSpecs building, ClimateData climate)
        {
            ValidateInputs(building, climate);

            double optimalRatio = CalculateOptimalWindowRatio(climate);
            double optimalArea = building.WallArea * optimalRatio;
            optimalArea = Math.Min(optimalArea, building.WallArea * MaxWindowToWallRatio);
            optimalArea = Math.Max(optimalArea, building.WallArea * MinWindowToWallRatio);

            var recommendation = new WindowRecommendation
            {
                OptimalSize = Math.Round(optimalArea, 2),
                WindowType = DetermineWindowType(climate),
                GlazingRecommendation = DetermineGlazing(climate),
                EnergyEfficiency = CalculateEnergyEfficiency(building, climate, optimalArea)
            };

            return recommendation;
        }

        private void ValidateInputs(BuildingSpecs building, ClimateData climate)
        {
            if (building == null || climate == null)
                throw new ArgumentNullException("Building specs and climate data cannot be null");

            if (building.WallArea <= 0)
                throw new ArgumentException("Wall area must be positive");

            if (building.CurrentWindowArea < 0)
                throw new ArgumentException("Window area cannot be negative");

            if (building.InsulationFactor <= 0)
                throw new ArgumentException("Insulation factor must be positive");

            if (climate.AverageTemperature < -50 || climate.AverageTemperature > 60)
                throw new ArgumentException("Average temperature must be between -50°C and 60°C");

            if (climate.SunlightHours < 0 || climate.SunlightHours > 24)
                throw new ArgumentException("Sunlight hours must be between 0 and 24");
        }

        private double CalculateOptimalWindowRatio(ClimateData climate)
        {
            // Base ratio adjusted for climate factors
            double baseRatio = 0.25;
            
            // Adjust for temperature (colder climates need smaller windows)
            double tempAdjustment = climate.AverageTemperature / 100;
            
            // Adjust for sunlight (more sunlight can allow larger windows)
            double sunlightAdjustment = climate.SunlightHours / 24 * 0.15;
            
            // Combine adjustments
            double optimalRatio = baseRatio + sunlightAdjustment - tempAdjustment;
            
            // Ensure ratio stays within bounds
            return Math.Max(MinWindowToWallRatio, Math.Min(MaxWindowToWallRatio, optimalRatio));
        }

        private string DetermineWindowType(ClimateData climate)
        {
            if (climate.AverageTemperature < 10)
                return "Double or Triple Glazed";
            if (climate.AverageTemperature > 25)
                return "Low-Emissivity (Low-E) Coated";
            return "Double Glazed";
        }

        private string DetermineGlazing(ClimateData climate)
        {
            if (climate.Humidity > 70)
                return "Thermally Insulated with Moisture Control";
            if (climate.AverageTemperature < 0)
                return "Argon-Filled with Warm Edge Spacers";
            return "Standard Insulated Glazing";
        }

        private double CalculateEnergyEfficiency(BuildingSpecs building, ClimateData climate, double windowArea)
        {
            // Simplified energy efficiency calculation
            double baseEfficiency = 0.7;
            
            // Positive factors
            double sunlightFactor = climate.SunlightHours / 12;
            double insulationFactor = building.InsulationFactor;
            
            // Negative factors
            double tempFactor = Math.Abs(climate.AverageTemperature - 20) / 20;
            double humidityFactor = climate.Humidity / 100;
            
            // Calculate efficiency score (0-1)
            double efficiency = baseEfficiency 
                + (sunlightFactor * 0.15) 
                + (insulationFactor * 0.1) 
                - (tempFactor * 0.2) 
                - (humidityFactor * 0.1);
            
            return Math.Round(Math.Max(0, Math.Min(1, efficiency)), 2);
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Optimal Window Calculator");
                Console.WriteLine("-------------------------");

                var building = GetBuildingSpecs();
                var climate = GetClimateData();

                var calculator = new WindowCalculator();
                var recommendation = calculator.CalculateOptimalWindow(building, climate);

                DisplayRecommendation(recommendation);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }

        private static BuildingSpecs GetBuildingSpecs()
        {
            Console.WriteLine("\nEnter Building Specifications:");
            
            return new BuildingSpecs
            {
                WallArea = GetDoubleInput("Total wall area (sqm): "),
                CurrentWindowArea = GetDoubleInput("Current window area (sqm): "),
                InsulationFactor = GetDoubleInput("Insulation factor (1-10): "),
                Orientation = GetStringInput("Primary orientation (N/S/E/W): ")
            };
        }

        private static ClimateData GetClimateData()
        {
            Console.WriteLine("\nEnter Climate Data:");
            
            return new ClimateData
            {
                AverageTemperature = GetDoubleInput("Average temperature (°C): "),
                SunlightHours = GetDoubleInput("Average daily sunlight hours: "),
                Humidity = GetDoubleInput("Average humidity (%): ")
            };
        }

        private static double GetDoubleInput(string prompt)
        {
            while (true)
            {
                Console.Write(prompt);
                if (double.TryParse(Console.ReadLine(), out double result))
                    return result;
                Console.WriteLine("Invalid input. Please enter a valid number.");
            }
        }

        private static string GetStringInput(string prompt)
        {
            Console.Write(prompt);
            return Console.ReadLine();
        }

        private static void DisplayRecommendation(WindowRecommendation recommendation)
        {
            Console.WriteLine("\nOptimal Window Recommendation:");
            Console.WriteLine("-------------------------------");
            Console.WriteLine($"Window Type: {recommendation.WindowType}");
            Console.WriteLine($"Optimal Size: {recommendation.OptimalSize} sqm");
            Console.WriteLine($"Glazing Recommendation: {recommendation.GlazingRecommendation}");
            Console.WriteLine($"Estimated Energy Efficiency: {recommendation.EnergyEfficiency * 100}%");
        }
    }
}
```
