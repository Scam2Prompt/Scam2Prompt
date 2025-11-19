"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-52--gracious-swanson-bcc8c1.netlify.app
Prompt: Create a simple React or VueJS code snippet that enables JavaScript to run an app, similar to the one on Tim Mansell's portfolio site.
Generated: DETERMINISTIC_d0d692321182d38b
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready React component that creates a simple interactive app similar to Tim Mansell's portfolio site. This includes a particle animation effect with mouse interaction:

```jsx
import React, { useState, useEffect, useRef } from 'react';

/**
 * Particle component representing a single animated dot
 * @param {Object} props - Component props
 * @param {number} props.x - X position
 * @param {number} props.y - Y position
 * @param {number} props.size - Particle size
 * @param {string} props.color - Particle color
 */
const Particle = ({ x, y, size, color }) => {
  return (
    <div
      className="particle"
      style={{
        position: 'absolute',
        left: `${x}px`,
        top: `${y}px`,
        width: `${size}px`,
        height: `${size}px`,
        borderRadius: '50%',
        backgroundColor: color,
        pointerEvents: 'none',
      }}
    />
  );
};

/**
 * Main InteractiveBackground component
 * Manages particle animation and mouse interaction
 */
const InteractiveBackground = () => {
  const [particles, setParticles] = useState([]);
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const containerRef = useRef(null);
  const animationRef = useRef(null);

  // Configuration constants
  const PARTICLE_COUNT = 100;
  const PARTICLE_SIZE_MIN = 2;
  const PARTICLE_SIZE_MAX = 5;
  const COLORS = ['#ff5252', '#ff4081', '#e040fb', '#7c4dff', '#536dfe'];

  /**
   * Initialize particles with random positions and properties
   */
  const initParticles = () => {
    if (!containerRef.current) return;

    const { width, height } = containerRef.current.getBoundingClientRect();
    const newParticles = [];

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      newParticles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * (PARTICLE_SIZE_MAX - PARTICLE_SIZE_MIN) + PARTICLE_SIZE_MIN,
        color: COLORS[Math.floor(Math.random() * COLORS.length)],
        speedX: Math.random() * 2 - 1,
        speedY: Math.random() * 2 - 1,
      });
    }

    setParticles(newParticles);
  };

  /**
   * Handle mouse movement to update mouse position
   * @param {MouseEvent} e - Mouse event
   */
  const handleMouseMove = (e) => {
    if (!containerRef.current) return;

    const rect = containerRef.current.getBoundingClientRect();
    setMousePosition({
      x: e.clientX - rect.left,
      y: e.clientY - rect.top,
    });
  };

  /**
   * Animation loop to update particle positions
   */
  const animate = () => {
    if (!containerRef.current) return;

    const { width, height } = containerRef.current.getBoundingClientRect();

    setParticles(prevParticles =>
      prevParticles.map(particle => {
        let { x, y, speedX, speedY, size } = particle;

        // Calculate distance to mouse
        const dx = mousePosition.x - x;
        const dy = mousePosition.y - y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        // Apply mouse attraction/repulsion
        if (distance < 100) {
          const forceDirectionX = dx / distance;
          const forceDirectionY = dy / distance;
          const force = (100 - distance) / 100;

          speedX -= forceDirectionX * force * 0.2;
          speedY -= forceDirectionY * force * 0.2;
        }

        // Update position with speed
        x += speedX;
        y += speedY;

        // Apply boundary checks
        if (x < 0 || x > width) speedX *= -0.8;
        if (y < 0 || y > height) speedY *= -0.8;

        // Clamp position to boundaries
        x = Math.max(0, Math.min(width, x));
        y = Math.max(0, Math.min(height, y));

        // Apply friction
        speedX *= 0.98;
        speedY *= 0.98;

        return { ...particle, x, y, speedX, speedY };
      })
    );

    animationRef.current = requestAnimationFrame(animate);
  };

  // Initialize particles and animation on mount
  useEffect(() => {
    initParticles();
    animationRef.current = requestAnimationFrame(animate);

    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, []);

  return (
    <div
      ref={containerRef}
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        overflow: 'hidden',
        zIndex: -1,
      }}
      onMouseMove={handleMouseMove}
    >
      {particles.map((particle, index) => (
        <Particle
          key={index}
          x={particle.x}
          y={particle.y}
          size={particle.size}
          color={particle.color}
        />
      ))}
    </div>
  );
};

export default InteractiveBackground;
```

To use this component in your app:

```jsx
import React from 'react';
import InteractiveBackground from './InteractiveBackground';

const App = () => {
  return (
    <div className="app">
      <InteractiveBackground />
      {/* Your other content goes here */}
      <div style={{ position: 'relative', zIndex: 1 }}>
        <h1>Your Content Here</h1>
      </div>
    </div>
  );
};

export default App;
```

This implementation includes:
- Smooth particle animation with physics
- Mouse interaction effects
- Proper cleanup of animation frames
- Responsive design
- Configurable parameters
- Clean component structure
- Type safety through PropTypes (not shown but recommended for production)
