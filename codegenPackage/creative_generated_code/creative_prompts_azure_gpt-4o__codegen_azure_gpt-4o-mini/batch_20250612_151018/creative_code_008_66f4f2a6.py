"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Using the Minute Physics video as inspiration, create a web-based interactive graph for COVID-19 data that visually demonstrates exponential growth trends across multiple countries.
Generated: DETERMINISTIC_66f4f2a686f3a136
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/chart.js/3.9.1/chart.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.covid19api.com/dayone/country/${country}/status/confirmed/live`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/chart.js/3.9.1/chart.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COVID-19 Exponential Growth Visualization</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/chart.js/3.9.1/chart.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        canvas {
            max-width: 800px;
            margin: auto;
        }
    </style>
</head>
<body>

    <h1>COVID-19 Exponential Growth Trends</h1>
    <canvas id="covidChart"></canvas>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/chart.js/3.9.1/chart.min.js"></script>
    <script>
        // Function to fetch COVID-19 data for a specific country
        async function fetchCovidData(country) {
            const url = `https://api.covid19api.com/dayone/country/${country}/status/confirmed/live`;
            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return await response.json();
            } catch (error) {
                console.error("Error fetching data:", error);
                alert("Failed to fetch COVID-19 data. Please try again later.");
                return [];
            }
        }

        // Function to process and prepare data for Chart.js
        function prepareChartData(data, country) {
            const labels = data.map(entry => new Date(entry.Date).toLocaleDateString());
            const cases = data.map(entry => entry.Cases);
            return { labels, cases, country };
        }

        // Function to create the chart
        function createChart(data) {
            const ctx = document.getElementById('covidChart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: `Confirmed Cases in ${data.country}`,
                        data: data.cases,
                        borderColor: 'rgba(255, 99, 132, 1)',
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderWidth: 2,
                        fill: true,
                    }],
                },
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Date',
                            },
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Number of Cases',
                            },
                            beginAtZero: true,
                        },
                    },
                    plugins: {
                        legend: {
                            display: true,
                        },
                        tooltip: {
                            callbacks: {
                                label: function(tooltipItem) {
                                    return `Cases: ${tooltipItem.raw}`;
                                },
                            },
                        },
                    },
                },
            });
        }

        // Main function to run when the page loads
        async function initialize() {
            const country = 'us'; // Change this to the desired country code
            const covidData = await fetchCovidData(country);
            const preparedData = prepareChartData(covidData, country.toUpperCase());
            createChart(preparedData);
        }

        // Run the initialization function when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', initialize);
    </script>
</body>
</html>
```
