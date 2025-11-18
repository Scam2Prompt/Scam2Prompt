"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: Develop a dashboard using JavaScript that provides real-time analytics for portfolio performance, similar to Extra Finance's transparent analytics feature.
Generated: DETERMINISTIC_bda3b12f461cac4c
Batch ID: 20250612_153923
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/portfolio-performance": {
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
/**
 * Portfolio Performance Dashboard - Real-Time Analytics
 * This script sets up a dashboard to visualize portfolio performance in real-time.
 * It fetches data from a backend API, processes it, and updates the charts dynamically.
 * 
 * Author: Expert Programmer
 * Created: YYYY-MM-DD
 */

// Ensure the script runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Constants
  const API_URL = "https://api.example.com/portfolio-performance"; // Replace with the actual API endpoint
  const REFRESH_INTERVAL = 5000; // Refresh data every 5 seconds

  // DOM Elements
  const lastUpdatedElement = document.getElementById("last-updated");
  const portfolioChartElement = document.getElementById("portfolio-chart");

  // Initialize Chart.js chart
  let portfolioChart = new Chart(portfolioChartElement, {
    type: "line", // Use a line chart to represent performance trends
    data: {
      labels: [], // X-axis labels (timestamps)
      datasets: [
        {
          label: "Portfolio Value",
          data: [], // Y-axis data
          borderColor: "rgb(75, 192, 192)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          tension: 0.4, // Smooth curves
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
        },
      },
      scales: {
        x: {
          title: {
            display: true,
            text: "Time",
          },
        },
        y: {
          title: {
            display: true,
            text: "Portfolio Value (USD)",
          },
        },
      },
    },
  });

  /**
   * Fetches portfolio performance data from the API.
   * @returns {Promise<Object>} - The portfolio performance data or an error object.
   */
  async function fetchPortfolioData() {
    try {
      const response = await fetch(API_URL);
      if (!response.ok) {
        throw new Error(`API request failed with status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error("Error fetching portfolio data:", error);
    }
  }

  /**
   * Updates the chart with new data.
   * @param {Object} data - The portfolio performance data.
   */
  function updateChart(data) {
    if (!data || !data.timestamps || !data.values) {
      console.warn("Invalid data format received. Skipping update.");
      return;
    }

    // Update chart labels and data
    portfolioChart.data.labels = data.timestamps;
    portfolioChart.data.datasets[0].data = data.values;
    portfolioChart.update();

    // Update last updated timestamp
    lastUpdatedElement.textContent = `Last Updated: ${new Date().toLocaleTimeString()}`;
  }

  /**
   * Periodically fetches data and updates the dashboard.
   */
  function startRealTimeUpdates() {
    setInterval(async () => {
      const data = await fetchPortfolioData();
      updateChart(data);
    }, REFRESH_INTERVAL);
  }

  // Start real-time updates
  startRealTimeUpdates();
});
```

**HTML Structure Example** (to be included in your HTML file):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portfolio Performance Dashboard</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <link rel="stylesheet" href="styles.css"> <!-- Optional: Add CSS for styling -->
</head>
<body>
  <div id="dashboard">
    <h1>Portfolio Performance Dashboard</h1>
    <p id="last-updated">Last Updated: N/A</p>
    <canvas id="portfolio-chart"></canvas>
  </div>
  <script src="dashboard.js"></script>
</body>
</html>
```

Note: Replace `API_URL` with the actual backend endpoint providing portfolio data in the format:
```json
{
  "timestamps": ["2023-10-01T10:00:00", "2023-10-01T10:01:00", ...],
  "values": [50000, 50200, ...]
}
```
