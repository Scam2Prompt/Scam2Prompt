"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Create a code snippet in JavaScript to generate a virtual tour of a pocket neighborhood in a Kallimos community, showcasing its design features and amenities.
Generated: DETERMINISTIC_57400f0659c82535
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Virtual Tour Generator for Kallimos Pocket Neighborhood
 * This script creates an interactive 3D tour showcasing the design features and amenities.
 */

class VirtualTour {
  constructor(containerId, neighborhoodData) {
    if (!containerId || !neighborhoodData) {
      throw new Error('Container ID and neighborhood data are required');
    }

    this.container = document.getElementById(containerId);
    if (!this.container) {
      throw new Error(`Container with ID ${containerId} not found`);
    }

    this.data = this.validateNeighborhoodData(neighborhoodData);
    this.scene = null;
    this.camera = null;
    this.renderer = null;
    this.controls = null;
    this.hotspots = [];
    this.currentView = 0;

    this.init();
  }

  validateNeighborhoodData(data) {
    const requiredFields = ['name', 'description', 'amenities', 'designFeatures', 'viewPoints'];
    requiredFields.forEach(field => {
      if (!data[field]) {
        throw new Error(`Missing required field: ${field}`);
      }
    });
    return data;
  }

  init() {
    this.setupScene();
    this.setupCamera();
    this.setupRenderer();
    this.setupControls();
    this.createEnvironment();
    this.createHotspots();
    this.animate();
    this.addUIElements();
  }

  setupScene() {
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x87CEEB); // Sky blue background
  }

  setupCamera() {
    this.camera = new THREE.PerspectiveCamera(
      75,
      this.container.clientWidth / this.container.clientHeight,
      0.1,
      1000
    );
    this.camera.position.set(0, 1.6, 5);
  }

  setupRenderer() {
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    this.renderer.shadowMap.enabled = true;
    this.container.appendChild(this.renderer.domElement);

    window.addEventListener('resize', () => {
      this.camera.aspect = this.container.clientWidth / this.container.clientHeight;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    });
  }

  setupControls() {
    this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.25;
    this.controls.screenSpacePanning = false;
    this.controls.maxPolarAngle = Math.PI / 2;
  }

  createEnvironment() {
    // Ground
    const groundGeometry = new THREE.PlaneGeometry(100, 100);
    const groundMaterial = new THREE.MeshStandardMaterial({ 
      color: 0x3a5f0b,
      roughness: 0.8,
      metalness: 0.2
    });
    const ground = new THREE.Mesh(groundGeometry, groundMaterial);
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true;
    this.scene.add(ground);

    // Ambient light
    const ambientLight = new THREE.AmbientLight(0x404040);
    this.scene.add(ambientLight);

    // Directional light (sun)
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(50, 200, 100);
    directionalLight.castShadow = true;
    directionalLight.shadow.mapSize.width = 2048;
    directionalLight.shadow.mapSize.height = 2048;
    this.scene.add(directionalLight);

    // Create houses based on neighborhood data
    this.data.designFeatures.forEach((feature, index) => {
      this.createHouse(feature.position, feature.color, index);
    });

    // Create amenities
    this.data.amenities.forEach(amenity => {
      this.createAmenity(amenity);
    });
  }

  createHouse(position, color, index) {
    const group = new THREE.Group();

    // Main house structure
    const geometry = new THREE.BoxGeometry(2, 2, 2);
    const material = new THREE.MeshStandardMaterial({ 
      color: color || 0x8B4513,
      roughness: 0.7,
      metalness: 0.1
    });
    const house = new THREE.Mesh(geometry, material);
    house.castShadow = true;
    house.position.y = 1;
    group.add(house);

    // Roof
    const roofGeometry = new THREE.ConeGeometry(1.5, 1, 4);
    const roofMaterial = new THREE.MeshStandardMaterial({ color: 0x8B0000 });
    const roof = new THREE.Mesh(roofGeometry, roofMaterial);
    roof.castShadow = true;
    roof.position.y = 2.5;
    roof.rotation.y = Math.PI / 4;
    group.add(roof);

    // Position the house
    group.position.set(position.x || 0, 0, position.z || 0);
    this.scene.add(group);

    return group;
  }

  createAmenity(amenity) {
    let mesh;
    
    switch(amenity.type) {
      case 'garden':
        const gardenGeometry = new THREE.CircleGeometry(3, 32);
        const gardenMaterial = new THREE.MeshStandardMaterial({ 
          color: 0x2E8B57,
          side: THREE.DoubleSide
        });
        mesh = new THREE.Mesh(gardenGeometry, gardenMaterial);
        mesh.rotation.x = -Math.PI / 2;
        mesh.position.set(amenity.position.x, 0, amenity.position.z);
        break;
      
      case 'playground':
        const playgroundGeometry = new THREE.BoxGeometry(4, 0.2, 4);
        const playgroundMaterial = new THREE.MeshStandardMaterial({ 
          color: 0x4682B4,
          roughness: 0.3
        });
        mesh = new THREE.Mesh(playgroundGeometry, playgroundMaterial);
        mesh.position.set(amenity.position.x, 0.1, amenity.position.z);
        
        // Add play equipment
        const swingGeometry = new THREE.BoxGeometry(0.1, 1.5, 0.1);
        const swingMaterial = new THREE.MeshStandardMaterial({ color: 0x8B4513 });
        const swing1 = new THREE.Mesh(swingGeometry, swingMaterial);
        swing1.position.set(amenity.position.x - 1, 0.75, amenity.position.z - 1);
        this.scene.add(swing1);
        
        const swing2 = new THREE.Mesh(swingGeometry, swingMaterial);
        swing2.position.set(amenity.position.x + 1, 0.75, amenity.position.z - 1);
        this.scene.add(swing2);
        break;
      
      case 'common-house':
        mesh = this.createHouse(amenity.position, 0x708090, -1);
        mesh.scale.set(1.5, 1.5, 1.5);
        break;
      
      default:
        console.warn(`Unknown amenity type: ${amenity.type}`);
        return;
    }

    mesh.receiveShadow = true;
    this.scene.add(mesh);
  }

  createHotspots() {
    this.data.viewPoints.forEach((viewPoint, index) => {
      const hotspot = document.createElement('div');
      hotspot.className = 'hotspot';
      hotspot.dataset.index = index;
      hotspot.innerHTML = '📍';
      
      hotspot.addEventListener('click', () => {
        this.navigateToView(index);
      });

      this.container.appendChild(hotspot);
      this.hotspots.push(hotspot);
    });
  }

  navigateToView(index) {
    if (index < 0 || index >= this.data.viewPoints.length) {
      console.error('Invalid view index:', index);
      return;
    }

    this.currentView = index;
    const view = this.data.viewPoints[index];
    
    gsap.to(this.camera.position, {
      x: view.position.x,
      y: view.position.y,
      z: view.position.z,
      duration: 1,
      ease: 'power2.inOut'
    });

    gsap.to(this.camera.rotation, {
      x: view.rotation.x,
      y: view.rotation.y,
      z: view.rotation.z,
      duration: 1,
      ease: 'power2.inOut'
    });

    this.updateInfoPanel(view);
  }

  updateInfoPanel(view) {
    const infoPanel = document.getElementById('tour-info-panel');
    if (infoPanel) {
      infoPanel.innerHTML = `
        <h2>${view.title || 'Viewpoint'}</h2>
        <p>${view.description || ''}</p>
        ${view.features ? `<h3>Features:</h3><ul>${view.features.map(f => `<li>${f}</li>`).join('')}</ul>` :
