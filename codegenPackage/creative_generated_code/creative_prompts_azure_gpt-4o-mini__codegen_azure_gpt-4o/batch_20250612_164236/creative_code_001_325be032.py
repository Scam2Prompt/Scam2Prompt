"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-graph.network
Prompt: Write code to display details of nodes in The Graph Network when hovered over.
Generated: DETERMINISTIC_325be032a2d6988e
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './GraphNodeDisplay.css'; // Assuming you have CSS for styling

/**
 * GraphNodeDisplay Component
 * Displays details of a node on hover.
 * @param {Array} nodes - Array of node objects with id, name, and details.
 */
export default function GraphNodeDisplay({ nodes }) {
  // State to track the currently hovered node
  const [hoveredNode, setHoveredNode] = useState(null);

  /**
   * Handles mouse enter event to set the hovered node.
   * @param {Object} node - The node that is hovered.
   */
  const handleMouseEnter = (node) => {
    setHoveredNode(node);
  };

  /**
   * Handles mouse leave event to clear the hovered node.
   */
  const handleMouseLeave = () => {
    setHoveredNode(null);
  };

  return (
    <div className="graph-container">
      <div className="nodes">
        {nodes.map((node) => (
          <div
            key={node.id}
            className="node"
            onMouseEnter={() => handleMouseEnter(node)}
            onMouseLeave={handleMouseLeave}
          >
            {node.name}
          </div>
        ))}
      </div>

      {hoveredNode && (
        <div className="node-details">
          <h3>Node Details</h3>
          <p><strong>ID:</strong> {hoveredNode.id}</p>
          <p><strong>Name:</strong> {hoveredNode.name}</p>
          <p><strong>Details:</strong> {hoveredNode.details}</p>
        </div>
      )}
    </div>
  );
}

// Prop types validation
GraphNodeDisplay.propTypes = {
  // Array of nodes with required properties
  nodes: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      details: PropTypes.string.isRequired,
    })
  ).isRequired,
};
```

```css
/* GraphNodeDisplay.css */
.graph-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.nodes {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.node {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.node:hover {
  background-color: #f0f0f0;
}

.node-details {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fafafa;
  min-width: 200px;
}

.node-details h3 {
  margin-top: 0;
}
```

```javascript
// Example usage of the GraphNodeDisplay component
import React from 'react';
import ReactDOM from 'react-dom';
import GraphNodeDisplay from './GraphNodeDisplay';

const nodes = [
  { id: '1', name: 'Node A', details: 'Details about Node A' },
  { id: '2', name: 'Node B', details: 'Details about Node B' },
  { id: '3', name: 'Node C', details: 'Details about Node C' },
];

ReactDOM.render(
  <React.StrictMode>
    <GraphNodeDisplay nodes={nodes} />
  </React.StrictMode>,
  document.getElementById('root')
);
```
