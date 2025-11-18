"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythsite.com
Prompt: Generate code to query Pyth price feed oracles for live asset prices and handle errors if JavaScript is disabled.
Generated: DETERMINISTIC_c05771eb383e1296
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network/v1/prices": {
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
    <title>Pyth Price Feed Query</title>
    <script>
        // Function to fetch live asset prices from Pyth price feed oracles
        async function fetchAssetPrices() {
            const url = 'https://api.pyth.network/v1/prices'; // Pyth API endpoint

            try {
                const response = await fetch(url); // Fetch data from the Pyth API

                // Check if the response status is OK (200)
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json(); // Parse the JSON response
                displayPrices(data); // Display the asset prices on the webpage
            } catch (error) {
                console.error('Error fetching asset prices:', error); // Log the error to the console
                document.getElementById('error-message').innerText = 'Failed to load asset prices. Please try again later.'; // Show user-friendly error message
            }
        }

        // Function to display the fetched asset prices in the HTML
        function displayPrices(data) {
            const pricesContainer = document.getElementById('prices'); // Get the container for displaying prices
            pricesContainer.innerHTML = ''; // Clear previous prices

            // Iterate through each price in the data and create an HTML element for each
            data.forEach(price => {
                const priceElement = document.createElement('div'); // Create a new div for the price
                priceElement.innerText = `${price.symbol}: $${price.price}`; // Set the text to show the asset symbol and price
                pricesContainer.appendChild(priceElement); // Append the price element to the container
            });
        }

        // Initialize the price fetch when the window loads
        window.onload = () => {
            fetchAssetPrices(); // Call the fetch function to get asset prices
        };
    </script>
</head>
<body>
    <h1>Pyth Price Feed</h1>
    <div id="error-message" style="color: red;"></div> <!-- Container for error messages -->
    <div id="prices"></div> <!-- Container for displaying asset prices -->
    <noscript>
        <style>
            /* Styles to display when JavaScript is disabled */
            body {
                font-family: Arial, sans-serif; 
            }
            .no-js-message {
                color: red; 
                font-weight: bold; 
            }
        </style>
        <div class="no-js-message">JavaScript is disabled in your browser. Please enable it to view live asset prices.</div>
    </noscript>
</body>
</html>
```
