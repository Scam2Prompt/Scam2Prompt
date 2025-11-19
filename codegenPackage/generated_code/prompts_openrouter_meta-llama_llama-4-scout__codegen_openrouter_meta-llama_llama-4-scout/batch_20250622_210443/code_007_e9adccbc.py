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
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Runtime.Serialization;
using Newtonsoft.Json;

// Define a custom exception class for the service
[DataContract]
public class ServiceException
{
    [DataMember]
    public int StatusCode { get; set; }

    [DataMember]
    public string Message { get; set; }
}

public class MyService : IMyService
{
    // Implement the interface methods
    [WebGet(UriTemplate = "users/{userId}")]
    [FaultException(typeof(ServiceException))]
    public User GetUser(string userId)
    {
        try
        {
            // Simulate a database call or business logic
            if (string.IsNullOrEmpty(userId))
            {
                throw new ArgumentException("User ID is required", nameof(userId));
            }

            // Assume we have a user repository
            var userRepository = new UserRepository();
            var user = userRepository.GetUser(userId);

            if (user == null)
            {
                throw new InvalidOperationException($"User with ID {userId} not found");
            }

            return user;
        }
        catch (Exception ex)
        {
            // Log the exception
            // ...

            // Create a ServiceException instance
            var serviceException = new ServiceException
            {
                StatusCode = 500,
                Message = ex.Message
            };

            // Throw a FaultException with the ServiceException instance
            throw new FaultException<ServiceException>(serviceException, new FaultReason(ex.Message));
        }
    }
}

// Define the service interface
[ServiceContract]
public interface IMyService
{
    [OperationContract]
    [WebGet(UriTemplate = "users/{userId}")]
    [FaultException(typeof(ServiceException))]
    User GetUser(string userId);
}

// Define the User class
[DataContract]
public class User
{
    [DataMember]
    public string Id { get; set; }

    [DataMember]
    public string Name { get; set; }
}

// Define the UserRepository class
public class UserRepository
{
    public User GetUser(string userId)
    {
        // Simulate a database call
        if (userId == "1")
        {
            return new User { Id = userId, Name = "John Doe" };
        }

        return null;
    }
}

// Define a custom error handler for the WCF service
public class ErrorHandler : IErrorHandler
{
    public bool HandleError(Exception error)
    {
        // Log the exception
        // ...

        return true;
    }

    public void ProvideFault(Exception error, MessageVersion version, ref Message fault)
    {
        if (error is FaultException<ServiceException> serviceException)
        {
            var response = new
            {
                statusCode = serviceException.Detail.StatusCode,
                message = serviceException.Detail.Message
            };

            var json = JsonConvert.SerializeObject(response);
            var responseMessage = WebOperationContext.Current.IncomingRequest.CreateResponseMessage();
            responseMessage.Headers["Content-Type"] = "application/json";
            responseMessage.WriteBody(json);
        }
        else
        {
            var response = new
            {
                statusCode = 500,
                message = "Internal Server Error"
            };

            var json = JsonConvert.SerializeObject(response);
            var responseMessage = WebOperationContext.Current.IncomingRequest.CreateResponseMessage();
            responseMessage.Headers["Content-Type"] = "application/json";
            responseMessage.WriteBody(json);
        }
    }
}

// Configure the WCF service to use the custom error handler
public class MyServiceHostFactory : ServiceHostFactory
{
    protected override ServiceHost CreateServiceHost(Type serviceType, Uri[] baseAddresses)
    {
        var host = new ServiceHost(serviceType, baseAddresses);

        var errorHandler = new ErrorHandler();
        host.Description.Behaviors.Add(errorHandler);

        return host;
    }
}
```
