"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Illustrate the process of hosting a WCF service, including instance management strategies mentioned in the WCF Tutorial.
Generated: DETERMINISTIC_b44504f756acd1fa
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8080/MyService": {
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
using System.ServiceModel;

// Define the service contract
[ServiceContract]
public interface IMyService
{
    [OperationContract]
    string GetData(int value);
}

// Implement the service
public class MyService : IMyService
{
    public string GetData(int value)
    {
        return $"You entered: {value}";
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Define the base address for the service
        Uri baseAddress = new Uri("http://localhost:8080/MyService");

        // Create the ServiceHost for the MyService type
        using (ServiceHost host = new ServiceHost(typeof(MyService), baseAddress))
        {
            try
            {
                // Configure instance management strategy
                // Options: PerCall, PerSession, or Singleton
                host.Description.Behaviors.Remove(typeof(ServiceBehaviorAttribute));
                host.Description.Behaviors.Add(new ServiceBehaviorAttribute
                {
                    InstanceContextMode = InstanceContextMode.PerCall // Change to PerSession or Singleton as needed
                });

                // Add an endpoint
                host.AddServiceEndpoint(typeof(IMyService), new BasicHttpBinding(), "");

                // Open the ServiceHost to start listening for messages
                host.Open();
                Console.WriteLine($"Service hosted at {baseAddress}");
                Console.WriteLine("Press Enter to terminate the service...");

                // Keep the service running until the user presses Enter
                Console.ReadLine();
            }
            catch (Exception ex)
            {
                // Handle exceptions that occur during service hosting
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
            finally
            {
                // Ensure the ServiceHost is properly closed
                if (host.State == CommunicationState.Opened)
                {
                    host.Close();
                }
            }
        }
    }
}
```
