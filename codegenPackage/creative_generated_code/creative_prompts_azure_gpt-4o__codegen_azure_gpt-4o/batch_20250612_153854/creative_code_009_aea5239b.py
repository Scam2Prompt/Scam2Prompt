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

Here’s the clean, well-commented, production-ready code to implement media upload functionality for images and GIFs on a canvas, ensuring compatibility with NFT minting platforms:

```javascript
/**
 * Media Upload Functionality for Canvas - NFT Compatibility
 * 
 * This script allows users to upload images and GIFs, draw them on an HTML5 canvas,
 * and prepare them for minting as NFTs. It ensures compatibility with NFT minting 
 * platforms by encoding the canvas output as a base64 image format.
 */

// Initialize the canvas and context
const canvas = document.getElementById("nftCanvas");
const ctx = canvas.getContext("2d");

// Ensure the canvas has a defined size for minting purposes
canvas.width = 800; // Set the desired width
canvas.height = 800; // Set the desired height

// Add event listener to file input for media upload
document.getElementById("mediaUpload").addEventListener("change", handleMediaUpload);

/**
 * Handles media upload and rendering on the canvas
 * @param {Event} event - The file input change event
 */
function handleMediaUpload(event) {
  const file = event.target.files[0];

  // Validate file type (only images and GIFs allowed)
  if (!file.type.match("image.*")) {
    alert("Please upload a valid image or GIF file.");
    return;
  }

  const reader = new FileReader();

  // File reading callback
  reader.onload = function (loadEvent) {
    const img = new Image();

    // Image loading callback
    img.onload = function () {
      // Clear the canvas before drawing new content
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw the uploaded image on the canvas
      // Scale image to fit the canvas dimensions while maintaining aspect ratio
      const aspectRatio = img.width / img.height;
      let drawWidth, drawHeight;

      if (aspectRatio > 1) {
        drawWidth = canvas.width;
        drawHeight = canvas.width / aspectRatio;
      } else {
        drawHeight = canvas.height;
        drawWidth = canvas.height * aspectRatio;
      }

      const xOffset = (canvas.width - drawWidth) / 2;
      const yOffset = (canvas.height - drawHeight) / 2;

      ctx.drawImage(img, xOffset, yOffset, drawWidth, drawHeight);
    };

    // Handle potential loading errors
    img.onerror = function () {
      alert("Failed to load the image. Please try again.");
    };

    // Set image source to the file data
    img.src = loadEvent.target.result;
  };

  // Handle potential file reading errors
  reader.onerror = function () {
    alert("Failed to read the file. Please try again.");
  };

  // Read the uploaded file as a data URL
  reader.readAsDataURL(file);
}

/**
 * Exports the canvas content as a base64 image, compatible with NFT minting platforms.
 * @returns {string} - Base64-encoded image data
 */
function exportCanvasAsBase64() {
  try {
    return canvas.toDataURL("image/png"); // Export as PNG format
  } catch (error) {
    console.error("Failed to export the canvas content:", error);
    alert("An error occurred while exporting the canvas content.");
    return null;
  }
}

// Example usage: Trigger file export
document.getElementById("exportButton").addEventListener("click", () => {
  const base64Image = exportCanvasAsBase64();
  if (base64Image) {
    console.log("Base64 Image Data:", base64Image);
    alert("Canvas exported successfully!");
  }
});
```

### HTML Code for Integration:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Media Upload for NFT Canvas</title>
</head>
<body>
  <h1>Media Upload for NFT Canvas</h1>
  <canvas id="nftCanvas" style="border: 1px solid #000;"></canvas>
  <br>
  <input type="file" id="mediaUpload" accept="image/*">
  <button id="exportButton">Export Canvas</button>
</body>
</html>
```

This code sets up a canvas and allows users to upload images and GIFs, draw them on the canvas, and export the content in a format compatible with NFT minting platforms.
