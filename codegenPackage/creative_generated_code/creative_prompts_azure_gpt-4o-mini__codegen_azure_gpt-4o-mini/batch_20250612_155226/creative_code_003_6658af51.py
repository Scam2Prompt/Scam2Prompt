"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simple-bridge.pages.dev
Prompt: Create a JavaScript example that allows users to select cryptocurrency pairs for exchange, referencing the supported coins on SimpleSwap.
Generated: DETERMINISTIC_6658af51b7b875d0
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SimpleSwap Crypto Pair Selector
// This script allows users to select cryptocurrency pairs for exchange 
// using a dropdown menu populated by supported coins from SimpleSwap.

const supportedCoins = [
    { symbol: 'BTC', name: 'Bitcoin' },
    { symbol: 'ETH', name: 'Ethereum' },
    { symbol: 'LTC', name: 'Litecoin' },
    { symbol: 'XRP', name: 'Ripple' },
    { symbol: 'BCH', name: 'Bitcoin Cash' },
    // Add more supported coins as needed
];

// Function to populate dropdowns with cryptocurrency options
function populateDropdowns() {
    const fromSelect = document.getElementById('fromCurrency');
    const toSelect = document.getElementById('toCurrency');

    // Clear existing options
    fromSelect.innerHTML = '';
    toSelect.innerHTML = '';

    // Populate fromCurrency dropdown
    supportedCoins.forEach(coin => {
        const option = document.createElement('option');
        option.value = coin.symbol;
        option.textContent = coin.name;
        fromSelect.appendChild(option);
    });

    // Populate toCurrency dropdown
    supportedCoins.forEach(coin => {
        const option = document.createElement('option');
        option.value = coin.symbol;
        option.textContent = coin.name;
        toSelect.appendChild(option);
    });
}

// Function to handle currency pair selection
function handlePairSelection() {
    const fromCurrency = document.getElementById('fromCurrency').value;
    const toCurrency = document.getElementById('toCurrency').value;

    // Validate selection
    if (fromCurrency === toCurrency) {
        alert("Please select different currencies for exchange.");
        return;
    }

    console.log(`Selected Pair: ${fromCurrency} to ${toCurrency}`);
    // Here you would typically call the SimpleSwap API to execute the exchange
}

// Initialize the dropdowns on page load
window.onload = () => {
    populateDropdowns();

    // Add event listener for selection change
    document.getElementById('exchangeBtn').addEventListener('click', handlePairSelection);
};

// HTML structure to be included in your HTML file
// <select id="fromCurrency"></select>
// <select id="toCurrency"></select>
// <button id="exchangeBtn">Exchange</button>
```

This JavaScript code provides a basic implementation to allow users to select cryptocurrency pairs for exchange and includes validation to prevent selecting the same currency pair. The relevant HTML structure is also suggested as part of the comments.
