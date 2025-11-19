"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Write a code snippet in JavaScript to create an interactive 3D model of a backyard with a fence, deck, and pergola, using a library like Three.js, incorporating materials and textures commonly used in outdoor construction."
Generated: DETERMINISTIC_bd5ec1e8926f96f2
Batch ID: 20250622_210703
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

// Set up the scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById('canvas'),
  antialias: true
});

// Add some ambient light to the scene
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

// Create the backyard model
const createBackyard = () => {
  // Create the ground
  const groundGeometry = new THREE.PlaneGeometry(100, 100);
  const groundMaterial = new THREE.MeshPhongMaterial({
    color: 0x964B00, // Brown color
    texture: new THREE.CanvasTexture(createGrassTexture())
  });
  groundMaterial.texture.repeat.set(10, 10);
  groundMaterial.texture.wrapS = groundMaterial.texture.wrapT = THREE.RepeatWrapping;
  const ground = new THREE.Mesh(groundGeometry, groundMaterial);
  ground.rotation.x = -Math.PI / 2;
  scene.add(ground);

  // Create the fence
  const fenceGeometry = new THREE.BoxGeometry(100, 2, 0.1);
  const fenceMaterial = new THREE.MeshPhongMaterial({
    color: 0x786C3B // Wood color
  });
  const fence = new THREE.Mesh(fenceGeometry, fenceMaterial);
  fence.position.y = 1;
  scene.add(fence);

  // Create the deck
  const deckGeometry = new THREE.PlaneGeometry(20, 20);
  const deckMaterial = new THREE.MeshPhongMaterial({
    color: 0x663300, // Wood color
    texture: new THREE.CanvasTexture(createWoodTexture())
  });
  deckMaterial.texture.repeat.set(5, 5);
  deckMaterial.texture.wrapS = deckMaterial.texture.wrapT = THREE.RepeatWrapping;
  const deck = new THREE.Mesh(deckGeometry, deckMaterial);
  deck.rotation.x = -Math.PI / 2;
  deck.position.z = -20;
  scene.add(deck);

  // Create the pergola
  const pergolaGeometry = new THREE.BoxGeometry(5, 5, 0.1);
  const pergolaMaterial = new THREE.MeshPhongMaterial({
    color: 0x786C3B // Wood color
  });
  const pergola = new THREE.Mesh(pergolaGeometry, pergolaMaterial);
  pergola.position.z = -20;
  pergola.position.y = 2.5;
  scene.add(pergola);

  // Add some posts to the pergola
  for (let i = 0; i < 4; i++) {
    const postGeometry = new THREE.CylinderGeometry(0.2, 0.2, 5, 32);
    const postMaterial = new THREE.MeshPhongMaterial({
      color: 0x786C3B // Wood color
    });
    const post = new THREE.Mesh(postGeometry, postMaterial);
    post.position.z = -20;
    post.position.y = 2.5;
    post.rotation.x = Math.PI / 2;
    post.position.x = (i % 2 === 0) ? -2.5 : 2.5;
    post.position.z = (i < 2) ? -2.5 : 2.5;
    scene.add(post);
  }
};

// Create grass texture
const createGrassTexture = () => {
  const canvas = document.createElement('canvas');
  canvas.width = 256;
  canvas.height = 256;
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = 'green';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  for (let i = 0; i < 100; i++) {
    ctx.fillStyle = `rgba(0, 128, 0, ${Math.random() * 0.5 + 0.5})`;
    ctx.beginPath();
    ctx.arc(Math.random() * canvas.width, Math.random() * canvas.height, Math.random() * 5 + 2, 0, 2 * Math.PI);
    ctx.fill();
  }
  return canvas;
};

// Create wood texture
const createWoodTexture = () => {
  const canvas = document.createElement('canvas');
  canvas.width = 256;
  canvas.height = 256;
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = '#786C3B';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#452B1F';
  for (let i = 0; i < 100; i++) {
    ctx.beginPath();
    ctx.arc(Math.random() * canvas.width, Math.random() * canvas.height, Math.random() * 2 + 1, 0, 2 * Math.PI);
    ctx.fill();
  }
  return canvas;
};

// Add lights
const pointLight = new THREE.PointLight(0xffffff, 1, 100);
pointLight.position.set(0, 10, 0);
scene.add(pointLight);

// Set up camera and renderer
camera.position.z = 50;
renderer.setSize(window.innerWidth, window.innerHeight);

// Create interactive controls
const controls = new OrbitControls(camera, renderer.domElement);

// Animate the scene
const animate = () => {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
};

// Initialize the backyard model
createBackyard();

// Start animating
animate();

// Handle window resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```
