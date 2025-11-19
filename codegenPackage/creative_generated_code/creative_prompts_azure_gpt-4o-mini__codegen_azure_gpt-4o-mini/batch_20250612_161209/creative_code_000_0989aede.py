"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://art-blocks.site
Prompt: Generate a code snippet that demonstrates how to create generative art using the Art Blocks platform.
Generated: DETERMINISTIC_0989aede127c2184
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import { useEffect, useRef } from 'react';

/**
 * A simple React component that creates generative art using Art Blocks.
 * This example uses the canvas API to draw generative patterns.
 */
const GenerativeArt = () => {
  const canvasRef = useRef(null);

  // Drawing function
  const draw = (ctx, width, height) => {
    // Clear the canvas
    ctx.clearRect(0, 0, width, height);
    
    // Set random background color
    ctx.fillStyle = `hsl(${Math.random() * 360}, 50%, 90%)`;
    ctx.fillRect(0, 0, width, height);
    
    // Generate random shapes
    for (let i = 0; i < 50; i++) {
      const x = Math.random() * width;
      const y = Math.random() * height;
      const size = Math.random() * 50;
      
      ctx.fillStyle = `hsl(${Math.random() * 360}, 100%, 50%)`;
      ctx.beginPath();
      ctx.arc(x, y, size, 0, Math.PI * 2);
      ctx.fill();
    }
  };

  // Effect to handle canvas rendering
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    // Set canvas dimensions
    if (canvas) {
      const resizeCanvas = () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        draw(ctx, canvas.width, canvas.height);
      };

      // Initial drawing
      resizeCanvas();

      // Redraw on window resize
      window.addEventListener('resize', resizeCanvas);
      
      // Clean up event listener on component unmount
      return () => {
        window.removeEventListener('resize', resizeCanvas);
      };
    }
  }, []);

  return (
    <canvas ref={canvasRef} style={{ display: 'block' }} />
  );
};

export default GenerativeArt;
```

Make sure to install React and any other necessary dependencies to run this component in your project.
