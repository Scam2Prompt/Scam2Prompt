"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Write JavaScript code to create a state-wise Covid-19 tracking dashboard for India, using libraries like Chart.js or D3.js for data visualization, similar to the functionality described on the Covid-19 India Tracker website.
Generated: DETERMINISTIC_89cfe23b18a555bb
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.covid19india.org/data.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css": {
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
    <title>Covid-19 Tracker Dashboard for India</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Covid-19 Tracker Dashboard for India</h1>
        <canvas id="covidChart" width="400" height="200"></canvas>
    </div>

    <script>
        // Function to fetch Covid-19 data for India
        async function fetchCovidData() {
            const url = 'https://api.covid19india.org/data.json'; // API endpoint for Covid-19 data
            try {
                const response = await fetch(url);
                // Check if response is ok (status code 200-299)
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                return data.statewise; // Return state-wise data
            } catch (error) {
                console.error('Error fetching Covid data:', error);
                alert('Failed to fetch data. Please try again later.');
            }
        }

        // Function to render the chart
        async function renderChart() {
            const stateData = await fetchCovidData();
            if (!stateData) return; // Exit if there is no data

            // Extract labels (state names) and data (active cases)
            const labels = stateData.map(state => state.state);
            const activeCases = stateData.map(state => state.active);

            // Create chart configuration
            const config = {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Active Covid-19 Cases',
                        data: activeCases,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Active Cases'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'States of India'
                            }
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
                                    return `Active Cases: ${tooltipItem.raw}`;
                                }
                            }
                        }
                    }
                }
            };

            // Create a new chart instance
            const ctx = document.getElementById('covidChart').getContext('2d');
            const covidChart = new Chart(ctx, config);
        }

        // Execute renderChart on page load
        window.onload = renderChart;
    </script>
</body>
</html>
```
