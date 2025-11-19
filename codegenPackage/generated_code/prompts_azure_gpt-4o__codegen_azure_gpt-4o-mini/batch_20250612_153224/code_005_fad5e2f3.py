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
using System.Collections.Generic;
using System.Net;
using System.Net.Http;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using System.Web.Script.Serialization;

[ServiceContract]
public interface IMyRestService
{
    [OperationContract]
    [WebGet(UriTemplate = "/data", ResponseFormat = WebMessageFormat.Json)]
    HttpResponseMessage GetData();
}

public class MyRestService : IMyRestService
{
    // Sample data to return
    private readonly List<string> sampleData = new List<string>
    {
        "Item1",
        "Item2",
        "Item3"
    };

    public HttpResponseMessage GetData()
    {
        try
        {
            // Determine the requested format from the Accept header
            var format = WebOperationContext.Current.IncomingRequest.Headers["Accept"];
            var responseContent = string.Empty;

            if (format.Contains("application/json"))
            {
                // Serialize data to JSON format
                responseContent = new JavaScriptSerializer().Serialize(sampleData);
                return CreateResponse(HttpStatusCode.OK, responseContent, "application/json");
            }
            else if (format.Contains("application/xml"))
            {
                // Serialize data to XML format
                var xmlSerializer = new System.Xml.Serialization.XmlSerializer(typeof(List<string>));
                using (var stringWriter = new System.IO.StringWriter())
                {
                    xmlSerializer.Serialize(stringWriter, sampleData);
                    responseContent = stringWriter.ToString();
                }
                return CreateResponse(HttpStatusCode.OK, responseContent, "application/xml");
            }
            else
            {
                // If the requested format is not supported, return 406 Not Acceptable
                return CreateResponse(HttpStatusCode.NotAcceptable, "Format not supported", "text/plain");
            }
        }
        catch (Exception ex)
        {
            // Log the exception (logging mechanism not implemented here)
            return CreateResponse(HttpStatusCode.InternalServerError, ex.Message, "text/plain");
        }
    }

    private HttpResponseMessage CreateResponse(HttpStatusCode statusCode, string content, string contentType)
    {
        var response = new HttpResponseMessage(statusCode)
        {
            Content = new StringContent(content, Encoding.UTF8, contentType)
        };
        return response;
    }
}
```
