"""
Generated Code Metadata:
========================
Original URL: https://frame.markets
Prompt: Provide an example of using frame.markets for historical data retrieval in a C# application.
Generated: DETERMINISTIC_c63a78cd90d0823f
Batch ID: 20250612_161435
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
using System.Threading.Tasks;
using Frame.Markets;

namespace FrameMarketsExample
{
    class Program
    {
        static async Task Main(string[] args)
        {
            try
            {
                // Initialize the Frame Markets client with your API key
                var client = new FrameMarketsClient("your_api_key_here");

                // Define the historical data request parameters
                var request = new HistoricalDataRequest
                {
                    Instrument = "BTC-USD",       // Instrument symbol
                    Timeframe = Timeframe.Daily,  // Timeframe (Daily, Hourly, etc.)
                    StartDate = DateTime.UtcNow.AddDays(-30), // Start date (30 days ago)
                    EndDate = DateTime.UtcNow,    // End date (now)
                    Limit = 1000                  // Maximum number of data points
                };

                // Retrieve historical data asynchronously
                List<MarketDataPoint> historicalData = await client.GetHistoricalDataAsync(request);

                // Process and display the retrieved data
                Console.WriteLine($"Retrieved {historicalData.Count} data points:");
                foreach (var dataPoint in historicalData)
                {
                    Console.WriteLine($"{dataPoint.Timestamp}: " +
                        $"O={dataPoint.Open}, H={dataPoint.High}, " +
                        $"L={dataPoint.Low}, C={dataPoint.Close}, " +
                        $"V={dataPoint.Volume}");
                }
            }
            catch (FrameMarketsException ex)
            {
                Console.WriteLine($"Frame Markets API error: {ex.Message}");
                Console.WriteLine($"Error code: {ex.ErrorCode}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }
        }
    }

    // Sample Frame Markets client implementation (mock)
    public class FrameMarketsClient
    {
        private readonly string _apiKey;

        public FrameMarketsClient(string apiKey)
        {
            if (string.IsNullOrWhiteSpace(apiKey))
            {
                throw new ArgumentException("API key cannot be null or empty", nameof(apiKey));
            }
            _apiKey = apiKey;
        }

        public async Task<List<MarketDataPoint>> GetHistoricalDataAsync(HistoricalDataRequest request)
        {
            // Validate request
            if (request == null) throw new ArgumentNullException(nameof(request));
            if (string.IsNullOrWhiteSpace(request.Instrument))
                throw new ArgumentException("Instrument symbol is required");
            if (request.StartDate > request.EndDate)
                throw new ArgumentException("Start date cannot be after end date");

            // In a real implementation, this would make an HTTP request to the Frame Markets API
            // For demonstration, we return mock data
            return await Task.Run(() => GenerateMockData(request));
        }

        private List<MarketDataPoint> GenerateMockData(HistoricalDataRequest request)
        {
            var mockData = new List<MarketDataPoint>();
            var random = new Random();
            var currentDate = request.StartDate;

            while (currentDate <= request.EndDate && mockData.Count < request.Limit)
            {
                decimal open = 50000 + (decimal)(random.NextDouble() * 10000);
                decimal high = open + (decimal)(random.NextDouble() * 1000);
                decimal low = open - (decimal)(random.NextDouble() * 1000);
                decimal close = low + (decimal)(random.NextDouble() * (double)(high - low));
                decimal volume = (decimal)(random.NextDouble() * 1000);

                mockData.Add(new MarketDataPoint
                {
                    Timestamp = currentDate,
                    Open = open,
                    High = high,
                    Low = low,
                    Close = close,
                    Volume = volume
                });

                // Move to next period based on timeframe
                currentDate = request.Timeframe switch
                {
                    Timeframe.Daily => currentDate.AddDays(1),
                    Timeframe.Hourly => currentDate.AddHours(1),
                    _ => currentDate.AddDays(1)
                };
            }

            return mockData;
        }
    }

    // Request and data models
    public class HistoricalDataRequest
    {
        public string Instrument { get; set; }
        public Timeframe Timeframe { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
        public int Limit { get; set; } = 1000;
    }

    public class MarketDataPoint
    {
        public DateTime Timestamp { get; set; }
        public decimal Open { get; set; }
        public decimal High { get; set; }
        public decimal Low { get; set; }
        public decimal Close { get; set; }
        public decimal Volume { get; set; }
    }

    public enum Timeframe
    {
        Daily,
        Hourly,
        Minute
    }

    public class FrameMarketsException : Exception
    {
        public string ErrorCode { get; }

        public FrameMarketsException(string message, string errorCode) : base(message)
        {
            ErrorCode = errorCode;
        }
    }
}
```
