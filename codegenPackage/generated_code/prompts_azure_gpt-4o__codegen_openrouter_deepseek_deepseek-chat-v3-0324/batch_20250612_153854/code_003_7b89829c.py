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
 * Saves a canvas drawing as an image file.
 * @param {HTMLCanvasElement} canvas - The canvas element to save.
 * @param {string} fileName - The name of the file without extension.
 * @param {string} format - The image format ('png' or 'jpg').
 * @param {number} [jpgQuality=0.92] - The quality for JPG (0 to 1).
 */
function saveCanvasAsImage(canvas, fileName, format, jpgQuality = 0.92) {
    try {
        if (!canvas || !(canvas instanceof HTMLCanvasElement)) {
            throw new Error('Invalid canvas element provided');
        }

        if (!fileName || typeof fileName !== 'string') {
            throw new Error('Invalid file name provided');
        }

        format = format.toLowerCase();
        if (format !== 'png' && format !== 'jpg' && format !== 'jpeg') {
            throw new Error('Unsupported format. Use "png" or "jpg"');
        }

        if (format === 'jpg' || format === 'jpeg') {
            if (typeof jpgQuality !== 'number' || jpgQuality < 0 || jpgQuality > 1) {
                throw new Error('JPG quality must be between 0 and 1');
            }
        }

        const mimeType = format === 'png' ? 'image/png' : 'image/jpeg';
        const fullFileName = `${fileName}.${format === 'png' ? 'png' : 'jpg'}`;

        canvas.toBlob((blob) => {
            try {
                if (!blob) {
                    throw new Error('Failed to create image blob');
                }

                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = fullFileName;
                document.body.appendChild(a);
                a.click();
                
                // Cleanup
                setTimeout(() => {
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                }, 100);
            } catch (error) {
                console.error('Error during download:', error);
            }
        }, mimeType, format === 'jpg' || format === 'jpeg' ? jpgQuality : undefined);
    } catch (error) {
        console.error('Error saving canvas as image:', error);
    }
}
```
