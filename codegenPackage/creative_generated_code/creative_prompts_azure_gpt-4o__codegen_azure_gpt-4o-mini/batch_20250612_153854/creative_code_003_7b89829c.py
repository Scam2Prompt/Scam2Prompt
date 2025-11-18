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
 * Saves the content of a canvas as a PNG or JPG file.
 *
 * @param {HTMLCanvasElement} canvas - The canvas element to be saved.
 * @param {string} format - The format to save the image in ('png' or 'jpg').
 * @param {string} [filename='canvas-image'] - The name of the file to be saved.
 * @throws Will throw an error if the format is not supported.
 */
function saveCanvasAsImage(canvas, format, filename = 'canvas-image') {
    // Validate input parameters
    if (!(canvas instanceof HTMLCanvasElement)) {
        throw new Error('The provided element is not a valid canvas.');
    }
    
    // Validate format
    const validFormats = ['png', 'jpg'];
    if (!validFormats.includes(format.toLowerCase())) {
        throw new Error(`Unsupported format: ${format}. Use 'png' or 'jpg'.`);
    }

    // Define the image type and quality
    const mimeType = format.toLowerCase() === 'png' ? 'image/png' : 'image/jpeg';
    const quality = format.toLowerCase() === 'jpg' ? 0.9 : undefined; // JPG quality (0 to 1)

    // Create the image URL from the canvas
    const imageUrl = canvas.toDataURL(mimeType, quality);

    // Create a temporary link element
    const link = document.createElement('a');
    link.href = imageUrl;
    link.download = `${filename}.${format}`;

    // Trigger the download
    document.body.appendChild(link); // Append the link to the body
    link.click(); // Programmatically click the link to trigger the download
    document.body.removeChild(link); // Remove the link from the document
}

// Example usage:
// Assuming there's a canvas element in your HTML with the id 'myCanvas'
// const canvas = document.getElementById('myCanvas');
// saveCanvasAsImage(canvas, 'png', 'my-drawing');
```
