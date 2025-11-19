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
 * Validates a model card JSON object against the Lineage AI platform's IP license requirements.
 * @param {Object} modelCard - The model card JSON object to validate.
 * @returns {Object} An object containing validation results: { isValid: boolean, errors: string[] }
 */
function validateModelCard(modelCard) {
    const errors = [];
    const validLicenses = [
        'Apache-2.0',
        'MIT',
        'BSD-3-Clause',
        'GPL-3.0',
        'LGPL-3.0',
        'AGPL-3.0',
        'MPL-2.0',
        'Boost-1.0',
        'Unlicense',
        'CC-BY-4.0',
        'CC-BY-SA-4.0',
        'CC0-1.0',
        'ODC-BY-1.0',
        'Artistic-2.0',
        'Proprietary',
        'Other'
    ];

    // Check if modelCard is an object
    if (typeof modelCard !== 'object' || modelCard === null) {
        errors.push('Model card must be a valid JSON object');
        return { isValid: false, errors };
    }

    // Validate required fields
    const requiredFields = ['name', 'version', 'license'];
    for (const field of requiredFields) {
        if (!modelCard[field]) {
            errors.push(`Missing required field: ${field}`);
        }
    }

    // Validate license field
    if (modelCard.license) {
        if (!validLicenses.includes(modelCard.license)) {
            errors.push(`Invalid license. Must be one of: ${validLicenses.join(', ')}`);
        }

        if (modelCard.license === 'Proprietary' && !modelCard.license_details) {
            errors.push('Proprietary license requires license_details field');
        }

        if (modelCard.license === 'Other' && !modelCard.license_details) {
            errors.push('Other license requires license_details field');
        }
    }

    // Validate version format (semver-like)
    if (modelCard.version && !/^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?$/.test(modelCard.version)) {
        errors.push('Version must follow semantic versioning format (e.g., 1.0.0 or 1.0.0-alpha)');
    }

    // Validate optional fields if present
    if (modelCard.license_details && typeof modelCard.license_details !== 'string') {
        errors.push('license_details must be a string if provided');
    }

    if (modelCard.citation && typeof modelCard.citation !== 'string') {
        errors.push('citation must be a string if provided');
    }

    return {
        isValid: errors.length === 0,
        errors
    };
}

/**
 * Parses and validates a model card JSON string.
 * @param {string} jsonString - The JSON string to parse and validate.
 * @returns {Object} An object containing: { modelCard: Object|null, isValid: boolean, errors: string[] }
 */
function parseAndValidateModelCard(jsonString) {
    try {
        const modelCard = JSON.parse(jsonString);
        const validationResult = validateModelCard(modelCard);
        
        return {
            modelCard: validationResult.isValid ? modelCard : null,
            isValid: validationResult.isValid,
            errors: validationResult.errors
        };
    } catch (error) {
        return {
            modelCard: null,
            isValid: false,
            errors: [`Invalid JSON: ${error.message}`]
        };
    }
}

// Export functions for use in other modules
module.exports = {
    validateModelCard,
    parseAndValidateModelCard
};
```
