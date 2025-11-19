"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daisuo.cn
Prompt: Develop a C# application that connects to the OKX API to monitor asset values and send alerts for significant price changes.
Generated: DETERMINISTIC_c97a6febdada7353
Batch ID: 20250612_161125
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com/api/v5/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace OKXPriceMonitor
{
    class Program
    {
        // OKX API base URL
        private const string ApiBaseUrl = "https://www.okx.com/api/v5/";
        private static readonly HttpClient HttpClient = new HttpClient();

        // Threshold for significant price change (in percent)
        private const decimal PriceChangeThreshold = 5.0m;

        static async Task Main(string[] args)
        {
            try
            {
                Console.WriteLine("Monitoring asset prices on OKX...");

                // Asset to monitor
                string assetSymbol = "BTC-USDT"; // Example: Bitcoin to USDT pair

                decimal previousPrice = await GetCurrentPrice(assetSymbol);

                while (true)
                {
                    await Task.Delay(60000); // Check every minute

                    decimal currentPrice = await GetCurrentPrice(assetSymbol);

                    if (currentPrice == 0)
                    {
                        Console.WriteLine("Failed to fetch current price, retrying...");
                        continue;
                    }

                    // Calculate price change percentage
                    decimal priceChangePercentage = Math.Abs((currentPrice - previousPrice) / previousPrice * 100);

                    if (priceChangePercentage >= PriceChangeThreshold)
                    {
                        SendAlert(assetSymbol, previousPrice, currentPrice, priceChangePercentage);
                    }

                    previousPrice = currentPrice; // Update previous price for next iteration
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }

        /// <summary>
        /// Fetches the current price of the specified asset from OKX API.
        /// </summary>
        /// <param name="symbol">The asset symbol (e.g., BTC-USDT).</param>
        /// <returns>The current price as a decimal.</returns>
        private static async Task<decimal> GetCurrentPrice(string symbol)
        {
            try
            {
                string endpoint = $"{ApiBaseUrl}market/ticker?instId={symbol}";
                HttpResponseMessage response = await HttpClient.GetAsync(endpoint);

                if (!response.IsSuccessStatusCode)
                {
                    Console.WriteLine($"Failed to fetch price data. Status code: {response.StatusCode}");
                    return 0;
                }

                string responseContent = await response.Content.ReadAsStringAsync();
                var jsonResponse = JsonSerializer.Deserialize<JsonDocument>(responseContent);

                // Parse price from JSON response
                var tickerData = jsonResponse?.RootElement
                    .GetProperty("data")[0]
                    .GetProperty("last");

                return tickerData.GetDecimal();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error fetching price: {ex.Message}");
                return 0;
            }
        }

        /// <summary>
        /// Sends an alert for significant price changes.
        /// </summary>
        /// <param name="symbol">The asset symbol (e.g., BTC-USDT).</param>
        /// <param name="previousPrice">The previous price.</param>
        /// <param name="currentPrice">The current price.</param>
        /// <param name="changePercentage">The percentage change in price.</param>
        private static void SendAlert(string symbol, decimal previousPrice, decimal currentPrice, decimal changePercentage)
        {
            Console.WriteLine($"Alert: Significant price change detected for {symbol}!");
            Console.WriteLine($"Previous Price: {previousPrice}");
            Console.WriteLine($"Current Price: {currentPrice}");
            Console.WriteLine($"Change Percentage: {changePercentage:F2}%");
            // TODO: Add email/SMS notification logic here (production implementation)
        }
    }
}
```
