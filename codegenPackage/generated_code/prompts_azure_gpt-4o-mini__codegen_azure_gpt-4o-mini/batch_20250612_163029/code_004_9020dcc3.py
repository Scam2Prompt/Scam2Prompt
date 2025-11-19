"""
Generated Code Metadata:
========================
Original URL: https://thearbitrixedge.com
Prompt: Create a C# application that configures trading parameters for the Arbitrix Edge software, allowing users to customize their trading strategies.
Generated: DETERMINISTIC_9020dcc3698b9a02
Batch ID: 20250612_163029
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
using System.IO;
using Newtonsoft.Json;

namespace ArbitrixEdgeConfigurator
{
    // Class to hold trading parameters
    public class TradingParameters
    {
        public string StrategyName { get; set; }
        public decimal BuyThreshold { get; set; }
        public decimal SellThreshold { get; set; }
        public int MaxTrades { get; set; }
        public bool EnableStopLoss { get; set; }
        public decimal StopLossPercentage { get; set; }
    }

    // Class to handle configuration operations
    public class Configurator
    {
        private const string ConfigFilePath = "tradingConfig.json";

        // Method to load trading parameters from a JSON file
        public TradingParameters LoadParameters()
        {
            try
            {
                if (!File.Exists(ConfigFilePath))
                {
                    throw new FileNotFoundException("Configuration file not found.");
                }

                var json = File.ReadAllText(ConfigFilePath);
                return JsonConvert.DeserializeObject<TradingParameters>(json);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error loading parameters: {ex.Message}");
                return null;
            }
        }

        // Method to save trading parameters to a JSON file
        public void SaveParameters(TradingParameters parameters)
        {
            try
            {
                var json = JsonConvert.SerializeObject(parameters, Formatting.Indented);
                File.WriteAllText(ConfigFilePath, json);
                Console.WriteLine("Parameters saved successfully.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error saving parameters: {ex.Message}");
            }
        }
    }

    // Main application class
    class Program
    {
        static void Main(string[] args)
        {
            var configurator = new Configurator();
            TradingParameters parameters = null;

            // Load existing parameters or create new ones
            parameters = configurator.LoadParameters() ?? new TradingParameters();

            // Display current parameters
            Console.WriteLine("Current Trading Parameters:");
            Console.WriteLine($"Strategy Name: {parameters.StrategyName}");
            Console.WriteLine($"Buy Threshold: {parameters.BuyThreshold}");
            Console.WriteLine($"Sell Threshold: {parameters.SellThreshold}");
            Console.WriteLine($"Max Trades: {parameters.MaxTrades}");
            Console.WriteLine($"Enable Stop Loss: {parameters.EnableStopLoss}");
            Console.WriteLine($"Stop Loss Percentage: {parameters.StopLossPercentage}");

            // User input for new parameters
            Console.WriteLine("\nEnter new trading parameters:");

            Console.Write("Strategy Name: ");
            parameters.StrategyName = Console.ReadLine();

            Console.Write("Buy Threshold: ");
            parameters.BuyThreshold = decimal.Parse(Console.ReadLine());

            Console.Write("Sell Threshold: ");
            parameters.SellThreshold = decimal.Parse(Console.ReadLine());

            Console.Write("Max Trades: ");
            parameters.MaxTrades = int.Parse(Console.ReadLine());

            Console.Write("Enable Stop Loss (true/false): ");
            parameters.EnableStopLoss = bool.Parse(Console.ReadLine());

            if (parameters.EnableStopLoss)
            {
                Console.Write("Stop Loss Percentage: ");
                parameters.StopLossPercentage = decimal.Parse(Console.ReadLine());
            }

            // Save updated parameters
            configurator.SaveParameters(parameters);
        }
    }
}
```

Make sure to include the Newtonsoft.Json NuGet package in your project to handle JSON serialization and deserialization.
