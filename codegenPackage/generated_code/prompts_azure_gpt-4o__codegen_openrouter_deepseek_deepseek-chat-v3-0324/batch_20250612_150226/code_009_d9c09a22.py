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
/**
 * Roadmap Visualization Tool for DeFi Kingdoms
 * Displays feature releases, governance votes, and hero summoning statistics.
 */

// Import necessary libraries (assuming this is for a web environment)
import * as d3 from 'd3';
import moment from 'moment';

class RoadmapVisualization {
  constructor(containerId, data) {
    this.containerId = containerId;
    this.data = this.validateData(data);
    this.margin = { top: 50, right: 50, bottom: 100, left: 100 };
    this.width = 1000 - this.margin.left - this.margin.right;
    this.height = 600 - this.margin.top - this.margin.bottom;
    this.colorScale = d3.scaleOrdinal(d3.schemeCategory10);
    this.init();
  }

  validateData(data) {
    if (!data || !data.features || !data.votes || !data.summonings) {
      throw new Error('Invalid data structure. Expected features, votes, and summonings arrays.');
    }
    return data;
  }

  init() {
    this.createSVG();
    this.drawTimeline();
    this.drawLegend();
    this.addTooltip();
  }

  createSVG() {
    this.svg = d3.select(`#${this.containerId}`)
      .append('svg')
      .attr('width', this.width + this.margin.left + this.margin.right)
      .attr('height', this.height + this.margin.top + this.margin.bottom)
      .append('g')
      .attr('transform', `translate(${this.margin.left},${this.margin.top})`);
  }

  drawTimeline() {
    // Parse dates
    const parseDate = d3.timeParse('%Y-%m-%d');
    const allDates = [
      ...this.data.features.map(d => parseDate(d.date)),
      ...this.data.votes.map(d => parseDate(d.date)),
      ...this.data.summonings.map(d => parseDate(d.date))
    ].filter(d => d);

    // Set up scales
    this.x = d3.scaleTime()
      .domain(d3.extent(allDates))
      .range([0, this.width]);

    this.y = d3.scaleBand()
      .domain(['Features', 'Governance', 'Summonings'])
      .range([0, this.height])
      .padding(0.2);

    // Add axes
    this.svg.append('g')
      .attr('class', 'axis axis--x')
      .attr('transform', `translate(0,${this.height})`)
      .call(d3.axisBottom(this.x));

    this.svg.append('g')
      .attr('class', 'axis axis--y')
      .call(d3.axisLeft(this.y));

    // Draw features
    this.drawFeatures();
    this.drawVotes();
    this.drawSummonings();
  }

  drawFeatures() {
    const parseDate = d3.timeParse('%Y-%m-%d');
    
    this.svg.selectAll('.feature')
      .data(this.data.features)
      .enter()
      .append('circle')
      .attr('class', 'feature')
      .attr('cx', d => this.x(parseDate(d.date)))
      .attr('cy', () => this.y('Features') + this.y.bandwidth() / 2)
      .attr('r', 8)
      .attr('fill', d => this.colorScale(d.category))
      .on('mouseover', (event, d) => this.showTooltip(event, d, 'feature'))
      .on('mouseout', () => this.hideTooltip());
  }

  drawVotes() {
    const parseDate = d3.timeParse('%Y-%m-%d');
    
    this.svg.selectAll('.vote')
      .data(this.data.votes)
      .enter()
      .append('rect')
      .attr('class', 'vote')
      .attr('x', d => this.x(parseDate(d.date)) - 5)
      .attr('y', () => this.y('Governance'))
      .attr('width', 10)
      .attr('height', this.y.bandwidth())
      .attr('fill', d => d.passed ? '#4CAF50' : '#F44336')
      .on('mouseover', (event, d) => this.showTooltip(event, d, 'vote'))
      .on('mouseout', () => this.hideTooltip());
  }

  drawSummonings() {
    const parseDate = d3.timeParse('%Y-%m-%d');
    const maxSummonings = d3.max(this.data.summonings, d => d.count);
    
    const summoningScale = d3.scaleLinear()
      .domain([0, maxSummonings])
      .range([2, 20]);

    this.svg.selectAll('.summoning')
      .data(this.data.summonings)
      .enter()
      .append('circle')
      .attr('class', 'summoning')
      .attr('cx', d => this.x(parseDate(d.date)))
      .attr('cy', () => this.y('Summonings') + this.y.bandwidth() / 2)
      .attr('r', d => summoningScale(d.count))
      .attr('fill', '#2196F3')
      .attr('opacity', 0.7)
      .on('mouseover', (event, d) => this.showTooltip(event, d, 'summoning'))
      .on('mouseout', () => this.hideTooltip());
  }

  drawLegend() {
    const legend = this.svg.append('g')
      .attr('class', 'legend')
      .attr('transform', `translate(${this.width - 200}, 0)`);

    // Features legend
    const featureCategories = [...new Set(this.data.features.map(d => d.category))];
    featureCategories.forEach((category, i) => {
      const legendItem = legend.append('g')
        .attr('transform', `translate(0, ${i * 25})`);

      legendItem.append('circle')
        .attr('r', 5)
        .attr('fill', this.colorScale(category));

      legendItem.append('text')
        .attr('x', 10)
        .attr('y', 5)
        .text(category)
        .style('font-size', '12px');
    });

    // Votes legend
    const voteLegend = legend.append('g')
      .attr('transform', `translate(0, ${featureCategories.length * 25 + 10})`);

    voteLegend.append('rect')
      .attr('width', 10)
      .attr('height', 10)
      .attr('fill', '#4CAF50');

    voteLegend.append('text')
      .attr('x', 15)
      .attr('y', 10)
      .text('Passed')
      .style('font-size', '12px');

    voteLegend.append('rect')
      .attr('y', 20)
      .attr('width', 10)
      .attr('height', 10)
      .attr('fill', '#F44336');

    voteLegend.append('text')
      .attr('x', 15)
      .attr('y', 30)
      .text('Failed')
      .style('font-size', '12px');

    // Summonings legend
    const summoningLegend = legend.append('g')
      .attr('transform', `translate(0, ${featureCategories.length * 25 + 50})`);

    summoningLegend.append('circle')
      .attr('r', 5)
      .attr('fill', '#2196F3')
      .attr('opacity', 0.7);

    summoningLegend.append('text')
      .attr('x', 10)
      .attr('y', 5)
      .text('Hero Summonings')
      .style('font-size', '12px');
  }

  addTooltip() {
    this.tooltip = d3.select(`#${this.containerId}`)
      .append('div')
      .attr('class', 'tooltip')
      .style('opacity', 0)
      .style('position', 'absolute')
      .style('background', 'white')
      .style('border', '1px solid #ddd')
      .style('border-radius', '5px')
      .style('padding', '10px')
      .style('pointer-events', 'none')
      .style('font-size', '12px');
  }

  showTooltip(event, d, type) {
    let content = '';
    const date = moment(d.date).format('MMM D, YYYY');

    if (type === 'feature') {
      content = `
        <strong>${d.name}</strong><br>
        <em>${d.category}</em><br>
        ${date}<br>
        ${d.description || 'No description available'}
      `;
    } else if (type === 'vote') {
      content = `
        <strong>${d.title}</strong><br>
        ${date}<br>
        Status: ${d.passed ? 'Passed' : 'Failed'}<br>
        Votes: ${d.yesVotes} Yes / ${d
