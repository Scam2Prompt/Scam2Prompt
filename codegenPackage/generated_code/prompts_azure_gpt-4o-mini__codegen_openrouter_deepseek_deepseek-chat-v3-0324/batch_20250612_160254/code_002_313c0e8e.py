"""
Generated Code Metadata:
========================
Original URL: https://www.pics3dstudio.com
Prompt: Write a function that integrates 360-degree panoramic images into a web application, inspired by the projects listed on PICS3DStudio.
Generated: DETERMINISTIC_313c0e8e22cb1208
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * PanoramicViewer - A class to integrate 360-degree panoramic images into a web application.
 * Inspired by PICS3DStudio projects.
 */
class PanoramicViewer {
  /**
   * Constructor for the PanoramicViewer.
   * @param {string} containerId - The ID of the container element where the viewer will be rendered.
   * @param {string} imageUrl - The URL of the 360-degree panoramic image.
   * @param {Object} options - Configuration options for the viewer.
   * @param {boolean} [options.autoRotate=false] - Whether the panorama should auto-rotate.
   * @param {number} [options.autoRotateSpeed=1.0] - Speed of auto-rotation (degrees per second).
   * @param {boolean} [options.showControls=true] - Whether to show navigation controls.
   */
  constructor(containerId, imageUrl, options = {}) {
    this.container = document.getElementById(containerId);
    this.imageUrl = imageUrl;
    this.options = {
      autoRotate: options.autoRotate || false,
      autoRotateSpeed: options.autoRotateSpeed || 1.0,
      showControls: options.showControls !== false,
    };

    if (!this.container) {
      throw new Error(`Container element with ID '${containerId}' not found.`);
    }

    this.init();
  }

  /**
   * Initializes the panoramic viewer.
   */
  init() {
    // Create the necessary DOM elements
    this.createViewerElements();

    // Initialize the Three.js scene
    this.initThreeJS();

    // Load the panoramic image
    this.loadPanoramicImage();

    // Set up event listeners
    this.setupEventListeners();

    // Start the animation loop
    this.animate();
  }

  /**
   * Creates the DOM elements needed for the viewer.
   */
  createViewerElements() {
    this.viewerContainer = document.createElement('div');
    this.viewerContainer.className = 'panoramic-viewer-container';
    this.viewerContainer.style.width = '100%';
    this.viewerContainer.style.height = '100%';
    this.container.appendChild(this.viewerContainer);
  }

  /**
   * Initializes Three.js components.
   */
  initThreeJS() {
    // Create scene
    this.scene = new THREE.Scene();

    // Create camera
    this.camera = new THREE.PerspectiveCamera(
      75,
      this.viewerContainer.clientWidth / this.viewerContainer.clientHeight,
      0.1,
      1000
    );
    this.camera.position.z = 0.1;

    // Create renderer
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setSize(
      this.viewerContainer.clientWidth,
      this.viewerContainer.clientHeight
    );
    this.viewerContainer.appendChild(this.renderer.domElement);

    // Initialize controls if enabled
    if (this.options.showControls) {
      this.controls = new THREE.OrbitControls(
        this.camera,
        this.renderer.domElement
      );
      this.controls.enableDamping = true;
      this.controls.dampingFactor = 0.25;
      this.controls.screenSpacePanning = false;
      this.controls.minDistance = 0.1;
      this.controls.maxDistance = 0.1;
    }

    // Handle window resize
    window.addEventListener('resize', () => this.handleResize());
  }

  /**
   * Loads the panoramic image and creates the sphere geometry.
   */
  loadPanoramicImage() {
    const textureLoader = new THREE.TextureLoader();
    textureLoader.load(
      this.imageUrl,
      (texture) => {
        // Create sphere geometry
        const geometry = new THREE.SphereGeometry(500, 60, 40);
        geometry.scale(-1, 1, 1);

        // Create material with the loaded texture
        const material = new THREE.MeshBasicMaterial({
          map: texture,
        });

        // Create mesh and add to scene
        this.sphere = new THREE.Mesh(geometry, material);
        this.scene.add(this.sphere);

        // Set initial rotation
        this.sphere.rotation.y = -Math.PI / 2;
      },
      undefined,
      (error) => {
        console.error('Error loading panoramic image:', error);
        throw new Error('Failed to load panoramic image.');
      }
    );
  }

  /**
   * Sets up event listeners for user interaction.
   */
  setupEventListeners() {
    let isDragging = false;
    let previousMousePosition = { x: 0, y: 0 };

    this.viewerContainer.addEventListener('mousedown', (e) => {
      isDragging = true;
      previousMousePosition = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging || !this.sphere) return;

      const deltaMove = {
        x: e.clientX - previousMousePosition.x,
        y: e.clientY - previousMousePosition.y,
      };

      this.sphere.rotation.y += deltaMove.x * 0.01;
      this.sphere.rotation.x += deltaMove.y * 0.01;

      previousMousePosition = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
    });

    // Touch events for mobile
    this.viewerContainer.addEventListener('touchstart', (e) => {
      isDragging = true;
      previousMousePosition = {
        x: e.touches[0].clientX,
        y: e.touches[0].clientY,
      };
      e.preventDefault();
    });

    window.addEventListener('touchmove', (e) => {
      if (!isDragging || !this.sphere) return;

      const deltaMove = {
        x: e.touches[0].clientX - previousMousePosition.x,
        y: e.touches[0].clientY - previousMousePosition.y,
      };

      this.sphere.rotation.y += deltaMove.x * 0.01;
      this.sphere.rotation.x += deltaMove.y * 0.01;

      previousMousePosition = {
        x: e.touches[0].clientX,
        y: e.touches[0].clientY,
      };
      e.preventDefault();
    });

    window.addEventListener('touchend', () => {
      isDragging = false;
    });
  }

  /**
   * Handles window resize events.
   */
  handleResize() {
    this.camera.aspect =
      this.viewerContainer.clientWidth / this.viewerContainer.clientHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(
      this.viewerContainer.clientWidth,
      this.viewerContainer.clientHeight
    );
  }

  /**
   * Animation loop for rendering and auto-rotation.
   */
  animate() {
    requestAnimationFrame(() => this.animate());

    if (this.options.autoRotate && this.sphere) {
      this.sphere.rotation.y += (this.options.autoRotateSpeed * Math.PI) / 180 / 60;
    }

    if (this.controls) {
      this.controls.update();
    }

    this.renderer.render(this.scene, this.camera);
  }

  /**
   * Cleans up resources and removes the viewer.
   */
  destroy() {
    window.removeEventListener('resize', this.handleResize);
    if (this.viewerContainer && this.viewerContainer.parentNode) {
      this.viewerContainer.parentNode.removeChild(this.viewerContainer);
    }
    if (this.renderer) {
      this.renderer.dispose();
    }
  }
}

// Example usage:
// const viewer = new PanoramicViewer('viewer-container', 'path/to/panorama.jpg', {
//   autoRotate: true,
//   autoRotateSpeed: 0.5
// });
```
