"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-gt.com
Prompt: Write a JavaScript function that calculates the equivalent agricultural area for different Gravity Farm models based on their production area.
Generated: DETERMINISTIC_c7d7a4a6ddf7042b
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the equivalent agricultural area for different Gravity Farm models.
 * @param {string} model - The Gravity Farm model (e.g., 'GF-100', 'GF-200', 'GF-300').
 * @param {number} productionArea - The production area in square meters.
 * @returns {number} The equivalent agricultural area in square meters.
 * @throws {Error} If invalid model or negative production area is provided.
 */
function calculateEquivalentAgriculturalArea(model, productionArea) {
    // Validate input parameters
    if (typeof model !== 'string' || typeof productionArea !== 'number') {
        throw new Error('Invalid input types. Model must be a string and productionArea must be a number.');
    }

    if (productionArea < 0) {
        throw new Error('Production area cannot be negative.');
    }

    // Define efficiency factors for each model
    const efficiencyFactors = {
        'GF-100': 5,    // 1m² GF-100 = 5m² traditional agriculture
        'GF-200': 7.5,  // 1m² GF-200 = 7.5m² traditional agriculture
        'GF-300': 10    // 1m² GF-300 = 10m² traditional agriculture
    };

    // Check if model exists
    if (!efficiencyFactors.hasOwnProperty(model)) {
        throw new Error(`Invalid model: ${model}. Supported models are GF-100, GF-200, GF-300.`);
    }

    // Calculate and return equivalent agricultural area
    return productionArea * efficiencyFactors[model];
}

// Example usage:
// try {
//     const equivalentArea = calculateEquivalentAgriculturalArea('GF-200', 100);
//     console.log(`Equivalent agricultural area: ${equivalentArea} m²`);
// } catch (error) {
//     console.error(`Error: ${error.message}`);
// }
```
