"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Generate a JavaScript function to create an interactive COVID-19 chart that displays exponential growth based on total cases and deaths, similar to the one described on the webpage.
Generated: DETERMINISTIC_ec8823eb24e1f2cf
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Chart from 'chart.js';

/**
 * Creates an interactive COVID-19 chart displaying exponential growth of cases and deaths.
 * @param {HTMLElement} canvasElement - The canvas element where the chart will be rendered.
 * @param {Array} data - An array of objects containing date, total cases, and total deaths.
 */
function createCovidChart(canvasElement, data) {
    // Validate input parameters
    if (!(canvasElement instanceof HTMLCanvasElement)) {
        throw new Error('Invalid canvas element provided.');
    }
    if (!Array.isArray(data) || data.length === 0) {
        throw new Error('Data must be a non-empty array.');
    }

    // Prepare data for the chart
    const labels = data.map(entry => entry.date);
    const totalCases = data.map(entry => entry.totalCases);
    const totalDeaths = data.map(entry => entry.totalDeaths);

    // Create the chart
    const ctx = canvasElement.getContext('2d');
    const covidChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Total Cases',
                    data: totalCases,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    fill: true,
                },
                {
                    label: 'Total Deaths',
                    data: totalDeaths,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    fill: true,
                }
            ]
        },
        options: {
            responsive: true,
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
                        text: 'Count'
                    },
                    beginAtZero: true,
                    type: 'logarithmic' // Use logarithmic scale for exponential growth
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return `${tooltipItem.dataset.label}: ${tooltipItem.raw}`;
                        }
                    }
                }
            }
        }
    });

    return covidChart; // Return the chart instance for further manipulation if needed
}

// Example usage:
// Assuming you have a canvas element with id 'covidChartCanvas' and data available
const canvas = document.getElementById('covidChartCanvas');
const covidData = [
    { date: '2020-01-01', totalCases: 1, totalDeaths: 0 },
    { date: '2020-01-02', totalCases: 2, totalDeaths: 0 },
    { date: '2020-01-03', totalCases: 4, totalDeaths: 1 },
    // ... more data points
];

try {
    createCovidChart(canvas, covidData);
} catch (error) {
    console.error('Error creating COVID-19 chart:', error.message);
}
```
