"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Provide code examples for simplified configuration and validation in WCF 4.5, as described in the "Simplified Config | Config Validation" section.
Generated: DETERMINISTIC_2b8ca53b22e16667
Batch ID: 20250612_153224
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

# Generated Code:
# ===============

**WCF 4.5 Simplified Configuration and Validation Example**

### Service Contract

```csharp
using System.ServiceModel;

[ServiceContract]
public interface IMyService
{
    [OperationContract]
    string GetData(int value);
}
```

### Service Implementation

```csharp
using System;

public class MyService : IMyService
{
    public string GetData(int value)
    {
        return string.Format("You entered: {0}", value);
    }
}
```

### Simplified Configuration

```csharp
using System.ServiceModel;

[ServiceBehavior(InstanceContextMode = InstanceContextMode.PerCall, 
                 ConcurrencyMode = ConcurrencyMode.Multiple)]
public class MyServiceHost : MyService, IMyService
{
}
```

### Host Configuration

```csharp
using System;
using System.ServiceModel;
using System.ServiceModel.Description;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Create a new service host
            using (var host = new ServiceHost(typeof(MyService)))
            {
                // Open the host
                host.Open();

                Console.WriteLine("Service is running. Press any key to stop.");

                // Wait for a key press
                Console.ReadKey();

                // Close the host
                host.Close();
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: {0}", ex.Message);
        }
    }
}
```

### Client Configuration

```csharp
using System;
using System.ServiceModel;

class Client
{
    static void Main(string[] args)
    {
        try
        {
            // Create a new channel factory
            var factory = new ChannelFactory<IMyService>(new NetTcpBinding(), 
                new EndpointAddress("net.tcp://localhost:8080/MyService"));

            // Create a new channel
            using (var channel = factory.CreateChannel())
            {
                // Call the service
                var result = channel.GetData(10);

                Console.WriteLine("Result: {0}", result);
            }

            // Close the factory
            factory.Close();
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: {0}", ex.Message);
        }
    }
}
```

### Web.config (for IIS Hosting)

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.serviceModel>
    <services>
      <service name="MyService" behaviorConfiguration="MetadataBehavior">
        <host>
          <baseAddresses>
            <add baseAddress="http://localhost:8080/MyService" />
          </baseAddresses>
        </host>
        <endpoint address="" binding="basicHttpBinding" contract="IMyService" />
        <endpoint address="mex" binding="mexHttpBinding" contract="IMetadataExchange" />
      </service>
    </services>
    <behaviors>
      <serviceBehaviors>
        <behavior name="MetadataBehavior">
          <serviceMetadata httpGetEnabled="true" httpsGetEnabled="false" />
          <serviceDebug includeExceptionDetailInFaults="false" />
        </behavior>
      </serviceBehaviors>
    </behaviors>
  </system.serviceModel>
</configuration>
```
