"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Create a state-wise Covid-19 tracker for India using JavaScript, including functionality to sort states by active cases and visualize the data using a library like Highcharts.
Generated: DETERMINISTIC_ae2a24cb0a71f9a1
Batch ID: 20250612_151018
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://code.highcharts.com/modules/accessibility.js": {
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
  },
  "https://code.highcharts.com/modules/exporting.js": {
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
  "https://code.highcharts.com/modules/export-data.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>India COVID-19 Tracker</title>
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/export-data.js"></script>
    <script src="https://code.highcharts.com/modules/accessibility.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .controls {
            margin: 20px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        button {
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            cursor: pointer;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        #chart-container {
            height: 400px;
            margin-top: 20px;
        }
        .loading {
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>India COVID-19 State-wise Tracker</h1>
        
        <div class="controls">
            <div>
                <button id="sort-active">Sort by Active Cases</button>
                <button id="sort-confirmed">Sort by Confirmed Cases</button>
                <button id="sort-recovered">Sort by Recovered Cases</button>
                <button id="sort-deaths">Sort by Deaths</button>
            </div>
            <div>
                <button id="refresh">Refresh Data</button>
            </div>
        </div>

        <div id="loading" class="loading">Loading data...</div>
        
        <table id="covid-table">
            <thead>
                <tr>
                    <th>State/UT</th>
                    <th>Confirmed</th>
                    <th>Active</th>
                    <th>Recovered</th>
                    <th>Deaths</th>
                </tr>
            </thead>
            <tbody id="table-body"></tbody>
        </table>

        <div id="chart-container"></div>
    </div>

    <script>
        // Global variable to store COVID data
        let covidData = [];
        let sortDirection = {
            state: true,
            confirmed: true,
            active: true,
            recovered: true,
            deaths: true
        };

        // DOM elements
        const tableBody = document.getElementById('table-body');
        const loadingElement = document.getElementById('loading');
        const sortActiveBtn = document.getElementById('sort-active');
        const sortConfirmedBtn = document.getElementById('sort-confirmed');
        const sortRecoveredBtn = document.getElementById('sort-recovered');
        const sortDeathsBtn = document.getElementById('sort-deaths');
        const refreshBtn = document.getElementById('refresh');

        // Initialize the application
        document.addEventListener('DOMContentLoaded', () => {
            fetchCovidData();
            
            // Event listeners for sorting buttons
            sortActiveBtn.addEventListener('click', () => sortData('active'));
            sortConfirmedBtn.addEventListener('click', () => sortData('confirmed'));
            sortRecoveredBtn.addEventListener('click', () => sortData('recovered'));
            sortDeathsBtn.addEventListener('click', () => sortData('deaths'));
            refreshBtn.addEventListener('click', fetchCovidData);
        });

        // Fetch COVID-19 data from API
        async function fetchCovidData() {
            try {
                loadingElement.style.display = 'block';
                tableBody.innerHTML = '';
                
                const response = await fetch('https://api.covid19india.org/data.json');
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                covidData = data.statewise.slice(1); // Remove the first entry (India total)
                
                renderTable(covidData);
                renderChart(covidData);
                loadingElement.style.display = 'none';
            } catch (error) {
                loadingElement.innerHTML = `Error fetching data: ${error.message}`;
                console.error('Error fetching COVID data:', error);
            }
        }

        // Render the data table
        function renderTable(data) {
            tableBody.innerHTML = '';
            
            data.forEach(state => {
                const row = document.createElement('tr');
                
                row.innerHTML = `
                    <td>${state.state}</td>
                    <td>${parseInt(state.confirmed).toLocaleString()}</td>
                    <td>${parseInt(state.active).toLocaleString()}</td>
                    <td>${parseInt(state.recovered).toLocaleString()}</td>
                    <td>${parseInt(state.deaths).toLocaleString()}</td>
                `;
                
                tableBody.appendChild(row);
            });
        }

        // Sort data by specified field
        function sortData(field) {
            const sortedData = [...covidData].sort((a, b) => {
                const valueA = parseInt(a[field]);
                const valueB = parseInt(b[field]);
                
                if (sortDirection[field]) {
                    return valueB - valueA; // Descending
                } else {
                    return valueA - valueB; // Ascending
                }
            });
            
            sortDirection[field] = !sortDirection[field];
            renderTable(sortedData);
            renderChart(sortedData);
        }

        // Render the chart using Highcharts
        function renderChart(data) {
            // Prepare data for the chart
            const categories = data.map(state => state.state);
            const confirmedData = data.map(state => parseInt(state.confirmed));
            const activeData = data.map(state => parseInt(state.active));
            const recoveredData = data.map(state => parseInt(state.recovered));
            const deathsData = data.map(state => parseInt(state.deaths));
            
            Highcharts.chart('chart-container', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'COVID-19 Cases by State/UT'
                },
                subtitle: {
                    text: 'Source: covid19india.org'
                },
                xAxis: {
                    categories: categories,
                    crosshair: true,
                    labels: {
                        rotation: -45,
                        style: {
                            fontSize: '10px'
                        }
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Number of Cases'
                    }
                },
                tooltip: {
                    headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                    pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                        '<td style="padding:0"><b>{point.y:,0f}</b></td></tr>',
                    footerFormat: '</table>',
                    shared: true,
                    useHTML: true
                },
                plotOptions: {
                    column: {
                        pointPadding: 0.2,
                        borderWidth: 0
                    }
                },
                series: [{
                    name: 'Confirmed',
                    data: confirmedData,
                    color: '#3498db'
                }, {
                    name: 'Active',
                    data: activeData,
                    color: '#f39c12'
                }, {
                    name: 'Recovered',
                    data: recoveredData,
                    color: '#2ecc71'
                }, {
                    name: 'Deaths',
                    data: deathsData,
                    color: '#e74c3c'
                }],
                exporting: {
                    enabled: true
                },
                credits: {
                    enabled: false
                }
            });
        }
    </script>
</body>
</html>
```
