"""
Generated Code Metadata:
========================
Original URL: https://paxfulcn.com
Prompt: Provide an example of how to use jQuery to find a specific list item based on a data attribute, as shown in the code with $('#ulStocks').find("li[scode='...']").
Generated: DETERMINISTIC_1554faa397d750cb
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Example of finding a list item by data attribute using jQuery
$(document).ready(function() {
    // Sample function to find and highlight a list item by stock code
    function findStockByCode(stockCode) {
        try {
            // Find the list item with matching data attribute
            var $stockItem = $('#ulStocks').find("li[data-scode='" + stockCode + "']");
            
            if ($stockItem.length) {
                // Highlight the found item
                $stockItem.css('background-color', 'yellow');
                console.log('Found stock item:', $stockItem.text());
                return $stockItem;
            } else {
                console.log('Stock item not found with code:', stockCode);
                return null;
            }
        } catch (error) {
            console.error('Error finding stock item:', error);
            return null;
        }
    }

    // Example usage
    findStockByCode('AAPL');
});

// Sample HTML structure this would work with:
/*
<ul id="ulStocks">
    <li data-scode="AAPL">Apple Inc.</li>
    <li data-scode="GOOGL">Alphabet Inc.</li>
    <li data-scode="MSFT">Microsoft Corporation</li>
</ul>
*/
```
