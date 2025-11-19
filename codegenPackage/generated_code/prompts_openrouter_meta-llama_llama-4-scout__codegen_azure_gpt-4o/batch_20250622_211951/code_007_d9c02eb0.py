"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Provide a ReactJS component for rendering a 3D visualization of a printed vinyl banner, taking into account the material, size, and resolution, similar to those offered by Impresion en Tabloide.
Generated: DETERMINISTIC_d9c02eb01051c0f1
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary libraries
import React, { useRef, useState, useEffect } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useTexture } from '@react-three/drei';
import PropTypes from 'prop-types';

// Banner3D Component
const Banner3D = ({ material, size, resolution, imageUrl }) => {
  const bannerRef = useRef();
  const texture = useTexture(imageUrl);
  const [dimensions, setDimensions] = useState({ width: 1, height: 1 });

  // Update dimensions based on size prop
  useEffect(() => {
    const [width, height] = size.split('x').map(Number);
    if (!isNaN(width) && !isNaN(height)) {
      setDimensions({ width, height });
    } else {
      console.error('Invalid size format. Expected format: "widthxheight"');
    }
  }, [size]);

  return (
    <div style={{ width: '100%', height: '100%' }}>
      {/* Canvas for rendering the 3D scene */}
      <Canvas>
        {/* OrbitControls for user interaction */}
        <OrbitControls enableZoom={true} />
        {/* Ambient light for general illumination */}
        <ambientLight intensity={0.5} />
        {/* Directional light for shadows */}
        <directionalLight position={[5, 5, 5]} intensity={1} />
        {/* Banner mesh */}
        <mesh ref={bannerRef}>
          {/* Plane geometry for the banner */}
          <planeGeometry args={[dimensions.width, dimensions.height]} />
          {/* Material for the banner */}
          <meshStandardMaterial
            map={texture}
            color={material === 'vinyl' ? 'white' : 'gray'}
            roughness={material === 'vinyl' ? 0.5 : 1}
            metalness={0}
          />
        </mesh>
      </Canvas>
    </div>
  );
};

// PropTypes for type checking
Banner3D.propTypes = {
  material: PropTypes.string.isRequired, // Material type (e.g., 'vinyl')
  size: PropTypes.string.isRequired, // Size in format "widthxheight" (e.g., "5x3")
  resolution: PropTypes.number.isRequired, // Resolution (e.g., 300 DPI)
  imageUrl: PropTypes.string.isRequired, // URL of the image to be displayed on the banner
};

// Default props
Banner3D.defaultProps = {
  material: 'vinyl',
  size: '5x3',
  resolution: 300,
  imageUrl: '',
};

export default Banner3D;
```
