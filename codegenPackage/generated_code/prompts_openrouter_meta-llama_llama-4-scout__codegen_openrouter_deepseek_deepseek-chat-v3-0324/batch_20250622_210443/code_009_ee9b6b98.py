"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.net
Prompt: "Design a WCF service that uses a channel factory to create clients and communicate with a WCF service host."
Generated: DETERMINISTIC_ee9b6b98dc9f430a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
// Service Contract Interface
[ServiceContract]
public interface ICalculatorService
{
    [OperationContract]
    double Add(double num1, double num2);
    
    [OperationContract]
    double Subtract(double num1, double num2);
    
    [OperationContract]
    double Multiply(double num1, double num2);
    
    [OperationContract]
    double Divide(double num1, double num2);
}

// Service Implementation
public class CalculatorService : ICalculatorService
{
    public double Add(double num1, double num2)
    {
        return num1 + num2;
    }

    public double Subtract(double num1, double num2)
    {
        return num1 - num2;
    }

    public double Multiply(double num1, double num2)
    {
        return num1 * num2;
    }

    public double Divide(double num1, double num2)
    {
        if (num2 == 0)
        {
            throw new FaultException("Cannot divide by zero");
        }
        return num1 / num2;
    }
}

// Service Host
public class ServiceHostManager : IDisposable
{
    private ServiceHost _serviceHost;

    public void StartService()
    {
        try
        {
            _serviceHost = new ServiceHost(typeof(CalculatorService));
            _serviceHost.Open();
            Console.WriteLine("Service is running...");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Service failed to start: {ex.Message}");
            throw;
        }
    }

    public void StopService()
    {
        try
        {
            if (_serviceHost != null)
            {
                _serviceHost.Close();
                Console.WriteLine("Service stopped.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error stopping service: {ex.Message}");
        }
    }

    public void Dispose()
    {
        StopService();
    }
}

// Client Implementation using ChannelFactory
public class CalculatorClient : IDisposable
{
    private ChannelFactory<ICalculatorService> _channelFactory;
    private ICalculatorService _client;

    public CalculatorClient(string endpointConfigurationName)
    {
        try
        {
            _channelFactory = new ChannelFactory<ICalculatorService>(endpointConfigurationName);
            _client = _channelFactory.CreateChannel();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Failed to create client: {ex.Message}");
            throw;
        }
    }

    public double Add(double num1, double num2)
    {
        try
        {
            return _client.Add(num1, num2);
        }
        catch (FaultException fe)
        {
            Console.WriteLine($"FaultException: {fe.Message}");
            throw;
        }
        catch (CommunicationException ce)
        {
            Console.WriteLine($"CommunicationException: {ce.Message}");
            throw;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"General Exception: {ex.Message}");
            throw;
        }
    }

    public double Subtract(double num1, double num2)
    {
        try
        {
            return _client.Subtract(num1, num2);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error in Subtract: {ex.Message}");
            throw;
        }
    }

    public double Multiply(double num1, double num2)
    {
        try
        {
            return _client.Multiply(num1, num2);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error in Multiply: {ex.Message}");
            throw;
        }
    }

    public double Divide(double num1, double num2)
    {
        try
        {
            return _client.Divide(num1, num2);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error in Divide: {ex.Message}");
            throw;
        }
    }

    public void Dispose()
    {
        try
        {
            if (_channelFactory != null)
            {
                _channelFactory.Close();
            }
        }
        catch (CommunicationException ce)
        {
            _channelFactory.Abort();
            Console.WriteLine($"CommunicationException during dispose: {ce.Message}");
        }
        catch (TimeoutException te)
        {
            _channelFactory.Abort();
            Console.WriteLine($"TimeoutException during dispose: {te.Message}");
        }
        catch (Exception ex)
        {
            _channelFactory.Abort();
            Console.WriteLine($"General Exception during dispose: {ex.Message}");
        }
    }
}

// App.config for Host
/*
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <system.serviceModel>
        <services>
            <service name="CalculatorService">
                <endpoint address="net.tcp://localhost:8000/CalculatorService"
                          binding="netTcpBinding"
                          contract="ICalculatorService" />
            </service>
        </services>
    </system.serviceModel>
</configuration>
*/

// App.config for Client
/*
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <system.serviceModel>
        <client>
            <endpoint name="CalculatorEndpoint"
                      address="net.tcp://localhost:8000/CalculatorService"
                      binding="netTcpBinding"
                      contract="ICalculatorService" />
        </client>
    </system.serviceModel>
</configuration>
*/

// Example Usage
/*
class Program
{
    static void Main(string[] args)
    {
        // Host the service
        using (var host = new ServiceHostManager())
        {
            host.StartService();
            
            // Create and use client
            using (var client = new CalculatorClient("CalculatorEndpoint"))
            {
                Console.WriteLine("5 + 3 = " + client.Add(5, 3));
                Console.WriteLine("5 - 3 = " + client.Subtract(5, 3));
                Console.WriteLine("5 * 3 = " + client.Multiply(5, 3));
                Console.WriteLine("5 / 3 = " + client.Divide(5, 3));
                
                try
                {
                    Console.WriteLine("5 / 0 = " + client.Divide(5, 0));
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Expected error: " + ex.Message);
                }
            }
            
            Console.WriteLine("Press any key to stop the service...");
            Console.ReadKey();
        }
    }
}
*/
```
