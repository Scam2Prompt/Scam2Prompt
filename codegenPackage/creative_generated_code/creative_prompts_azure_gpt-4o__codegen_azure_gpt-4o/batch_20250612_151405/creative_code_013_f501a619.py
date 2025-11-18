"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-en.web.app
Prompt: Develop a JavaScript application to display Scotty AI's tokenomics data visually, including allocations for staking, development, exchange listings, and marketing.
Generated: DETERMINISTIC_f501a619a70c60d6
Batch ID: 20250612_151405
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js": {
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
// Scotty AI Tokenomics Dashboard
// This script creates a visual representation of token allocations using a pie chart.
// It uses Chart.js, a popular JavaScript library for data visualization.

// Ensure you have included Chart.js in your project via CDN or package manager.
// Example CDN: <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

// Function to initialize the chart
function initializeTokenomicsChart() {
    // Token allocation data
    const tokenData = {
        staking: 40,      // 40% of tokens allocated for staking
        development: 25,  // 25% of tokens allocated for development
        exchangeListings: 20, // 20% of tokens allocated for exchange listings
        marketing: 15     // 15% of tokens allocated for marketing
    };

    // Get the canvas element from the DOM
    const ctx = document.getElementById('tokenomicsChart').getContext('2d');

    // Create the pie chart
    const tokenomicsChart = new Chart(ctx, {
        type: 'pie',  // Chart type: Pie chart
        data: {
            labels: ['Staking', 'Development', 'Exchange Listings', 'Marketing'], // Define labels
            datasets: [{
                data: Object.values(tokenData), // Populate data from tokenData
                backgroundColor: [
                    '#4CAF50', // Green for staking
                    '#2196F3', // Blue for development
                    '#FFC107', // Yellow for exchange listings
                    '#F44336'  // Red for marketing
                ], // Define color scheme
                borderColor: '#ffffff', // White border
                borderWidth: 1
            }]
        },
        options: {
            responsive: true, // Make chart responsive
            plugins: {
                legend: { // Customize legend
                    position: 'top'
                },
                tooltip: { // Customize tooltip
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.raw || 0;
                            return `${label}: ${value}%`;
                        }
                    }
                }
            }
        }
    });

    console.log('Tokenomics chart successfully initialized.');
}

// Error handling to ensure the DOM element exists before chart initialization
document.addEventListener('DOMContentLoaded', () => {
    try {
        const canvasExists = document.getElementById('tokenomicsChart');
        if (!canvasExists) {
            throw new Error('Canvas element with ID "tokenomicsChart" not found. Please ensure the HTML contains this element.');
        }
        initializeTokenomicsChart(); // Initialize the chart if canvas exists
    } catch (error) {
        console.error(error.message);
    }
});

/* HTML Structure (Place this in your HTML file)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scotty AI Tokenomics Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script> <!-- Include Chart.js -->
    <script src="your-script.js"></script> <!-- Replace with the filename of this JavaScript code -->
</head>
<body>
    <div style="width: 50%; margin: auto; text-align: center;">
        <h1>Scotty AI Tokenomics</h1>
        <canvas id="tokenomicsChart"></canvas> <!-- Canvas element for the chart -->
    </div>
</body>
</html>
*/
```
