"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: How can I use a library like Three.js to create interactive, 3D visuals of planetary ecosystems, like those featured in Stellar Crop, and what are some best practices for optimizing performance?
Generated: DETERMINISTIC_bf87d84ced459bc8
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the necessary Three.js modules
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

// Initialize the scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Add orbit controls for user interaction
const controls = new OrbitControls(camera, renderer.domElement);

// Create a simple planetary ecosystem with a sphere representing a planet
const createPlanet = (radius, color, position) => {
    const geometry = new THREE.SphereGeometry(radius, 32, 32);
    const material = new THREE.MeshStandardMaterial({ color: color });
    const planet = new THREE.Mesh(geometry, material);
    planet.position.set(position.x, position.y, position.z);
    return planet;
};

// Add lighting to the scene
const ambientLight = new THREE.AmbientLight(0x404040); // Soft white light
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5);
scene.add(directionalLight);

// Create planets and add them to the scene
const planet1 = createPlanet(1, 0x00ff00, { x: -3, y: 0, z: 0 });
const planet2 = createPlanet(1.5, 0x0000ff, { x: 3, y: 0, z: 0 });
scene.add(planet1);
scene.add(planet2);

// Set the camera position
camera.position.z = 5;

// Handle window resizing
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
    
    // Rotate planets for a dynamic effect
    planet1.rotation.y += 0.01;
    planet2.rotation.y += 0.01;

    controls.update(); // Update controls
    renderer.render(scene, camera);
};

// Start the animation
animate();

// Error handling for WebGL context
try {
    if (!renderer.getContext()) {
        throw new Error('WebGL context not available. Please check your browser settings.');
    }
} catch (error) {
    console.error('Error initializing WebGL:', error);
}
```

### Best Practices for Optimizing Performance:
1. **Use Instancing**: For multiple similar objects, use instanced meshes to reduce draw calls.
2. **Level of Detail (LOD)**: Implement LOD techniques to reduce the complexity of distant objects.
3. **Texture Optimization**: Use compressed textures and mipmaps to improve loading times and performance.
4. **Frustum Culling**: Ensure that only objects within the camera's view are rendered.
5. **Batching**: Group static objects together to minimize state changes and draw calls.
6. **Use Efficient Materials**: Prefer simpler materials and avoid complex shaders unless necessary.
