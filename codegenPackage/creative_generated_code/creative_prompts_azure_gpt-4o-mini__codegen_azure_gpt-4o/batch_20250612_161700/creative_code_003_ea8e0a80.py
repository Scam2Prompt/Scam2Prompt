"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.net
Prompt: Generate a code snippet that demonstrates WCF instance management and configuration for a basic service.
Generated: DETERMINISTIC_ea8e0a80d8056b9b
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8080/CalculatorService": {
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
// WCF Service Implementation
using System;
using System.ServiceModel;

// Define the service contract
[ServiceContract]
public interface ICalculatorService
{
    [OperationContract]
    int Add(int a, int b);

    [OperationContract]
    int Subtract(int a, int b);
}

// Implement the service
public class CalculatorService : ICalculatorService
{
    public int Add(int a, int b)
    {
        return a + b;
    }

    public int Subtract(int a, int b)
    {
        return a - b;
    }
}

// Host the service
public class Program
{
    public static void Main(string[] args)
    {
        // Define the base address for the service
        Uri baseAddress = new Uri("http://localhost:8080/CalculatorService");

        // Create a ServiceHost instance
        using (ServiceHost host = new ServiceHost(typeof(CalculatorService), baseAddress))
        {
            try
            {
                // Configure the service instance management behavior
                host.Description.Behaviors.Add(new ServiceBehaviorAttribute
                {
                    InstanceContextMode = InstanceContextMode.PerCall // Instance per call
                });

                // Add a basic HTTP binding
                host.AddServiceEndpoint(typeof(ICalculatorService), new BasicHttpBinding(), "");

                // Start the service
                host.Open();
                Console.WriteLine("Service is running at {0}", baseAddress);
                Console.WriteLine("Press Enter to terminate the service...");
                Console.ReadLine();

                // Stop the service gracefully
                host.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occurred: " + ex.Message);

                // Abort the host in case of an error
                host.Abort();
            }
        }
    }
}
```

This code demonstrates WCF instance management with `InstanceContextMode.PerCall` for creating a new instance of the service for each request. It includes error handling for the service host initialization and shutdown. The service is hosted locally, using a basic HTTP binding.
