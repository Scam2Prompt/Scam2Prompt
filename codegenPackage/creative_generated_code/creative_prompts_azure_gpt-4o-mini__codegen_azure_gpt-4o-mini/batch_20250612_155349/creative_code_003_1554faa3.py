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
    <title>jQuery Data Attribute Example</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        #ulStocks {
            list-style: none;
            padding: 0;
        }
        li {
            padding: 5px;
            border: 1px solid #ccc;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <ul id="ulStocks">
        <li scode="AAPL">Apple Inc.</li>
        <li scode="GOOGL">Alphabet Inc.</li>
        <li scode="AMZN">Amazon.com Inc.</li>
        <li scode="TSLA">Tesla Inc.</li>
    </ul>

    <script>
        $(document).ready(function() {
            // Function to find a list item based on the data attribute 'scode'
            function findStockByCode(stockCode) {
                try {
                    // Find the list item with the specified 'scode' data attribute
                    var stockItem = $('#ulStocks').find("li[scode='" + stockCode + "']");
                    
                    // Check if the item was found
                    if (stockItem.length > 0) {
                        // Highlight the found item
                        stockItem.css('background-color', 'yellow');
                        console.log('Found stock:', stockItem.text());
                    } else {
                        console.warn('Stock with scode "' + stockCode + '" not found.');
                    }
                } catch (error) {
                    console.error('An error occurred while finding the stock:', error);
                }
            }

            // Example usage: find stock with scode 'AAPL'
            findStockByCode('AAPL');
        });
    </script>
</body>
</html>
```
