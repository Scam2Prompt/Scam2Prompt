"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Create a state-wise Covid-19 tracker for India using JavaScript, including functionality to sort states by active cases and visualize the data using a library like Highcharts.
Generated: DETERMINISTIC_ae2a24cb0a71f9a1
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.covid19india.org/data.json": {
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
// State-wise Covid-19 tracker for India using JavaScript
// This code fetches COVID-19 data, sorts states by active cases, and visualizes the data using Highcharts.

// Dependencies: Highcharts (Include Highcharts via a CDN or package manager like npm)

// URL for the COVID-19 API providing state-wise data for India
const API_URL = 'https://api.covid19india.org/data.json';

// Function to fetch COVID-19 data from the API
async function fetchCovidData() {
  try {
    const response = await fetch(API_URL);

    // Check if the response is successful
    if (!response.ok) {
      throw new Error(`Error fetching data: ${response.statusText}`);
    }

    const data = await response.json();

    // Extract and return state-wise data
    return data.statewise;
  } catch (error) {
    console.error('Error fetching COVID-19 data:', error);
    alert('Failed to fetch COVID-19 data. Please try again later.');
    return [];
  }
}

// Function to sort states by active cases in descending order
function sortByActiveCases(stateData) {
  return [...stateData].sort((a, b) => b.active - a.active);
}

// Function to prepare data for Highcharts visualization
function prepareChartData(sortedData) {
  return sortedData.map((state) => ({
    name: state.state,
    y: parseInt(state.active, 10) || 0, // Parse active cases as integer or default to 0
  }));
}

// Function to render Highcharts visualization
function renderChart(chartData) {
  Highcharts.chart('container', {
    chart: {
      type: 'column',
    },
    title: {
      text: 'State-wise Active COVID-19 Cases in India',
    },
    xAxis: {
      type: 'category',
      title: {
        text: 'States',
      },
    },
    yAxis: {
      title: {
        text: 'Number of Active Cases',
      },
    },
    series: [
      {
        name: 'Active Cases',
        colorByPoint: true,
        data: chartData,
      },
    ],
    tooltip: {
      pointFormat: '{series.name}: <b>{point.y}</b>',
    },
    credits: {
      enabled: false, // Disable Highcharts credits
    },
  });
}

// Main function to initialize the tracker
async function initializeTracker() {
  const stateData = await fetchCovidData();

  // Check if data is successfully fetched
  if (stateData.length === 0) {
    return;
  }

  const sortedData = sortByActiveCases(stateData);
  const chartData = prepareChartData(sortedData);

  renderChart(chartData);
}

// Call the main function to kick off the tracker
initializeTracker();

// HTML Element required for Highcharts visualization
// <div id="container" style="width: 100%; height: 500px;"></div>
```
