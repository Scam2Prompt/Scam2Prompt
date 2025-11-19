"""
Generated Code Metadata:
========================
Original URL: https://tinfun.pages.dev
Prompt: Develop a code example that visualizes the architecture of TinFun's "Water Hub" and "Chongyuan Tower" using a JavaScript library like Three.js.
Generated: DETERMINISTIC_45c9786bafa81c63
Batch ID: 20250612_140246
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

// Define constants for the scene
const WATER_HUB_SCALE = 1;
const CHONGYUAN_TOWER_SCALE = 1;
const CAMERA_DISTANCE = 500;

// Initialize the scene, camera, and renderer
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xf0f0f0);

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = CAMERA_DISTANCE;

const renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById('canvas'),
  antialias: true
});
renderer.setSize(window.innerWidth, window.innerHeight);

// Create Water Hub model
const waterHubGeometry = new THREE.BoxGeometry(100 * WATER_HUB_SCALE, 20 * WATER_HUB_SCALE, 100 * WATER_HUB_SCALE);
const waterHubMaterial = new THREE.MeshPhongMaterial({ color: 0x87CEEB });
const waterHub = new THREE.Mesh(waterHubGeometry, waterHubMaterial);
waterHub.position.y = 10 * WATER_HUB_SCALE;
scene.add(waterHub);

// Create Chongyuan Tower model
const chongyuanTowerGeometry = new THREE.CylinderGeometry(20 * CHONGYUAN_TOWER_SCALE, 20 * CHONGYUAN_TOWER_SCALE, 100 * CHONGYUAN_TOWER_SCALE, 32);
const chongyuanTowerMaterial = new THREE.MeshPhongMaterial({ color: 0x964B00 });
const chongyuanTower = new THREE.Mesh(chongyuanTowerGeometry, chongyuanTowerMaterial);
chongyuanTower.position.y = 50 * CHONGYUAN_TOWER_SCALE;
scene.add(chongyuanTower);

// Add lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const pointLight = new THREE.PointLight(0xffffff, 1, 1000);
pointLight.position.set(0, 100, 0);
scene.add(pointLight);

// Add orbit controls
const controls = new OrbitControls(camera, renderer.domElement);

// Animate the scene
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}

// Handle window resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Start the animation
animate();
```
