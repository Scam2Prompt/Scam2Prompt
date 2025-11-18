"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.net
Prompt: Provide a code example of using ChannelFactory caching in WCF for efficient service consumption, as explained on https://topwcftutorials.net.
Generated: DETERMINISTIC_9d9fbf70a9914741
Batch ID: 20250612_152924
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
using System.Collections.Generic;

namespace WcfChannelFactoryCaching
{
    // Example service contract
    [ServiceContract]
    public interface IMyService
    {
        [OperationContract]
        string GetData(int value);
    }

    // Caching ChannelFactory for WCF services
    public static class ChannelFactoryCache<T>
    {
        private static readonly Dictionary<string, ChannelFactory<T>> _cache = new();

        // Method to get or create a ChannelFactory
        public static ChannelFactory<T> GetChannelFactory(string endpointAddress)
        {
            if (_cache.ContainsKey(endpointAddress))
            {
                return _cache[endpointAddress];
            }
            else
            {
                var factory = new ChannelFactory<T>(new BasicHttpBinding(), new EndpointAddress(endpointAddress));
                _cache[endpointAddress] = factory;
                return factory;
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            string endpointAddress = "http://localhost:8080/MyService";

            try
            {
                // Obtain the channel factory from the cache
                var channelFactory = ChannelFactoryCache<IMyService>.GetChannelFactory(endpointAddress);
                
                // Create a channel to the service
                var channel = channelFactory.CreateChannel();

                // Call the service method
                string result = channel.GetData(42);
                Console.WriteLine($"Service response: {result}");

                // Close the channel
                ((IClientChannel)channel).Close();
            }
            catch (FaultException ex)
            {
                // Handle WCF service fault exception
                Console.WriteLine($"Service Fault: {ex.Message}");
            }
            catch (CommunicationException ex)
            {
                // Handle communication exceptions
                Console.WriteLine($"Communication Error: {ex.Message}");
            }
            catch (Exception ex)
            {
                // Handle any other exceptions
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
