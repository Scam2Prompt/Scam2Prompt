"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digital-hub.top
Prompt: Generate JavaScript code to visualize the energy consumption of data centers, inspired by the environmental insights on Digital Hub.
Generated: DETERMINISTIC_4361c3d35b73f59b
Batch ID: 20250612_151109
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
// Importing necessary libraries
import Chart from 'chart.js'; // Ensure Chart.js is included in your project

// Constants for the visualization
const DATA_CENTER_DATA = [
    { label: 'Data Center 1', consumption: 200 },
    { label: 'Data Center 2', consumption: 350 },
    { label: 'Data Center 3', consumption: 280 },
    { label: 'Data Center 4', consumption: 500 },
    { label: 'Data Center 5', consumption: 150 }
];

// Function to create a bar chart for energy consumption
function createEnergyConsumptionChart(data) {
    // Get the context of the canvas element
    const ctx = document.getElementById('energyChart').getContext('2d');

    // Prepare the data for the chart
    const labels = data.map(dc => dc.label);
    const consumptionValues = data.map(dc => dc.consumption);

    // Create a new chart instance
    const energyChart = new Chart(ctx, {
        type: 'bar', // Type of chart
        data: {
            labels: labels,
            datasets: [{
                label: 'Energy Consumption (kWh)',
                data: consumptionValues,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Energy Consumption (kWh)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Data Centers'
                    }
                }
            },
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Energy Consumption of Data Centers'
                }
            }
        }
    });

    return energyChart;
}

// Function to initialize the chart
function initializeChart() {
    try {
        // Check if the canvas element exists
        const canvasElement = document.getElementById('energyChart');
        if (!canvasElement) {
            throw new Error('Canvas element with id "energyChart" not found.');
        }
        
        // Call the function to create the chart
        createEnergyConsumptionChart(DATA_CENTER_DATA);
    } catch (error) {
        console.error('Error initializing chart:', error);
    }
}

// Ensure the DOM is fully loaded before initializing the chart
document.addEventListener('DOMContentLoaded', () => {
    initializeChart();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Energy Consumption Visualization</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="path/to/your/javascript.js" defer></script>
</head>
<body>

    <h1>Energy Consumption Visualization of Data Centers</h1>
    <canvas id="energyChart" width="400" height="200"></canvas>

</body>
</html>
```
