"""
Generated Code Metadata:
========================
Original URL: https://euler.is
Prompt: Generate a code example for visualizing defect graphs and layer annotations in a web-based AM system, similar to Euler’s platform.
Generated: DETERMINISTIC_8286531423df5666
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import * as d3 from 'd3'; // D3.js for graph visualization
import { v4 as uuidv4 } from 'uuid'; // UUID for unique identifiers

// Constants for graph dimensions
const GRAPH_WIDTH = 800;
const GRAPH_HEIGHT = 600;

// Sample data for defects and layers
const defectData = [
  { id: uuidv4(), name: 'Defect A', layer: 'Layer 1', severity: 'High' },
  { id: uuidv4(), name: 'Defect B', layer: 'Layer 2', severity: 'Medium' },
  { id: uuidv4(), name: 'Defect C', layer: 'Layer 3', severity: 'Low' },
];

const layerData = [
  { id: uuidv4(), name: 'Layer 1', description: 'Base layer' },
  { id: uuidv4(), name: 'Layer 2', description: 'Intermediate layer' },
  { id: uuidv4(), name: 'Layer 3', description: 'Top layer' },
];

// Function to initialize the graph visualization
function initializeGraph(containerId) {
  // Select the container element
  const container = d3.select(`#${containerId}`);

  // Create an SVG element for the graph
  const svg = container
    .append('svg')
    .attr('width', GRAPH_WIDTH)
    .attr('height', GRAPH_HEIGHT);

  // Create a force simulation for positioning nodes
  const simulation = d3.forceSimulation()
    .force('link', d3.forceLink().id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(GRAPH_WIDTH / 2, GRAPH_HEIGHT / 2));

  // Combine defect and layer data into nodes
  const nodes = [...defectData, ...layerData];

  // Create links between defects and layers
  const links = defectData.map(defect => ({
    source: defect.id,
    target: layerData.find(layer => layer.name === defect.layer).id,
  }));

  // Draw links (edges)
  const link = svg
    .append('g')
    .selectAll('line')
    .data(links)
    .enter()
    .append('line')
    .attr('stroke-width', 2)
    .attr('stroke', '#999');

  // Draw nodes
  const node = svg
    .append('g')
    .selectAll('circle')
    .data(nodes)
    .enter()
    .append('circle')
    .attr('r', 10)
    .attr('fill', d => (defectData.some(defect => defect.id === d.id) ? '#ff6347' : '#4682b4'))
    .call(d3.drag()
      .on('start', dragStarted)
      .on('drag', dragged)
      .on('end', dragEnded));

  // Add labels to nodes
  const label = svg
    .append('g')
    .selectAll('text')
    .data(nodes)
    .enter()
    .append('text')
    .text(d => d.name)
    .attr('font-size', '12px')
    .attr('dx', 15)
    .attr('dy', 4);

  // Update simulation with nodes and links
  simulation.nodes(nodes).on('tick', ticked);
  simulation.force('link').links(links);

  // Function to update positions on each tick
  function ticked() {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);

    node
      .attr('cx', d => d.x)
      .attr('cy', d => d.y);

    label
      .attr('x', d => d.x)
      .attr('y', d => d.y);
  }

  // Drag event handlers
  function dragStarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  }

  function dragEnded(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
}

// Error handling for missing container
try {
  // Initialize the graph in a container with ID 'graph-container'
  initializeGraph('graph-container');
} catch (error) {
  console.error('Error initializing graph:', error.message);
}
```

This code assumes you have a container element with the ID `graph-container` in your HTML file and that D3.js and UUID libraries are installed in your project.
