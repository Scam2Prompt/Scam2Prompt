"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tinfun.pages.dev
Prompt: Develop a code example that visualizes the architecture of TinFun's "Water Hub" and "Chongyuan Tower" using a JavaScript library like Three.js.
Generated: DETERMINISTIC_45c9786bafa81c63
Batch ID: 20250612_140246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Include Three.js library via CDN or package manager in your environment.
// CDN example: <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

// Production-ready visualization of TinFun's "Water Hub" and "Chongyuan Tower"
// using Three.js. This code creates a basic architecture scene for visualization.

document.addEventListener("DOMContentLoaded", () => {
  // Create the main Three.js scene
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x87ceeb); // Set background color to sky blue

  // Set up the camera to view the scene
  const camera = new THREE.PerspectiveCamera(
    75, // FOV
    window.innerWidth / window.innerHeight, // Aspect ratio
    0.1, // Near clipping plane
    1000 // Far clipping plane
  );
  camera.position.set(0, 10, 20); // Position camera to view objects

  // Configure the WebGL renderer
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  // Add ambient lighting to the scene
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.6); // Soft white light
  scene.add(ambientLight);

  // Add a directional light for shadows and highlights
  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(10, 20, 10);
  directionalLight.castShadow = true;
  scene.add(directionalLight);

  // Add a plane to represent the ground
  const groundGeometry = new THREE.PlaneGeometry(50, 50);
  const groundMaterial = new THREE.MeshStandardMaterial({ color: 0x228b22 }); // Grass green
  const ground = new THREE.Mesh(groundGeometry, groundMaterial);
  ground.rotation.x = -Math.PI / 2; // Rotate to make it horizontal
  ground.receiveShadow = true;
  scene.add(ground);

  // Create the "Water Hub" architecture (a cylindrical structure with a dome)
  const waterHubBaseGeometry = new THREE.CylinderGeometry(5, 5, 2, 32);
  const waterHubBaseMaterial = new THREE.MeshStandardMaterial({ color: 0x1e90ff }); // Water blue
  const waterHubBase = new THREE.Mesh(waterHubBaseGeometry, waterHubBaseMaterial);
  waterHubBase.position.set(-10, 1, 0); // Position the base of Water Hub
  waterHubBase.castShadow = true;
  scene.add(waterHubBase);

  const waterHubDomeGeometry = new THREE.SphereGeometry(5, 32, 16);
  const waterHubDomeMaterial = new THREE.MeshStandardMaterial({ color: 0x00bfff }); // Aqua blue
  const waterHubDome = new THREE.Mesh(waterHubDomeGeometry, waterHubDomeMaterial);
  waterHubDome.scale.set(1, 0.5, 1); // Flatten to create a dome shape
  waterHubDome.position.set(-10, 3, 0); // Position the dome on top of the base
  waterHubDome.castShadow = true;
  scene.add(waterHubDome);

  // Create the "Chongyuan Tower" architecture (a tall, three-tiered tower)
  const towerBaseGeometry = new THREE.BoxGeometry(4, 4, 4);
  const towerBaseMaterial = new THREE.MeshStandardMaterial({ color: 0x8b0000 }); // Dark red
  const towerBase = new THREE.Mesh(towerBaseGeometry, towerBaseMaterial);
  towerBase.position.set(10, 2, 0); // Position the base of Chongyuan Tower
  towerBase.castShadow = true;
  scene.add(towerBase);

  const towerMiddleGeometry = new THREE.BoxGeometry(3, 3, 3);
  const towerMiddleMaterial = new THREE.MeshStandardMaterial({ color: 0xff4500 }); // Orange red
  const towerMiddle = new THREE.Mesh(towerMiddleGeometry, towerMiddleMaterial);
  towerMiddle.position.set(10, 5.5, 0); // Position the middle section
  towerMiddle.castShadow = true;
  scene.add(towerMiddle);

  const towerTopGeometry = new THREE.BoxGeometry(2, 2, 2);
  const towerTopMaterial = new THREE.MeshStandardMaterial({ color: 0xffd700 }); // Gold
  const towerTop = new THREE.Mesh(towerTopGeometry, towerTopMaterial);
  towerTop.position.set(10, 8.5, 0); // Position the top section
  towerTop.castShadow = true;
  scene.add(towerTop);

  // Animation loop to render the scene
  const animate = () => {
    requestAnimationFrame(animate);

    // Rotate structures for dynamic visualization
    waterHubBase.rotation.y += 0.01;
    waterHubDome.rotation.y += 0.01;
    towerBase.rotation.y += 0.005;
    towerMiddle.rotation.y += 0.005;
    towerTop.rotation.y += 0.005;

    renderer.render(scene, camera);
  };

  // Handle window resize events
  window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  // Start the animation loop
  animate();
});
```
