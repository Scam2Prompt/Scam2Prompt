"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Create a state-wise Covid-19 tracker for India using JavaScript, including functionality to sort states by active cases and visualize the data using a library like Highcharts.
Generated: DETERMINISTIC_ae2a24cb0a71f9a1
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.covid19india.org/data.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.highcharts.com/highcharts.js": {
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
    <title>India Covid-19 Tracker</title>
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <style>
        #chart-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <h1>State-wise Covid-19 Tracker for India</h1>
    <div id="chart-container"></div>

    <script>
        // Function to fetch Covid-19 data for India
        async function fetchCovidData() {
            try {
                const response = await fetch('https://api.covid19india.org/data.json');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                return data.statewise;
            } catch (error) {
                console.error('Fetch error: ', error);
                alert('Failed to fetch data. Please try again later.');
            }
        }

        // Function to process and sort Covid data by active cases
        function processCovidData(statesData) {
            return statesData
                .filter(state => state.state !== 'Total') // Exclude total counts
                .sort((a, b) => b.active - a.active); // Sort by active cases descending
        }

        // Function to render the Highcharts graph
        function renderChart(sortedStates) {
            const states = sortedStates.map(state => state.state);
            const activeCases = sortedStates.map(state => parseInt(state.active));

            Highcharts.chart('chart-container', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Active Covid-19 Cases in India by State'
                },
                xAxis: {
                    categories: states,
                    title: {
                        text: 'States'
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Number of Active Cases'
                    }
                },
                series: [{
                    name: 'Active Cases',
                    data: activeCases
                }],
                tooltip: {
                    pointFormat: 'Active Cases: <b>{point.y}</b>'
                }
            });
        }

        // Main function to execute the tracker
        async function initCovidTracker() {
            const statesData = await fetchCovidData();
            if (statesData) {
                const sortedStates = processCovidData(statesData);
                renderChart(sortedStates);
            }
        }

        // Initialize the Covid tracker on page load
        window.onload = initCovidTracker;
    </script>
</body>
</html>
```
