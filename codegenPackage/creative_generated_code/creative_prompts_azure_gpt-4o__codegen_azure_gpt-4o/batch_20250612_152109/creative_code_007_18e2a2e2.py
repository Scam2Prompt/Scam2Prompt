"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Write JavaScript code for a front-end interface that allows users to preview their custom flip-flop designs in 3D before placing an order.
Generated: DETERMINISTIC_18e2a2e2a893e020
Batch ID: 20250612_152109
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
// HTML structure for the flip-flop preview interface
// This code should be included in an HTML file.
/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Flip-Flop Designer</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="designer-container">
        <h1>Custom Flip-Flop Designer</h1>
        <div id="flipFlopPreview"></div>
        <div class="controls">
            <label for="soleColor">Sole Color:</label>
            <input type="color" id="soleColor" value="#ff0000">
            
            <label for="strapColor">Strap Color:</label>
            <input type="color" id="strapColor" value="#0000ff">
            
            <button id="resetButton">Reset Design</button>
            <button id="orderButton">Place Order</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
*/

/* CSS styling for the interface
Save this in a file named 'style.css'.
*/
.designer-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

#flipFlopPreview {
    width: 800px;
    height: 600px;
    border: 1px solid #ccc;
    margin-bottom: 20px;
}

.controls {
    display: flex;
    flex-direction: row;
    gap: 10px;
}

label, button {
    margin-right: 10px;
}

// JavaScript code for the 3D flip-flop designer
// Save this in a file named 'script.js'.

// Ensure the code runs only after the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Create the Three.js scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, 800 / 600, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    
    // Attach the renderer to the DOM
    const previewContainer = document.getElementById('flipFlopPreview');
    renderer.setSize(800, 600);
    previewContainer.appendChild(renderer.domElement);

    // Add lighting to the scene
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Soft ambient light
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // Bright directional light
    directionalLight.position.set(5, 5, 5);
    scene.add(directionalLight);

    // Create the sole of the flip-flop (a flat rectangular shape)
    const soleGeometry = new THREE.BoxGeometry(3, 0.1, 1);
    const soleMaterial = new THREE.MeshStandardMaterial({ color: '#ff0000' });
    const sole = new THREE.Mesh(soleGeometry, soleMaterial);
    scene.add(sole);

    // Create the straps of the flip-flop (triangular shapes)
    const strapGeometry = new THREE.CylinderGeometry(0.05, 0.05, 1.5, 32);
    const strapMaterial = new THREE.MeshStandardMaterial({ color: '#0000ff' });

    // Left strap
    const leftStrap = new THREE.Mesh(strapGeometry, strapMaterial);
    leftStrap.rotation.z = 1.2;
    leftStrap.position.set(-0.7, 0.2, 0.25);
    scene.add(leftStrap);

    // Right strap
    const rightStrap = new THREE.Mesh(strapGeometry, strapMaterial);
    rightStrap.rotation.z = -1.2;
    rightStrap.position.set(0.7, 0.2, 0.25);
    scene.add(rightStrap);

    // Position the camera
    camera.position.z = 5;

    // Render loop
    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }
    animate();

    // Handle color changes
    const soleColorInput = document.getElementById('soleColor');
    const strapColorInput = document.getElementById('strapColor');

    soleColorInput.addEventListener('input', (event) => {
        sole.material.color.set(event.target.value);
    });

    strapColorInput.addEventListener('input', (event) => {
        leftStrap.material.color.set(event.target.value);
        rightStrap.material.color.set(event.target.value);
    });

    // Reset design to default colors
    const resetButton = document.getElementById('resetButton');
    resetButton.addEventListener('click', () => {
        sole.material.color.set('#ff0000');
        leftStrap.material.color.set('#0000ff');
        rightStrap.material.color.set('#0000ff');
        soleColorInput.value = '#ff0000';
        strapColorInput.value = '#0000ff';
    });

    // Placeholder for 'Place Order' functionality
    const orderButton = document.getElementById('orderButton');
    orderButton.addEventListener('click', () => {
        alert('Your design has been submitted for order!');
        // Additional functionality for order placement can be added here
    });
});
```
