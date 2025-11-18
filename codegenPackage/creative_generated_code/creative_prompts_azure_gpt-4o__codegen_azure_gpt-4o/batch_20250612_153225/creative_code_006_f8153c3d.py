"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-cat.pages.dev
Prompt: Create a JavaScript program to fetch historical USDT price data from a finance API and plot it using a charting library.
Generated: DETERMINISTIC_f8153c3de96aaca8
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/historical-price-data": {
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
// Import required libraries
// Ensure you have installed axios and chart.js via npm before running this code
const axios = require('axios'); // For making HTTP requests
const Chart = require('chart.js'); // For rendering charts in the browser

// Function to fetch historical USDT price data from the finance API
async function fetchHistoricalUSDTPrices() {
    try {
        const apiUrl = 'https://api.example.com/historical-price-data'; // Replace with the actual API URL
        const response = await axios.get(apiUrl, {
            params: {
                symbol: 'USDT', // Specify the cryptocurrency symbol
                currency: 'USD', // Specify the fiat currency
                interval: 'daily', // Interval for the price data
                limit: 30 // Number of data points to fetch
            }
        });

        // Check if the response contains valid data
        if (response.data && Array.isArray(response.data.prices)) {
            return response.data.prices; // Return the array of price data
        } else {
            throw new Error('Invalid response data format.');
        }
    } catch (error) {
        console.error('Error fetching historical USDT price data:', error.message);
        throw error; // Rethrow error for further handling
    }
}

// Function to plot the price data using Chart.js
function plotPriceData(priceData) {
    // Extract dates and prices from the data
    const dates = priceData.map(dataPoint => dataPoint.date); // Assuming `date` is a field in the API response
    const prices = priceData.map(dataPoint => dataPoint.price); // Assuming `price` is a field in the API response

    // Create a canvas element dynamically to render the chart
    const canvas = document.createElement('canvas');
    canvas.id = 'priceChart';
    document.body.appendChild(canvas);

    // Render the chart
    new Chart(canvas, {
        type: 'line', // Line chart
        data: {
            labels: dates, // X-axis labels (dates)
            datasets: [{
                label: 'USDT Price (USD)',
                data: prices, // Y-axis data (prices)
                borderColor: 'rgba(75, 192, 192, 1)', // Line color
                backgroundColor: 'rgba(75, 192, 192, 0.2)', // Fill color
                borderWidth: 2 // Line thickness
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true // Show legend
                },
                tooltip: {
                    enabled: true // Enable tooltips
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Price (USD)'
                    }
                }
            }
        }
    });
}

// Main function to execute the program
async function main() {
    try {
        // Fetch historical USDT price data
        const priceData = await fetchHistoricalUSDTPrices();

        // Plot the price data
        plotPriceData(priceData);
    } catch (error) {
        console.error('Failed to execute program:', error.message);
    }
}

// Run the program
main();
```

**Note:** Replace `'https://api.example.com/historical-price-data'` with the actual finance API endpoint. This script assumes the API returns a JSON response with `prices` containing an array of objects, each having `date` and `price` fields. Make sure to handle CORS appropriately if running in a browser environment.
