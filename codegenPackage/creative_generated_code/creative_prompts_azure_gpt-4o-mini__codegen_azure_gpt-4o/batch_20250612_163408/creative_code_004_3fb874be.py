"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Describe how to implement mouse hover functionality to display additional information on a COVID-19 graph, similar to the interactive features highlighted in the webpage content.
Generated: DETERMINISTIC_3fb874be136946dc
Batch ID: 20250612_163408
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/covid-data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://d3js.org/d3.v6.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is production-ready code for implementing mouse hover functionality to display additional information on a COVID-19 graph using JavaScript and the D3.js library:

```javascript
/**
 * Interactive COVID-19 graph with mouse hover functionality.
 * This code dynamically displays additional information when the mouse hovers over data points on the graph.
 */

// Load the data and render the graph
async function renderCovidGraph() {
  // Dimensions of the graph
  const margin = { top: 50, right: 50, bottom: 50, left: 50 };
  const width = 800 - margin.left - margin.right;
  const height = 400 - margin.top - margin.bottom;

  // Load COVID-19 data (example structure: { date: 'YYYY-MM-DD', cases: Number, deaths: Number })
  const data = await fetchCovidData();

  // Parse date format and scale axes
  const parseDate = d3.timeParse('%Y-%m-%d');
  data.forEach(d => {
    d.date = parseDate(d.date);
  });

  // Create SVG container
  const svg = d3.select('#covid-graph')
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', `translate(${margin.left}, ${margin.top})`);

  // Define scales
  const xScale = d3.scaleTime()
    .domain(d3.extent(data, d => d.date))
    .range([0, width]);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => Math.max(d.cases, d.deaths))])
    .range([height, 0]);

  // Create axes
  svg.append('g')
    .attr('transform', `translate(0, ${height})`)
    .call(d3.axisBottom(xScale).ticks(10).tickFormat(d3.timeFormat('%b %d')));

  svg.append('g').call(d3.axisLeft(yScale));

  // Line generator for cases and deaths
  const lineCases = d3.line()
    .x(d => xScale(d.date))
    .y(d => yScale(d.cases));

  const lineDeaths = d3.line()
    .x(d => xScale(d.date))
    .y(d => yScale(d.deaths));

  // Draw lines for cases and deaths
  svg.append('path')
    .datum(data)
    .attr('fill', 'none')
    .attr('stroke', 'blue')
    .attr('stroke-width', 2)
    .attr('d', lineCases);

  svg.append('path')
    .datum(data)
    .attr('fill', 'none')
    .attr('stroke', 'red')
    .attr('stroke-width', 2)
    .attr('d', lineDeaths);

  // Tooltip for hover functionality
  const tooltip = d3.select('body').append('div')
    .style('position', 'absolute')
    .style('background', 'rgba(0, 0, 0, 0.7)')
    .style('color', '#fff')
    .style('padding', '5px 10px')
    .style('border-radius', '4px')
    .style('pointer-events', 'none')
    .style('opacity', 0);

  // Add circles and hover functionality
  svg.selectAll('.data-point')
    .data(data)
    .enter()
    .append('circle')
    .attr('class', 'data-point')
    .attr('cx', d => xScale(d.date))
    .attr('cy', d => yScale(d.cases))
    .attr('r', 5)
    .attr('fill', 'blue')
    .on('mouseover', (event, d) => {
      tooltip.style('opacity', 1)
        .html(`<strong>Date:</strong> ${d3.timeFormat('%b %d, %Y')(d.date)}<br>
               <strong>Cases:</strong> ${d.cases}<br>
               <strong>Deaths:</strong> ${d.deaths}`);
    })
    .on('mousemove', event => {
      tooltip.style('left', `${event.pageX + 10}px`)
        .style('top', `${event.pageY}px`);
    })
    .on('mouseout', () => {
      tooltip.style('opacity', 0);
    });

  svg.selectAll('.data-point-death')
    .data(data)
    .enter()
    .append('circle')
    .attr('class', 'data-point-death')
    .attr('cx', d => xScale(d.date))
    .attr('cy', d => yScale(d.deaths))
    .attr('r', 5)
    .attr('fill', 'red')
    .on('mouseover', (event, d) => {
      tooltip.style('opacity', 1)
        .html(`<strong>Date:</strong> ${d3.timeFormat('%b %d, %Y')(d.date)}<br>
               <strong>Cases:</strong> ${d.cases}<br>
               <strong>Deaths:</strong> ${d.deaths}`);
    })
    .on('mousemove', event => {
      tooltip.style('left', `${event.pageX + 10}px`)
        .style('top', `${event.pageY}px`);
    })
    .on('mouseout', () => {
      tooltip.style('opacity', 0);
    });
}

// Function to fetch COVID-19 data
async function fetchCovidData() {
  try {
    const response = await fetch('https://api.example.com/covid-data');
    if (!response.ok) {
      throw new Error('Failed to fetch COVID-19 data');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching COVID-19 data:', error);
    return [];
  }
}

// Execute graph rendering
renderCovidGraph();
```

### To use this code:
1. Include the D3.js library in your project (via `<script src="https://d3js.org/d3.v6.min.js"></script>`).
2. Ensure your HTML includes a container element with the ID `covid-graph`, e.g., `<div id="covid-graph"></div>`.
3. Replace the `fetchCovidData` function's API URL with the actual endpoint providing COVID-19 data in the expected format.

This code adheres to best practices, includes error handling, and is ready for production.
