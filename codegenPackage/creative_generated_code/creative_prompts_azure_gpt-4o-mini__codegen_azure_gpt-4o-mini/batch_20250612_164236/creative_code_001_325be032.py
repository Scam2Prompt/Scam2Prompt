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
import React, { useState, useEffect } from 'react';
import { Graph } from 'react-d3-graph'; // Third-party library for graph visualization

// Define the GraphComponent
const GraphComponent = ({ data }) => {
  const [hoveredNode, setHoveredNode] = useState(null);

  // Configuration for the graph
  const graphConfig = {
    node: {
      color: 'lightblue',
      size: 600,
      highlightColor: 'lightgreen',
      highlightStrokeColor: 'black',
    },
    link: {
      highlightColor: 'lightblue',
    },
  };

  // Function to handle mouse over event
  const onNodeHover = (nodeId) => {
    setHoveredNode(nodeId);
  };

  // Function to handle mouse out event
  const onNodeOut = () => {
    setHoveredNode(null);
  };

  // Render the graph with hover capabilities
  return (
    <div>
      <Graph
        id="graph-id"
        data={data}
        config={graphConfig}
        onNodeMouseOver={onNodeHover}
        onNodeMouseOut={onNodeOut}
      />
      {hoveredNode && (
        <div className="tooltip">
          <h3>Node Details</h3>
          <p>{`Node ID: ${hoveredNode}`}</p>
          {/* You can extend this section to show more details as needed */}
        </div>
      )}
    </div>
  );
};

// Sample data structure for the graph
const sampleData = {
  nodes: [
    { id: '1' },
    { id: '2' },
    { id: '3' },
  ],
  links: [
    { source: '1', target: '2' },
    { source: '2', target: '3' },
  ],
};

// Main App component
const App = () => {
  // Using effect to simulate a data fetch
  useEffect(() => {
    // Simulated API call
    const fetchData = async () => {
      try {
        // In a real app, you would fetch data from an API
        // const response = await fetch('API_URL');
        // const data = await response.json();
        // setData(data);
        console.log("Fetched data successfully");
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>The Graph Network</h1>
      <GraphComponent data={sampleData} />
    </div>
  );
};

// Export the App component
export default App;
```
