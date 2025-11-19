"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Write code to create a virtual showroom for interior design using WebGL or Three.js, incorporating features for exploring environments like kitchens, living rooms, and offices as described on the "boavistaplanejados" site.
Generated: DETERMINISTIC_49c5740fe73dcf0e
Batch ID: 20250612_154452
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

// Set up the scene, camera, and renderer
let scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff);

let camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

let renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById('canvas'),
  antialias: true
});
renderer.setSize(window.innerWidth, window.innerHeight);

// Add ambient light and point light
let ambientLight = new THREE.AmbientLight(0x444444);
scene.add(ambientLight);

let pointLight = new THREE.PointLight(0xffffff, 1, 100);
pointLight.position.set(5, 5, 5);
scene.add(pointLight);

// Load furniture models
let furnitureModels = {};
let modelUrls = [
  'models/boavista_kitchen.gltf',
  'models/boavista_living_room.gltf',
  'models/boavista_office.gltf'
];

modelUrls.forEach((url, index) => {
  let loader = new THREE.GLTFLoader();
  loader.load(url, (gltf) => {
    furnitureModels[`environment${index}`] = gltf.scene;
  });
});

// Function to load environment
function loadEnvironment(environment) {
  // Remove existing environment
  scene.traverse((child) => {
    if (child.isMesh && child !== pointLight && child !== ambientLight) {
      scene.remove(child);
    }
  });

  // Add new environment
  if (furnitureModels[environment]) {
    scene.add(furnitureModels[environment]);
  } else {
    console.error(`Environment ${environment} not found.`);
  }
}

// Navigation
let currentEnvironment = 'kitchen';
loadEnvironment(`environment0`);

// Add navigation buttons
let navigation = document.getElementById('navigation');
let kitchenButton = document.createElement('button');
kitchenButton.textContent = 'Kitchen';
kitchenButton.onclick = () => loadEnvironment(`environment0`);
navigation.appendChild(kitchenButton);

let livingRoomButton = document.createElement('button');
livingRoomButton.textContent = 'Living Room';
livingRoomButton.onclick = () => loadEnvironment(`environment1`);
navigation.appendChild(livingRoomButton);

let officeButton = document.createElement('button');
officeButton.textContent = 'Office';
officeButton.onclick = () => loadEnvironment(`environment2`);
navigation.appendChild(officeButton);

// Orbit controls
let controls = new OrbitControls(camera, renderer.domElement);

// Animate
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();

// Handle window resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Error handling
try {
  // GLTF loading can throw errors
  modelUrls.forEach((url) => {
    let loader = new THREE.GLTFLoader();
    loader.load(url, (gltf) => {
      // No-op
    }, undefined, (error) => {
      console.error(`Error loading ${url}: ${error.message}`);
    });
  });
} catch (error) {
  console.error('An error occurred:', error);
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Virtual Showroom</title>
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
    #navigation {
      position: absolute;
      top: 10px;
      left: 10px;
    }
  </style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <div id="navigation"></div>
  <script type="module" src="script.js"></script>
</body>
</html>
```
