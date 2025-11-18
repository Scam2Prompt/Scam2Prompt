"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cadv.io
Prompt: Develop a code example in JavaScript that integrates cadvio's Oculus Rift support for creating an immersive 3D walkthrough experience.
Generated: DETERMINISTIC_6786a89931b3d5e8
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary dependencies from cadvio and Oculus SDK
import { Scene, WebGLRenderer, PerspectiveCamera } from 'three';
import { VRButton } from 'three/examples/jsm/webxr/VRButton.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

// Initialize the scene, camera, and renderer
const scene = new Scene();
const camera = new PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Add VR button to enable Oculus support
document.body.appendChild(VRButton.createButton(renderer));

// Setup OrbitControls for user navigation
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
controls.dampingFactor = 0.25;
controls.screenSpacePanning = false;

// Load a 3D model using GLTFLoader
const loader = new GLTFLoader();
loader.load(
    'path/to/your/model.glb', // Replace with the path to your 3D model
    (gltf) => {
        scene.add(gltf.scene);
    },
    (xhr) => {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
    },
    (error) => {
        console.error('An error occurred while loading the model:', error);
    }
);

// Set the camera position
camera.position.set(0, 1.6, 3); // Adjust the height for an immersive experience

// Handle window resize
window.addEventListener('resize', () => {
    const width = window.innerWidth;
    const height = window.innerHeight;
    renderer.setSize(width, height);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
});

// Animation loop
const animate = () => {
    requestAnimationFrame(animate);
    controls.update(); // Update the controls
    renderer.render(scene, camera);
};

// Start the animation loop
animate();
```

### Notes:
- Make sure to replace `'path/to/your/model.glb'` with the actual path to your 3D model file.
- Ensure you have the necessary `three.js` libraries and dependencies installed in your project for this code to work.
