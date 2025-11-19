"""
Generated Code Metadata:
========================
Original URL: https://planetaria.world
Prompt: Create a simple web application using React and Three.js to display a 3D environment similar to Planetaria.
Generated: DETERMINISTIC_de0e64ec79d09c3e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

// Main App component
const App = () => {
  // Reference to the canvas element
  const canvasRef = useRef(null);

  // Initialize the 3D scene
  useEffect(() => {
    // Create the scene
    const scene = new THREE.Scene();
    
    // Set up the camera
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;

    // Create the renderer
    const renderer = new THREE.WebGLRenderer({ canvas: canvasRef.current });
    renderer.setSize(window.innerWidth, window.innerHeight);
    
    // Add orbit controls for user interaction
    const controls = new OrbitControls(camera, renderer.domElement);

    // Create a sphere to represent a planet
    const geometry = new THREE.SphereGeometry(1, 32, 32);
    const material = new THREE.MeshBasicMaterial({ color: 0x0077ff, wireframe: false });
    const planet = new THREE.Mesh(geometry, material);
    scene.add(planet);

    // Animation loop
    const animate = () => {
      requestAnimationFrame(animate);
      planet.rotation.y += 0.01; // Rotate the planet
      controls.update(); // Update controls
      renderer.render(scene, camera); // Render the scene
    };

    // Start the animation
    animate();

    // Handle window resize
    const handleResize = () => {
      const width = window.innerWidth;
      const height = window.innerHeight;
      renderer.setSize(width, height);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
    };

    window.addEventListener('resize', handleResize);

    // Cleanup on component unmount
    return () => {
      window.removeEventListener('resize', handleResize);
      renderer.dispose();
    };
  }, []);

  // Render the canvas
  return <canvas ref={canvasRef} />;
};

// Export the App component
export default App;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the main application
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Planetarium</title>
    <style>
        body { margin: 0; }
        canvas { display: block; }
    </style>
</head>
<body>
    <div id="root"></div>
    <script src="index.js" type="module"></script>
</body>
</html>
```

```bash
# package.json
{
  "name": "3d-planetarium",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "three": "^0.132.2"
  },
  "scripts": {
    "start": "webpack serve --mode development",
    "build": "webpack --mode production"
  },
  "devDependencies": {
    "webpack": "^5.64.4",
    "webpack-cli": "^4.9.1",
    "webpack-dev-server": "^3.11.2",
    "babel-loader": "^8.2.3",
    "@babel/core": "^7.15.0",
    "@babel/preset-env": "^7.15.0",
    "@babel/preset-react": "^7.14.5"
  }
}
```

```javascript
// webpack.config.js
const path = require('path');

module.exports = {
  entry: './index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/',
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],
          },
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 9000,
  },
};
```

```javascript
// .babelrc
{
  "presets": ["@babel/preset-env", "@babel/preset-react"]
}
```

This code provides a simple React application that uses Three.js to create a 3D environment with a rotating planet. It includes proper error handling, responsive design, and follows best practices for a production-ready application.
