"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Develop a code snippet in JavaScript to validate the documents required for the Water Tank & Domestic Water Pump Grant New Scheme 2023-2024 offered by DBM.
Generated: DETERMINISTIC_2c9285f1e1d4ede6
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates the documents required for the Water Tank & Domestic Water Pump Grant New Scheme 2023-2024.
 * 
 * @param {Object} documents - An object containing the required documents.
 * @param {string} documents.applicantName - The name of the applicant.
 * @param {string} documents.icNumber - The IC number of the applicant.
 * @param {string} documents.address - The address of the applicant.
 * @param {string} documents.waterTankReceipt - The receipt number for the water tank purchase.
 * @param {string} documents.domesticWaterPumpReceipt - The receipt number for the domestic water pump purchase.
 * @param {string} documents.incomeProof - The income proof document number.
 * @returns {Object} An object containing a boolean indicating whether the documents are valid and an array of error messages.
 */

function validateDocuments(documents) {
    const requiredFields = [
        'applicantName',
        'icNumber',
        'address',
        'waterTankReceipt',
        'domesticWaterPumpReceipt',
        'incomeProof'
    ];

    let isValid = true;
    let errorMessages = [];

    // Check if all required fields are present
    requiredFields.forEach(field => {
        if (!(field in documents)) {
            isValid = false;
            errorMessages.push(`Missing required field: ${field}`);
        }
    });

    // Validate applicant name
    if (isValid && typeof documents.applicantName !== 'string' || documents.applicantName.trim() === '') {
        isValid = false;
        errorMessages.push('Applicant name must be a non-empty string');
    }

    // Validate IC number
    if (isValid && !/^[0-9]{12}$/.test(documents.icNumber)) {
        isValid = false;
        errorMessages.push('IC number must be 12 digits');
    }

    // Validate address
    if (isValid && typeof documents.address !== 'string' || documents.address.trim() === '') {
        isValid = false;
        errorMessages.push('Address must be a non-empty string');
    }

    // Validate water tank receipt
    if (isValid && typeof documents.waterTankReceipt !== 'string' || documents.waterTankReceipt.trim() === '') {
        isValid = false;
        errorMessages.push('Water tank receipt must be a non-empty string');
    }

    // Validate domestic water pump receipt
    if (isValid && typeof documents.domesticWaterPumpReceipt !== 'string' || documents.domesticWaterPumpReceipt.trim() === '') {
        isValid = false;
        errorMessages.push('Domestic water pump receipt must be a non-empty string');
    }

    // Validate income proof
    if (isValid && typeof documents.incomeProof !== 'string' || documents.incomeProof.trim() === '') {
        isValid = false;
        errorMessages.push('Income proof must be a non-empty string');
    }

    return { isValid, errorMessages };
}

// Example usage
try {
    const documents = {
        applicantName: 'John Doe',
        icNumber: '123456789012',
        address: '123 Main Street',
        waterTankReceipt: 'WT12345',
        domesticWaterPumpReceipt: 'DWP67890',
        incomeProof: 'IP123456'
    };

    const { isValid, errorMessages } = validateDocuments(documents);

    if (isValid) {
        console.log('Documents are valid');
    } else {
        console.log('Documents are invalid:');
        errorMessages.forEach(error => console.log(error));
    }
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
