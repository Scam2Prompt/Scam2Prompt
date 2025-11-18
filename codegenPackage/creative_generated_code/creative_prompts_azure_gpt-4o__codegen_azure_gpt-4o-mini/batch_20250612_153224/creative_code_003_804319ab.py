"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaforce360.com
Prompt: Write JavaScript code to integrate interactive motion graphics into a website, inspired by Meta Force 360’s approach to animation-driven storytelling.
Generated: DETERMINISTIC_804319ab81296d71
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries for animation and interaction
import { Scene, WebGLRenderer, PerspectiveCamera, BoxGeometry, MeshBasicMaterial, Mesh, AnimationMixer, Clock } from 'three';

// Setting up a basic 3D scene
const scene = new Scene();
const renderer = new WebGLRenderer({ antialias: true });
const camera = new PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

// Setting up the canvas size
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Creating a geometry and material for the animated object
const geometry = new BoxGeometry();
const material = new MeshBasicMaterial({ color: 0x00ff00 });
const cube = new Mesh(geometry, material);

// Adding the cube to the scene
scene.add(cube);
camera.position.z = 5;

// Initialize clock for managing animation loop timing
const clock = new Clock();

// Animation loop
function animate() {
    // Calculate delta time
    const delta = clock.getDelta();

    // Rotate the cube for animation
    cube.rotation.x += delta;
    cube.rotation.y += delta;

    // Render the scene
    renderer.render(scene, camera);

    // Request the next frame
    requestAnimationFrame(animate);
}

// Error handling for the animation setup
try {
    animate();
} catch (error) {
    console.error("An error occurred during the animation loop:", error);
}

// Handle window resize events
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// Prevent memory leaks by properly disposing of the renderer on page unload
window.addEventListener('beforeunload', () => {
    renderer.dispose();
});
```

This code creates an interactive 3D scene with a rotating cube, using the Three.js library. It includes proper error handling, responsive design, and memory management.
