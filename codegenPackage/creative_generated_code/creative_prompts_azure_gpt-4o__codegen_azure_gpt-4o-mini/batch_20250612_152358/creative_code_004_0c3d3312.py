"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrus.vercel.app
Prompt: Create a JavaScript application that visualizes the ring systems of Saturn and Uranus based on the descriptions provided on the Astrus website.
Generated: DETERMINISTIC_0c3d3312dea07cec
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import * as THREE from 'three'; // Import Three.js for 3D rendering
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'; // Import OrbitControls for camera manipulation

// Initialize scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Initialize orbit controls to allow user interaction
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; // an animation effect for smoother controls
controls.dampingFactor = 0.25; // damping factor

// Function to create Saturn's ring system
function createSaturnRings() {
    const ringGeometry = new THREE.RingGeometry(1, 1.2, 64);
    const ringMaterial = new THREE.MeshBasicMaterial({
        color: 0xaaaaaa,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.7
    });
    const ring = new THREE.Mesh(ringGeometry, ringMaterial);
    ring.rotation.x = Math.PI / 2; // Rotate to lay flat
    scene.add(ring);
}

// Function to create Uranus' ring system
function createUranusRings() {
    const ringGeometry = new THREE.RingGeometry(0.5, 0.7, 64);
    const ringMaterial = new THREE.MeshBasicMaterial({
        color: 0x0077ff,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.5
    });
    const ring = new THREE.Mesh(ringGeometry, ringMaterial);
    ring.rotation.x = Math.PI / 2; // Rotate to lay flat
    ring.position.x = 5; // Position the rings to the side
    scene.add(ring);
}

// Add simple ambient light to the scene
const ambientLight = new THREE.AmbientLight(0x404040); // soft white light
scene.add(ambientLight);

// Position the camera
camera.position.z = 5;

// Create the ring systems
createSaturnRings();
createUranusRings();

// Function to animate the scene
function animate() {
    requestAnimationFrame(animate);

    // Update controls
    controls.update();

    // Render the scene
    renderer.render(scene, camera);
}

// Handle window resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// Start the animation loop
animate();
```
