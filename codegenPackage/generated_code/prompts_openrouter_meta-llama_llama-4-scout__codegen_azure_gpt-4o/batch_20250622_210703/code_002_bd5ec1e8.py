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
// Import the Three.js library
import * as THREE from 'three';

// Create the main scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x87CEEB); // Sky blue background

// Create the camera
const camera = new THREE.PerspectiveCamera(
  75, // Field of view
  window.innerWidth / window.innerHeight, // Aspect ratio
  0.1, // Near clipping plane
  1000 // Far clipping plane
);
camera.position.set(0, 10, 20); // Position the camera

// Create the renderer
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Add lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Soft ambient light
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // Sunlight-like directional light
directionalLight.position.set(10, 20, 10);
scene.add(directionalLight);

// Load textures
const textureLoader = new THREE.TextureLoader();
const woodTexture = textureLoader.load('textures/wood.jpg'); // Replace with actual texture path
const grassTexture = textureLoader.load('textures/grass.jpg'); // Replace with actual texture path
const fenceTexture = textureLoader.load('textures/fence.jpg'); // Replace with actual texture path

// Create the ground (grass)
const groundGeometry = new THREE.PlaneGeometry(50, 50);
const groundMaterial = new THREE.MeshStandardMaterial({ map: grassTexture });
const ground = new THREE.Mesh(groundGeometry, groundMaterial);
ground.rotation.x = -Math.PI / 2; // Rotate to lay flat
scene.add(ground);

// Create the deck
const deckGeometry = new THREE.BoxGeometry(10, 0.5, 10);
const deckMaterial = new THREE.MeshStandardMaterial({ map: woodTexture });
const deck = new THREE.Mesh(deckGeometry, deckMaterial);
deck.position.set(0, 0.25, 0); // Slightly above the ground
scene.add(deck);

// Create the fence
const fenceGeometry = new THREE.BoxGeometry(0.2, 2, 10);
const fenceMaterial = new THREE.MeshStandardMaterial({ map: fenceTexture });
const fenceLeft = new THREE.Mesh(fenceGeometry, fenceMaterial);
fenceLeft.position.set(-5, 1, 0); // Left side
scene.add(fenceLeft);

const fenceRight = fenceLeft.clone();
fenceRight.position.set(5, 1, 0); // Right side
scene.add(fenceRight);

const fenceBack = new THREE.Mesh(new THREE.BoxGeometry(10, 2, 0.2), fenceMaterial);
fenceBack.position.set(0, 1, -5); // Back side
scene.add(fenceBack);

// Create the pergola
const pergolaMaterial = new THREE.MeshStandardMaterial({ map: woodTexture });

// Pergola posts
const postGeometry = new THREE.BoxGeometry(0.2, 3, 0.2);
const post1 = new THREE.Mesh(postGeometry, pergolaMaterial);
post1.position.set(-4, 1.5, -4);
scene.add(post1);

const post2 = post1.clone();
post2.position.set(4, 1.5, -4);
scene.add(post2);

const post3 = post1.clone();
post3.position.set(-4, 1.5, 4);
scene.add(post3);

const post4 = post1.clone();
post4.position.set(4, 1.5, 4);
scene.add(post4);

// Pergola beams
const beamGeometry = new THREE.BoxGeometry(8, 0.2, 0.2);
const beam = new THREE.Mesh(beamGeometry, pergolaMaterial);
beam.position.set(0, 3, -4);
scene.add(beam);

const beam2 = beam.clone();
beam2.position.set(0, 3, 4);
scene.add(beam2);

const crossBeamGeometry = new THREE.BoxGeometry(0.2, 0.2, 8);
const crossBeam = new THREE.Mesh(crossBeamGeometry, pergolaMaterial);
crossBeam.position.set(-4, 3, 0);
scene.add(crossBeam);

const crossBeam2 = crossBeam.clone();
crossBeam2.position.set(4, 3, 0);
scene.add(crossBeam2);

// Handle window resizing
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();
```

**Note:** Replace `'textures/wood.jpg'`, `'textures/grass.jpg'`, and `'textures/fence.jpg'` with actual paths to texture files. Ensure the texture files are accessible in your project directory.
