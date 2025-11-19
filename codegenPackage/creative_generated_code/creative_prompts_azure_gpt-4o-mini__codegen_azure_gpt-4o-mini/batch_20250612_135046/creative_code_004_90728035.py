"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseal.ch
Prompt: Explain how to implement network visualization features from Openseal.ch in a web application.
Generated: DETERMINISTIC_9072803573c957b3
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { forceSimulation, forceManyBody, forceLink, forceCenter } from 'd3-force';

// Define the NetworkVisualization component
const NetworkVisualization = ({ data }) => {
    const svgRef = useRef();

    useEffect(() => {
        // Check if data is provided
        if (!data || !data.nodes || !data.links) {
            console.error("Invalid data: Expected { nodes: [...], links: [...] }");
            return;
        }

        // Set dimensions for the SVG canvas
        const width = 800;
        const height = 600;

        // Create the SVG canvas
        const svg = d3.select(svgRef.current)
            .attr("width", width)
            .attr("height", height);

        // Create the simulation
        const simulation = forceSimulation(data.nodes)
            .force("link", forceLink().id(d => d.id).distance(100))
            .force("charge", forceManyBody().strength(-300))
            .force("center", forceCenter(width / 2, height / 2));

        // Create links (edges)
        const link = svg.selectAll(".link")
            .data(data.links)
            .enter().append("line")
            .attr("class", "link")
            .attr("stroke", "#999")
            .attr("stroke-opacity", 0.6)
            .attr("stroke-width", 1);

        // Create nodes (vertices)
        const node = svg.selectAll(".node")
            .data(data.nodes)
            .enter().append("g")
            .attr("class", "node")
            .call(d3.drag()
                .on("start", dragStarted)
                .on("drag", dragged)
                .on("end", dragEnded));

        // Append circles to nodes
        node.append("circle")
            .attr("r", 5)
            .attr("fill", "#69b3a2");

        // Append labels to nodes
        node.append("text")
            .attr("dy", 3)
            .attr("x", 6)
            .text(d => d.id);

        // Update positions on each tick of the simulation
        simulation.on("tick", () => {
            link.attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            node.attr("transform", d => `translate(${d.x},${d.y})`);
        });

        // Handle drag events
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

        // Cleanup on component unmount
        return () => {
            svg.selectAll("*").remove();
        };
    }, [data]);

    // Render the SVG element
    return <svg ref={svgRef}></svg>;
};

// Example usage of the NetworkVisualization component
const App = () => {
    const data = {
        nodes: [{ id: "1" }, { id: "2" }, { id: "3" }],
        links: [{ source: "1", target: "2" }, { source: "2", target: "3" }]
    };

    return (
        <div>
            <h1>Network Visualization</h1>
            <NetworkVisualization data={data} />
        </div>
    );
};

export default App;
```
