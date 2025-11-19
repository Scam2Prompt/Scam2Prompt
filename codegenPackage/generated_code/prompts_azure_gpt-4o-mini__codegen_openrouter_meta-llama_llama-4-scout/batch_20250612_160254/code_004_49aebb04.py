"""
Generated Code Metadata:
========================
Original URL: https://www.pics3dstudio.com
Prompt: Create a sample code that implements a virtual tour feature for properties such as the La Estancia De Cafayate House 2024, utilizing WebVR or similar technologies.
Generated: DETERMINISTIC_49aebb04d81f91c3
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { VRButton } from 'three/examples/jsm/webxr/VRButton.js';

// Set up the scene, camera, and renderer
let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
let renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById('canvas'),
  antialias: true
});

// Add some basic lighting to the scene
let ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

let pointLight = new THREE.PointLight(0xffffff, 1, 100);
pointLight.position.set(5, 5, 5);
scene.add(pointLight);

// Load the 3D model of the property
let loader = new THREE.GLTFLoader();
loader.load('LaEstanciaDeCafayateHouse2024.gltf', (gltf) => {
  scene.add(gltf.scene);
});

// Set up the camera and renderer for VR
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.xr.enabled = true;

// Add VR button to the page
document.body.appendChild(VRButton.createButton(renderer));

// Set up orbit controls for non-VR interaction
let controls = new OrbitControls(camera, renderer.domElement);

// Define the camera position and rotation
camera.position.z = 5;

// Animate the scene
function animate(timestamp) {
  requestAnimationFrame(animate);

  // Update the orbit controls
  controls.update();

  // Render the scene
  renderer.render(scene, camera);
}

requestAnimationFrame(animate);

// Handle window resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();

  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Handle VR session start and end
renderer.xr.addEventListener('sessionstart', () => {
  console.log('VR session started');
});

renderer.xr.addEventListener('sessionend', () => {
  console.log('VR session ended');
});

// Handle errors
try {
  // Try to request VR session
  navigator.xr.requestSession('immersive-vr', {
    requiredFeatures: ['bounded-floor', 'plane-detection', 'plane-anchoring'],
    optionalFeatures: ['prismatic-form', 'webxr-plane-detection']
  }).then((session) => {
    renderer.xr.setSession(session);
  }).catch((error) => {
    console.error('Error requesting VR session:', error);
  });
} catch (error) {
  console.error('Error setting up VR:', error);
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>La Estancia De Cafayate House 2024 Virtual Tour</title>
  <style>
    body {
      margin: 0;
      background-color: #f0f0f0;
    }
    #canvas {
      width: 100%;
      height: 100vh;
      display: block;
    }
  </style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <script type="module" src="script.js"></script>
</body>
</html>
```
