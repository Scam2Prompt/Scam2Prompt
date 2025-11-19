"""
Generated Code Metadata:
========================
Original URL: https://parsflooring.net
Prompt: Recommend a suitable JavaScript library for creating an interactive 3D flooring design tool that allows users to visualize different flooring patterns and materials.
Generated: DETERMINISTIC_20a6ddc9bf0161bb
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import Three.js library for 3D rendering
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { RGBELoader } from 'three/examples/jsm/loaders/RGBELoader.js';

class FlooringDesignTool {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      throw new Error(`Container element with ID ${containerId} not found`);
    }

    this.initScene();
    this.initCamera();
    this.initRenderer();
    this.initControls();
    this.initLights();
    this.loadEnvironment();
    this.createFloor();
    this.animate();

    window.addEventListener('resize', this.onWindowResize.bind(this));
  }

  initScene() {
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0xf0f0f0);
  }

  initCamera() {
    this.camera = new THREE.PerspectiveCamera(
      75,
      this.container.clientWidth / this.container.clientHeight,
      0.1,
      1000
    );
    this.camera.position.set(5, 5, 5);
  }

  initRenderer() {
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setSize(
      this.container.clientWidth,
      this.container.clientHeight
    );
    this.renderer.setPixelRatio(window.devicePixelRatio);
    this.renderer.outputEncoding = THREE.sRGBEncoding;
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1;
    this.container.appendChild(this.renderer.domElement);
  }

  initControls() {
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.05;
    this.controls.screenSpacePanning = false;
    this.controls.minDistance = 1;
    this.controls.maxDistance = 20;
  }

  initLights() {
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    this.scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(5, 10, 7);
    directionalLight.castShadow = true;
    directionalLight.shadow.mapSize.width = 1024;
    directionalLight.shadow.mapSize.height = 1024;
    this.scene.add(directionalLight);
  }

  loadEnvironment() {
    new RGBELoader()
      .load('assets/environment.hdr', (texture) => {
        texture.mapping = THREE.EquirectangularReflectionMapping;
        this.scene.environment = texture;
      })
      .catch((error) => {
        console.error('Error loading HDR environment:', error);
      });
  }

  createFloor() {
    const floorGeometry = new THREE.PlaneGeometry(10, 10);
    const floorMaterial = new THREE.MeshStandardMaterial({
      color: 0xdddddd,
      roughness: 0.1,
      metalness: 0.0,
    });
    this.floor = new THREE.Mesh(floorGeometry, floorMaterial);
    this.floor.rotation.x = -Math.PI / 2;
    this.floor.receiveShadow = true;
    this.scene.add(this.floor);
  }

  changeFloorMaterial(textureUrl, options = {}) {
    const loader = new THREE.TextureLoader();
    loader.load(
      textureUrl,
      (texture) => {
        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;
        texture.repeat.set(options.repeatX || 1, options.repeatY || 1);

        this.floor.material.map = texture;
        this.floor.material.needsUpdate = true;
      },
      undefined,
      (error) => {
        console.error('Error loading floor texture:', error);
      }
    );
  }

  changeFloorPattern(patternType, options = {}) {
    // Implement different floor patterns (herringbone, checkerboard, etc.)
    // This would typically involve creating custom shaders or geometry
    console.log(`Changing floor pattern to ${patternType}`);
  }

  onWindowResize() {
    this.camera.aspect = this.container.clientWidth / this.container.clientHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(
      this.container.clientWidth,
      this.container.clientHeight
    );
  }

  animate() {
    requestAnimationFrame(this.animate.bind(this));
    this.controls.update();
    this.renderer.render(this.scene, this.camera);
  }
}

// Example usage:
// const flooringTool = new FlooringDesignTool('flooring-container');
// flooringTool.changeFloorMaterial('assets/wood_texture.jpg', { repeatX: 2, repeatY: 2 });
```
