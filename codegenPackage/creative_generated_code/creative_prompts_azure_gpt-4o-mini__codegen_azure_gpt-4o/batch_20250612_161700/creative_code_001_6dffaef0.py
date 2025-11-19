"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.net
Prompt: Write a C# code example for consuming a WCF REST service using jQuery, as described in the WCF tutorial.
Generated: DETERMINISTIC_6dffaef0aa9d981d
Batch ID: 20250612_161700
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8080/MyService/hello/${name}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8080/MyService": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```csharp
// C# - WCF REST Service Implementation
using System;
using System.ServiceModel;
using System.ServiceModel.Web;

// Define the Service Contract
[ServiceContract]
public interface IMyService
{
    [OperationContract]
    [WebInvoke(Method = "GET",
               ResponseFormat = WebMessageFormat.Json,
               UriTemplate = "/hello/{name}")]
    string SayHello(string name);
}

// Implement the Service Contract
public class MyService : IMyService
{
    public string SayHello(string name)
    {
        // Return a greeting message
        return $"Hello, {name}!";
    }
}

// Service Host Configuration
class Program
{
    static void Main(string[] args)
    {
        // Create the base URI for hosting the service
        string baseAddress = "http://localhost:8080/MyService";
        
        // Create a WebServiceHost instance
        using (WebServiceHost host = new WebServiceHost(typeof(MyService), new Uri(baseAddress)))
        {
            // Open the service host
            host.Open();
            Console.WriteLine($"Service is running at {baseAddress}. Press ENTER to stop.");
            Console.ReadLine();
        }
    }
}
```

```html
<!-- HTML - Example Page Using jQuery to Consume the WCF REST Service -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WCF REST Service Consumer</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Consume WCF REST Service</h1>
    <label for="name">Enter your name:</label>
    <input type="text" id="name" placeholder="Your name">
    <button id="submit">Say Hello</button>
    <div id="result"></div>

    <script>
        $(document).ready(function() {
            // Event listener for the button click
            $('#submit').on('click', function() {
                // Get the name entered in the input field
                const name = $('#name').val();
                
                // Send an AJAX GET request to the WCF REST service
                $.ajax({
                    url: `http://localhost:8080/MyService/hello/${name}`,
                    type: 'GET',
                    dataType: 'json',
                    success: function(response) {
                        // Display the response from the service
                        $('#result').text(response);
                    },
                    error: function(xhr, status, error) {
                        // Handle any errors
                        console.error(`Error: ${error}`);
                        $('#result').text(`An error occurred: ${error}`);
                    }
                });
            });
        });
    </script>
</body>
</html>
```
