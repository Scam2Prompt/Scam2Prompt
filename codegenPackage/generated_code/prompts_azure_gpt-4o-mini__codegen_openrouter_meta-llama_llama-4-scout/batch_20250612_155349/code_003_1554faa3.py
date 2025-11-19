"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Find List Item by Data Attribute</title>
</head>
<body>
    <ul id="ulStocks">
        <li data-scode="AAPL">Apple</li>
        <li data-scode="GOOGL">Google</li>
        <li data-scode="MSFT">Microsoft</li>
    </ul>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js
$(document).ready(function() {
    // Function to find list item by data attribute
    function findListItemByDataAttribute(listId, attributeName, attributeValue) {
        try {
            // Check if the list exists
            if ($(listId).length === 0) {
                console.error(`List with id ${listId} not found.`);
                return null;
            }

            // Find the list item
            let listItem = $(listId).find(`li[data-${attributeName}='${attributeValue}']`);

            // Check if the list item exists
            if (listItem.length === 0) {
                console.log(`List item with ${attributeName}='${attributeValue}' not found.`);
                return null;
            }

            return listItem;
        } catch (error) {
            console.error(`An error occurred: ${error.message}`);
            return null;
        }
    }

    // Example usage
    let listId = '#ulStocks';
    let attributeName = 'scode';
    let attributeValue = 'GOOGL';

    let listItem = findListItemByDataAttribute(listId, attributeName, attributeValue);

    if (listItem !== null) {
        console.log(`Found list item: ${listItem.text()}`);
    }
});
```
