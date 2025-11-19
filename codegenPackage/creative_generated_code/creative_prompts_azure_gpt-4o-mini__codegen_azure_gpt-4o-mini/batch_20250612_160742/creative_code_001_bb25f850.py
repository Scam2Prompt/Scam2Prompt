"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roninwallet-login4.godaddysites.com
Prompt: Write a JavaScript function that validates user input for a real estate inquiry form, ensuring it captures details like budget and property type as mentioned in the Ronin Wallet services.
Generated: DETERMINISTIC_bb25f85019a8cedb
Batch ID: 20250612_160742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a real estate inquiry form.
 *
 * @param {Object} inquiryData - The inquiry data object containing user input.
 * @param {number} inquiryData.budget - The user's budget for the property.
 * @param {string} inquiryData.propertyType - The type of property being inquired about.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRealEstateInquiry(inquiryData) {
    const validationResults = {
        isValid: true,
        errors: []
    };

    // Validate budget
    if (typeof inquiryData.budget !== 'number' || inquiryData.budget <= 0) {
        validationResults.isValid = false;
        validationResults.errors.push('Budget must be a positive number.');
    }

    // Validate property type
    const validPropertyTypes = ['house', 'apartment', 'condo', 'land'];
    if (!inquiryData.propertyType || !validPropertyTypes.includes(inquiryData.propertyType.toLowerCase())) {
        validationResults.isValid = false;
        validationResults.errors.push(`Property type must be one of the following: ${validPropertyTypes.join(', ')}.`);
    }

    return validationResults;
}

// Example usage:
const inquiry = {
    budget: 250000,
    propertyType: 'house'
};

const result = validateRealEstateInquiry(inquiry);

if (!result.isValid) {
    console.error('Validation failed:', result.errors);
} else {
    console.log('Validation successful:', inquiry);
}
```
