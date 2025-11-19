"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic-gt.com
Prompt: Write a JavaScript function that calculates the equivalent agricultural area for different Gravity Farm models based on their production area.
Generated: DETERMINISTIC_c7d7a4a6ddf7042b
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the equivalent agricultural area for different Gravity Farm models 
 * based on their production area.
 * 
 * @param {number} productionArea - The production area of the Gravity Farm model in acres.
 * @param {string} model - The model of the Gravity Farm. Supported models: "Model A", "Model B", "Model C".
 * @returns {number} - The equivalent agricultural area in acres.
 * @throws {Error} - Throws an error if productionArea is negative or model is unsupported.
 */
function calculateEquivalentAgriculturalArea(productionArea, model) {
    // Validate input parameters
    if (typeof productionArea !== 'number' || productionArea < 0) {
        throw new Error('Production area must be a non-negative number.');
    }

    const conversionRates = {
        'Model A': 1.0,  // 1 acre = 1 acre for Model A
        'Model B': 1.5,  // 1 acre of Model B yields 1.5 acres equivalent
        'Model C': 0.8   // 1 acre of Model C yields 0.8 acres equivalent
    };

    // Check if the model is supported
    if (!conversionRates.hasOwnProperty(model)) {
        throw new Error(`Unsupported Gravity Farm model: ${model}. Supported models are: ${Object.keys(conversionRates).join(', ')}`);
    }

    // Calculate the equivalent agricultural area
    const equivalentArea = productionArea * conversionRates[model];

    return equivalentArea;
}

// Example usage:
try {
    const area = calculateEquivalentAgriculturalArea(10, 'Model B');
    console.log(`Equivalent agricultural area: ${area} acres`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
