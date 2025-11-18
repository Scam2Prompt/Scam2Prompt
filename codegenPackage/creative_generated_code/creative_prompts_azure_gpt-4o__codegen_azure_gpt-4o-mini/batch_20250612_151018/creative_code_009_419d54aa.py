"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Write code to implement a JavaScript-based Covid-19 dashboard for India that requires enabling JavaScript for full functionality, similar to the Covid-19 India Tracker website.
Generated: DETERMINISTIC_419d54aae8de7c5e
Batch ID: 20250612_151018
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
  "https://api.covid19india.org/": {
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
    <title>COVID-19 Dashboard for India</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container">
        <h1>COVID-19 Dashboard for India</h1>
        <div id="stats">
            <div class="card">
                <h2>Total Cases</h2>
                <p id="totalCases">Loading...</p>
            </div>
            <div class="card">
                <h2>Total Recovered</h2>
                <p id="totalRecovered">Loading...</p>
            </div>
            <div class="card">
                <h2>Total Deaths</h2>
                <p id="totalDeaths">Loading...</p>
            </div>
        </div>
        <canvas id="covidChart" width="400" height="200"></canvas>
        <p class="footer">Data Source: <a href="https://api.covid19india.org/">COVID19India API</a></p>
    </div>

    <script>
        // Fetch COVID-19 data from the API
        async function fetchCovidData() {
            try {
                const response = await fetch('https://api.covid19india.org/data.json');
                // Check if the response is ok (status in the range 200-299)
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                return data;
            } catch (error) {
                console.error('Failed to fetch data:', error);
                document.getElementById('stats').innerHTML = '<p>Error fetching COVID-19 data. Please try again later.</p>';
                throw error; // Rethrow for further handling if necessary
            }
        }

        // Update the dashboard with the fetched data
        function updateDashboard(data) {
            const latestData = data.statewise[0]; // Get the latest data for India
            document.getElementById('totalCases').innerText = latestData.confirmed;
            document.getElementById('totalRecovered').innerText = latestData.recovered;
            document.getElementById('totalDeaths').innerText = latestData.deaths;

            const dates = data.cases_time_series.map(entry => entry.date);
            const cases = data.cases_time_series.map(entry => entry.totalconfirmed);
            const recovered = data.cases_time_series.map(entry => entry.totalrecovered);
            const deaths = data.cases_time_series.map(entry => entry.totaldeceased);

            // Create a chart showing cases over time
            const ctx = document.getElementById('covidChart').getContext('2d');
            const covidChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: dates,
                    datasets: [
                        {
                            label: 'Total Cases',
                            data: cases,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1,
                            fill: false
                        },
                        {
                            label: 'Total Recovered',
                            data: recovered,
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1,
                            fill: false
                        },
                        {
                            label: 'Total Deaths',
                            data: deaths,
                            borderColor: 'rgba(153, 102, 255, 1)',
                            borderWidth: 1,
                            fill: false
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }

        // Initialize the dashboard
        async function initDashboard() {
            try {
                const covidData = await fetchCovidData();
                updateDashboard(covidData);
            } catch (error) {
                console.error('Error during initialization:', error);
            }
        }

        // Call the initialization function when the DOM is fully loaded
        $(document).ready(function() {
            initDashboard();
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

#stats {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.card {
    background: #e7e7e7;
    border-radius: 8px;
    padding: 15px;
    flex: 1;
    margin: 0 10px;
    text-align: center;
}

.card h2 {
    margin: 0 0 10px;
}

.card p {
    font-size: 1.5em;
    margin: 0;
}

.footer {
    text-align: center;
    margin-top: 20px;
}

.footer a {
    text-decoration: none;
    color: blue;
}
```
