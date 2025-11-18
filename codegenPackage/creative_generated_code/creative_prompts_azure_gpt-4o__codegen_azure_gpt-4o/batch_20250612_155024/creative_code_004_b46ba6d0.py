"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-staking.vercel.app
Prompt: Provide an example of how to configure a JavaScript app to display live Sui staking metrics using an API.
Generated: DETERMINISTIC_b46ba6d0c278d8b0
Batch ID: 20250612_155024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sui-staking.example.com": {
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
// live-sui-staking.js
// This script fetches live Sui staking metrics from an API and displays them in a JavaScript application.

// Configuration constants
const API_BASE_URL = "https://api.sui-staking.example.com"; // Replace with actual API URL
const METRICS_ENDPOINT = "/staking-metrics";
const REFRESH_INTERVAL_MS = 5000; // Refresh data every 5 seconds

// Select DOM element to display metrics
const metricsContainer = document.getElementById("staking-metrics-container");

// Utility function to format numbers (e.g., staking amounts)
function formatNumber(number) {
  return new Intl.NumberFormat('en-US', { maximumFractionDigits: 2 }).format(number);
}

// Function to fetch staking metrics from the API
async function fetchStakingMetrics() {
  try {
    const response = await fetch(`${API_BASE_URL}${METRICS_ENDPOINT}`);

    // Check if the response is OK (HTTP status code 200)
    if (!response.ok) {
      throw new Error(`Failed to fetch staking metrics: ${response.status} ${response.statusText}`);
    }

    // Parse JSON response
    const data = await response.json();

    // Update the UI with the fetched metrics
    updateMetricsDisplay(data);
  } catch (error) {
    // Log errors to the console (production apps may log to external monitoring services)
    console.error("Error fetching staking metrics:", error);

    // Display an error message in the UI
    metricsContainer.innerHTML = `<p class="error">Unable to load staking metrics. Please try again later.</p>`;
  }
}

// Function to update metrics display in the UI
function updateMetricsDisplay(metrics) {
  // Example metrics structure:
  // metrics = { totalStaked: 1000000, activeValidators: 30, apy: 12.5 };

  metricsContainer.innerHTML = `
    <p><strong>Total Staked:</strong> ${formatNumber(metrics.totalStaked)} SUI</p>
    <p><strong>Active Validators:</strong> ${metrics.activeValidators}</p>
    <p><strong>APY:</strong> ${metrics.apy}%</p>
  `;
}

// Function to start the live metrics update loop
function startMetricsUpdates() {
  // Fetch metrics immediately on app start
  fetchStakingMetrics();

  // Set up periodic updates
  setInterval(fetchStakingMetrics, REFRESH_INTERVAL_MS);
}

// Initialize the app
document.addEventListener("DOMContentLoaded", () => {
  // Start fetching and displaying staking metrics
  startMetricsUpdates();
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Sui Staking Metrics</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background-color: #f9f9f9;
    }
    #staking-metrics-container {
      border: 1px solid #ddd;
      padding: 10px;
      background-color: #fff;
      border-radius: 5px;
    }
    .error {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Live Sui Staking Metrics</h1>
  <div id="staking-metrics-container">
    <p>Loading metrics...</p>
  </div>

  <!-- Include the JavaScript file -->
  <script src="live-sui-staking.js"></script>
</body>
</html>
```
