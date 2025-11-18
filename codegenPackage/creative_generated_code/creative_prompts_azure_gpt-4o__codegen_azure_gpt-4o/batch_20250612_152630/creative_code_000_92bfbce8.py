"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpetrarz.pages.dev
Prompt: Write a script using the Coinlib API to fetch cryptocurrency prices for Ethereum, Binance, and Polygon chains, and display them in a decentralized Dapp interface.
Generated: DETERMINISTIC_92bfbce8a8643364
Batch ID: 20250612_152630
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://coinlib.io/api/v1/coin": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const express = require('express'); // Framework for creating the API server
const fetch = require('node-fetch'); // Library for making HTTP requests
const path = require('path');        // Module for handling file paths

// Initialize the Express application
const app = express();

// Configure API key and endpoint for Coinlib API
const COINLIB_API_KEY = 'your_coinlib_api_key'; // Replace with your actual API key
const COINLIB_ENDPOINT = 'https://coinlib.io/api/v1/coin';

// List of cryptocurrencies to fetch prices for
const CRYPTOCURRENCIES = ['Ethereum', 'Binance Coin', 'Polygon'];

// Serve static files for the Dapp interface
app.use(express.static(path.join(__dirname, 'public')));

/**
 * Fetch cryptocurrency price data from the Coinlib API.
 * @param {string} symbol - Symbol of the cryptocurrency (e.g., 'ETH', 'BNB', 'MATIC').
 * @returns {Promise<Object>} - Price data object for the cryptocurrency.
 */
async function fetchCryptoPrice(symbol) {
    try {
        const url = `${COINLIB_ENDPOINT}?key=${COINLIB_API_KEY}&pref=USD&symbol=${symbol}`;
        const response = await fetch(url);

        // Ensure API response is valid
        if (!response.ok) {
            throw new Error(`Failed to fetch data for ${symbol}: ${response.statusText}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error(`Error fetching cryptocurrency price for ${symbol}:`, error.message);
        return null; // Return null in case of an error
    }
}

/**
 * API endpoint to fetch cryptocurrency prices for the specified chains.
 * Users can send requests to `/prices` to receive an updated list.
 */
app.get('/prices', async (req, res) => {
    try {
        const prices = await Promise.all(
            CRYPTOCURRENCIES.map(async (crypto) => {
                const symbol = {
                    Ethereum: 'ETH',
                    'Binance Coin': 'BNB',
                    Polygon: 'MATIC',
                }[crypto];

                const priceData = await fetchCryptoPrice(symbol);
                if (priceData) {
                    return { name: crypto, price: priceData.price };
                } else {
                    return { name: crypto, price: 'Error fetching price' };
                }
            })
        );

        res.json({ success: true, data: prices });
    } catch (error) {
        console.error('Error fetching cryptocurrency prices:', error.message);
        res.status(500).json({ success: false, error: 'Internal Server Error' });
    }
});

// Start the server and listen for incoming requests
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Instructions to display the Dapp interface
// Save the following HTML file in a 'public' folder as 'index.html':

/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Prices Dapp</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        table {
            margin: auto;
            border-collapse: collapse;
            width: 50%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Cryptocurrency Prices</h1>
    <table id="crypto-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Price (USD)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td colspan="2">Loading...</td>
            </tr>
        </tbody>
    </table>
    <script>
        async function fetchPrices() {
            try {
                const response = await fetch('/prices');
                const data = await response.json();

                const tableBody = document.querySelector('#crypto-table tbody');
                tableBody.innerHTML = '';

                data.data.forEach((crypto) => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${crypto.name}</td>
                        <td>${crypto.price}</td>
                    `;
                    tableBody.appendChild(row);
                });
            } catch (error) {
                console.error('Error fetching prices:', error);
            }
        }

        fetchPrices();

        // Refresh prices every minute
        setInterval(fetchPrices, 60000);
    </script>
</body>
</html>
*/
```
