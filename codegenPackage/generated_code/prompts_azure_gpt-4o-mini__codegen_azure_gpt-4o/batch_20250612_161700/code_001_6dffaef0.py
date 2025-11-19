"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.net
Prompt: Write a C# code example for consuming a WCF REST service using jQuery, as described in the WCF tutorial.
Generated: DETERMINISTIC_6dffaef0aa9d981d
Batch ID: 20250612_161700
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8080/MyService/GetData/${value}`,": {
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
  },
  "http://localhost:8080/MyService": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

### C# Code: WCF REST Service Implementation

```csharp
using System;
using System.ServiceModel;
using System.ServiceModel.Web;

// Define the service contract
[ServiceContract]
public interface IMyService
{
    [OperationContract]
    [WebGet(UriTemplate = "/GetData/{value}", ResponseFormat = WebMessageFormat.Json)]
    string GetData(string value);
}

// Implement the service
public class MyService : IMyService
{
    public string GetData(string value)
    {
        return $"You entered: {value}";
    }
}

// Host the service
class Program
{
    static void Main(string[] args)
    {
        // Define the base address for the service
        string baseAddress = "http://localhost:8080/MyService";

        // Create the service host
        using (WebServiceHost host = new WebServiceHost(typeof(MyService), new Uri(baseAddress)))
        {
            try
            {
                // Open the host
                host.Open();
                Console.WriteLine($"Service is running at {baseAddress}");
                Console.WriteLine("Press Enter to terminate the service...");
                Console.ReadLine();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```

### jQuery Code: Consuming the WCF REST Service

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consume WCF REST Service</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Consume WCF REST Service</h1>
    <input type="text" id="inputValue" placeholder="Enter a value">
    <button id="callService">Call Service</button>
    <p id="result"></p>

    <script>
        $(document).ready(function () {
            // Attach click event to the button
            $('#callService').click(function () {
                // Get the input value
                const value = $('#inputValue').val();

                // Validate input
                if (!value) {
                    alert('Please enter a value.');
                    return;
                }

                // Call the WCF REST service
                $.ajax({
                    url: `http://localhost:8080/MyService/GetData/${value}`,
                    type: 'GET',
                    dataType: 'json',
                    success: function (response) {
                        // Display the result
                        $('#result').text(response);
                    },
                    error: function (xhr, status, error) {
                        // Handle errors
                        console.error('Error:', error);
                        alert('An error occurred while calling the service.');
                    }
                });
            });
        });
    </script>
</body>
</html>
```
