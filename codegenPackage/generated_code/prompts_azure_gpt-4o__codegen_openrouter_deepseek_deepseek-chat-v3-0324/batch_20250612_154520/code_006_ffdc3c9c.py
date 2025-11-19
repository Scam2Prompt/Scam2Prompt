"""
Generated Code Metadata:
========================
Original URL: https://www.pics3dstudio.com
Prompt: Create a JavaScript application to embed 360-degree virtual tours of architectural projects, similar to the immersive experiences highlighted by PICS3DStudio's "Valley House 2023."
Generated: DETERMINISTIC_ffdc3c9c1e5f905b
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// 360 Virtual Tour Viewer
// A production-ready JavaScript application for embedding 360-degree virtual tours

class VirtualTourViewer {
  /**
   * Initialize the Virtual Tour Viewer
   * @param {string} containerId - ID of the DOM element to contain the viewer
   * @param {Object} options - Configuration options
   */
  constructor(containerId, options = {}) {
    // Default options
    const defaults = {
      initialScene: 'default',
      autoRotate: false,
      autoRotateSpeed: 0.5,
      showControls: true,
      loadingMessage: 'Loading virtual tour...',
      errorMessage: 'Failed to load virtual tour.',
      scenes: {},
      hotspotColor: '#ffffff',
      hotspotRadius: 10,
      onSceneChange: null,
      onLoad: null,
      onError: null
    };

    this.options = { ...defaults, ...options };
    this.container = document.getElementById(containerId);
    this.currentScene = null;
    this.isLoaded = false;
    this.renderer = null;
    this.scene = null;
    this.camera = null;
    this.sphere = null;
    this.controls = null;
    this.animationId = null;

    if (!this.container) {
      throw new Error(`Container element with ID '${containerId}' not found.`);
    }

    this.init();
  }

  /**
   * Initialize the Three.js scene and renderer
   */
  init() {
    try {
      // Show loading message
      this.showLoading();

      // Check if Three.js is available
      if (typeof THREE === 'undefined') {
        throw new Error('Three.js library is required but not loaded.');
      }

      // Create renderer
      this.renderer = new THREE.WebGLRenderer({ antialias: true });
      this.renderer.setPixelRatio(window.devicePixelRatio);
      this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
      this.container.appendChild(this.renderer.domElement);

      // Create scene
      this.scene = new THREE.Scene();

      // Create camera
      this.camera = new THREE.PerspectiveCamera(
        75,
        this.container.clientWidth / this.container.clientHeight,
        0.1,
        1000
      );
      this.camera.position.z = 0.01;

      // Add controls if enabled
      if (this.options.showControls) {
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.25;
        this.controls.screenSpacePanning = false;
        this.controls.minDistance = 0.1;
        this.controls.maxDistance = 0.1;
        this.controls.maxPolarAngle = Math.PI;
      }

      // Load initial scene
      this.loadScene(this.options.initialScene);

      // Handle window resize
      window.addEventListener('resize', this.handleResize.bind(this));

      // Animation loop
      this.animate();

      if (typeof this.options.onLoad === 'function') {
        this.options.onLoad();
      }

      this.isLoaded = true;
    } catch (error) {
      this.handleError(error);
    }
  }

  /**
   * Load a scene by name
   * @param {string} sceneName - Name of the scene to load
   */
  loadScene(sceneName) {
    if (!this.options.scenes[sceneName]) {
      throw new Error(`Scene '${sceneName}' not found in configuration.`);
    }

    try {
      // Show loading state
      this.showLoading();

      // Remove existing sphere if present
      if (this.sphere) {
        this.scene.remove(this.sphere);
      }

      // Create new sphere geometry
      const geometry = new THREE.SphereGeometry(500, 60, 40);
      geometry.scale(-1, 1, 1);

      // Load texture
      const texture = new THREE.TextureLoader().load(
        this.options.scenes[sceneName].panorama,
        () => {
          // Texture loaded successfully
          const material = new THREE.MeshBasicMaterial({ map: texture });
          this.sphere = new THREE.Mesh(geometry, material);
          this.scene.add(this.sphere);

          // Add hotspots if defined
          if (this.options.scenes[sceneName].hotspots) {
            this.addHotspots(this.options.scenes[sceneName].hotspots);
          }

          // Update current scene
          this.currentScene = sceneName;

          // Hide loading state
          this.hideLoading();

          // Call scene change callback
          if (typeof this.options.onSceneChange === 'function') {
            this.options.onSceneChange(sceneName);
          }
        },
        undefined,
        (error) => {
          this.handleError(error);
        }
      );
    } catch (error) {
      this.handleError(error);
    }
  }

  /**
   * Add hotspots to the current scene
   * @param {Array} hotspots - Array of hotspot configurations
   */
  addHotspots(hotspots) {
    hotspots.forEach((hotspot) => {
      const { yaw, pitch, scene, tooltip } = hotspot;

      // Convert angles to radians
      const phi = THREE.MathUtils.degToRad(90 - pitch);
      const theta = THREE.MathUtils.degToRad(yaw);

      // Calculate position on sphere
      const position = new THREE.Vector3();
      position.setFromSphericalCoords(450, phi, theta);

      // Create hotspot geometry
      const geometry = new THREE.SphereGeometry(
        this.options.hotspotRadius,
        16,
        16
      );
      const material = new THREE.MeshBasicMaterial({
        color: this.options.hotspotColor,
        transparent: true,
        opacity: 0.8
      });
      const sphere = new THREE.Mesh(geometry, material);
      sphere.position.copy(position);

      // Add click/tap event
      sphere.userData = { scene, tooltip };
      sphere.cursor = 'pointer';
      this.addInteraction(sphere);

      this.scene.add(sphere);

      // Add tooltip if specified
      if (tooltip) {
        this.addTooltip(sphere, tooltip);
      }
    });
  }

  /**
   * Add interaction to a hotspot
   * @param {THREE.Mesh} mesh - The hotspot mesh
   */
  addInteraction(mesh) {
    const domElement = this.renderer.domElement;

    // Handle pointer events
    const onPointerUp = (event) => {
      event.preventDefault();

      // Raycasting to detect clicks
      const raycaster = new THREE.Raycaster();
      const mouse = new THREE.Vector2();

      // Calculate mouse position in normalized device coordinates
      const rect = domElement.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

      // Set the raycaster
      raycaster.setFromCamera(mouse, this.camera);

      // Check for intersections
      const intersects = raycaster.intersectObject(mesh);

      if (intersects.length > 0) {
        if (mesh.userData.scene) {
          this.loadScene(mesh.userData.scene);
        }
      }
    };

    domElement.addEventListener('pointerup', onPointerUp);
  }

  /**
   * Add a tooltip to a hotspot
   * @param {THREE.Mesh} mesh - The hotspot mesh
   * @param {string} text - Tooltip text
   */
  addTooltip(mesh, text) {
    const tooltip = document.createElement('div');
    tooltip.className = 'virtual-tour-tooltip';
    tooltip.textContent = text;
    tooltip.style.position = 'absolute';
    tooltip.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    tooltip.style.color = 'white';
    tooltip.style.padding = '5px 10px';
    tooltip.style.borderRadius = '3px';
    tooltip.style.pointerEvents = 'none';
    tooltip.style.display = 'none';
    this.container.appendChild(tooltip);

    const domElement = this.renderer.domElement;

    // Show/hide tooltip on hover
    domElement.addEventListener('pointermove', (event) => {
      const raycaster = new THREE.Raycaster();
      const mouse = new THREE.Vector2();

      const rect = domElement.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, this.camera);
      const intersects = raycaster.intersectObject(mesh);

      if (intersects.length > 0) {
        tooltip.style.display = 'block';
        tooltip.style.left = `${event.clientX}px`;
        tooltip.style.top = `${event.clientY - 30}px`;
      } else {
