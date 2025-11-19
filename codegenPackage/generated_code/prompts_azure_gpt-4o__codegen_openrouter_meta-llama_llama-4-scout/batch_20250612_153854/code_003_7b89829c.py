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
 * Saves a canvas drawing as a PNG or JPG file.
 * 
 * @param {HTMLCanvasElement} canvas The canvas element to save.
 * @param {string} type The file type to save as. Can be 'png' or 'jpg'.
 * @param {string} filename The filename to save the file as.
 */
function saveCanvasAsImage(canvas, type, filename) {
    // Check if the canvas is valid
    if (!(canvas instanceof HTMLCanvasElement)) {
        throw new Error('Invalid canvas element');
    }

    // Check if the file type is valid
    if (type.toLowerCase() !== 'png' && type.toLowerCase() !== 'jpg' && type.toLowerCase() !== 'jpeg') {
        throw new Error('Invalid file type. Must be png, jpg, or jpeg');
    }

    // Get the file extension based on the file type
    let fileExtension;
    switch (type.toLowerCase()) {
        case 'png':
            fileExtension = 'png';
            break;
        case 'jpg':
        case 'jpeg':
            fileExtension = 'jpg';
            break;
    }

    // Get the canvas data URL
    let dataURL;
    try {
        dataURL = canvas.toDataURL(`image/${fileExtension}`);
    } catch (error) {
        throw new Error(`Failed to get canvas data URL: ${error.message}`);
    }

    // Create a link element to download the file
    const link = document.createElement('a');
    link.href = dataURL;
    link.download = filename || `image.${fileExtension}`;

    // Simulate a click on the link to download the file
    try {
        link.click();
    } catch (error) {
        throw new Error(`Failed to download file: ${error.message}`);
    }
}

// Example usage:
const canvas = document.getElementById('myCanvas');
saveCanvasAsImage(canvas, 'png', 'my_image');
```

```javascript
// Alternatively, using a more modern approach with async/await and try-catch
async function saveCanvasAsImageAsync(canvas, type, filename) {
    try {
        // Check if the canvas is valid
        if (!(canvas instanceof HTMLCanvasElement)) {
            throw new Error('Invalid canvas element');
        }

        // Check if the file type is valid
        if (type.toLowerCase() !== 'png' && type.toLowerCase() !== 'jpg' && type.toLowerCase() !== 'jpeg') {
            throw new Error('Invalid file type. Must be png, jpg, or jpeg');
        }

        // Get the file extension based on the file type
        let fileExtension;
        switch (type.toLowerCase()) {
            case 'png':
                fileExtension = 'png';
                break;
            case 'jpg':
            case 'jpeg':
                fileExtension = 'jpg';
                break;
        }

        // Get the canvas data URL
        const dataURL = canvas.toDataURL(`image/${fileExtension}`);

        // Create a blob from the data URL
        const blob = await (await fetch(dataURL)).blob();

        // Create a link element to download the file
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = filename || `image.${fileExtension}`;

        // Simulate a click on the link to download the file
        link.click();
    } catch (error) {
        console.error(`Failed to save canvas as image: ${error.message}`);
    }
}

// Example usage:
const canvas = document.getElementById('myCanvas');
saveCanvasAsImageAsync(canvas, 'png', 'my_image');
```
