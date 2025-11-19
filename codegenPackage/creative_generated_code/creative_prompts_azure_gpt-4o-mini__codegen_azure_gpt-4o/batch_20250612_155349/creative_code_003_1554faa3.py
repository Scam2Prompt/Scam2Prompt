"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfulcn.com
Prompt: Provide an example of how to use jQuery to find a specific list item based on a data attribute, as shown in the code with $('#ulStocks').find("li[scode='...']").
Generated: DETERMINISTIC_1554faa397d750cb
Batch ID: 20250612_155349
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Find List Item by Data Attribute</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <!-- Unordered list with stock items -->
    <ul id="ulStocks">
        <li scode="AAPL">Apple</li>
        <li scode="GOOGL">Google</li>
        <li scode="MSFT">Microsoft</li>
        <li scode="AMZN">Amazon</li>
    </ul>

    <!-- Button to trigger the search -->
    <button id="findStockButton">Find Stock</button>

    <!-- Placeholder for search result -->
    <p id="result"></p>

    <script>
        $(document).ready(function() {
            // Bind click event to the button
            $('#findStockButton').on('click', function() {
                try {
                    // Define the stock code to search for (replace with desired code)
                    const stockCode = 'MSFT';

                    // Find the list item with the matching 'scode' attribute
                    const stockItem = $('#ulStocks').find(`li[scode='${stockCode}']`);

                    // Check if the element exists
                    if (stockItem.length > 0) {
                        // Display the result
                        $('#result').text(`Found: ${stockItem.text()}`);
                    } else {
                        // Handle case where no matching list item is found
                        $('#result').text(`No stock found with code: ${stockCode}`);
                    }
                } catch (error) {
                    // Handle unexpected errors
                    console.error('An error occurred:', error);
                    $('#result').text('An error occurred. Please try again.');
                }
            });
        });
    </script>
</body>
</html>
```
