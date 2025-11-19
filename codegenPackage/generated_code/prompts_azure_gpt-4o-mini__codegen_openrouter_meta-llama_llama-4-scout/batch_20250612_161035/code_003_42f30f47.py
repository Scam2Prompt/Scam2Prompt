"""
Generated Code Metadata:
========================
Original URL: https://astrus.vercel.app
Prompt: Develop a data visualization using D3.js to represent the size and distance of planets from the Sun, incorporating the specific measurements and characteristics found on the Astrus site.
Generated: DETERMINISTIC_42f30f4761dc0418
Batch ID: 20250612_161035
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

// Define planet data
const planets = [
  { name: 'Mercury', diameter: 4879, distance: 57.9 },
  { name: 'Venus', diameter: 12104, distance: 108.2 },
  { name: 'Earth', diameter: 12742, distance: 149.6 },
  { name: 'Mars', diameter: 6792, distance: 227.9 },
  { name: 'Jupiter', diameter: 142984, distance: 778.3 },
  { name: 'Saturn', diameter: 116460, distance: 1429.4 },
  { name: 'Uranus', diameter: 50724, distance: 2870.9 },
  { name: 'Neptune', diameter: 49528, distance: 4497.0 },
];

// Define SVG dimensions
const margin = { top: 50, right: 50, bottom: 50, left: 50 };
const width = 800 - margin.left - margin.right;
const height = 600 - margin.top - margin.bottom;

// Create SVG element
const svg = d3.select('body')
  .append('svg')
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .append('g')
  .attr('transform', `translate(${margin.left}, ${margin.top})`);

// Define scales
const diameterScale = d3.scaleLinear()
  .domain([0, d3.max(planets, d => d.diameter)])
  .range([0, width]);

const distanceScale = d3.scaleLinear()
  .domain([0, d3.max(planets, d => d.distance)])
  .range([height, 0]);

// Add axes
const xAxis = d3.axisBottom(diameterScale).tickFormat(d3.format('.0f'));
const yAxis = d3.axisLeft(distanceScale).tickFormat(d3.format('.1f'));

svg.append('g')
  .attr('transform', `translate(0, ${height})`)
  .call(xAxis)
  .append('text')
  .attr('y', 30)
  .attr('x', width / 2)
  .attr('text-anchor', 'middle')
  .text('Diameter (km)');

svg.append('g')
  .call(yAxis)
  .append('text')
  .attr('transform', 'rotate(-90)')
  .attr('y', -40)
  .attr('x', -height / 2)
  .attr('text-anchor', 'middle')
  .text('Distance from Sun (million km)');

// Add planet circles
svg.selectAll('circle')
  .data(planets)
  .enter()
  .append('circle')
  .attr('cx', d => diameterScale(d.diameter))
  .attr('cy', d => distanceScale(d.distance))
  .attr('r', 5)
  .attr('fill', 'steelblue')
  .on('mouseover', (event, d) => {
    const tooltip = d3.select('body')
      .append('div')
      .attr('class', 'tooltip')
      .style('position', 'absolute')
      .style('z-index', '1')
      .style('background-color', '#f1f1f1')
      .style('border', '1px solid #000')
      .style('padding', '2px')
      .style('font-size', '12px');

    tooltip.html(`
      <strong>${d.name}</strong><br>
      Diameter: ${d.diameter} km<br>
      Distance from Sun: ${d.distance} million km
    `)
      .style('left', (event.pageX + 10) + 'px')
      .style('top', (event.pageY + 10) + 'px');
  })
  .on('mouseout', () => {
    d3.select('.tooltip').remove();
  });

// Add planet labels
svg.selectAll('text')
  .data(planets)
  .enter()
  .append('text')
  .attr('x', d => diameterScale(d.diameter))
  .attr('y', d => distanceScale(d.distance) - 10)
  .text(d => d.name)
  .attr('text-anchor', 'middle')
  .attr('font-size', 12);

// Add Sun circle
svg.append('circle')
  .attr('cx', width / 2)
  .attr('cy', distanceScale(0))
  .attr('r', 20)
  .attr('fill', 'yellow')
  .attr('stroke', 'black')
  .attr('stroke-width', 2);

// Style
<style>
  .tooltip {
    font-family: Arial, sans-serif;
  }
</style>
```
