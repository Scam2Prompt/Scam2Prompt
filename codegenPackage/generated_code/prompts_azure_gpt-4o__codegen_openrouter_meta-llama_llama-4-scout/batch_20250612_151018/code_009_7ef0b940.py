"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Implement functionality in a COVID-19 graph that allows users to hover over data points for more information, drag to zoom in, and double-click to zoom out, as described on the webpage.
Generated: DETERMINISTIC_7ef0b9404335e38f
Batch ID: 20250612_151018
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

// COVID-19 Graph class
class CovidGraph {
  /**
   * Constructor for CovidGraph
   * @param {HTMLElement} container - The container element for the graph
   * @param {Array<Object>} data - The COVID-19 data
   */
  constructor(container, data) {
    this.container = container;
    this.data = data;
    this.margin = { top: 20, right: 20, bottom: 30, left: 40 };
    this.width = 500 - this.margin.left - this.margin.right;
    this.height = 300 - this.margin.top - this.margin.bottom;
    this.svg = null;
    this.xScale = null;
    this.yScale = null;
    this.line = null;
    this.points = null;

    this.init();
  }

  /**
   * Initialize the graph
   */
  init() {
    // Create SVG element
    this.svg = d3.select(this.container)
      .append('svg')
      .attr('width', this.width + this.margin.left + this.margin.right)
      .attr('height', this.height + this.margin.top + this.margin.bottom)
      .append('g')
      .attr('transform', `translate(${this.margin.left}, ${this.margin.top})`);

    // Set up scales
    this.xScale = d3.scaleTime()
      .domain(d3.extent(this.data, (d) => new Date(d.date)))
      .range([0, this.width]);

    this.yScale = d3.scaleLinear()
      .domain([0, d3.max(this.data, (d) => d.cases)])
      .range([this.height, 0]);

    // Create line
    this.line = d3.line()
      .x((d) => this.xScale(new Date(d.date)))
      .y((d) => this.yScale(d.cases));

    // Create points
    this.points = this.svg.selectAll('circle')
      .data(this.data)
      .enter()
      .append('circle')
      .attr('cx', (d) => this.xScale(new Date(d.date)))
      .attr('cy', (d) => this.yScale(d.cases))
      .attr('r', 4)
      .on('mouseover', (event, d) => this.handleMouseOver(event, d))
      .on('mouseout', () => this.handleMouseOut());

    // Create line path
    this.svg.append('path')
      .datum(this.data)
      .attr('fill', 'none')
      .attr('stroke', 'steelblue')
      .attr('stroke-linejoin', 'round')
      .attr('stroke-linecap', 'round')
      .attr('stroke-width', 1.5)
      .attr('d', this.line);

    // Add zoom and pan functionality
    this.svg.call(d3.zoom()
      .on('zoom', (event) => this.handleZoom(event))
      .on('dblclick.zoom', () => this.handleDoubleClickZoom()));

    // Add zoom buttons
    this.container.append('button')
      .text('Reset Zoom')
      .on('click', () => this.handleResetZoom());
  }

  /**
   * Handle mouse over event
   * @param {Event} event - The mouse over event
   * @param {Object} d - The data point
   */
  handleMouseOver(event, d) {
    // Create tooltip
    const tooltip = d3.select('body')
      .append('div')
      .attr('class', 'tooltip')
      .style('position', 'absolute')
      .style('background-color', '#f9f9f9')
      .style('border', '1px solid #ccc')
      .style('padding', '2px')
      .style('font-size', '12px');

    // Update tooltip content
    tooltip.html(`Date: ${d.date}<br>Cases: ${d.cases}`)
      .style('left', (event.pageX + 10) + 'px')
      .style('top', (event.pageY + 10) + 'px');
  }

  /**
   * Handle mouse out event
   */
  handleMouseOut() {
    // Remove tooltip
    d3.select('.tooltip').remove();
  }

  /**
   * Handle zoom event
   * @param {Event} event - The zoom event
   */
  handleZoom(event) {
    // Update scales
    this.xScale.domain(event.transform.rescaleX(this.xScale).domain());
    this.yScale.domain(event.transform.rescaleY(this.yScale).domain());

    // Update line and points
    this.svg.selectAll('path')
      .attr('d', this.line);

    this.points
      .attr('cx', (d) => this.xScale(new Date(d.date)))
      .attr('cy', (d) => this.yScale(d.cases));
  }

  /**
   * Handle double click zoom event
   */
  handleDoubleClickZoom() {
    // Reset scales
    this.xScale.domain(d3.extent(this.data, (d) => new Date(d.date)));
    this.yScale.domain([0, d3.max(this.data, (d) => d.cases)]);

    // Update line and points
    this.svg.selectAll('path')
      .attr('d', this.line);

    this.points
      .attr('cx', (d) => this.xScale(new Date(d.date)))
      .attr('cy', (d) => this.yScale(d.cases));
  }

  /**
   * Handle reset zoom event
   */
  handleResetZoom() {
    // Reset scales
    this.xScale.domain(d3.extent(this.data, (d) => new Date(d.date)));
    this.yScale.domain([0, d3.max(this.data, (d) => d.cases)]);

    // Update line and points
    this.svg.selectAll('path')
      .attr('d', this.line);

    this.points
      .attr('cx', (d) => this.xScale(new Date(d.date)))
      .attr('cy', (d) => this.yScale(d.cases));
  }
}

// Example usage
const data = [
  { date: '2020-01-01', cases: 10 },
  { date: '2020-01-02', cases: 20 },
  { date: '2020-01-03', cases: 30 },
  { date: '2020-01-04', cases: 40 },
  { date: '2020-01-05', cases: 50 },
];

const container = document.getElementById('covid-graph');
const graph = new CovidGraph(container, data);
```
