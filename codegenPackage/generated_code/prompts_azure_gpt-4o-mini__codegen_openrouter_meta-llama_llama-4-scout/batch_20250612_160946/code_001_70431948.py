"""
Generated Code Metadata:
========================
Original URL: https://hwii-net.pages.dev
Prompt: Write a JavaScript function that creates a random noise generator, inspired by the "noise" theme mentioned on hwii.net.
Generated: DETERMINISTIC_704319483eddac93
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a Perlin noise function.
 * 
 * @param {number} seed - The seed for the random number generator.
 * @returns {function} A function that generates Perlin noise.
 */
function generatePerlinNoise(seed) {
    // Initialize the random number generator with the given seed.
    const random = new_seed_random(seed);

    // Define the Perlin noise function.
    return function(x, y) {
        // Calculate the integer part of x and y.
        const integerX = Math.floor(x);
        const integerY = Math.floor(y);

        // Calculate the fractional part of x and y.
        const fractionalX = x - integerX;
        const fractionalY = y - integerY;

        // Generate random values for the corners of the square.
        const v1 = random(integerX, integerY);
        const v2 = random(integerX + 1, integerY);
        const v3 = random(integerX, integerY + 1);
        const v4 = random(integerX + 1, integerY + 1);

        // Calculate the noise values for the top and bottom of the square.
        const i1 = interpolate(v1, v2, fractionalX);
        const i2 = interpolate(v3, v4, fractionalX);

        // Return the interpolated noise value.
        return interpolate(i1, i2, fractionalY);
    };
}

/**
 * Generates a random number based on the given coordinates.
 * 
 * @param {number} x - The x coordinate.
 * @param {number} y - The y coordinate.
 * @returns {number} A random number between 0 and 1.
 */
function new_seed_random(seed) {
    let x = seed;
    return function(x, y) {
        x += y * 387420;
        x = (x << 13) ^ x;
        return (x * (x * x * 15731 + 789221) + 1376312589) / 4294967296;
    };
}

/**
 * Interpolates between two values.
 * 
 * @param {number} a - The first value.
 * @param {number} b - The second value.
 * @param {number} x - The interpolation factor.
 * @returns {number} The interpolated value.
 */
function interpolate(a, b, x) {
    const ft = x * 3.1415927;
    const f = (1 - Math.cos(ft)) * 0.5;
    return  a * (1 - f) + b * f;
}

// Example usage:
const noise = generatePerlinNoise(42);
for (let i = 0; i < 10; i++) {
    console.log(noise(i / 10, i / 10));
}
```
