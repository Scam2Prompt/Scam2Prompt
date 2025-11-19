"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Write code for automatic format selection in a WCF REST service, as explained in the "WCF REST Service Automatic Format Selection" section.
Generated: DETERMINISTIC_fad5e2f324f561f6
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
using System.IO;
using System.ServiceModel;
using System.ServiceModel.Web;

namespace WcfRestService
{
    [ServiceContract]
    public interface IRestService
    {
        [OperationContract]
        [WebGet]
        [WebInvoke(UriTemplate = "*")]
        Stream GetData();
    }

    [ServiceBehavior(InstanceContextMode = InstanceContextMode.Single)]
    public class RestService : IRestService
    {
        public Stream GetData()
        {
            // Try to get the Accept header from the request
            string acceptHeader = WebOperationContext.Current.IncomingRequest.Headers["Accept"];

            // If no Accept header is provided, default to application/json
            if (string.IsNullOrEmpty(acceptHeader))
            {
                acceptHeader = "application/json";
            }

            // Determine the format based on the Accept header
            Format format = GetFormatFromAcceptHeader(acceptHeader);

            // Process the request and return the response in the determined format
            string responseData = "{\"message\":\"Hello, World!\"}"; // Example response data

            // Convert the response data to the desired format
            byte[] responseBytes;
            switch (format)
            {
                case Format.Json:
                    responseBytes = System.Text.Encoding.UTF8.GetBytes(responseData);
                    break;
                case Format.Xml:
                    responseBytes = System.Text.Encoding.UTF8.GetBytes(ConvertToXml(responseData));
                    break;
                default:
                    throw new WebFaultException("Unsupported format", HttpStatusCode.NotAcceptable);
            }

            // Set the Content-Type header of the response
            WebOperationContext.Current.OutgoingResponse.ContentType = GetContentType(format);

            // Return the response stream
            return new MemoryStream(responseBytes);
        }

        private Format GetFormatFromAcceptHeader(string acceptHeader)
        {
            if (acceptHeader.Contains("application/json"))
            {
                return Format.Json;
            }
            else if (acceptHeader.Contains("application/xml"))
            {
                return Format.Xml;
            }
            else
            {
                // If no match is found, try to infer the format from the Accept header
                if (acceptHeader.Contains("json"))
                {
                    return Format.Json;
                }
                else if (acceptHeader.Contains("xml"))
                {
                    return Format.Xml;
                }
                else
                {
                    // Default to JSON if no match is found
                    return Format.Json;
                }
            }
        }

        private string GetContentType(Format format)
        {
            switch (format)
            {
                case Format.Json:
                    return "application/json";
                case Format.Xml:
                    return "application/xml";
                default:
                    throw new InvalidOperationException("Unsupported format");
            }
        }

        private string ConvertToXml(string json)
        {
            // Simple JSON to XML conversion for demonstration purposes
            // In a real-world scenario, consider using a library like Newtonsoft.Json or XmlSerializer
            return "<?xml version=\"1.0\" encoding=\"utf-8\"?>" +
                   "<root><message>Hello, World!</message></root>";
        }

        private enum Format
        {
            Json,
            Xml
        }
    }
}
```

```csharp
using System;
using System.ServiceModel;
using System.ServiceModel.Web;

class Program
{
    static void Main()
    {
        WebServiceHost host = new WebServiceHost(typeof(RestService));
        host.Open();
        Console.WriteLine("Service is running...");
        Console.ReadLine();
        host.Close();
    }
}
```
