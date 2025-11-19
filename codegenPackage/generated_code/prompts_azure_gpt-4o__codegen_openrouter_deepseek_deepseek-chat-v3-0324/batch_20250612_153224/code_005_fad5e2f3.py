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
using System.Linq;
using System.ServiceModel;
using System.ServiceModel.Activation;
using System.ServiceModel.Channels;
using System.ServiceModel.Description;
using System.ServiceModel.Web;
using System.Text;
using System.Net;

namespace WcfRestService
{
    /// <summary>
    /// Custom WebHttpBehavior that enables automatic format selection
    /// </summary>
    public class AutomaticFormatWebHttpBehavior : WebHttpBehavior
    {
        protected override IDispatchMessageFormatter GetRequestDispatchFormatter(OperationDescription operationDescription, ServiceEndpoint endpoint)
        {
            // Use the base formatter for non-GET operations
            if (operationDescription.Messages[0].Body.Parts.Count > 0)
                return base.GetRequestDispatchFormatter(operationDescription, endpoint);

            // Return a custom formatter for GET operations
            return new AutomaticFormatDispatchFormatter(operationDescription, this.GetQueryStringConverter(operationDescription));
        }

        protected override IDispatchMessageFormatter GetReplyDispatchFormatter(OperationDescription operationDescription, ServiceEndpoint endpoint)
        {
            // Return a custom formatter that handles automatic format selection
            return new AutomaticFormatDispatchFormatter(operationDescription, this.GetQueryStringConverter(operationDescription));
        }
    }

    /// <summary>
    /// Custom dispatch formatter that handles automatic format selection
    /// </summary>
    public class AutomaticFormatDispatchFormatter : IDispatchMessageFormatter
    {
        private readonly OperationDescription _operation;
        private readonly QueryStringConverter _queryStringConverter;

        public AutomaticFormatDispatchFormatter(OperationDescription operation, QueryStringConverter queryStringConverter)
        {
            _operation = operation;
            _queryStringConverter = queryStringConverter;
        }

        public void DeserializeRequest(Message message, object[] parameters)
        {
            if (parameters.Length == 0)
                return;

            if (WebOperationContext.Current.IncomingRequest.Method == "GET")
            {
                // Handle GET requests with query string parameters
                var queryParameters = WebOperationContext.Current.IncomingRequest.UriTemplateMatch.QueryParameters;
                var parameterInfos = _operation.Messages[0].Body.Parts;

                for (int i = 0; i < parameters.Length; i++)
                {
                    var parameterName = parameterInfos[i].Name;
                    if (queryParameters.AllKeys.Contains(parameterName))
                    {
                        parameters[i] = _queryStringConverter.ConvertStringToValue(
                            queryParameters[parameterName], 
                            parameterInfos[i].Type);
                    }
                }
            }
            else
            {
                // Handle other HTTP methods with message body
                var formatter = new WebBodyFormatMessageFormatter(_operation, this._queryStringConverter);
                formatter.DeserializeRequest(message, parameters);
            }
        }

        public Message SerializeReply(MessageVersion messageVersion, object[] parameters, object result)
        {
            // Get the format from the Accept header or default to JSON
            var format = GetResponseFormat();

            // Set the response format in the context
            WebOperationContext.Current.OutgoingResponse.Format = format;

            // Create appropriate formatter based on the format
            var formatter = new WebBodyFormatMessageFormatter(_operation, this._queryStringConverter);
            return formatter.SerializeReply(messageVersion, parameters, result);
        }

        private WebMessageFormat GetResponseFormat()
        {
            // Check Accept header for format preference
            var acceptHeader = WebOperationContext.Current.IncomingRequest.Headers["Accept"];

            if (!string.IsNullOrEmpty(acceptHeader))
            {
                if (acceptHeader.Contains("application/xml") || acceptHeader.Contains("text/xml"))
                {
                    return WebMessageFormat.Xml;
                }
                if (acceptHeader.Contains("application/json"))
                {
                    return WebMessageFormat.Json;
                }
            }

            // Check format query parameter if Accept header is not specified
            var formatParam = WebOperationContext.Current.IncomingRequest.UriTemplateMatch.QueryParameters["format"];
            if (!string.IsNullOrEmpty(formatParam))
            {
                if (formatParam.Equals("xml", StringComparison.OrdinalIgnoreCase))
                {
                    return WebMessageFormat.Xml;
                }
                if (formatParam.Equals("json", StringComparison.OrdinalIgnoreCase))
                {
                    return WebMessageFormat.Json;
                }
            }

            // Default to JSON if no format is specified
            return WebMessageFormat.Json;
        }
    }

    /// <summary>
    /// Service contract for the REST service
    /// </summary>
    [ServiceContract]
    public interface ISampleService
    {
        [OperationContract]
        [WebGet(UriTemplate = "/data/{id}")]
        SampleData GetData(string id);

        [OperationContract]
        [WebInvoke(Method = "POST", UriTemplate = "/data")]
        SampleData PostData(SampleData data);
    }

    /// <summary>
    /// Sample data structure
    /// </summary>
    public class SampleData
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public int Value { get; set; }
    }

    /// <summary>
    /// Service implementation
    /// </summary>
    [AspNetCompatibilityRequirements(RequirementsMode = AspNetCompatibilityRequirementsMode.Allowed)]
    [ServiceBehavior(InstanceContextMode = InstanceContextMode.PerCall)]
    public class SampleService : ISampleService
    {
        public SampleData GetData(string id)
        {
            // In a real service, you would fetch data from a database
            return new SampleData
            {
                Id = id,
                Name = "Sample Item",
                Value = 42
            };
        }

        public SampleData PostData(SampleData data)
        {
            // In a real service, you would save the data
            return data;
        }
    }

    /// <summary>
    /// Service host factory that applies the automatic format behavior
    /// </summary>
    public class AutomaticFormatWebServiceHostFactory : WebServiceHostFactory
    {
        protected override ServiceHost CreateServiceHost(Type serviceType, Uri[] baseAddresses)
        {
            var host = base.CreateServiceHost(serviceType, baseAddresses);

            foreach (var endpoint in host.Description.Endpoints)
            {
                if (endpoint.Binding is WebHttpBinding)
                {
                    endpoint.Behaviors.Add(new AutomaticFormatWebHttpBehavior());
                }
            }

            return host;
        }
    }
}
```
