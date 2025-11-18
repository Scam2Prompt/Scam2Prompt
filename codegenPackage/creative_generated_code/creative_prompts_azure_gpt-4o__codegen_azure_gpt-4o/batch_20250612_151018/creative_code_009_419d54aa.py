"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Write code to implement a JavaScript-based Covid-19 dashboard for India that requires enabling JavaScript for full functionality, similar to the Covid-19 India Tracker website.
Generated: DETERMINISTIC_419d54aae8de7c5e
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.covid19india.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.covid19india.org/v4/min/data.min.json": {
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
    <title>Covid-19 India Dashboard</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="app.js"></script>
</head>
<body>
    <noscript>
        <p>Please enable JavaScript to view the Covid-19 India Dashboard.</p>
    </noscript>

    <header>
        <h1>Covid-19 India Dashboard</h1>
    </header>

    <main>
        <section id="summary">
            <h2>Summary</h2>
            <div id="summary-data">
                <!-- Summary data will be dynamically added here -->
            </div>
        </section>

        <section id="statewise">
            <h2>Statewise Data</h2>
            <table id="statewise-table">
                <thead>
                    <tr>
                        <th>State</th>
                        <th>Confirmed</th>
                        <th>Active</th>
                        <th>Recovered</th>
                        <th>Deaths</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Statewise data will be dynamically added here -->
                </tbody>
            </table>
        </section>
    </main>

    <footer>
        <p>Data Source: <a href="https://api.covid19india.org" target="_blank">Covid19 India API</a></p>
    </footer>
</body>
</html>
```

```css
/* styles.css - Basic styling for the dashboard */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
}

header {
    background-color: #007bff;
    color: white;
    padding: 1rem;
    text-align: center;
}

main {
    padding: 20px;
}

section {
    margin-bottom: 20px;
}

h2 {
    color: #333;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
}

th {
    background-color: #007bff;
    color: white;
}

footer {
    text-align: center;
    padding: 10px;
    background-color: #f1f1f1;
}
```

```javascript
// app.js - JavaScript for Covid-19 India Dashboard

// API endpoint for fetching Covid-19 data
const API_URL = "https://api.covid19india.org/v4/min/data.min.json";

// Function to fetch data from the API
async function fetchCovidData() {
    try {
        const response = await fetch(API_URL);

        // Check if the response is valid
        if (!response.ok) {
            throw new Error("Failed to fetch data from API");
        }

        const data = await response.json();
        populateDashboard(data);
    } catch (error) {
        console.error("Error fetching Covid-19 data:", error);
        alert("Failed to load data. Please try again later.");
    }
}

// Function to populate the dashboard with data
function populateDashboard(data) {
    // Populate summary data
    const summaryElement = document.getElementById("summary-data");
    const total = data.TT; // TT stands for "Total" in the API
    summaryElement.innerHTML = `
        <p><strong>Confirmed:</strong> ${total.total.confirmed || 0}</p>
        <p><strong>Active:</strong> ${total.total.confirmed - total.total.recovered - total.total.deceased || 0}</p>
        <p><strong>Recovered:</strong> ${total.total.recovered || 0}</p>
        <p><strong>Deaths:</strong> ${total.total.deceased || 0}</p>
    `;

    // Populate statewise data
    const statewiseTableBody = document.querySelector("#statewise-table tbody");
    statewiseTableBody.innerHTML = ""; // Clear existing rows

    for (const [stateCode, stateData] of Object.entries(data)) {
        if (stateCode === "TT") continue; // Skip total data

        const confirmed = stateData.total.confirmed || 0;
        const recovered = stateData.total.recovered || 0;
        const deceased = stateData.total.deceased || 0;
        const active = confirmed - recovered - deceased;

        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${stateData.meta.name || stateCode}</td>
            <td>${confirmed}</td>
            <td>${active}</td>
            <td>${recovered}</td>
            <td>${deceased}</td>
        `;
        statewiseTableBody.appendChild(row);
    }
}

// Load data on page load
document.addEventListener("DOMContentLoaded", fetchCovidData);
```
