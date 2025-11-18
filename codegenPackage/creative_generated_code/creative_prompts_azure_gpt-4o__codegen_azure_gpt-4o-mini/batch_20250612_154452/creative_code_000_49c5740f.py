"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Write code to create a virtual showroom for interior design using WebGL or Three.js, incorporating features for exploring environments like kitchens, living rooms, and offices as described on the "boavistaplanejados" site.
Generated: DETERMINISTIC_49c5740fe73dcf0e
Batch ID: 20250612_154452
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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Showroom</title>
    <style>
        body { margin: 0; }
        canvas { display: block; }
        #menu { position: absolute; top: 20px; left: 20px; z-index: 1; }
        button { padding: 10px; font-size: 16px; }
    </style>
</head>
<body>
    <div id="menu">
        <button id="kitchenButton">Kitchen</button>
        <button id="livingRoomButton">Living Room</button>
        <button id="officeButton">Office</button>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Initialize the scene, camera, and renderer
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Function to create a room (kitchen, living room, office)
        function createRoom(type) {
            // Clear existing objects in the scene
            while (scene.children.length > 0) {
                scene.remove(scene.children[0]);
            }

            // Create room geometry
            let roomGeometry = new THREE.BoxGeometry(10, 10, 10);
            let roomMaterial = new THREE.MeshBasicMaterial({ color: 0xffffff, wireframe: true });
            let room = new THREE.Mesh(roomGeometry, roomMaterial);
            scene.add(room);

            // Position the camera
            camera.position.z = 15;

            // Add room-specific details
            switch (type) {
                case 'kitchen':
                    addKitchenDetails();
                    break;
                case 'livingRoom':
                    addLivingRoomDetails();
                    break;
                case 'office':
                    addOfficeDetails();
                    break;
                default:
                    console.warn('Unknown room type:', type);
            }
        }

        // Function to add kitchen details
        function addKitchenDetails() {
            const floorTexture = new THREE.TextureLoader().load('path/to/kitchen-floor.jpg');
            const floorMaterial = new THREE.MeshBasicMaterial({ map: floorTexture });
            const floorGeometry = new THREE.PlaneGeometry(10, 10);
            const floor = new THREE.Mesh(floorGeometry, floorMaterial);
            floor.rotation.x = -Math.PI / 2; // Rotate to horizontal
            scene.add(floor);
            console.log("Kitchen details added.");
        }

        // Function to add living room details
        function addLivingRoomDetails() {
            const floorTexture = new THREE.TextureLoader().load('path/to/livingroom-floor.jpg');
            const floorMaterial = new THREE.MeshBasicMaterial({ map: floorTexture });
            const floorGeometry = new THREE.PlaneGeometry(10, 10);
            const floor = new THREE.Mesh(floorGeometry, floorMaterial);
            floor.rotation.x = -Math.PI / 2;
            scene.add(floor);
            console.log("Living room details added.");
        }

        // Function to add office details
        function addOfficeDetails() {
            const floorTexture = new THREE.TextureLoader().load('path/to/office-floor.jpg');
            const floorMaterial = new THREE.MeshBasicMaterial({ map: floorTexture });
            const floorGeometry = new THREE.PlaneGeometry(10, 10);
            const floor = new THREE.Mesh(floorGeometry, floorMaterial);
            floor.rotation.x = -Math.PI / 2;
            scene.add(floor);
            console.log("Office details added.");
        }

        // Button event listeners for changing rooms
        document.getElementById('kitchenButton').addEventListener('click', () => createRoom('kitchen'));
        document.getElementById('livingRoomButton').addEventListener('click', () => createRoom('livingRoom'));
        document.getElementById('officeButton').addEventListener('click', () => createRoom('office'));

        // Animation loop
        function animate() {
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        }
        animate();

        // Handle window resize
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
</body>
</html>
``` 

This code sets up a basic virtual showroom using Three.js with functionality to switch between different room types (kitchen, living room, office). Textures for the floors are placeholders and should be replaced with actual paths to image files.
