"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Create a data visualization dashboard using D3.js to showcase the success of Iowa youth in school and their preparation for a productive adulthood.
Generated: DETERMINISTIC_02a890c7d890d68b
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import * as d3 from 'd3';
import data from './iowa_youth_data.json';

// Set up the dashboard dimensions
const margin = { top: 20, right: 20, bottom: 30, left: 40 };
const width = 800 - margin.left - margin.right;
const height = 600 - margin.top - margin.bottom;

// Create the SVG element
const svg = d3.select('body')
  .append('svg')
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .append('g')
  .attr('transform', `translate(${margin.left}, ${margin.top})`);

// Define the color scale
const colorScale = d3.scaleOrdinal()
  .domain(['Graduation Rate', 'College Enrollment', 'Career Readiness'])
  .range(['#4CAF50', '#2196F3', '#FF9800']);

// Load the data
d3.json('./iowa_youth_data.json').then(data => {
  // Check if data is loaded successfully
  if (!data) {
    throw new Error('Failed to load data');
  }

  // Create the dashboard components
  createBarChart(svg, data, width, height, colorScale);
  createLineChart(svg, data, width, height, colorScale);
  createScatterPlot(svg, data, width, height, colorScale);
});

// Function to create the bar chart
function createBarChart(svg, data, width, height, colorScale) {
  // Set up the bar chart dimensions
  const barChartWidth = width / 3;
  const barChartHeight = height / 2;
  const barChartMargin = { top: 20, right: 20, bottom: 30, left: 40 };

  // Create the bar chart SVG element
  const barChartSvg = svg.append('g')
    .attr('transform', `translate(0, 0)`);

  // Define the bar chart x and y scales
  const xScale = d3.scaleBand()
    .domain(data.map(d => d.year))
    .range([0, barChartWidth])
    .padding(0.2);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.graduationRate)])
    .range([barChartHeight, 0]);

  // Create the bar chart bars
  barChartSvg.selectAll('bar')
    .data(data)
    .enter()
    .append('rect')
    .attr('x', d => xScale(d.year))
    .attr('y', d => yScale(d.graduationRate))
    .attr('width', xScale.bandwidth())
    .attr('height', d => barChartHeight - yScale(d.graduationRate))
    .attr('fill', (d, i) => colorScale('Graduation Rate'));

  // Add bar chart labels and title
  barChartSvg.append('text')
    .attr('x', barChartWidth / 2)
    .attr('y', -10)
    .attr('text-anchor', 'middle')
    .text('Graduation Rate');

  barChartSvg.append('g')
    .attr('transform', `translate(0, ${barChartHeight})`)
    .call(d3.axisBottom(xScale));

  barChartSvg.append('g')
    .call(d3.axisLeft(yScale));
}

// Function to create the line chart
function createLineChart(svg, data, width, height, colorScale) {
  // Set up the line chart dimensions
  const lineChartWidth = width / 3;
  const lineChartHeight = height / 2;
  const lineChartMargin = { top: 20, right: 20, bottom: 30, left: 40 };

  // Create the line chart SVG element
  const lineChartSvg = svg.append('g')
    .attr('transform', `translate(${lineChartWidth}, 0)`);

  // Define the line chart x and y scales
  const xScale = d3.scaleLinear()
    .domain([d3.min(data, d => d.year), d3.max(data, d => d.year)])
    .range([0, lineChartWidth]);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.collegeEnrollment)])
    .range([lineChartHeight, 0]);

  // Create the line chart line
  const line = d3.line()
    .x(d => xScale(d.year))
    .y(d => yScale(d.collegeEnrollment));

  lineChartSvg.append('path')
    .datum(data)
    .attr('fill', 'none')
    .attr('stroke', colorScale('College Enrollment'))
    .attr('stroke-width', 1.5)
    .attr('d', line);

  // Add line chart labels and title
  lineChartSvg.append('text')
    .attr('x', lineChartWidth / 2)
    .attr('y', -10)
    .attr('text-anchor', 'middle')
    .text('College Enrollment');

  lineChartSvg.append('g')
    .attr('transform', `translate(0, ${lineChartHeight})`)
    .call(d3.axisBottom(xScale));

  lineChartSvg.append('g')
    .call(d3.axisLeft(yScale));
}

// Function to create the scatter plot
function createScatterPlot(svg, data, width, height, colorScale) {
  // Set up the scatter plot dimensions
  const scatterPlotWidth = width / 3;
  const scatterPlotHeight = height / 2;
  const scatterPlotMargin = { top: 20, right: 20, bottom: 30, left: 40 };

  // Create the scatter plot SVG element
  const scatterPlotSvg = svg.append('g')
    .attr('transform', `translate(${2 * scatterPlotWidth}, 0)`);

  // Define the scatter plot x and y scales
  const xScale = d3.scaleLinear()
    .domain([d3.min(data, d => d.year), d3.max(data, d => d.year)])
    .range([0, scatterPlotWidth]);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.careerReadiness)])
    .range([scatterPlotHeight, 0]);

  // Create the scatter plot points
  scatterPlotSvg.selectAll('circle')
    .data(data)
    .enter()
    .append('circle')
    .attr('cx', d => xScale(d.year))
    .attr('cy', d => yScale(d.careerReadiness))
    .attr('r', 5)
    .attr('fill', colorScale('Career Readiness'));

  // Add scatter plot labels and title
  scatterPlotSvg.append('text')
    .attr('x', scatterPlotWidth / 2)
    .attr('y', -10)
    .attr('text-anchor', 'middle')
    .text('Career Readiness');

  scatterPlotSvg.append('g')
    .attr('transform', `translate(0, ${scatterPlotHeight})`)
    .call(d3.axisBottom(xScale));

  scatterPlotSvg.append('g')
    .call(d3.axisLeft(yScale));
}
```

```json
// iowa_youth_data.json
[
  {
    "year": 2015,
    "graduationRate": 90,
    "collegeEnrollment": 70,
    "careerReadiness": 60
  },
  {
    "year": 2016,
    "graduationRate": 92,
    "collegeEnrollment": 72,
    "careerReadiness": 62
  },
  {
    "year": 2017,
    "graduationRate": 95,
    "collegeEnrollment": 75,
    "careerReadiness": 65
  },
  {
    "year": 2018,
    "graduationRate": 93,
    "collegeEnrollment": 78,
    "careerReadiness": 68
  },
  {
    "year": 2019,
    "graduationRate": 96,
    "collegeEnrollment": 80,
    "careerReadiness": 70
  }
]
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Iowa Youth Data Visualization Dashboard</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <script type="module" src="script.js"></script>
</body>
</html>
```
