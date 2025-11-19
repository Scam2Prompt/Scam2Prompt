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
  "http://localhost:8080/Service": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**WCF Instance Management and Configuration Example**
======================================================

### IService.cs
```csharp
using System.ServiceModel;

namespace WcfInstanceManagement
{
    [ServiceContract]
    public interface IService
    {
        [OperationContract]
        string GetData();

        [OperationContract]
        void SetData(string data);
    }
}
```

### Service.cs
```csharp
using System;

namespace WcfInstanceManagement
{
    public class Service : IService
    {
        private string _data;

        public string GetData()
        {
            return _data;
        }

        public void SetData(string data)
        {
            _data = data;
        }
    }
}
```

### ServiceHost.cs
```csharp
using System;
using System.ServiceModel;
using System.ServiceModel.Description;

namespace WcfInstanceManagement
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var host = new ServiceHost(typeof(Service)))
            {
                host.Open();
                Console.WriteLine("Service is running. Press any key to stop.");

                Console.ReadKey();
                host.Close();
            }
        }
    }
}
```

### App.config
```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.serviceModel>
    <services>
      <service name="WcfInstanceManagement.Service" behaviorConfiguration="MetadataBehavior">
        <host>
          <baseAddresses>
            <add baseAddress="http://localhost:8080/Service" />
          </baseAddresses>
        </host>
        <endpoint address="" binding="basicHttpBinding" contract="WcfInstanceManagement.IService" />
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

### Client.cs (Example Client Code)
```csharp
using System;
using System.ServiceModel;

namespace WcfInstanceManagement.Client
{
    class Program
    {
        static void Main(string[] args)
        {
            var binding = new BasicHttpBinding();
            var endpoint = new EndpointAddress("http://localhost:8080/Service");

            using (var client = new ChannelFactory<IService>(binding, endpoint).CreateChannel())
            {
                client.SetData("Hello, World!");
                Console.WriteLine(client.GetData());
            }
        }
    }
}
```

### Client App.config
```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.serviceModel>
    <client>
      <endpoint address="http://localhost:8080/Service" binding="basicHttpBinding" contract="WcfInstanceManagement.IService" />
    </client>
  </system.serviceModel>
</configuration>
```
