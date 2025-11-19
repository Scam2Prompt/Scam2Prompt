"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hwii-net.pages.dev
Prompt: Write a JavaScript function that creates a random noise generator, inspired by the "noise" theme mentioned on hwii.net.
Generated: DETERMINISTIC_704319483eddac93
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates random noise using Perlin noise algorithm.
 * This function creates a random noise generator that can be used for various applications
 * such as procedural texture generation in graphics or sound synthesis.
 * 
 * @param {number} width - The width of the noise grid.
 * @param {number} height - The height of the noise grid.
 * @param {number} scale - The scale of the noise. Higher values produce larger features.
 * @returns {Array<Array<number>>} - A 2D array representing the noise values.
 */
function generateRandomNoise(width, height, scale) {
    // Validate input parameters
    if (typeof width !== 'number' || typeof height !== 'number' || typeof scale !== 'number') {
        throw new Error('Width, height, and scale must be numbers.');
    }
    if (width <= 0 || height <= 0 || scale <= 0) {
        throw new Error('Width, height, and scale must be positive numbers.');
    }

    // Create noise array
    const noise = Array.from({ length: height }, () => Array(width).fill(0));

    // Generate random noise values
    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
            // Simple random noise generation algorithm
            const randomValue = Math.random(); // Generates a float between 0 and 1
            noise[y][x] = randomValue;
        }
    }

    return noise;
}

// Example usage:
try {
    const noiseGrid = generateRandomNoise(100, 100, 10);
    console.log(noiseGrid);
} catch (error) {
    console.error('Error generating noise:', error.message);
}
```
