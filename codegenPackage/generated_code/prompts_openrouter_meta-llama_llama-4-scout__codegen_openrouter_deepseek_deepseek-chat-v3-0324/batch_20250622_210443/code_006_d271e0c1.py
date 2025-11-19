"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.net
Prompt: "Write a WCF service contract that uses data contracts and message contracts for serialization and deserialization."
Generated: DETERMINISTIC_d271e0c15ed00cf7
Batch ID: 20250622_210443
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
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

namespace WcfServiceContractExample
{
    // Service Contract
    [ServiceContract]
    public interface IExampleService
    {
        [OperationContract]
        ResponseMessage ProcessRequest(RequestMessage request);
    }

    // Data Contract for complex data
    [DataContract]
    public class Customer
    {
        [DataMember]
        public int CustomerId { get; set; }

        [DataMember]
        public string Name { get; set; }

        [DataMember]
        public string Email { get; set; }
    }

    // Data Contract for complex data
    [DataContract]
    public class Order
    {
        [DataMember]
        public int OrderId { get; set; }

        [DataMember]
        public DateTime OrderDate { get; set; }

        [DataMember]
        public decimal TotalAmount { get; set; }

        [DataMember]
        public List<string> Items { get; set; }
    }

    // Message Contract for request
    [MessageContract]
    public class RequestMessage
    {
        [MessageHeader]
        public string AuthenticationToken { get; set; }

        [MessageBodyMember]
        public Customer Customer { get; set; }

        [MessageBodyMember]
        public Order Order { get; set; }
    }

    // Message Contract for response
    [MessageContract]
    public class ResponseMessage
    {
        [MessageHeader]
        public string StatusCode { get; set; }

        [MessageHeader]
        public string StatusMessage { get; set; }

        [MessageBodyMember]
        public Order ProcessedOrder { get; set; }

        [MessageBodyMember]
        public DateTime ProcessedDate { get; set; }
    }

    // Service implementation
    public class ExampleService : IExampleService
    {
        public ResponseMessage ProcessRequest(RequestMessage request)
        {
            try
            {
                // Validate authentication token
                if (string.IsNullOrEmpty(request.AuthenticationToken))
                {
                    throw new FaultException("Authentication token is required");
                }

                // Process the request
                var response = new ResponseMessage
                {
                    StatusCode = "200",
                    StatusMessage = "Success",
                    ProcessedOrder = request.Order,
                    ProcessedDate = DateTime.UtcNow
                };

                // Add processing logic here
                response.ProcessedOrder.TotalAmount *= 0.9m; // Apply 10% discount

                return response;
            }
            catch (FaultException)
            {
                throw;
            }
            catch (Exception ex)
            {
                throw new FaultException($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
