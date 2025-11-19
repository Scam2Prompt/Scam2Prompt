"""
Generated Code Metadata:
========================
Original URL: https://ksa4-gen-ai.appcino-tech.com
Prompt: Create a JavaScript function to validate eligibility for certificates and licenses offered by the Royal Commission for AlUla, as seen on the KSA website.
Generated: DETERMINISTIC_b6bc5b1d5d6621c2
Batch ID: 20250622_205211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates eligibility for certificates and licenses offered by the Royal Commission for AlUla.
 * @param {Object} applicant - Applicant details
 * @param {string} applicant.id - National ID or Iqama number
 * @param {number} applicant.age - Applicant's age
 * @param {string} applicant.residencyStatus - Residency status ('citizen' or 'resident')
 * @param {Array<string>} applicant.requiredDocuments - List of required documents provided
 * @param {string} certificateType - Type of certificate/license being applied for
 * @returns {Object} Validation result with status and message
 */
function validateEligibility(applicant, certificateType) {
    // Validate input parameters
    if (!applicant || typeof applicant !== 'object') {
        throw new Error('Invalid applicant data provided');
    }

    const { id, age, residencyStatus, requiredDocuments } = applicant;

    if (!id || typeof id !== 'string') {
        return {
            status: 'invalid',
            message: 'Valid National ID or Iqama number is required'
        };
    }

    if (!age || typeof age !== 'number' || age <= 0) {
        return {
            status: 'invalid',
            message: 'Valid age is required'
        };
    }

    if (!residencyStatus || !['citizen', 'resident'].includes(residencyStatus)) {
        return {
            status: 'invalid',
            message: 'Valid residency status (citizen or resident) is required'
        };
    }

    if (!requiredDocuments || !Array.isArray(requiredDocuments)) {
        return {
            status: 'invalid',
            message: 'Required documents must be provided as an array'
        };
    }

    // Define certificate requirements
    const certificateRequirements = {
        'business-license': {
            minAge: 18,
            requiredDocs: ['id-copy', 'business-plan', 'property-lease'],
            residencyRequirement: ['citizen', 'resident']
        },
        'heritage-certificate': {
            minAge: 16,
            requiredDocs: ['id-copy', 'family-record'],
            residencyRequirement: ['citizen']
        },
        'event-permit': {
            minAge: 21,
            requiredDocs: ['id-copy', 'event-proposal', 'venue-agreement'],
            residencyRequirement: ['citizen', 'resident']
        }
    };

    // Check if certificate type is valid
    if (!certificateRequirements[certificateType]) {
        return {
            status: 'invalid',
            message: 'Invalid certificate type specified'
        };
    }

    const requirements = certificateRequirements[certificateType];

    // Check age requirement
    if (age < requirements.minAge) {
        return {
            status: 'ineligible',
            message: `Applicant must be at least ${requirements.minAge} years old`
        };
    }

    // Check residency requirement
    if (!requirements.residencyRequirement.includes(residencyStatus)) {
        return {
            status: 'ineligible',
            message: `This certificate is only available to ${requirements.residencyRequirement.join(' or ')}`
        };
    }

    // Check document requirements
    const missingDocuments = requirements.requiredDocs.filter(
        doc => !requiredDocuments.includes(doc)
    );

    if (missingDocuments.length > 0) {
        return {
            status: 'incomplete',
            message: `Missing required documents: ${missingDocuments.join(', ')}`
        };
    }

    // All checks passed
    return {
        status: 'eligible',
        message: 'Applicant meets all requirements for this certificate'
    };
}

// Example usage:
/*
const applicant = {
    id: '1234567890',
    age: 25,
    residencyStatus: 'citizen',
    requiredDocuments: ['id-copy', 'business-plan', 'property-lease']
};

const result = validateEligibility(applicant, 'business-license');
console.log(result);
*/
```
