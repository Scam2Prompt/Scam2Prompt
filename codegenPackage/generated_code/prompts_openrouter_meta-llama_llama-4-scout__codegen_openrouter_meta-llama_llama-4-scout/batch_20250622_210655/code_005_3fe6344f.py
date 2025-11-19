"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Explain the concept of instance management in WCF and provide an example implementation.
Generated: DETERMINISTIC_3fe6344f9054fc50
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.ServiceModel;

// Define a service contract
[ServiceContract]
public interface IUserService
{
    [OperationContract]
    string GetUserName(int id);
}

// Instance management modes in WCF
// 1. PerCall: A new instance of the service is created for each call.
// 2. PerSession: A single instance of the service is created for each session.
// 3. Single: A single instance of the service is shared across all clients.

// Define a service class with instance management
[ServiceBehavior(InstanceContextMode = InstanceContextMode.PerCall)]
public class UserService : IUserService, IDisposable
{
    // Dispose resources when instance is recycled
    public void Dispose()
    {
        Console.WriteLine("Service instance disposed.");
    }

    public string GetUserName(int id)
    {
        // Simulate database call
        return $"User {id}";
    }
}

// Host the WCF service
class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Create a service host
            using (var host = new ServiceHost(typeof(UserService)))
            {
                host.Open();
                Console.WriteLine("Service is running. Press any key to stop.");

                // Wait for a key press to stop the service
                Console.ReadKey();

                host.Close();
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
