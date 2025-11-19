"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.net
Prompt: Write a C# code example for consuming a WCF REST service using jQuery, as described in the WCF tutorial.
Generated: DETERMINISTIC_6dffaef0aa9d981d
Batch ID: 20250612_161700
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:yourport/YourService.svc/items/": {
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
// WCF Service Contract
[ServiceContract]
public interface IMyService
{
    [OperationContract]
    [WebGet(ResponseFormat = WebMessageFormat.Json, UriTemplate = "items/{id}")]
    Item GetItem(string id);
}

// Data Contract
[DataContract]
public class Item
{
    [DataMember]
    public int Id { get; set; }

    [DataMember]
    public string Name { get; set; }
}

// Service Implementation
public class MyService : IMyService
{
    public Item GetItem(string id)
    {
        // Simple error handling
        if (!int.TryParse(id, out int itemId))
        {
            throw new FaultException("Invalid item ID.");
        }

        // Normally, you would fetch the item from a data source
        return new Item { Id = itemId, Name = $"Item {itemId}" };
    }
}

// Web.config Configuration for WCF Service
<configuration>
  <system.serviceModel>
    <services>
      <service name="YourNamespace.MyService">
        <endpoint address="" binding="webHttpBinding" contract="YourNamespace.IMyService" behaviorConfiguration="webBehavior"/>
      </service>
    </services>
    <behaviors>
      <endpointBehaviors>
        <behavior name="webBehavior">
          <webHttp/>
        </behavior>
      </endpointBehaviors>
    </behaviors>
  </system.serviceModel>
</configuration>
```

```html
<!-- HTML Page to Consume the WCF REST Service using jQuery -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WCF REST Service Example</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
    <h1>WCF REST Service Client</h1>
    <input type="text" id="itemId" placeholder="Enter Item ID" />
    <button id="fetchItem">Fetch Item</button>
    <div id="result"></div>

    <script>
        $(document).ready(function() {
            $('#fetchItem').click(function() {
                // Get the item ID from user input
                var itemId = $('#itemId').val();

                // AJAX request to the WCF REST service
                $.ajax({
                    url: 'http://localhost:yourport/YourService.svc/items/' + itemId,
                    type: 'GET',
                    dataType: 'json',
                    success: function(data) {
                        // Display the fetched item data
                        $('#result').html('<p>Item ID: ' + data.Id + '</p><p>Item Name: ' + data.Name + '</p>');
                    },
                    error: function(xhr, status, error) {
                        // Handle errors
                        $('#result').html('<p>Error: ' + xhr.responseText + '</p>');
                    }
                });
            });
        });
    </script>
</body>
</html>
```
