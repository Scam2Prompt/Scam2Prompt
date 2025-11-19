"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: "Write a JavaScript code to visualize data from a motion capture system, similar to Olaf Schirm's 'Motion Capture' project, using a library like D3.js."
Generated: DETERMINISTIC_804b468ade98b36a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import * as d3 from 'd3';
import { motionCaptureData } from './motionCaptureData'; // Sample data

// Set up SVG dimensions
const margin = { top: 20, right: 20, bottom: 30, left: 40 };
const width = 800 - margin.left - margin.right;
const height = 600 - margin.top - margin.bottom;

// Create SVG element
const svg = d3.select('body')
  .append('svg')
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .append('g')
  .attr('transform', `translate(${margin.left}, ${margin.top})`);

// Load and visualize motion capture data
function visualizeMotionCaptureData(data) {
  // Check if data is valid
  if (!data || !data.skeletons) {
    throw new Error('Invalid motion capture data');
  }

  // Extract skeleton data
  const skeletons = data.skeletons;

  // Define joint connections
  const jointConnections = [
    { source: 'Hips', target: 'Spine' },
    { source: 'Spine', target: 'Spine1' },
    { source: 'Spine1', target: 'Spine2' },
    { source: 'Spine2', target: 'Neck' },
    { source: 'Neck', target: 'Head' },
    { source: 'Hips', target: 'LeftUpLeg' },
    { source: 'LeftUpLeg', target: 'LeftLeg' },
    { source: 'LeftLeg', target: 'LeftFoot' },
    { source: 'Hips', target: 'RightUpLeg' },
    { source: 'RightUpLeg', target: 'RightLeg' },
    { source: 'RightLeg', target: 'RightFoot' },
  ];

  // Create joint scales
  const xScale = d3.scaleLinear()
    .domain(d3.extent(data.frameTimes))
    .range([0, width]);

  const yScale = d3.scaleLinear()
    .domain([0, 100]) // Assume joint positions are within 0-100 range
    .range([height, 0]);

  // Draw joint connections
  svg.selectAll('line')
    .data(jointConnections)
    .enter()
    .append('line')
    .attr('x1', (d) => xScale(data.frameTimes[0]) + skeletons[0].joints[d.source].x)
    .attr('y1', (d) => yScale(skeletons[0].joints[d.source].y))
    .attr('x2', (d) => xScale(data.frameTimes[0]) + skeletons[0].joints[d.target].x)
    .attr('y2', (d) => yScale(skeletons[0].joints[d.target].y))
    .attr('stroke', 'black')
    .attr('stroke-width', 2);

  // Draw joints
  svg.selectAll('circle')
    .data(skeletons[0].joints)
    .enter()
    .append('circle')
    .attr('cx', (d) => xScale(data.frameTimes[0]) + d.x)
    .attr('cy', (d) => yScale(d.y))
    .attr('r', 5)
    .attr('fill', 'black');

  // Animate joints over time
  const frameTimes = data.frameTimes;
  const numFrames = frameTimes.length;
  let currentFrame = 0;

  function animate() {
    if (currentFrame >= numFrames) {
      currentFrame = 0;
    }

    const currentSkeleton = skeletons[currentFrame];

    // Update joint connections
    svg.selectAll('line')
      .data(jointConnections)
      .attr('x1', (d) => xScale(frameTimes[currentFrame]) + currentSkeleton.joints[d.source].x)
      .attr('y1', (d) => yScale(currentSkeleton.joints[d.source].y))
      .attr('x2', (d) => xScale(frameTimes[currentFrame]) + currentSkeleton.joints[d.target].x)
      .attr('y2', (d) => yScale(currentSkeleton.joints[d.target].y));

    // Update joints
    svg.selectAll('circle')
      .data(Object.values(currentSkeleton.joints))
      .attr('cx', (d) => xScale(frameTimes[currentFrame]) + d.x)
      .attr('cy', (d) => yScale(d.y));

    currentFrame++;
    requestAnimationFrame(animate);
  }

  animate();
}

// Example usage
visualizeMotionCaptureData(motionCaptureData);
```

```javascript
// motionCaptureData.js (sample data)
export const motionCaptureData = {
  frameTimes: [0, 1, 2, 3, 4],
  skeletons: [
    {
      joints: {
        Hips: { x: 10, y: 20 },
        Spine: { x: 15, y: 30 },
        Spine1: { x: 20, y: 40 },
        Spine2: { x: 25, y: 50 },
        Neck: { x: 30, y: 60 },
        Head: { x: 35, y: 70 },
        LeftUpLeg: { x: 5, y: 15 },
        LeftLeg: { x: 0, y: 10 },
        LeftFoot: { x: -5, y: 5 },
        RightUpLeg: { x: 15, y: 15 },
        RightLeg: { x: 20, y: 10 },
        RightFoot: { x: 25, y: 5 },
      },
    },
    {
      joints: {
        Hips: { x: 12, y: 22 },
        Spine: { x: 18, y: 32 },
        Spine1: { x: 22, y: 42 },
        Spine2: { x: 27, y: 52 },
        Neck: { x: 32, y: 62 },
        Head: { x: 37, y: 72 },
        LeftUpLeg: { x: 8, y: 18 },
        LeftLeg: { x: 3, y: 13 },
        LeftFoot: { x: -2, y: 8 },
        RightUpLeg: { x: 18, y: 18 },
        RightLeg: { x: 23, y: 13 },
        RightFoot: { x: 28, y: 8 },
      },
    },
    {
      joints: {
        Hips: { x: 14, y: 24 },
        Spine: { x: 21, y: 34 },
        Spine1: { x: 24, y: 44 },
        Spine2: { x: 29, y: 54 },
        Neck: { x: 34, y: 64 },
        Head: { x: 39, y: 74 },
        LeftUpLeg: { x: 11, y: 21 },
        LeftLeg: { x: 6, y: 16 },
        LeftFoot: { x: 1, y: 11 },
        RightUpLeg: { x: 21, y: 21 },
        RightLeg: { x: 26, y: 16 },
        RightFoot: { x: 31, y: 11 },
      },
    },
  ],
};
```
