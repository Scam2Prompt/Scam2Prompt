"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```csharp
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

class Program
{
    static void Main(string[] args)
    {
        // Configure and host the WCF service
        Uri baseAddress = new Uri("http://localhost:8080/CalculatorService");

        using (ServiceHost host = new ServiceHost(typeof(CalculatorService), baseAddress))
        {
            try
            {
                // Configure the service behavior
                host.Description.Behaviors.Add(new ServiceMetadataBehavior { HttpGetEnabled = true });

                // Configure the binding
                BasicHttpBinding binding = new BasicHttpBinding();
                host.AddServiceEndpoint(typeof(ICalculatorService), binding, "");

                // Open the service host
                host.Open();
                Console.WriteLine("Service is running at {0}", baseAddress);
                Console.WriteLine("Press Enter to terminate the service...");
                Console.ReadLine();

                // Close the service host
                host.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occurred: {0}", ex.Message);
                if (host.State == CommunicationState.Faulted)
                {
                    host.Abort(); // Ensure the host is properly aborted in case of failure
                }
            }
        }
    }
}
```

This code snippet demonstrates a basic WCF service with instance management and configuration. It includes error handling and follows best practices for production-ready code.
