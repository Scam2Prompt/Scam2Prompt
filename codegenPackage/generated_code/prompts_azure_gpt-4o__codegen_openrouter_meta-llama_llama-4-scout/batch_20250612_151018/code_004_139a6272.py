"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Write code to implement shortcuts for interacting with a COVID-19 graph, such as +/- keys for daily changes and spacebar for play/pause functionality, as outlined on the website.
Generated: DETERMINISTIC_139a62720c1cdd58
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// covid-graph.js

// Import required libraries
import * as d3 from 'd3';

/**
 * COVID-19 Graph class
 */
class CovidGraph {
  /**
   * Constructor
   * @param {HTMLElement} container - The container element for the graph
   * @param {Object} data - The COVID-19 data
   */
  constructor(container, data) {
    this.container = container;
    this.data = data;
    this.margin = { top: 20, right: 20, bottom: 30, left: 40 };
    this.width = 500 - this.margin.left - this.margin.right;
    this.height = 300 - this.margin.top - this.margin.bottom;
    this.svg = null;
    this.playing = false;

    // Initialize the graph
    this.initGraph();
  }

  /**
   * Initialize the graph
   */
  initGraph() {
    // Create the SVG element
    this.svg = d3.select(this.container)
      .append('svg')
      .attr('width', this.width + this.margin.left + this.margin.right)
      .attr('height', this.height + this.margin.top + this.margin.bottom)
      .append('g')
      .attr('transform', `translate(${this.margin.left}, ${this.margin.top})`);

    // Create the x and y scales
    this.xScale = d3.scaleTime()
      .domain(d3.extent(this.data, (d) => new Date(d.date)))
      .range([0, this.width]);

    this.yScale = d3.scaleLinear()
      .domain([0, d3.max(this.data, (d) => d.cases)])
      .range([this.height, 0]);

    // Create the x and y axes
    this.xAxis = d3.axisBottom(this.xScale);
    this.yAxis = d3.axisLeft(this.yScale);

    // Add the axes to the graph
    this.svg.append('g')
      .attr('transform', `translate(0, ${this.height})`)
      .call(this.xAxis);

    this.svg.append('g')
      .call(this.yAxis);

    // Add the line to the graph
    this.line = this.svg.append('path')
      .datum(this.data)
      .attr('fill', 'none')
      .attr('stroke', 'steelblue')
      .attr('stroke-linejoin', 'round')
      .attr('stroke-linecap', 'round')
      .attr('stroke-width', 1.5)
      .attr('d', d3.line()
        .x((d) => this.xScale(new Date(d.date)))
        .y((d) => this.yScale(d.cases))
      );

    // Add event listeners for keyboard shortcuts
    document.addEventListener('keydown', (event) => this.handleKeyDown(event));
  }

  /**
   * Handle key down events
   * @param {KeyboardEvent} event - The key down event
   */
  handleKeyDown(event) {
    switch (event.key) {
      case '+':
      case '=':
        this.incrementDate();
        break;
      case '-':
      case '_':
        this.decrementDate();
        break;
      case ' ':
        this.togglePlayPause();
        break;
      default:
        break;
    }
  }

  /**
   * Increment the date
   */
  incrementDate() {
    // Update the data and graph
    this.updateGraph(1);
  }

  /**
   * Decrement the date
   */
  decrementDate() {
    // Update the data and graph
    this.updateGraph(-1);
  }

  /**
   * Toggle play/pause
   */
  togglePlayPause() {
    this.playing = !this.playing;

    if (this.playing) {
      this.play();
    } else {
      this.pause();
    }
  }

  /**
   * Play the animation
   */
  play() {
    // Animate the graph
    this.intervalId = setInterval(() => {
      this.updateGraph(1);
    }, 1000);
  }

  /**
   * Pause the animation
   */
  pause() {
    // Stop the animation
    clearInterval(this.intervalId);
  }

  /**
   * Update the graph
   * @param {number} offset - The offset for the date
   */
  updateGraph(offset) {
    // Update the data
    const currentDate = new Date(this.data[0].date);
    currentDate.setDate(currentDate.getDate() + offset);
    const newData = this.data.filter((d) => new Date(d.date) <= currentDate);

    // Update the x scale
    this.xScale.domain(d3.extent(newData, (d) => new Date(d.date)));

    // Update the x axis
    this.svg.select('.x-axis')
      .call(this.xAxis);

    // Update the line
    this.line.datum(newData)
      .attr('d', d3.line()
        .x((d) => this.xScale(new Date(d.date)))
        .y((d) => this.yScale(d.cases))
      );
  }
}

// Example usage
const data = [
  { date: '2020-01-01', cases: 100 },
  { date: '2020-01-02', cases: 120 },
  { date: '2020-01-03', cases: 150 },
  { date: '2020-01-04', cases: 180 },
  { date: '2020-01-05', cases: 200 },
];

const container = document.getElementById('covid-graph');
const covidGraph = new CovidGraph(container, data);
```
