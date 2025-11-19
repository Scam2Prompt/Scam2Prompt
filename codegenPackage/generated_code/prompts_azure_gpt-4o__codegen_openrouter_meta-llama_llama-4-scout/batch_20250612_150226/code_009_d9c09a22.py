"""
Generated Code Metadata:
========================
Original URL: https://defikingdoms.pages.dev
Prompt: Create a roadmap visualization tool in JavaScript to display feature releases, governance votes, and hero summoning statistics for DeFi Kingdoms.
Generated: DETERMINISTIC_d9c09a22d97a638c
Batch ID: 20250612_150226
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
import { Chart } from 'chart.js';

// Define the RoadmapVisualizationTool class
class RoadmapVisualizationTool {
  /**
   * Constructor for the RoadmapVisualizationTool class
   * @param {Object} data - The data to be visualized
   * @param {string} containerId - The ID of the container element
   */
  constructor(data, containerId) {
    this.data = data;
    this.containerId = containerId;
  }

  /**
   * Render the roadmap visualization
   */
  render() {
    // Create the container element
    const container = document.getElementById(this.containerId);

    // Check if the container exists
    if (!container) {
      throw new Error(`Container element with ID ${this.containerId} not found`);
    }

    // Create the SVG element
    const svg = d3.select(container)
      .append('svg')
      .attr('width', 800)
      .attr('height', 600);

    // Define the margins
    const margins = {
      top: 20,
      right: 20,
      bottom: 30,
      left: 40,
    };

    // Define the x and y scales
    const xScale = d3.scaleTime()
      .domain(d3.extent(this.data, (d) => d.date))
      .range([margins.left, 800 - margins.right]);

    const yScale = d3.scaleLinear()
      .domain([0, d3.max(this.data, (d) => d.value)])
      .range([600 - margins.bottom, margins.top]);

    // Create the x and y axes
    const xAxis = d3.axisBottom(xScale);
    const yAxis = d3.axisLeft(yScale);

    // Add the x and y axes to the SVG element
    svg.append('g')
      .attr('transform', `translate(0, ${600 - margins.bottom})`)
      .call(xAxis);

    svg.append('g')
      .attr('transform', `translate(${margins.left}, 0)`)
      .call(yAxis);

    // Create the line generator
    const line = d3.line()
      .x((d) => xScale(d.date))
      .y((d) => yScale(d.value));

    // Add the line to the SVG element
    svg.append('path')
      .datum(this.data)
      .attr('fill', 'none')
      .attr('stroke', 'steelblue')
      .attr('stroke-width', 1.5)
      .attr('d', line);

    // Create a chart.js canvas for hero summoning statistics
    const ctx = document.createElement('canvas');
    container.appendChild(ctx);

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: this.data.map((d) => d.date.toLocaleDateString()),
        datasets: [{
          label: 'Hero Summoning Statistics',
          data: this.data.map((d) => d.heroSummoningStatistics),
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
        }],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });

    // Create a table for governance votes
    const table = document.createElement('table');
    container.appendChild(table);

    const thead = document.createElement('thead');
    table.appendChild(thead);

    const tbody = document.createElement('tbody');
    table.appendChild(tbody);

    const headerRow = document.createElement('tr');
    thead.appendChild(headerRow);

    const headerCells = ['Date', 'Vote Type', 'Result'];
    headerCells.forEach((cell) => {
      const th = document.createElement('th');
      th.textContent = cell;
      headerRow.appendChild(th);
    });

    this.data.forEach((d) => {
      const row = document.createElement('tr');
      tbody.appendChild(row);

      const cells = [
        d.date.toLocaleDateString(),
        d.governanceVoteType,
        d.governanceVoteResult,
      ];

      cells.forEach((cell) => {
        const td = document.createElement('td');
        td.textContent = cell;
        row.appendChild(td);
      });
    });
  }
}

// Example usage
const data = [
  {
    date: new Date('2022-01-01'),
    value: 10,
    heroSummoningStatistics: 100,
    governanceVoteType: 'Proposal 1',
    governanceVoteResult: 'Passed',
  },
  {
    date: new Date('2022-02-01'),
    value: 20,
    heroSummoningStatistics: 200,
    governanceVoteType: 'Proposal 2',
    governanceVoteResult: 'Failed',
  },
  {
    date: new Date('2022-03-01'),
    value: 30,
    heroSummoningStatistics: 300,
    governanceVoteType: 'Proposal 3',
    governanceVoteResult: 'Passed',
  },
];

const roadmapVisualizationTool = new RoadmapVisualizationTool(data, 'roadmap-container');
roadmapVisualizationTool.render();
```
