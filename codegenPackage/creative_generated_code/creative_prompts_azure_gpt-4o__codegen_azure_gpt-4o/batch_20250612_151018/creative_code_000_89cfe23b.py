"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Write JavaScript code to create a state-wise Covid-19 tracking dashboard for India, using libraries like Chart.js or D3.js for data visualization, similar to the functionality described on the Covid-19 India Tracker website.
Generated: DETERMINISTIC_89cfe23b18a555bb
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.covid19india.org/v4/min/data.min.json": {
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
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
// Ensure you include these libraries in your project via a CDN or npm package
// Example: npm install chart.js axios
import Chart from 'chart.js/auto';
import axios from 'axios';

// Define constants and configuration
const apiUrl = 'https://api.covid19india.org/v4/min/data.min.json'; // Example API endpoint
const dashboardElementId = 'covidDashboard';
const chartElementId = 'covidChart';

// Function to fetch Covid-19 data for India
async function fetchCovidData() {
  try {
    const response = await axios.get(apiUrl);
    return response.data;
  } catch (error) {
    console.error('Error fetching Covid-19 data:', error);
    alert('Failed to fetch Covid-19 data. Please try again later.');
    return null;
  }
}

// Function to process data and extract state-wise summary
function processCovidData(data) {
  if (!data) return [];

  const stateData = Object.entries(data).map(([state, details]) => {
    return {
      state,
      confirmed: details.total?.confirmed || 0,
      recovered: details.total?.recovered || 0,
      deceased: details.total?.deceased || 0,
    };
  });

  return stateData;
}

// Function to render the Covid-19 dashboard table
function renderDashboardTable(stateData) {
  const tableContainer = document.getElementById(dashboardElementId);

  if (!tableContainer) {
    console.error(`Element with id "${dashboardElementId}" not found.`);
    return;
  }

  // Clear existing content
  tableContainer.innerHTML = '';

  // Create table
  const table = document.createElement('table');
  table.className = 'covid-table';

  // Add table headers
  const headerRow = document.createElement('tr');
  const headers = ['State', 'Confirmed Cases', 'Recovered Cases', 'Deaths'];
  headers.forEach((header) => {
    const th = document.createElement('th');
    th.innerText = header;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  // Add rows for each state's data
  stateData.forEach((stateInfo) => {
    const row = document.createElement('tr');
    Object.values(stateInfo).forEach((value) => {
      const td = document.createElement('td');
      td.innerText = value;
      row.appendChild(td);
    });
    table.appendChild(row);
  });

  // Append table to container
  tableContainer.appendChild(table);
}

// Function to render the Covid-19 chart
function renderCovidChart(stateData) {
  const chartContainer = document.getElementById(chartElementId);

  if (!chartContainer) {
    console.error(`Element with id "${chartElementId}" not found.`);
    return;
  }

  const labels = stateData.map((stateInfo) => stateInfo.state);
  const confirmedData = stateData.map((stateInfo) => stateInfo.confirmed);

  // Create the chart
  new Chart(chartContainer, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Confirmed Cases',
          data: confirmedData,
          backgroundColor: 'rgba(255, 99, 132, 0.5)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: true,
        },
        title: {
          display: true,
          text: 'State-wise Covid-19 Confirmed Cases',
        },
      },
    },
  });
}

// Main function to initialize the dashboard
async function initializeDashboard() {
  console.log('Initializing Covid-19 dashboard...');
  const rawData = await fetchCovidData();

  if (!rawData) return;

  const stateData = processCovidData(rawData);

  renderDashboardTable(stateData);
  renderCovidChart(stateData);
}

// Start the dashboard initialization once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeDashboard);
```

**HTML Structure Required:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Covid-19 Dashboard</title>
  <script defer src="path/to/your/script.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    .covid-table {
      width: 100%;
      border-collapse: collapse;
    }
    .covid-table th, .covid-table td {
      border: 1px solid #ddd;
      padding: 8px;
    }
    .covid-table th {
      background-color: #f4f4f4;
      text-align: left;
    }
  </style>
</head>
<body>
  <h1>Covid-19 Tracking Dashboard</h1>
  <div id="covidDashboard"></div>
  <canvas id="covidChart"></canvas>
</body>
</html>
```

**Note:** Replace the API URL with a valid endpoint if the provided one is unavailable. Also, ensure you include the necessary libraries in your project (e.g., Chart.js and Axios).
