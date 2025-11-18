"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Create a function in JavaScript to parse and validate model card JSON files, ensuring compliance with the IP license options described on the Lineage AI platform.
Generated: DETERMINISTIC_b476432aedf87228
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to parse and validate a model card JSON file for compliance
 * with IP license options described on the Lineage AI platform.
 *
 * @param {string} jsonString - The JSON string representing the model card.
 * @returns {Object} An object containing the validation status and any errors found.
 *
 * Example usage:
 * const result = validateModelCard(jsonString);
 * if (result.isValid) {
 *   console.log("Model card is valid!");
 * } else {
 *   console.error("Validation errors:", result.errors);
 * }
 */
function validateModelCard(jsonString) {
  const allowedLicenses = [
    "Apache-2.0",
    "MIT",
    "GPL-3.0",
    "BSD-3-Clause",
    "CC-BY-4.0",
    "Proprietary"
  ]; // List of valid IP license options

  let parsedData;
  const errors = [];

  try {
    // Parse the JSON string
    parsedData = JSON.parse(jsonString);
  } catch (error) {
    errors.push("Invalid JSON format: " + error.message);
    return { isValid: false, errors };
  }

  // Validate required fields
  if (!parsedData.modelName || typeof parsedData.modelName !== "string") {
    errors.push("Missing or invalid 'modelName' field. Must be a non-empty string.");
  }

  if (!parsedData.version || typeof parsedData.version !== "string") {
    errors.push("Missing or invalid 'version' field. Must be a string.");
  }

  if (!parsedData.license || typeof parsedData.license !== "string") {
    errors.push("Missing or invalid 'license' field. Must be a string.");
  } else if (!allowedLicenses.includes(parsedData.license)) {
    errors.push(
      `Invalid license '${parsedData.license}'. Allowed licenses are: ${allowedLicenses.join(", ")}.`
    );
  }

  if (!parsedData.description || typeof parsedData.description !== "string") {
    errors.push("Missing or invalid 'description' field. Must be a non-empty string.");
  }

  // Return validation results
  const isValid = errors.length === 0;
  return { isValid, errors };
}

// Example usage:
// const jsonString = '{"modelName":"ExampleModel","version":"1.0","license":"MIT","description":"This is an example model card."}';
// const result = validateModelCard(jsonString);
// console.log(result);
```
