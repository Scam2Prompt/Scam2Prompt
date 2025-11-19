"""
Generated Code Metadata:
========================
Original URL: https://the-graph.network
Prompt: Create a simple node visualization for a delegator, curator, or indexer in The Graph Network using a JavaScript library like D3.js or Sigma.js.
Generated: DETERMINISTIC_9024dca06fb994de
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import D3.js library
import * as d3 from 'd3';

// Configuration for the visualization
const config = {
  width: 800, // Width of the SVG canvas
  height: 600, // Height of the SVG canvas
  nodeRadius: 20, // Radius of each node
  colors: {
    delegator: '#1f77b4', // Blue for delegators
    curator: '#ff7f0e', // Orange for curators
    indexer: '#2ca02c', // Green for indexers
  },
};

// Sample data for nodes and links
const graphData = {
  nodes: [
    { id: 'Delegator1', type: 'delegator' },
    { id: 'Curator1', type: 'curator' },
    { id: 'Indexer1', type: 'indexer' },
    { id: 'Delegator2', type: 'delegator' },
  ],
  links: [
    { source: 'Delegator1', target: 'Curator1' },
    { source: 'Curator1', target: 'Indexer1' },
    { source: 'Delegator2', target: 'Indexer1' },
  ],
};

// Create the SVG canvas
const svg = d3
  .select('body') // Append to the body of the HTML document
  .append('svg')
  .attr('width', config.width)
  .attr('height', config.height);

// Create a simulation for the force layout
const simulation = d3
  .forceSimulation(graphData.nodes)
  .force(
    'link',
    d3.forceLink(graphData.links).id((d) => d.id).distance(150) // Links with a fixed distance
  )
  .force('charge', d3.forceManyBody().strength(-300)) // Repulsion between nodes
  .force('center', d3.forceCenter(config.width / 2, config.height / 2)); // Center the graph

// Draw the links (edges)
const link = svg
  .selectAll('line')
  .data(graphData.links)
  .enter()
  .append('line')
  .attr('stroke', '#999') // Gray color for links
  .attr('stroke-width', 2); // Thickness of links

// Draw the nodes
const node = svg
  .selectAll('circle')
  .data(graphData.nodes)
  .enter()
  .append('circle')
  .attr('r', config.nodeRadius) // Radius of the node
  .attr('fill', (d) => config.colors[d.type]) // Color based on node type
  .call(
    d3
      .drag() // Enable dragging of nodes
      .on('start', (event, d) => {
        if (!event.active) simulation.alphaTarget(0.3).restart(); // Activate simulation
        d.fx = d.x; // Fix x position
        d.fy = d.y; // Fix y position
      })
      .on('drag', (event, d) => {
        d.fx = event.x; // Update x position
        d.fy = event.y; // Update y position
      })
      .on('end', (event, d) => {
        if (!event.active) simulation.alphaTarget(0); // Deactivate simulation
        d.fx = null; // Release x position
        d.fy = null; // Release y position
      })
  );

// Add labels to nodes
const labels = svg
  .selectAll('text')
  .data(graphData.nodes)
  .enter()
  .append('text')
  .text((d) => d.id) // Display node ID
  .attr('font-size', '12px') // Font size for labels
  .attr('text-anchor', 'middle') // Center the text
  .attr('dy', 4); // Adjust vertical alignment

// Update positions on each tick of the simulation
simulation.on('tick', () => {
  link
    .attr('x1', (d) => d.source.x)
    .attr('y1', (d) => d.source.y)
    .attr('x2', (d) => d.target.x)
    .attr('y2', (d) => d.target.y);

  node.attr('cx', (d) => d.x).attr('cy', (d) => d.y);

  labels.attr('x', (d) => d.x).attr('y', (d) => d.y);
});

// Error handling: Ensure the graphData is valid
if (!graphData.nodes || !graphData.links) {
  console.error('Invalid graph data: nodes and links are required.');
}
```

This code creates a simple node visualization using D3.js for delegators, curators, and indexers in The Graph Network. It includes nodes, links, labels, and drag functionality, and follows best practices for clean, production-ready code.
