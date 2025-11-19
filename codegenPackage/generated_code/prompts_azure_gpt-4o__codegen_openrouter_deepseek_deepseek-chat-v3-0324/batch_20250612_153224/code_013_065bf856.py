"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Generate a WCF service using ChannelFactory Cache, based on the examples provided in the "ChannelFactory Cache" section.
Generated: DETERMINISTIC_065bf856bcf74d9f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Concurrent;
using System.ServiceModel;
using System.ServiceModel.Channels;

namespace WcfChannelFactoryCache
{
    /// <summary>
    /// Provides a thread-safe cache for ChannelFactory instances.
    /// </summary>
    public static class ChannelFactoryCache
    {
        private static readonly ConcurrentDictionary<string, ChannelFactory> _cache = 
            new ConcurrentDictionary<string, ChannelFactory>();

        /// <summary>
        /// Gets or creates a ChannelFactory instance for the specified endpoint configuration.
        /// </summary>
        /// <typeparam name="TChannel">The service contract type.</typeparam>
        /// <param name="endpointConfigurationName">The endpoint configuration name.</param>
        /// <returns>A ChannelFactory instance.</returns>
        public static ChannelFactory<TChannel> GetFactory<TChannel>(string endpointConfigurationName)
        {
            if (string.IsNullOrWhiteSpace(endpointConfigurationName))
            {
                throw new ArgumentException("Endpoint configuration name cannot be null or empty.", nameof(endpointConfigurationName));
            }

            string cacheKey = $"{typeof(TChannel).FullName}_{endpointConfigurationName}";

            return (ChannelFactory<TChannel>)_cache.GetOrAdd(cacheKey, key =>
            {
                try
                {
                    var factory = new ChannelFactory<TChannel>(endpointConfigurationName);
                    // Ensure the factory is in a valid state before caching
                    if (factory.State != CommunicationState.Opened)
                    {
                        factory.Open();
                    }
                    return factory;
                }
                catch (Exception ex)
                {
                    throw new InvalidOperationException($"Failed to create ChannelFactory for {typeof(TChannel).Name}", ex);
                }
            });
        }

        /// <summary>
        /// Clears all cached ChannelFactory instances.
        /// </summary>
        public static void Clear()
        {
            foreach (var factory in _cache.Values)
            {
                try
                {
                    if (factory.State == CommunicationState.Opened)
                    {
                        factory.Close();
                    }
                    else
                    {
                        factory.Abort();
                    }
                }
                catch
                {
                    factory.Abort();
                }
            }
            _cache.Clear();
        }
    }

    /// <summary>
    /// Example service contract
    /// </summary>
    [ServiceContract]
    public interface IExampleService
    {
        [OperationContract]
        string GetData(int value);
    }

    /// <summary>
    /// Example client class demonstrating usage of the ChannelFactoryCache
    /// </summary>
    public class ExampleServiceClient : ClientBase<IExampleService>, IExampleService
    {
        public ExampleServiceClient(string endpointConfigurationName) 
            : base(endpointConfigurationName) { }

        public string GetData(int value)
        {
            return Channel.GetData(value);
        }

        /// <summary>
        /// Creates a channel using the cached factory
        /// </summary>
        public static IExampleService CreateChannel(string endpointConfigurationName)
        {
            var factory = ChannelFactoryCache.GetFactory<IExampleService>(endpointConfigurationName);
            return factory.CreateChannel();
        }
    }

    /// <summary>
    /// Example usage of the ChannelFactoryCache
    /// </summary>
    public class Program
    {
        public static void Main()
        {
            try
            {
                const string endpointName = "BasicHttpBinding_IExampleService";
                var client = ExampleServiceClient.CreateChannel(endpointName);

                try
                {
                    string result = client.GetData(42);
                    Console.WriteLine($"Service returned: {result}");

                    // Properly close the channel when done
                    ((IClientChannel)client).Close();
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error calling service: {ex.Message}");
                    ((IClientChannel)client).Abort();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error creating client: {ex.Message}");
            }
            finally
            {
                // Clear the cache when application exits
                ChannelFactoryCache.Clear();
            }
        }
    }
}
```
