"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-32--gallant-shirley-8651b6.netlify.app
Prompt: Write code to enable JavaScript-based interactivity for a Covid-19 tracking dashboard, including features like filtering state-wise data and displaying charts or tables.
Generated: DETERMINISTIC_96b5230c7d79dd61
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import * as d3 from 'd3';
import { Chart, registerables } from 'chart.js';
import 'chart.js/auto';

// Register chart.js components
Chart.register(...registerables);

// Covid19Tracker class
class Covid19Tracker {
  /**
   * Constructor for Covid19Tracker
   * @param {Object} data - Covid-19 tracking data
   * @param {HTMLElement} container - Container element for the dashboard
   */
  constructor(data, container) {
    this.data = data;
    this.container = container;
    this.stateFilter = '';
    this.chart = null;
    this.table = null;

    // Initialize dashboard
    this.initDashboard();
  }

  /**
   * Initialize the dashboard
   */
  initDashboard() {
    // Create filter dropdown
    this.createFilterDropdown();

    // Create chart container
    this.createChartContainer();

    // Create table container
    this.createTableContainer();

    // Add event listener for filter changes
    document.getElementById('state-filter').addEventListener('change', (e) => {
      this.stateFilter = e.target.value;
      this.updateChart();
      this.updateTable();
    });

    // Render initial chart and table
    this.updateChart();
    this.updateTable();
  }

  /**
   * Create filter dropdown
   */
  createFilterDropdown() {
    const filterContainer = document.createElement('div');
    filterContainer.className = 'filter-container';

    const filterLabel = document.createElement('label');
    filterLabel.textContent = 'Select State:';
    filterContainer.appendChild(filterLabel);

    const filterDropdown = document.createElement('select');
    filterDropdown.id = 'state-filter';

    // Get unique states from data
    const states = [...new Set(this.data.map((item) => item.state))].sort();

    // Create option elements for each state
    states.forEach((state) => {
      const option = document.createElement('option');
      option.value = state;
      option.textContent = state;
      filterDropdown.appendChild(option);
    });

    filterContainer.appendChild(filterDropdown);
    this.container.appendChild(filterContainer);
  }

  /**
   * Create chart container
   */
  createChartContainer() {
    const chartContainer = document.createElement('div');
    chartContainer.className = 'chart-container';
    this.container.appendChild(chartContainer);

    // Create canvas element for chart
    const chartCanvas = document.createElement('canvas');
    chartCanvas.id = 'chart-canvas';
    chartContainer.appendChild(chartCanvas);
  }

  /**
   * Create table container
   */
  createTableContainer() {
    const tableContainer = document.createElement('div');
    tableContainer.className = 'table-container';
    this.container.appendChild(tableContainer);

    // Create table element
    const table = document.createElement('table');
    table.id = 'data-table';
    tableContainer.appendChild(table);

    this.table = table;
  }

  /**
   * Update chart based on filter
   */
  updateChart() {
    // Filter data based on selected state
    const filteredData = this.data.filter((item) => item.state === this.stateFilter || this.stateFilter === '');

    // Create chart data
    const chartData = {
      labels: filteredData.map((item) => item.date),
      datasets: [
        {
          label: 'Cases',
          data: filteredData.map((item) => item.cases),
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
        },
        {
          label: 'Deaths',
          data: filteredData.map((item) => item.deaths),
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
        },
      ],
    };

    // Create chart options
    const chartOptions = {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    };

    // Destroy existing chart if it exists
    if (this.chart) {
      this.chart.destroy();
    }

    // Create new chart
    const chartCanvas = document.getElementById('chart-canvas');
    this.chart = new Chart(chartCanvas, {
      type: 'line',
      data: chartData,
      options: chartOptions,
    });
  }

  /**
   * Update table based on filter
   */
  updateTable() {
    // Filter data based on selected state
    const filteredData = this.data.filter((item) => item.state === this.stateFilter || this.stateFilter === '');

    // Clear existing table rows
    this.table.innerHTML = '';

    // Create table header
    const tableHeader = document.createElement('tr');
    const dateHeader = document.createElement('th');
    dateHeader.textContent = 'Date';
    tableHeader.appendChild(dateHeader);

    const casesHeader = document.createElement('th');
    casesHeader.textContent = 'Cases';
    tableHeader.appendChild(casesHeader);

    const deathsHeader = document.createElement('th');
    deathsHeader.textContent = 'Deaths';
    tableHeader.appendChild(deathsHeader);

    this.table.appendChild(tableHeader);

    // Create table rows
    filteredData.forEach((item) => {
      const tableRow = document.createElement('tr');

      const dateCell = document.createElement('td');
      dateCell.textContent = item.date;
      tableRow.appendChild(dateCell);

      const casesCell = document.createElement('td');
      casesCell.textContent = item.cases;
      tableRow.appendChild(casesCell);

      const deathsCell = document.createElement('td');
      deathsCell.textContent = item.deaths;
      tableRow.appendChild(deathsCell);

      this.table.appendChild(tableRow);
    });
  }
}

// Example usage
const covid19Data = [
  { state: 'New York', date: '2020-01-01', cases: 10, deaths: 0 },
  { state: 'New York', date: '2020-01-02', cases: 15, deaths: 0 },
  { state: 'California', date: '2020-01-01', cases: 5, deaths: 0 },
  { state: 'California', date: '2020-01-02', cases: 10, deaths: 0 },
];

const dashboardContainer = document.getElementById('dashboard-container');
const tracker = new Covid19Tracker(covid19Data, dashboardContainer);
```
