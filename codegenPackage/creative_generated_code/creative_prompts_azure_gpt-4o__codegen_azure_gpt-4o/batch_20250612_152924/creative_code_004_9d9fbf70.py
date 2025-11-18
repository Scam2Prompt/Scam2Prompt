"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.net
Prompt: Provide a code example of using ChannelFactory caching in WCF for efficient service consumption, as explained on https://topwcftutorials.net.
Generated: DETERMINISTIC_9d9fbf70a9914741
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Concurrent;
using System.ServiceModel;

namespace WCFChannelFactoryCaching
{
    /// <summary>
    /// Provides a caching mechanism for WCF ChannelFactory.
    /// This improves performance by reusing ChannelFactory instances.
    /// </summary>
    public static class ChannelFactoryCache<T>
    {
        // Thread-safe dictionary to store ChannelFactory instances
        private static readonly ConcurrentDictionary<string, ChannelFactory<T>> _cache = new ConcurrentDictionary<string, ChannelFactory<T>>();

        /// <summary>
        /// Retrieves a ChannelFactory instance from cache or creates a new one if not found.
        /// </summary>
        /// <param name="endpointConfigurationName">Name of the endpoint configuration defined in the config file.</param>
        /// <returns>Cached or newly created ChannelFactory instance.</returns>
        public static ChannelFactory<T> GetChannelFactory(string endpointConfigurationName)
        {
            return _cache.GetOrAdd(endpointConfigurationName, key =>
            {
                try
                {
                    // Create a new ChannelFactory for the given endpoint configuration name
                    return new ChannelFactory<T>(key);
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error creating ChannelFactory: {ex.Message}");
                    throw;
                }
            });
        }

        /// <summary>
        /// Clears the ChannelFactory cache. Can be used to reset cached factories.
        /// </summary>
        public static void ClearCache()
        {
            foreach (var factory in _cache.Values)
            {
                try
                {
                    // Attempt to close the factory gracefully
                    factory.Close();
                }
                catch
                {
                    // Abort the factory on error
                    factory.Abort();
                }
            }

            _cache.Clear();
        }
    }

    /// <summary>
    /// Example client code demonstrating how to use ChannelFactory caching.
    /// </summary>
    public class Program
    {
        static void Main(string[] args)
        {
            // Replace "MyServiceEndpoint" with the name of your endpoint configuration from the app.config/web.config file
            string endpointConfigurationName = "MyServiceEndpoint";

            try
            {
                // Retrieve a cached ChannelFactory instance
                var channelFactory = ChannelFactoryCache<IMyService>.GetChannelFactory(endpointConfigurationName);

                // Create a service client proxy
                IMyService client = channelFactory.CreateChannel();
                
                // Example call to the service
                string result = client.MyServiceMethod("Hello World");
                Console.WriteLine($"Service response: {result}");

                // Close the client proxy gracefully
                ((IClientChannel)client).Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error during service call: {ex.Message}");
            }
        }
    }

    /// <summary>
    /// Service contract for the WCF service.
    /// Replace with your actual service contract.
    /// </summary>
    [ServiceContract]
    public interface IMyService
    {
        [OperationContract]
        string MyServiceMethod(string input);
    }
}
```
