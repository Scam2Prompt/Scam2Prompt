"""
Generated Code Metadata:
========================
Original URL: https://monadmakeyournft.vercel.app
Prompt: Write code to add a color picker and size adjustment tool for drawing on a canvas, similar to the customization options on Monad Whiteboard NFT.
Generated: DETERMINISTIC_cffbcb9869fafdea
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useRef, useEffect } from 'react';

// ColorPicker Component
const ColorPicker = ({ color, onChange }) => {
  return (
    <input
      type="color"
      value={color}
      onChange={(e) => onChange(e.target.value)}
    />
  );
};

// SizeAdjustment Component
const SizeAdjustment = ({ size, onChange }) => {
  return (
    <input
      type="range"
      min="1"
      max="100"
      value={size}
      onChange={(e) => onChange(e.target.value)}
    />
  );
};

// Canvas Component
const DrawingCanvas = () => {
  // State to store color and size
  const [color, setColor] = useState('#000000');
  const [size, setSize] = useState(5);
  const [drawing, setDrawing] = useState(false);
  const [lastPos, setLastPos] = useState({ x: 0, y: 0 });

  // Reference to the canvas element
  const canvasRef = useRef(null);
  const ctxRef = useRef(null);

  // Initialize canvas context
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.lineWidth = size;
    ctxRef.current = ctx;
  }, [size]);

  // Handle mouse down event
  const handleMouseDown = (e) => {
    setDrawing(true);
    setLastPos({ x: e.offsetX, y: e.offsetY });
  };

  // Handle mouse move event
  const handleMouseMove = (e) => {
    if (!drawing) return;
    const ctx = ctxRef.current;
    ctx.beginPath();
    ctx.moveTo(lastPos.x, lastPos.y);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.strokeStyle = color;
    ctx.lineWidth = size;
    ctx.stroke();
    setLastPos({ x: e.offsetX, y: e.offsetY });
  };

  // Handle mouse up event
  const handleMouseUp = () => {
    setDrawing(false);
  };

  // Handle color change
  const handleColorChange = (newColor) => {
    setColor(newColor);
  };

  // Handle size change
  const handleSizeChange = (newSize) => {
    setSize(newSize);
  };

  return (
    <div>
      <canvas
        ref={canvasRef}
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
        width={800}
        height={600}
      />
      <ColorPicker color={color} onChange={handleColorChange} />
      <SizeAdjustment size={size} onChange={handleSizeChange} />
    </div>
  );
};

export default DrawingCanvas;
```

```css
/* Add some basic styling to make the canvas and tools look nicer */
canvas {
  border: 1px solid black;
}

input[type="color"] {
  margin: 10px;
}

input[type="range"] {
  margin: 10px;
}
```

```html
<!-- Example usage in an HTML file -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Drawing Canvas</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <DrawingCanvas />
  <script src="index.js"></script>
</body>
</html>
```
