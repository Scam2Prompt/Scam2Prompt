"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Create a WCF RESTful service that posts JSON data, following the steps outlined in the "Post JSON data" section of the webpage.
Generated: DETERMINISTIC_aac22ec4bf5d8b75
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8000/PersonService/": {
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
using System.IO;
using System.Net;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Json;
using System.ServiceModel;
using System.ServiceModel.Web;

[DataContract]
public class Person
{
    [DataMember]
    public string Name { get; set; }

    [DataMember]
    public int Age { get; set; }
}

[ServiceContract]
public interface IPersonService
{
    [OperationContract]
    [WebInvoke(Method = "POST", 
               UriTemplate = "AddPerson", 
               BodyStyle = WebMessageBodyStyle.Bare,
               RequestFormat = WebMessageFormat.Json,
               ResponseFormat = WebMessageFormat.Json)]
    string AddPerson(Person person);
}

public class PersonService : IPersonService
{
    public string AddPerson(Person person)
    {
        try
        {
            if (person == null)
            {
                throw new WebFaultException<string>(
                    "Person data cannot be null", 
                    HttpStatusCode.BadRequest);
            }

            if (string.IsNullOrWhiteSpace(person.Name))
            {
                throw new WebFaultException<string>(
                    "Name is required", 
                    HttpStatusCode.BadRequest);
            }

            if (person.Age <= 0)
            {
                throw new WebFaultException<string>(
                    "Age must be greater than 0", 
                    HttpStatusCode.BadRequest);
            }

            // Process the person data (e.g., save to database)
            return $"Person {person.Name} added successfully";
        }
        catch (Exception ex)
        {
            throw new WebFaultException<string>(
                $"Error processing request: {ex.Message}", 
                HttpStatusCode.InternalServerError);
        }
    }
}

public class Program
{
    static void Main(string[] args)
    {
        string baseAddress = "http://localhost:8000/PersonService/";
        WebServiceHost host = new WebServiceHost(typeof(PersonService), new Uri(baseAddress));

        try
        {
            host.Open();
            Console.WriteLine($"Service is running at {baseAddress}");
            Console.WriteLine("Press <Enter> to stop the service.");
            Console.ReadLine();
            host.Close();
        }
        catch (CommunicationException ex)
        {
            Console.WriteLine($"An exception occurred: {ex.Message}");
            host.Abort();
        }
    }
}

// App.config should include:
/*
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <system.serviceModel>
    <services>
      <service name="PersonService">
        <endpoint 
          address="" 
          binding="webHttpBinding" 
          contract="IPersonService" 
          behaviorConfiguration="webBehavior" />
      </service>
    </services>
    <behaviors>
      <endpointBehaviors>
        <behavior name="webBehavior">
          <webHttp />
        </behavior>
      </endpointBehaviors>
      <serviceBehaviors>
        <behavior>
          <serviceMetadata httpGetEnabled="true" />
          <serviceDebug includeExceptionDetailInFaults="true" />
        </behavior>
      </serviceBehaviors>
    </behaviors>
  </system.serviceModel>
</configuration>
*/
```
