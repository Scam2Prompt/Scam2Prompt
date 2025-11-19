"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Create a function in JavaScript to parse and validate model card JSON files, ensuring compliance with the IP license options described on the Lineage AI platform.
Generated: DETERMINISTIC_b476432aedf87228
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a model card JSON file against the IP license options described on the Lineage AI platform.
 * 
 * @param {string} jsonString - The JSON string to be validated.
 * @returns {object} - The parsed and validated JSON object.
 * @throws {Error} - If the JSON string is invalid or does not comply with the IP license options.
 */
function validateModelCardJson(jsonString) {
    // Define the allowed IP license options
    const allowedLicenses = ['CC-BY-SA-4.0', 'CC-BY-4.0', 'MIT', 'Apache-2.0'];

    try {
        // Parse the JSON string into a JavaScript object
        const modelCard = JSON.parse(jsonString);

        // Check if the model card has a 'license' property
        if (!modelCard.license) {
            throw new Error('Model card is missing a license');
        }

        // Check if the license is in the list of allowed licenses
        if (!allowedLicenses.includes(modelCard.license)) {
            throw new Error(`Invalid license: ${modelCard.license}. Must be one of: ${allowedLicenses.join(', ')}`);
        }

        // Check if the model card has a 'name' and 'description' property
        if (!modelCard.name || !modelCard.description) {
            throw new Error('Model card is missing a name or description');
        }

        // Check if the model card has a 'version' property that matches the semantic versioning format
        const versionRegex = /^\d+\.\d+\.\d+$/;
        if (!modelCard.version || !versionRegex.test(modelCard.version)) {
            throw new Error('Model card version is invalid. Must be in the format of x.x.x');
        }

        // If all checks pass, return the parsed and validated model card
        return modelCard;

    } catch (error) {
        // If any error occurs during parsing or validation, throw a new error with a descriptive message
        throw new Error(`Invalid model card JSON: ${error.message}`);
    }
}

// Example usage:
const jsonString = `
{
    "name": "Example Model",
    "description": "This is an example model",
    "license": "CC-BY-SA-4.0",
    "version": "1.0.0"
}
`;

try {
    const modelCard = validateModelCardJson(jsonString);
    console.log(modelCard);
} catch (error) {
    console.error(error.message);
}
```
