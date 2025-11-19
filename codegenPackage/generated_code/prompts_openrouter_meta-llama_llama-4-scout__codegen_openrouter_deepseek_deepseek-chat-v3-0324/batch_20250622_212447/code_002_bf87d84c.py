"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: How can I use a library like Three.js to create interactive, 3D visuals of planetary ecosystems, like those featured in Stellar Crop, and what are some best practices for optimizing performance?
Generated: DETERMINISTIC_bf87d84ced459bc8
Batch ID: 20250622_212447
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://threejs.org/examples/textures/planets/earth_normal_2048.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/loaders/GLTFLoader.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://threejs.org/examples/textures/planets/earth_specular_2048.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planetary Ecosystem Visualization</title>
    <style>
        body { 
            margin: 0; 
            overflow: hidden; 
            font-family: Arial, sans-serif;
        }
        canvas { 
            display: block; 
        }
        #info {
            position: absolute;
            top: 10px;
            width: 100%;
            text-align: center;
            color: white;
            pointer-events: none;
            text-shadow: 1px 1px 1px black;
        }
        #controls {
            position: absolute;
            bottom: 20px;
            left: 20px;
            background: rgba(0,0,0,0.5);
            padding: 10px;
            border-radius: 5px;
            color: white;
        }
    </style>
</head>
<body>
    <div id="info">Planetary Ecosystem Visualization</div>
    <div id="controls">
        <button id="rotate">Toggle Rotation</button>
        <button id="zoomIn">Zoom In</button>
        <button id="zoomOut">Zoom Out</button>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/loaders/GLTFLoader.js"></script>
    <script>
        // Main variables
        let scene, camera, renderer, planet, controls;
        let isRotating = true;
        const clock = new THREE.Clock();

        // Initialize the scene
        function init() {
            // Create scene
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x000000);

            // Create camera
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 5;

            // Create renderer
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setPixelRatio(window.devicePixelRatio);
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            // Add controls
            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;

            // Create planet
            createPlanet();

            // Add lighting
            const ambientLight = new THREE.AmbientLight(0x404040);
            scene.add(ambientLight);

            const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
            directionalLight.position.set(1, 1, 1);
            scene.add(directionalLight);

            // Event listeners
            window.addEventListener('resize', onWindowResize);
            document.getElementById('rotate').addEventListener('click', toggleRotation);
            document.getElementById('zoomIn').addEventListener('click', () => zoom(0.9));
            document.getElementById('zoomOut').addEventListener('click', () => zoom(1.1));

            // Start animation loop
            animate();
        }

        // Create planet with ecosystem elements
        function createPlanet() {
            // Planet geometry
            const geometry = new THREE.SphereGeometry(1, 64, 64);
            
            // Load textures
            const textureLoader = new THREE.TextureLoader();
            const planetTexture = textureLoader.load('https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg');
            const bumpMap = textureLoader.load('https://threejs.org/examples/textures/planets/earth_normal_2048.jpg');
            const specularMap = textureLoader.load('https://threejs.org/examples/textures/planets/earth_specular_2048.jpg');

            // Planet material
            const material = new THREE.MeshPhongMaterial({
                map: planetTexture,
                bumpMap: bumpMap,
                bumpScale: 0.05,
                specularMap: specularMap,
                specular: new THREE.Color('grey'),
                shininess: 5
            });

            // Create planet mesh
            planet = new THREE.Mesh(geometry, material);
            scene.add(planet);

            // Add simple ecosystem elements (trees as placeholders)
            addEcosystemElements();
        }

        // Add simple ecosystem elements
        function addEcosystemElements() {
            const treeGeometry = new THREE.ConeGeometry(0.05, 0.2, 8);
            const treeMaterial = new THREE.MeshPhongMaterial({ color: 0x00aa00 });

            // Distribute trees randomly on the planet surface
            for (let i = 0; i < 200; i++) {
                const tree = new THREE.Mesh(treeGeometry, treeMaterial);

                // Random position on sphere surface
                const theta = Math.random() * Math.PI * 2;
                const phi = Math.acos(2 * Math.random() - 1);
                const radius = 1.01; // Slightly above planet surface

                tree.position.x = radius * Math.sin(phi) * Math.cos(theta);
                tree.position.y = radius * Math.sin(phi) * Math.sin(theta);
                tree.position.z = radius * Math.cos(phi);

                // Make tree point outward from planet center
                tree.lookAt(0, 0, 0);
                tree.rotateX(Math.PI / 2);

                // Scale trees randomly
                const scale = 0.5 + Math.random();
                tree.scale.set(scale, scale, scale);

                scene.add(tree);
            }
        }

        // Animation loop
        function animate() {
            requestAnimationFrame(animate);

            const delta = clock.getDelta();

            if (isRotating) {
                planet.rotation.y += 0.1 * delta;
            }

            controls.update();
            renderer.render(scene, camera);
        }

        // Window resize handler
        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        // Toggle planet rotation
        function toggleRotation() {
            isRotating = !isRotating;
        }

        // Zoom camera
        function zoom(factor) {
            camera.position.z *= factor;
        }

        // Initialize the application
        init();
    </script>
</body>
</html>
```
