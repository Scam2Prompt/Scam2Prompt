"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Write code to integrate a currency selector into an e-commerce platform selling Brother sewing machines, allowing users to view prices in USD, EUR, GBP, and other currencies.
Generated: DETERMINISTIC_147f18837715d504
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brother Sewing Machines - Currency Selector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        select {
            margin: 20px 0;
            padding: 10px;
        }
        .price {
            font-size: 24px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>Brother Sewing Machines</h1>
    <label for="currency">Select Currency:</label>
    <select id="currency">
        <option value="USD" data-rate="1.00">USD</option>
        <option value="EUR" data-rate="0.85">EUR</option>
        <option value="GBP" data-rate="0.75">GBP</option>
        <option value="JPY" data-rate="110.00">JPY</option>
    </select>

    <div class="price" id="price">Price: $500.00</div>

    <script>
        // Function to convert price based on selected currency
        function convertCurrency(price, rate) {
            return (price * rate).toFixed(2);
        }

        // Function to update the displayed price based on selected currency
        function updatePrice() {
            const currencySelector = document.getElementById("currency");
            const selectedRate = parseFloat(currencySelector.selectedOptions[0].dataset.rate);
            const basePrice = 500.00; // Base price in USD
            const convertedPrice = convertCurrency(basePrice, selectedRate);
            const currencySymbol = currencySelector.value === "USD" ? "$" : currencySelector.value === "EUR" ? "€" : currencySelector.value === "GBP" ? "£" : "¥";
            document.getElementById("price").textContent = `Price: ${currencySymbol}${convertedPrice}`;
        }

        // Event listener for currency selection change
        document.getElementById("currency").addEventListener("change", updatePrice);
        
        // Initial price display
        updatePrice();
    </script>
</body>
</html>
```
