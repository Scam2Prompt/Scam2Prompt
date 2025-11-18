"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Generate code to implement media upload functionality (images and GIFs) on a canvas, ensuring compatibility with NFT minting platforms like Monad Whiteboard NFT.
Generated: DETERMINISTIC_aea5239bb225714f
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useRef, useState } from 'react';
import { fabric } from 'fabric';

const CanvasUploader = () => {
  // Reference to the canvas
  const canvasRef = useRef(null);
  const [error, setError] = useState("");

  // Initialize the canvas on component mount
  React.useEffect(() => {
    const canvas = new fabric.Canvas(canvasRef.current);
    canvas.setHeight(600);
    canvas.setWidth(800);
  }, []);

  // Function to handle file uploads
  const handleFileUpload = (event) => {
    const files = event.target.files;

    if (files.length === 0) {
      return setError("No files selected.");
    }

    const file = files[0];
    const validTypes = ['image/jpeg', 'image/png', 'image/gif'];

    // Check for valid file type
    if (!validTypes.includes(file.type)) {
      return setError("Invalid file type. Please upload an image (JPEG, PNG, GIF).");
    }

    // Clear previous error
    setError("");

    const reader = new FileReader();
    
    // Read the file and add to the canvas when loaded
    reader.onload = (e) => {
      const imgElement = new Image();
      imgElement.src = e.target.result;

      imgElement.onload = () => {
        const imgInstance = new fabric.Image(imgElement);
        imgInstance.set({
          left: 100,
          top: 100,
          angle: 0,
          opacity: 1,
        });

        // Add image instance to the canvas
        const canvas = canvasRef.current.getObjects();
        canvas.push(imgInstance);
        canvas.renderAll();
      };
    };

    reader.onerror = () => {
      setError("Error loading file. Please try again.");
    };

    reader.readAsDataURL(file);
  };

  return (
    <div>
      <h2>Media Upload to Canvas</h2>
      <input type="file" accept="image/*" onChange={handleFileUpload} />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <canvas ref={canvasRef} style={{ border: '1px solid #000' }} />
    </div>
  );
};

export default CanvasUploader;
```
