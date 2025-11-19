"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Generate a JavaScript function to create an interactive COVID-19 chart that displays exponential growth based on total cases and deaths, similar to the one described on the webpage.
Generated: DETERMINISTIC_ec8823eb24e1f2cf
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

// Function to create COVID-19 chart
function createCovidChart(data, totalCasesKey, totalDeathsKey) {
    // Check if data is valid
    if (!data || !Array.isArray(data) || data.length === 0) {
        throw new Error('Invalid data provided');
    }

    // Check if total cases and deaths keys exist in data
    if (!totalCasesKey || !totalDeathsKey) {
        throw new Error('Total cases and deaths keys are required');
    }

    // Set up chart dimensions and margins
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

    // Parse dates and extract relevant data
    data.forEach(d => {
        d.Date = new Date(d.Date);
        d[totalCasesKey] = +d[totalCasesKey];
        d[totalDeathsKey] = +d[totalDeathsKey];
    });

    // Set up x and y scales
    const xScale = d3.scaleTime()
        .domain(d3.extent(data, d => d.Date))
        .range([0, width]);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d[totalCasesKey])])
        .range([height, 0]);

    // Add x and y axes
    const xAxis = d3.axisBottom(xScale).tickFormat(d3.timeFormat('%Y-%m-%d'));
    svg.append('g')
        .attr('transform', `translate(0, ${height})`)
        .call(xAxis);

    const yAxis = d3.axisLeft(yScale);
    svg.append('g')
        .call(yAxis);

    // Add total cases line
    const totalCasesLine = d3.line()
        .x(d => xScale(d.Date))
        .y(d => yScale(d[totalCasesKey]));

    svg.append('path')
        .datum(data)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-width', 1.5)
        .attr('d', totalCasesLine);

    // Add total deaths line
    const totalDeathsLine = d3.line()
        .x(d => xScale(d.Date))
        .y(d => yScale(d[totalDeathsKey]));

    svg.append('path')
        .datum(data)
        .attr('fill', 'none')
        .attr('stroke', 'red')
        .attr('stroke-width', 1.5)
        .attr('stroke-dasharray', '3,3')
        .attr('d', totalDeathsLine);

    // Add labels and title
    svg.append('text')
        .attr('x', width / 2)
        .attr('y', -10)
        .attr('text-anchor', 'middle')
        .style('font-size', '16px')
        .text('COVID-19 Cases and Deaths Over Time');

    svg.append('text')
        .attr('transform', 'rotate(-90)')
        .attr('y', -30)
        .attr('x', -height / 2)
        .attr('text-anchor', 'middle')
        .style('font-size', '14px')
        .text('Number of Cases');

    svg.append('text')
        .attr('x', width / 2)
        .attr('y', height + 30)
        .attr('text-anchor', 'middle')
        .style('font-size', '14px')
        .text('Date');
}

// Example usage:
const covidData = [
    { Date: '2020-01-22', 'Total Cases': 0, 'Total Deaths': 0 },
    { Date: '2020-01-23', 'Total Cases': 1, 'Total Deaths': 0 },
    { Date: '2020-01-24', 'Total Cases': 2, 'Total Deaths': 0 },
    { Date: '2020-01-25', 'Total Cases': 4, 'Total Deaths': 1 },
    { Date: '2020-01-26', 'Total Cases': 8, 'Total Deaths': 1 },
    { Date: '2020-01-27', 'Total Cases': 16, 'Total Deaths': 2 },
    { Date: '2020-01-28', 'Total Cases': 32, 'Total Deaths': 3 },
    { Date: '2020-01-29', 'Total Cases': 64, 'Total Deaths': 5 },
    { Date: '2020-01-30', 'Total Cases': 128, 'Total Deaths': 8 },
    { Date: '2020-01-31', 'Total Cases': 256, 'Total Deaths': 12 },
];

createCovidChart(covidData, 'Total Cases', 'Total Deaths');
```
