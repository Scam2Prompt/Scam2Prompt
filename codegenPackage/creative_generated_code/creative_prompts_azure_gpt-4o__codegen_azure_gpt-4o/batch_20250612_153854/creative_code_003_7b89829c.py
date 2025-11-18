"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Create a function in JavaScript to save canvas drawings as PNG or JPG files, similar to the "Save as PNG" and "Save as JPG" features on Monad Whiteboard NFT.
Generated: DETERMINISTIC_7b89829c189f30e6
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to save canvas drawings as PNG or JPG files.
 * @param {HTMLCanvasElement} canvas - The canvas element containing the drawing.
 * @param {string} format - The desired file format ("png" or "jpg").
 * @param {string} filename - The name for the saved file.
 */
function saveCanvasAsImage(canvas, format, filename) {
  try {
    // Validate input parameters
    if (!(canvas instanceof HTMLCanvasElement)) {
      throw new Error("Invalid canvas element provided.");
    }
    if (!["png", "jpg"].includes(format.toLowerCase())) {
      throw new Error("Invalid format provided. Supported formats are 'png' and 'jpg'.");
    }
    if (typeof filename !== "string" || filename.trim() === "") {
      throw new Error("Invalid filename provided.");
    }

    // Generate the image data URL based on the format
    const mimeType = format.toLowerCase() === "jpg" ? "image/jpeg" : "image/png";
    const imageDataURL = canvas.toDataURL(mimeType);

    // Create an anchor element for downloading the image
    const link = document.createElement("a");
    link.href = imageDataURL;
    link.download = `${filename}.${format}`;

    // Trigger the download
    document.body.appendChild(link);
    link.click();

    // Clean up by removing the anchor element
    document.body.removeChild(link);
  } catch (error) {
    // Handle any errors encountered during execution
    console.error("Error saving canvas as image:", error.message);
  }
}

// Example usage:
// const canvas = document.getElementById("myCanvas");
// saveCanvasAsImage(canvas, "png", "myDrawing");
```
