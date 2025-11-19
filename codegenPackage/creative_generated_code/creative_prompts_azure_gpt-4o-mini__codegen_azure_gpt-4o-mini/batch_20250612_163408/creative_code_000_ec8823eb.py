"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Generate a JavaScript function to create an interactive COVID-19 chart that displays exponential growth based on total cases and deaths, similar to the one described on the webpage.
Generated: DETERMINISTIC_ec8823eb24e1f2cf
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries for charting
import Chart from 'chart.js';

/**
 * Function to create an interactive COVID-19 chart displaying exponential growth
 * based on total cases and deaths.
 * @param {HTMLElement} canvasElement - The canvas element where the chart will be rendered.
 * @param {Array} caseData - Array of total case numbers.
 * @param {Array} deathData - Array of total death numbers.
 */
function createCovidChart(canvasElement, caseData, deathData) {
    // Validate input data
    if (!canvasElement || !(caseData instanceof Array) || !(deathData instanceof Array)) {
        console.error("Invalid input: Please provide a valid canvas element and data arrays.");
        return;
    }

    // Check if caseData and deathData have the same length
    if (caseData.length !== deathData.length) {
        console.error("Mismatched data lengths: caseData and deathData should have the same number of elements.");
        return;
    }

    // Prepare the data for the chart
    const labels = caseData.map((_, index) => `Day ${index + 1}`); // Generating labels for days
    const chartData = {
        labels: labels,
        datasets: [
            {
                label: 'Total Cases',
                data: caseData,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true
            },
            {
                label: 'Total Deaths',
                data: deathData,
                borderColor: 'rgba(255, 99, 132, 1)',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: true
            }
        ]
    };

    // Chart configuration
    const config = {
        type: 'line',
        data: chartData,
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Cases / Deaths'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Days'
                    }
                }
            },
            plugins: {
                tooltip: {
                    mode: 'index',
                    intersect: false,
                },
                legend: {
                    display: true,
                    position: 'top',
                }
            }
        }
    };

    // Create the chart
    try {
        const covidChart = new Chart(canvasElement, config);
        console.log("COVID-19 chart created successfully.");
        return covidChart;
    } catch (error) {
        console.error("Error creating chart:", error);
    }
}

// Example usage:
// Assuming you have a canvas element with id 'covidChart'
// const canvas = document.getElementById('covidChart');
// const cases = [100, 200, 400, 800, 1600, 3200]; // Example case data
// const deaths = [1, 2, 4, 8, 16, 32]; // Example death data
// createCovidChart(canvas, cases, deaths);
```
