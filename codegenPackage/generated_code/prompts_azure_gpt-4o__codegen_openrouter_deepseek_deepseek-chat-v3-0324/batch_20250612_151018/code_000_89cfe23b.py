"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Write JavaScript code to create a state-wise Covid-19 tracking dashboard for India, using libraries like Chart.js or D3.js for data visualization, similar to the functionality described on the Covid-19 India Tracker website.
Generated: DETERMINISTIC_89cfe23b18a555bb
Batch ID: 20250612_151018
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.covid19india.org/state_district_wise.json": {
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
  "https://cdn.jsdelivr.net/npm/chart.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries (assuming this is in a Node.js environment or using ES modules)
const axios = require('axios');
const Chart = require('chart.js');

// Alternatively, for browser environment, include these via CDN in HTML:
// <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
// <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

// Configuration
const API_URL = 'https://api.covid19india.org/data.json';
const STATE_WISE_DATA_URL = 'https://api.covid19india.org/state_district_wise.json';

// DOM Elements
const stateSelector = document.getElementById('state-selector');
const statsContainer = document.getElementById('stats-container');
const chartContainer = document.getElementById('chart-container');
const lastUpdated = document.getElementById('last-updated');
const loadingIndicator = document.getElementById('loading-indicator');

// State data cache
let stateData = {};
let timeSeriesData = {};

// Initialize dashboard
async function initDashboard() {
    try {
        loadingIndicator.style.display = 'block';
        
        // Fetch data from API
        const [summaryResponse, stateWiseResponse] = await Promise.all([
            axios.get(API_URL),
            axios.get(STATE_WISE_DATA_URL)
        ]);

        // Process data
        processSummaryData(summaryResponse.data);
        processStateWiseData(stateWiseResponse.data);

        // Populate state selector
        populateStateSelector();

        // Set default state
        updateDashboard('Total');

        loadingIndicator.style.display = 'none';
    } catch (error) {
        console.error('Error initializing dashboard:', error);
        loadingIndicator.style.display = 'none';
        alert('Failed to load COVID-19 data. Please try again later.');
    }
}

// Process summary data
function processSummaryData(data) {
    // Store time series data
    timeSeriesData = data.cases_time_series.reduce((acc, day) => {
        acc.dates.push(day.date);
        acc.total.push(parseInt(day.totalconfirmed));
        acc.recovered.push(parseInt(day.totalrecovered));
        acc.deceased.push(parseInt(day.totaldeceased));
        return acc;
    }, { dates: [], total: [], recovered: [], deceased: [] });

    // Store state-wise data
    data.statewise.forEach(state => {
        stateData[state.state] = {
            confirmed: parseInt(state.confirmed),
            active: parseInt(state.active),
            recovered: parseInt(state.recovered),
            deaths: parseInt(state.deaths),
            lastUpdated: state.lastupdatedtime
        };
    });

    // Update last updated time
    lastUpdated.textContent = `Last Updated: ${data.statewise[0].lastupdatedtime}`;
}

// Process state-wise district data
function processStateWiseData(data) {
    Object.keys(data).forEach(state => {
        if (stateData[state]) {
            stateData[state].districts = {};
            Object.keys(data[state].districtData).forEach(district => {
                stateData[state].districts[district] = {
                    confirmed: data[state].districtData[district].confirmed,
                    active: data[state].districtData[district].active,
                    recovered: data[state].districtData[district].recovered,
                    deceased: data[state].districtData[district].deceased
                };
            });
        }
    });
}

// Populate state selector dropdown
function populateStateSelector() {
    const states = Object.keys(stateData).sort();
    
    states.forEach(state => {
        const option = document.createElement('option');
        option.value = state;
        option.textContent = state;
        stateSelector.appendChild(option);
    });
}

// Update dashboard with selected state data
function updateDashboard(selectedState) {
    if (!stateData[selectedState]) return;

    // Update stats
    updateStats(selectedState);

    // Update charts
    updateCharts(selectedState);
}

// Update statistics display
function updateStats(state) {
    const stats = stateData[state];
    
    statsContainer.innerHTML = `
        <div class="stat-card confirmed">
            <h3>Confirmed</h3>
            <p>${stats.confirmed.toLocaleString()}</p>
        </div>
        <div class="stat-card active">
            <h3>Active</h3>
            <p>${stats.active.toLocaleString()}</p>
        </div>
        <div class="stat-card recovered">
            <h3>Recovered</h3>
            <p>${stats.recovered.toLocaleString()}</p>
        </div>
        <div class="stat-card deceased">
            <h3>Deceased</h3>
            <p>${stats.deaths.toLocaleString()}</p>
        </div>
    `;
}

// Update charts
function updateCharts(state) {
    // Clear previous chart if exists
    while (chartContainer.firstChild) {
        chartContainer.removeChild(chartContainer.firstChild);
    }

    // Create canvas for chart
    const canvas = document.createElement('canvas');
    chartContainer.appendChild(canvas);

    // Prepare data for national or state view
    let chartData;
    if (state === 'Total') {
        chartData = {
            labels: timeSeriesData.dates,
            datasets: [
                {
                    label: 'Total Cases',
                    data: timeSeriesData.total,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    fill: true
                },
                {
                    label: 'Recovered',
                    data: timeSeriesData.recovered,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    fill: true
                },
                {
                    label: 'Deceased',
                    data: timeSeriesData.deceased,
                    borderColor: 'rgba(153, 102, 255, 1)',
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',
                    fill: true
                }
            ]
        };
    } else {
        // For state view, we would need state-specific time series data
        // This is a placeholder - actual implementation would require this data from the API
        chartData = {
            labels: ['Data not available for individual states'],
            datasets: [
                {
                    label: 'Confirmed Cases',
                    data: [stateData[state].confirmed],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }
            ]
        };
    }

    // Create chart
    new Chart(canvas, {
        type: 'line',
        data: chartData,
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: `COVID-19 Trends ${state === 'Total' ? 'in India' : `in ${state}`}`
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Event listeners
stateSelector.addEventListener('change', (e) => {
    updateDashboard(e.target.value);
});

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', initDashboard);
```
