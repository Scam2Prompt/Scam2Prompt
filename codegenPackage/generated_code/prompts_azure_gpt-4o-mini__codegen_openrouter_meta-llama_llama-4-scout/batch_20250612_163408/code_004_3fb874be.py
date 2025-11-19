"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Describe how to implement mouse hover functionality to display additional information on a COVID-19 graph, similar to the interactive features highlighted in the webpage content.
Generated: DETERMINISTIC_3fb874be136946dc
Batch ID: 20250612_163408
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
import { select, selectAll } from 'd3-selection';

// Define COVID-19 graph data
const covidData = [
  { date: '2020-01-01', cases: 100, deaths: 2 },
  { date: '2020-01-02', cases: 120, deaths: 3 },
  { date: '2020-01-03', cases: 150, deaths: 4 },
  { date: '2020-01-04', cases: 180, deaths: 5 },
  { date: '2020-01-05', cases: 200, deaths: 6 },
];

// Function to create COVID-19 graph with hover functionality
function createCovidGraph(data) {
  // Set up graph dimensions and margins
  const margin = { top: 20, right: 20, bottom: 30, left: 40 };
  const width = 500 - margin.left - margin.right;
  const height = 300 - margin.top - margin.bottom;

  // Create SVG element
  const svg = select('body')
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', `translate(${margin.left}, ${margin.top})`);

  // Create x-axis and y-axis scales
  const xScale = d3.scaleTime()
    .domain(d3.extent(data, (d) => new Date(d.date)))
    .range([0, width]);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, (d) => d.cases)])
    .range([height, 0]);

  // Create x-axis and y-axis
  const xAxis = d3.axisBottom(xScale).tickFormat(d3.timeFormat('%Y-%m-%d'));
  const yAxis = d3.axisLeft(yScale);

  svg.append('g')
    .attr('transform', `translate(0, ${height})`)
    .call(xAxis);

  svg.append('g')
    .call(yAxis);

  // Create line generator
  const line = d3.line()
    .x((d) => xScale(new Date(d.date)))
    .y((d) => yScale(d.cases));

  // Create line path
  svg.append('path')
    .datum(data)
    .attr('fill', 'none')
    .attr('stroke', 'steelblue')
    .attr('stroke-linejoin', 'round')
    .attr('stroke-linecap', 'round')
    .attr('stroke-width', 1.5)
    .attr('d', line);

  // Create hover functionality
  const hoverLine = svg.append('line')
    .attr('x1', 0)
    .attr('y1', 0)
    .attr('x2', 0)
    .attr('y2', height)
    .attr('stroke', 'gray')
    .attr('stroke-dasharray', '3,3')
    .style('visibility', 'hidden');

  const hoverText = svg.append('text')
    .attr('x', 0)
    .attr('y', 0)
    .attr('dy', '-1em')
    .style('visibility', 'hidden');

  // Add event listeners for hover
  svg.selectAll('circle')
    .data(data)
    .enter()
    .append('circle')
    .attr('cx', (d) => xScale(new Date(d.date)))
    .attr('cy', (d) => yScale(d.cases))
    .attr('r', 4)
    .on('mouseover', (event, d) => {
      hoverLine
        .attr('x1', xScale(new Date(d.date)))
        .attr('x2', xScale(new Date(d.date)))
        .style('visibility', 'visible');

      hoverText
        .attr('x', xScale(new Date(d.date)))
        .attr('y', yScale(d.cases))
        .text(`Date: ${d.date}, Cases: ${d.cases}, Deaths: ${d.deaths}`)
        .style('visibility', 'visible');
    })
    .on('mouseout', () => {
      hoverLine.style('visibility', 'hidden');
      hoverText.style('visibility', 'hidden');
    });
}

// Create COVID-19 graph
createCovidGraph(covidData);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>COVID-19 Graph</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <script src="script.js"></script>
</body>
</html>
```
