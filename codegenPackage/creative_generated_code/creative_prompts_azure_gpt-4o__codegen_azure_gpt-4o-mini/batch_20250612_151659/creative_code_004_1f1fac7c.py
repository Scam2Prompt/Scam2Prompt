"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://planetaria.world
Prompt: Write code to enable JavaScript-based rendering for a metaverse application, referencing the Planetaria platform.
Generated: DETERMINISTIC_1f1fac7c11b11bc3
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
import * as THREE from 'three'; // 3D rendering library
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'; // Camera controls
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'; // GLTF model loader

// Initialize the MetaverseRenderer class
class MetaverseRenderer {
    constructor(containerId) {
        // Validate input
        if (!containerId) {
            throw new Error("Container ID is required to initialize MetaverseRenderer.");
        }

        // Set up the scene, camera, and renderer
        this.container = document.getElementById(containerId);
        if (!this.container) {
            throw new Error(`Container with ID "${containerId}" not found.`);
        }

        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({ antialias: true }); // Enable anti-aliasing for smoother visuals
        
        // Set renderer size and add to container
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.container.appendChild(this.renderer.domElement);

        // Initialize controls
        this.controls = new OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true; // Smooth control
        this.controls.dampingFactor = 0.25;

        // Set camera position
        this.camera.position.set(0, 1, 5); // Position the camera

        // Add event listener for window resize
        window.addEventListener('resize', this.onWindowResize.bind(this));

        // Start rendering the scene
        this.animate();
    }

    // Load a GLTF model into the scene
    loadModel(url) {
        const loader = new GLTFLoader();
        loader.load(url, (gltf) => {
            this.scene.add(gltf.scene);
            console.log('Model loaded successfully:', gltf);
        }, undefined, (error) => {
            console.error('An error occurred while loading the model:', error);
        });
    }

    // Handle window resizing
    onWindowResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }

    // Animation loop
    animate() {
        requestAnimationFrame(this.animate.bind(this)); // Ensure 'this' refers to the MetaverseRenderer instance
        this.controls.update(); // Update controls
        this.renderer.render(this.scene, this.camera); // Render the scene
    }
}

// Usage example:
try {
    const metaverseRenderer = new MetaverseRenderer('metaverse-container');
    metaverseRenderer.loadModel('path/to/your/model.glb'); // Replace with the actual model path
} catch (error) {
    console.error('Failed to initialize MetaverseRenderer:', error);
}
```

Ensure you have the necessary libraries installed and accessible in your project for the above code to work, and replace `'path/to/your/model.glb'` with the actual path to your GLTF model.
