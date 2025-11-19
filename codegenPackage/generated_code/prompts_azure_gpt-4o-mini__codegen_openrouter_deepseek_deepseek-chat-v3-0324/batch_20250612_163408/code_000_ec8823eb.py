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

Here's a clean, production-ready JavaScript function to create an interactive COVID-19 chart using Chart.js:

```javascript
/**
 * Creates an interactive COVID-19 exponential growth chart using Chart.js
 * @param {string} canvasId - The ID of the canvas element where the chart will be rendered
 * @param {Object[]} data - Array of COVID-19 data objects
 * @param {string} data[].date - Date string (YYYY-MM-DD)
 * @param {number} data[].cases - Total confirmed cases
 * @param {number} data[].deaths - Total deaths
 * @param {string} [countryName="Global"] - Name of the country/region for the chart title
 * @returns {Chart} The created Chart.js instance
 */
function createCovidChart(canvasId, data, countryName = "Global") {
    // Validate inputs
    if (!canvasId || !document.getElementById(canvasId)) {
        throw new Error("Invalid canvas element ID");
    }
    if (!Array.isArray(data) || data.length === 0) {
        throw new Error("Data must be a non-empty array");
    }

    // Extract dates, cases, and deaths from the data
    const dates = data.map(item => item.date);
    const cases = data.map(item => item.cases);
    const deaths = data.map(item => item.deaths);

    // Get canvas context
    const ctx = document.getElementById(canvasId).getContext('2d');

    // Create the chart
    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [
                {
                    label: 'Total Cases',
                    data: cases,
                    borderColor: 'rgba(54, 162, 235, 1)',
                    backgroundColor: 'rgba(54, 162, 235, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.1
                },
                {
                    label: 'Total Deaths',
                    data: deaths,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: `COVID-19 Cases and Deaths in ${countryName}`,
                    font: {
                        size: 16
                    }
                },
                tooltip: {
                    mode: 'index',
                    intersect: false,
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.raw.toLocaleString()}`;
                        }
                    }
                },
                legend: {
                    position: 'top',
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    },
                    grid: {
                        display: false
                    }
                },
                y: {
                    type: 'logarithmic',
                    title: {
                        display: true,
                        text: 'Count (log scale)'
                    },
                    min: 1,
                    ticks: {
                        callback: function(value) {
                            return Number(value.toString()); // Clean up logarithmic labels
                        }
                    }
                }
            },
            interaction: {
                intersect: false,
                mode: 'nearest'
            }
        }
    });

    return chart;
}

// Example usage:
// const covidData = [
//     { date: "2020-01-01", cases: 100, deaths: 1 },
//     { date: "2020-01-15", cases: 500, deaths: 10 },
//     // ... more data points
// ];
// createCovidChart("covidChart", covidData, "United States");
```
