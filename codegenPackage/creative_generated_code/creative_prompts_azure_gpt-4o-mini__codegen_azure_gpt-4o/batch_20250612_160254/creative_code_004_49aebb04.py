"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pics3dstudio.com
Prompt: Create a sample code that implements a virtual tour feature for properties such as the La Estancia De Cafayate House 2024, utilizing WebVR or similar technologies.
Generated: DETERMINISTIC_49aebb04d81f91c3
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import * as THREE from 'three'; // Three.js library for 3D rendering
import { VRButton } from 'three/examples/jsm/webxr/VRButton'; // WebXR VR button for enabling VR mode
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'; // Controls for non-VR navigation

// Entry point function for initializing the virtual tour
function initVirtualTour() {
  // Create a scene
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x000000); // Set background color

  // Create a camera
  const camera = new THREE.PerspectiveCamera(
    75, // Field of view
    window.innerWidth / window.innerHeight, // Aspect ratio
    0.1, // Near clipping plane
    1000 // Far clipping plane
  );
  camera.position.set(0, 1.6, 3); // Position camera for typical VR perspective

  // Create a WebGL renderer
  const renderer = new THREE.WebGLRenderer({
    antialias: true, // Enable anti-aliasing for smoother edges
  });
  renderer.setSize(window.innerWidth, window.innerHeight); // Set renderer size
  renderer.xr.enabled = true; // Enable WebXR for VR mode
  document.body.appendChild(renderer.domElement); // Append renderer to DOM

  // Add VR button to enable VR mode
  document.body.appendChild(VRButton.createButton(renderer));

  // Add OrbitControls for non-VR navigation
  const controls = new OrbitControls(camera, renderer.domElement);

  // Load 360-degree texture for the virtual environment
  const textureLoader = new THREE.TextureLoader();
  const environmentTexture = textureLoader.load('path/to/360-image.jpg', (texture) => {
    // Apply the texture as a sphere geometry
    const geometry = new THREE.SphereGeometry(500, 60, 40); // Large sphere to encapsulate the viewer
    const material = new THREE.MeshBasicMaterial({
      map: texture, // Use the loaded texture
      side: THREE.DoubleSide, // Render both sides of the sphere
    });
    const sphere = new THREE.Mesh(geometry, material);
    sphere.scale.x = -1; // Reverse sphere rendering for inside view
    scene.add(sphere); // Add the sphere to the scene
  });

  // Error handling for texture loading
  environmentTexture.onError = (error) => {
    console.error('Error loading texture:', error);
  };

  // Render loop for animation
  function animate() {
    renderer.setAnimationLoop(() => {
      controls.update(); // Update controls for non-VR navigation
      renderer.render(scene, camera); // Render the scene from the camera perspective
    });
  }

  // Handle window resize events
  function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight; // Update camera aspect ratio
    camera.updateProjectionMatrix(); // Apply changes to camera projection matrix
    renderer.setSize(window.innerWidth, window.innerHeight); // Update renderer size
  }
  window.addEventListener('resize', onWindowResize);

  // Start the rendering loop
  animate();
}

// Initialize the virtual tour when the page loads
window.onload = initVirtualTour;
```

### Notes:
1. Replace `path/to/360-image.jpg` with the actual path to the 360-degree image for the virtual tour.
2. Ensure that the necessary libraries (`Three.js`, `VRButton`, etc.) are properly installed via a package manager like npm or included in the project as script tags if not using a bundler.
