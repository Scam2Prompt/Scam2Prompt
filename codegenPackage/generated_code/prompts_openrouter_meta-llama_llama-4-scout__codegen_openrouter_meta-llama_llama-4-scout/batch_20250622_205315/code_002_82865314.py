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
// Import required libraries
import * as d3 from 'd3';
import * as THREE from 'three';

// Define the DefectGraph class
class DefectGraph {
  /**
   * Constructor for DefectGraph
   * @param {HTMLElement} container - The container element for the graph
   * @param {Object} data - The defect graph data
   */
  constructor(container, data) {
    this.container = container;
    this.data = data;
    this.width = 800;
    this.height = 600;
    this.margin = { top: 20, right: 20, bottom: 30, left: 40 };

    // Initialize the SVG element
    this.svg = d3.select(container)
      .append('svg')
      .attr('width', this.width)
      .attr('height', this.height);

    // Initialize the force simulation
    this.simulation = d3.forceSimulation()
      .force('charge', d3.forceManyBody().strength(-500))
      .force('link', d3.forceLink().distance(150).strength(0.5))
      .force('center', d3.forceCenter(this.width / 2, this.height / 2));

    // Create the graph
    this.createGraph();
  }

  /**
   * Create the defect graph
   */
  createGraph() {
    // Create the nodes and links
    const nodes = this.data.nodes.map((node) => ({ ...node }));
    const links = this.data.links.map((link) => ({ ...link }));

    // Add nodes and links to the simulation
    this.simulation.nodes(nodes);
    this.simulation.force('link').links(links);

    // Create the node and link elements
    const nodeElements = this.svg.selectAll('circle')
      .data(nodes)
      .enter()
      .append('circle')
      .attr('r', 10)
      .attr('fill', (d) => d.color);

    const linkElements = this.svg.selectAll('line')
      .data(links)
      .enter()
      .append('line')
      .attr('stroke', 'gray')
      .attr('stroke-width', 2);

    // Update the node positions
    this.simulation.on('tick', () => {
      nodeElements
        .attr('cx', (d) => d.x)
        .attr('cy', (d) => d.y);

      linkElements
        .attr('x1', (d) => d.source.x)
        .attr('y1', (d) => d.source.y)
        .attr('x2', (d) => d.target.x)
        .attr('y2', (d) => d.target.y);
    });
  }
}

// Define the LayerAnnotations class
class LayerAnnotations {
  /**
   * Constructor for LayerAnnotations
   * @param {HTMLElement} container - The container element for the annotations
   * @param {Object} data - The layer annotation data
   */
  constructor(container, data) {
    this.container = container;
    this.data = data;

    // Initialize the Three.js scene
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    this.renderer = new THREE.WebGLRenderer({
      canvas: document.createElement('canvas'),
      antialias: true,
    });

    // Add the renderer to the container
    this.container.appendChild(this.renderer.domElement);

    // Create the annotations
    this.createAnnotations();
  }

  /**
   * Create the layer annotations
   */
  createAnnotations() {
    // Create the annotation meshes
    const annotationMeshes = this.data.annotations.map((annotation) => {
      const geometry = new THREE.TextGeometry(annotation.text, {
        font: 'Arial',
        size: 1,
        height: 0.1,
        curveSegments: 12,
      });

      const material = new THREE.MeshBasicMaterial({ color: annotation.color });
      const mesh = new THREE.Mesh(geometry, material);

      mesh.position.set(annotation.position.x, annotation.position.y, annotation.position.z);
      this.scene.add(mesh);

      return mesh;
    });

    // Animate the scene
    this.animate(annotationMeshes);
  }

  /**
   * Animate the scene
   * @param {THREE.Mesh[]} annotationMeshes - The annotation meshes
   */
  animate(annotationMeshes) {
    requestAnimationFrame(() => this.animate(annotationMeshes));

    // Rotate the annotation meshes
    annotationMeshes.forEach((mesh) => {
      mesh.rotation.x += 0.01;
      mesh.rotation.y += 0.01;
    });

    // Render the scene
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.render(this.scene, this.camera);
  }
}

// Example usage
const defectGraphContainer = document.getElementById('defect-graph');
const layerAnnotationsContainer = document.getElementById('layer-annotations');

const defectGraphData = {
  nodes: [
    { id: 1, color: 'red' },
    { id: 2, color: 'blue' },
    { id: 3, color: 'green' },
  ],
  links: [
    { source: 1, target: 2 },
    { source: 2, target: 3 },
    { source: 3, target: 1 },
  ],
};

const layerAnnotationsData = {
  annotations: [
    { text: 'Annotation 1', color: 'red', position: { x: 0, y: 0, z: 0 } },
    { text: 'Annotation 2', color: 'blue', position: { x: 1, y: 1, z: 1 } },
    { text: 'Annotation 3', color: 'green', position: { x: 2, y: 2, z: 2 } },
  ],
};

const defectGraph = new DefectGraph(defectGraphContainer, defectGraphData);
const layerAnnotations = new LayerAnnotations(layerAnnotationsContainer, layerAnnotationsData);
```
