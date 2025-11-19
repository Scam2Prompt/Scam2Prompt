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
 * Function to calculate the equivalent agricultural area for Gravity Farm models.
 * 
 * @param {string} model - The Gravity Farm model name (e.g., "ModelA", "ModelB").
 * @param {number} productionArea - The production area of the model in square meters.
 * @returns {number} The equivalent agricultural area in square meters.
 * @throws {Error} Throws an error if the model is unsupported or if the productionArea is invalid.
 */

function calculateEquivalentArea(model, productionArea) {
  // Validate input: ensure model is a string and productionArea is a positive number
  if (typeof model !== 'string' || productionArea <= 0 || isNaN(productionArea)) {
    throw new Error("Invalid input. Model must be a string and productionArea must be a positive number.");
  }

  // Define coefficients for various Gravity Farm models
  const modelCoefficients = {
    ModelA: 1.5, // ModelA produces 1.5x equivalent agricultural area
    ModelB: 2.0, // ModelB produces 2.0x equivalent agricultural area
    ModelC: 2.5, // ModelC produces 2.5x equivalent agricultural area
  };

  // Check if the provided model is supported
  if (!modelCoefficients.hasOwnProperty(model)) {
    throw new Error(`Unsupported model: ${model}. Supported models are ${Object.keys(modelCoefficients).join(", ")}.`);
  }

  // Calculate the equivalent agricultural area
  const coefficient = modelCoefficients[model];
  const equivalentArea = productionArea * coefficient;

  // Return the calculated equivalent agricultural area
  return equivalentArea;
}

// Example Usage:
// try {
//   const result = calculateEquivalentArea("ModelB", 100);
//   console.log(`Equivalent Agricultural Area: ${result} sq meters`);
// } catch (error) {
//   console.error(error.message);
// }
```
