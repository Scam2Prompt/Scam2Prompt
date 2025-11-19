"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pics3dstudio.com
Prompt: Write a function that integrates 360-degree panoramic images into a web application, inspired by the projects listed on PICS3DStudio.
Generated: DETERMINISTIC_313c0e8e22cb1208
Batch ID: 20250612_160254
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.rawgit.com/mrdoob/three.js/r128/examples/js/controls/OrbitControls.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>360-Degree Panoramic Viewer</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.rawgit.com/mrdoob/three.js/r128/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    <div id="panorama" style="width: 100%; height: 100vh;"></div>
    <script>
        /**
         * Initializes a 360-degree panoramic viewer using Three.js.
         * @param {string} imagePath - The path to the panoramic image.
         */
        function initPanorama(imagePath) {
            // Check if the image path is provided
            if (!imagePath) {
                console.error("Image path is required.");
                return;
            }

            // Create the scene
            const scene = new THREE.Scene();

            // Create the camera
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0, 0.1); // Position the camera slightly away from the center

            // Create the WebGL renderer
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('panorama').appendChild(renderer.domElement);

            // Add OrbitControls to allow user interaction
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
            controls.dampingFactor = 0.25;
            controls.screenSpacePanning = false; // Prevent panning outside of the sphere

            // Load the panoramic texture
            const textureLoader = new THREE.TextureLoader();
            textureLoader.load(imagePath, function(texture) {
                const geometry = new THREE.SphereGeometry(500, 60, 40);
                const material = new THREE.MeshBasicMaterial({
                    map: texture,
                    side: THREE.BackSide // Render the inside of the sphere
                });
                const sphere = new THREE.Mesh(geometry, material);
                
                // Add the sphere to the scene
                scene.add(sphere);

                // Render loop
                const animate = function() {
                    requestAnimationFrame(animate);
                    controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true
                    renderer.render(scene, camera);
                };
                animate();
            }, undefined, function(err) {
                console.error("An error occurred while loading the texture:", err);
            });

            // Handle window resize
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        }

        // Call the function with the path to your panoramic image
        initPanorama('path/to/your/panorama.jpg');
    </script>
</body>
</html>
```
