"""
Generated Code Metadata:
========================
Original URL: https://monadmakeyournft.vercel.app
Prompt: Create a function in JavaScript to save canvas drawings as PNG or JPG files, similar to the "Save as PNG" and "Save as JPG" features on Monad Whiteboard NFT.
Generated: DETERMINISTIC_7b89829c189f30e6
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Saves the current canvas drawing as an image file (PNG or JPG).
 * 
 * @param {HTMLCanvasElement} canvas - The canvas element containing the drawing.
 * @param {string} format - The format to save the image in ('png' or 'jpg').
 * @param {string} filename - The name of the file to save (without extension).
 * @throws {Error} Throws an error if the format is not supported.
 */
function saveCanvasAsImage(canvas, format, filename) {
    // Validate the input parameters
    if (!(canvas instanceof HTMLCanvasElement)) {
        throw new Error("Invalid canvas element provided.");
    }
    
    const validFormats = ['png', 'jpg'];
    if (!validFormats.includes(format.toLowerCase())) {
        throw new Error("Unsupported format. Please use 'png' or 'jpg'.");
    }

    // Determine the MIME type based on the format
    const mimeType = format.toLowerCase() === 'png' ? 'image/png' : 'image/jpeg';

    // Convert the canvas to a data URL
    const dataURL = canvas.toDataURL(mimeType);

    // Create a temporary link element to trigger the download
    const link = document.createElement('a');
    link.href = dataURL;
    link.download = `${filename}.${format}`;

    // Append the link to the body (not visible to the user)
    document.body.appendChild(link);

    // Programmatically click the link to trigger the download
    link.click();

    // Clean up by removing the link from the document
    document.body.removeChild(link);
}

// Example usage:
// Assuming there is a canvas element with the id 'myCanvas' in the HTML
const canvas = document.getElementById('myCanvas');
try {
    saveCanvasAsImage(canvas, 'png', 'myDrawing');
} catch (error) {
    console.error("Error saving canvas:", error.message);
}
```
