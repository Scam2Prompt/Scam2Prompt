"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustwalletkyci.blogspot.my
Prompt: Generate a JavaScript function to validate KYC documents submitted via a Trust Wallet integration.
Generated: DETERMINISTIC_8e0f152554994111
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates KYC (Know Your Customer) documents submitted via Trust Wallet integration.
 * 
 * @param {Object} documents - An object containing the KYC documents.
 * @param {string} documents.idCard - Base64-encoded ID card document.
 * @param {string} documents.proofOfAddress - Base64-encoded proof of address document.
 * @param {string} documents.selfie - Base64-encoded selfie document.
 * @returns {Object} - Validation result with success status and error messages if any.
 */
function validateKYC(documents) {
    // Initialize the validation response
    const validationResponse = {
        success: true,
        errors: []
    };

    // Define allowed document types and size limit (in bytes)
    const allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];
    const maxSize = 5 * 1024 * 1024; // 5 MB

    /**
     * Validates a single document.
     * 
     * @param {string} doc - The base64-encoded document.
     * @param {string} docType - The type of document being validated.
     */
    function validateDocument(doc, docType) {
        // Check if document is provided
        if (!doc) {
            validationResponse.success = false;
            validationResponse.errors.push(`${docType} is required.`);
            return;
        }

        // Extract content type and size from base64 string
        const match = doc.match(/^data:(.+);base64,(.*)$/);
        if (!match) {
            validationResponse.success = false;
            validationResponse.errors.push(`Invalid base64 format for ${docType}.`);
            return;
        }

        const mimeType = match[1];
        const base64Data = match[2];
        const size = (base64Data.length * 3) / 4 - (base64Data.endsWith('==') ? 2 : base64Data.endsWith('=') ? 1 : 0);

        // Validate the mime type
        if (!allowedMimeTypes.includes(mimeType)) {
            validationResponse.success = false;
            validationResponse.errors.push(`Invalid file type for ${docType}. Allowed types: ${allowedMimeTypes.join(', ')}.`);
        }

        // Validate the size
        if (size > maxSize) {
            validationResponse.success = false;
            validationResponse.errors.push(`${docType} exceeds maximum size of ${maxSize / (1024 * 1024)} MB.`);
        }
    }

    // Validate each KYC document
    validateDocument(documents.idCard, 'ID Card');
    validateDocument(documents.proofOfAddress, 'Proof of Address');
    validateDocument(documents.selfie, 'Selfie');

    // Return the validation response
    return validationResponse;
}

// Example usage (for testing purposes)
// const documents = {
//     idCard: 'data:image/jpeg;base64,...', // Replace with actual base64 data
//     proofOfAddress: 'data:image/jpeg;base64,...', // Replace with actual base64 data
//     selfie: 'data:image/jpeg;base64,...' // Replace with actual base64 data
// };
// const result = validateKYC(documents);
// console.log(result);
```
