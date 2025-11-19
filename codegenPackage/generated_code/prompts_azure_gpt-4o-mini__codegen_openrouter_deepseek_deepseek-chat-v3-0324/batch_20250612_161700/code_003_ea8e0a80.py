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
  "http://localhost:8000/CalculatorService/": {
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
// Service Contract
[ServiceContract]
public interface ICalculatorService
{
    [OperationContract]
    double Add(double n1, double n2);
    
    [OperationContract]
    double Subtract(double n1, double n2);
    
    [OperationContract]
    double Multiply(double n1, double n2);
    
    [OperationContract]
    double Divide(double n1, double n2);
}

// Service Implementation with different instance modes
[ServiceBehavior(InstanceContextMode = InstanceContextMode.PerCall)] // Can be PerSession or Single
public class CalculatorService : ICalculatorService
{
    private int _instanceCount = 0;

    public CalculatorService()
    {
        _instanceCount++;
        Console.WriteLine($"New service instance created. Total instances: {_instanceCount}");
    }

    public double Add(double n1, double n2)
    {
        return n1 + n2;
    }

    public double Subtract(double n1, double n2)
    {
        return n1 - n2;
    }

    public double Multiply(double n1, double n2)
    {
        return n1 * n2;
    }

    public double Divide(double n1, double n2)
    {
        if (n2 == 0)
        {
            throw new FaultException("Cannot divide by zero");
        }
        return n1 / n2;
    }
}

// Host Configuration
class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Create a URI to serve as the base address
            Uri baseAddress = new Uri("http://localhost:8000/CalculatorService/");

            // Create the ServiceHost
            using (ServiceHost host = new ServiceHost(typeof(CalculatorService), baseAddress))
            {
                // Enable metadata publishing
                ServiceMetadataBehavior smb = new ServiceMetadataBehavior();
                smb.HttpGetEnabled = true;
                smb.MetadataExporter.PolicyVersion = PolicyVersion.Policy15;
                host.Description.Behaviors.Add(smb);

                // Add service endpoint
                host.AddServiceEndpoint(typeof(ICalculatorService), new WSHttpBinding(), "");

                // Open the ServiceHost to start listening for messages
                host.Open();

                Console.WriteLine("The service is ready at {0}", baseAddress);
                Console.WriteLine("Press <Enter> to stop the service...");
                Console.ReadLine();

                // Close the ServiceHost
                host.Close();
            }
        }
        catch (CommunicationException ce)
        {
            Console.WriteLine("An exception occurred: {0}", ce.Message);
            Console.ReadLine();
        }
        catch (Exception ex)
        {
            Console.WriteLine("An unexpected exception occurred: {0}", ex.Message);
            Console.ReadLine();
        }
    }
}

// Client Configuration
class Client
{
    static void Main()
    {
        try
        {
            // Create a client
            CalculatorServiceClient client = new CalculatorServiceClient();

            // Call the Add service operation
            double value1 = 100.00D;
            double value2 = 15.99D;
            double result = client.Add(value1, value2);
            Console.WriteLine("Add({0},{1}) = {2}", value1, value2, result);

            // Call the Subtract service operation
            result = client.Subtract(value1, value2);
            Console.WriteLine("Subtract({0},{1}) = {2}", value1, value2, result);

            // Call the Multiply service operation
            result = client.Multiply(value1, value2);
            Console.WriteLine("Multiply({0},{1}) = {2}", value1, value2, result);

            // Call the Divide service operation
            result = client.Divide(value1, value2);
            Console.WriteLine("Divide({0},{1}) = {2}", value1, value2, result);

            // Close the client
            client.Close();
        }
        catch (FaultException fe)
        {
            Console.WriteLine("Service fault: {0}", fe.Message);
        }
        catch (CommunicationException ce)
        {
            Console.WriteLine("Communication exception: {0}", ce.Message);
        }
        catch (TimeoutException te)
        {
            Console.WriteLine("Timeout exception: {0}", te.Message);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Unexpected exception: {0}", ex.Message);
        }

        Console.WriteLine("Press <Enter> to exit...");
        Console.ReadLine();
    }
}

// App.config for Host
/*
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <system.serviceModel>
        <services>
            <service name="CalculatorService" behaviorConfiguration="CalculatorServiceBehavior">
                <host>
                    <baseAddresses>
                        <add baseAddress="http://localhost:8000/CalculatorService/"/>
                    </baseAddresses>
                </host>
                <endpoint address="" binding="wsHttpBinding" contract="ICalculatorService"/>
                <endpoint address="mex" binding="mexHttpBinding" contract="IMetadataExchange"/>
            </service>
        </services>
        <behaviors>
            <serviceBehaviors>
                <behavior name="CalculatorServiceBehavior">
                    <serviceMetadata httpGetEnabled="True"/>
                    <serviceDebug includeExceptionDetailInFaults="False"/>
                </behavior>
            </serviceBehaviors>
        </behaviors>
    </system.serviceModel>
</configuration>
*/

// App.config for Client
/*
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <system.serviceModel>
        <client>
            <endpoint address="http://localhost:8000/CalculatorService/"
                binding="wsHttpBinding" contract="ICalculatorService"
                name="WSHttpBinding_ICalculatorService">
            </endpoint>
        </client>
    </system.serviceModel>
</configuration>
*/
```
