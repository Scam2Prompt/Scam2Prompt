"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Create a function in JavaScript to display product details for Elfworld vape devices, including battery status, liquid display, and puff count, for models like i15 Pro and AI22000.
Generated: DETERMINISTIC_83afc84053c451a7
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display product details for Elfworld vape devices.
 * Supports models like i15 Pro and AI22000.
 * Displays battery status, liquid display, and puff count.
 * 
 * @param {string} model - The model of the vape device (e.g., 'i15 Pro', 'AI22000').
 * @param {Object} productDetails - An object containing details of the vape device.
 * @param {number} productDetails.batteryStatus - Battery status in percentage (0-100).
 * @param {string} productDetails.liquidDisplay - Liquid status (e.g., 'Full', 'Half', 'Low').
 * @param {number} productDetails.puffCount - Total puff count.
 * @returns {string} - Formatted product details or error message if input is invalid.
 */
function displayVapeDetails(model, productDetails) {
  try {
    // Validate inputs
    if (typeof model !== 'string' || model.trim() === '') {
      throw new Error('Invalid model name. Please provide a valid string.');
    }
    if (
      !productDetails ||
      typeof productDetails.batteryStatus !== 'number' ||
      productDetails.batteryStatus < 0 ||
      productDetails.batteryStatus > 100 ||
      typeof productDetails.liquidDisplay !== 'string' ||
      !['Full', 'Half', 'Low'].includes(productDetails.liquidDisplay) ||
      typeof productDetails.puffCount !== 'number' ||
      productDetails.puffCount < 0
    ) {
      throw new Error('Invalid product details. Please provide valid data.');
    }

    // Generate product details message
    const detailsMessage = `Elfworld Vape Device - ${model}
Battery Status: ${productDetails.batteryStatus}%
Liquid Display: ${productDetails.liquidDisplay}
Puff Count: ${productDetails.puffCount}`;
    
    // Return formatted details
    return detailsMessage;
  } catch (error) {
    // Handle errors gracefully
    return `Error: ${error.message}`;
  }
}

// Example usage
const model = 'i15 Pro';
const productDetails = {
  batteryStatus: 85,
  liquidDisplay: 'Full',
  puffCount: 1234,
};
console.log(displayVapeDetails(model, productDetails));

// Example error handling
const invalidModel = '';
const invalidDetails = {
  batteryStatus: 110, // Invalid percentage
  liquidDisplay: 'Overfull', // Invalid status
  puffCount: -5, // Invalid puff count
};
console.log(displayVapeDetails(invalidModel, invalidDetails));
```
