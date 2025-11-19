"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.net
Prompt: "How to implement exception handling in a WCF RESTful service using C# and return error responses in JSON format?"
Generated: DETERMINISTIC_e9adccbcf7bcee33
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
using System.Net;

namespace WcfRestfulService
{
    [DataContract]
    public class ErrorResponse
    {
        [DataMember]
        public string ErrorMessage { get; set; }

        [DataMember]
        public string ErrorDetails { get; set; }

        [DataMember]
        public HttpStatusCode StatusCode { get; set; }
    }

    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        [WebInvoke(Method = "GET",
            ResponseFormat = WebMessageFormat.Json,
            BodyStyle = WebMessageBodyStyle.Wrapped,
            UriTemplate = "getdata/{value}")]
        string GetData(string value);
    }

    public class Service1 : IService1
    {
        public string GetData(string value)
        {
            try
            {
                if (string.IsNullOrEmpty(value))
                {
                    throw new ArgumentNullException(nameof(value), "Value cannot be null or empty");
                }

                if (value == "error")
                {
                    throw new InvalidOperationException("Simulated error condition");
                }

                return string.Format("You entered: {0}", value);
            }
            catch (ArgumentNullException ex)
            {
                throw new WebFaultException<ErrorResponse>(
                    new ErrorResponse
                    {
                        ErrorMessage = "Bad Request",
                        ErrorDetails = ex.Message,
                        StatusCode = HttpStatusCode.BadRequest
                    }, HttpStatusCode.BadRequest);
            }
            catch (InvalidOperationException ex)
            {
                throw new WebFaultException<ErrorResponse>(
                    new ErrorResponse
                    {
                        ErrorMessage = "Operation Failed",
                        ErrorDetails = ex.Message,
                        StatusCode = HttpStatusCode.InternalServerError
                    }, HttpStatusCode.InternalServerError);
            }
            catch (Exception ex)
            {
                throw new WebFaultException<ErrorResponse>(
                    new ErrorResponse
                    {
                        ErrorMessage = "Server Error",
                        ErrorDetails = ex.Message,
                        StatusCode = HttpStatusCode.InternalServerError
                    }, HttpStatusCode.InternalServerError);
            }
        }
    }

    public class GlobalErrorHandler : IErrorHandler
    {
        public bool HandleError(Exception error)
        {
            return true;
        }

        public void ProvideFault(Exception error, MessageVersion version, ref Message fault)
        {
            if (error is WebFaultException<ErrorResponse>)
            {
                return;
            }

            var errorResponse = new ErrorResponse
            {
                ErrorMessage = "Unexpected Error",
                ErrorDetails = error.Message,
                StatusCode = HttpStatusCode.InternalServerError
            };

            fault = Message.CreateMessage(
                version,
                WebFaultException.CreateMessageFault(errorResponse, new DataContractSerializer(typeof(ErrorResponse))),
                null);
        }
    }

    public class GlobalErrorBehavior : Attribute, IServiceBehavior
    {
        public void AddBindingParameters(ServiceDescription serviceDescription, ServiceHostBase serviceHostBase, Collection<ServiceEndpoint> endpoints, BindingParameterCollection bindingParameters)
        {
        }

        public void ApplyDispatchBehavior(ServiceDescription serviceDescription, ServiceHostBase serviceHostBase)
        {
            foreach (ChannelDispatcher channelDispatcher in serviceHostBase.ChannelDispatchers)
            {
                channelDispatcher.ErrorHandlers.Add(new GlobalErrorHandler());
            }
        }

        public void Validate(ServiceDescription serviceDescription, ServiceHostBase serviceHostBase)
        {
        }
    }
}
```
