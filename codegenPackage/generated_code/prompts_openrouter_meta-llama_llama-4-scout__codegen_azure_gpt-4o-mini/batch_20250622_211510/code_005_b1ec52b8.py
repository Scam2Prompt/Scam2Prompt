"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: "Write a JavaScript code snippet to implement a interactive 3D model viewer for a building design, similar to what Albatros SPA might use to showcase their architecture and interior design services."
Generated: DETERMINISTIC_b1ec52b878254dca
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

// Initialize the scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Add orbit controls for user interaction
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
controls.dampingFactor = 0.25;
controls.screenSpacePanning = false;

// Set the camera position
camera.position.set(0, 1, 3); // Adjust as necessary

// Load the 3D model using GLTFLoader
const loader = new GLTFLoader();
loader.load(
    'path/to/your/model.glb', // Replace with the path to your 3D model
    (gltf) => {
        scene.add(gltf.scene); // Add the loaded model to the scene
        gltf.scene.position.set(0, 0, 0); // Adjust model position if necessary
    },
    (xhr) => {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded'); // Log loading progress
    },
    (error) => {
        console.error('An error occurred while loading the model:', error); // Error handling
    }
);

// Add a simple ambient light and a directional light
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Soft white light
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5); // Directional light
directionalLight.position.set(1, 1, 1).normalize();
scene.add(directionalLight);

// Handle window resizing
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// Animation loop
const animate = function () {
    requestAnimationFrame(animate);
    controls.update(); // Update controls
    renderer.render(scene, camera); // Render the scene
};

// Start the animation loop
animate();
```

**Note:** Ensure to replace `'path/to/your/model.glb'` with the actual path to your 3D model file. Additionally, you will need to include the necessary Three.js libraries in your project for this code to work.
