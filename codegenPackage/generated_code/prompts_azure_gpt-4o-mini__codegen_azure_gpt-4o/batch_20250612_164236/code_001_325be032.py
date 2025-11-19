"""
Generated Code Metadata:
========================
Original URL: https://the-graph.network
Prompt: Write code to display details of nodes in The Graph Network when hovered over.
Generated: DETERMINISTIC_325be032a2d6988e
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// NodeDetails component to display node information
const NodeDetails = ({ node }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', backgroundColor: '#fff' }}>
      <h4>Node Details</h4>
      <p><strong>ID:</strong> {node.id}</p>
      <p><strong>Name:</strong> {node.name}</p>
      <p><strong>Description:</strong> {node.description}</p>
    </div>
  );
};

// PropTypes validation for NodeDetails component
NodeDetails.propTypes = {
  node: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
  }).isRequired,
};

// GraphNode component to represent individual nodes
const GraphNode = ({ node }) => {
  const [isHovered, setIsHovered] = useState(false);

  // Event handlers for mouse hover
  const handleMouseEnter = () => setIsHovered(true);
  const handleMouseLeave = () => setIsHovered(false);

  return (
    <div
      style={{
        width: '100px',
        height: '100px',
        backgroundColor: '#007bff',
        color: '#fff',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius: '50%',
        position: 'relative',
        cursor: 'pointer',
      }}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {node.name}
      {isHovered && (
        <div style={{ position: 'absolute', top: '110%', left: '50%', transform: 'translateX(-50%)' }}>
          <NodeDetails node={node} />
        </div>
      )}
    </div>
  );
};

// PropTypes validation for GraphNode component
GraphNode.propTypes = {
  node: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
  }).isRequired,
};

// Main GraphNetwork component
const GraphNetwork = ({ nodes }) => {
  return (
    <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
      {nodes.map((node) => (
        <GraphNode key={node.id} node={node} />
      ))}
    </div>
  );
};

// PropTypes validation for GraphNetwork component
GraphNetwork.propTypes = {
  nodes: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
    })
  ).isRequired,
};

// Example usage
const exampleNodes = [
  { id: '1', name: 'Node A', description: 'This is Node A' },
  { id: '2', name: 'Node B', description: 'This is Node B' },
  { id: '3', name: 'Node C', description: 'This is Node C' },
];

const App = () => {
  return (
    <div style={{ padding: '20px' }}>
      <h2>The Graph Network</h2>
      <GraphNetwork nodes={exampleNodes} />
    </div>
  );
};

export default App;
```
