"""
Generated Code Metadata:
========================
Original URL: https://celesfia.site
Prompt: "Write a JavaScript function that checks for compliance with privacy policies in user data handling."
Generated: DETERMINISTIC_738092787df9f767
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if user data handling complies with specified privacy policies.
 * @param {Object} userData - The user data object to be checked.
 * @param {Object} policy - The privacy policy requirements.
 * @param {Array<string>} policy.requiredFields - Fields that must be present.
 * @param {Array<string>} policy.sensitiveFields - Fields that require encryption.
 * @param {Object} policy.retentionPolicy - Data retention requirements.
 * @param {number} policy.retentionPolicy.maxDays - Maximum days data can be retained.
 * @returns {Object} An object containing compliance status and issues found.
 */
function checkPrivacyCompliance(userData, policy) {
    const result = {
        isCompliant: true,
        issues: []
    };

    // Validate input parameters
    if (!userData || typeof userData !== 'object') {
        throw new Error('Invalid user data: must be an object');
    }
    if (!policy || typeof policy !== 'object') {
        throw new Error('Invalid policy: must be an object');
    }

    // Check required fields
    if (policy.requiredFields && Array.isArray(policy.requiredFields)) {
        policy.requiredFields.forEach(field => {
            if (!(field in userData)) {
                result.isCompliant = false;
                result.issues.push(`Missing required field: ${field}`);
            }
        });
    }

    // Check sensitive fields encryption
    if (policy.sensitiveFields && Array.isArray(policy.sensitiveFields)) {
        policy.sensitiveFields.forEach(field => {
            if (field in userData) {
                const value = userData[field];
                if (typeof value === 'string' && !value.startsWith('enc:')) {
                    result.isCompliant = false;
                    result.issues.push(`Sensitive field not encrypted: ${field}`);
                }
            }
        });
    }

    // Check data retention policy
    if (policy.retentionPolicy && typeof policy.retentionPolicy === 'object') {
        const { maxDays } = policy.retentionPolicy;
        if (typeof maxDays === 'number' && userData.createdAt) {
            const createdAt = new Date(userData.createdAt);
            if (isNaN(createdAt.getTime())) {
                result.isCompliant = false;
                result.issues.push('Invalid createdAt date format');
            } else {
                const currentDate = new Date();
                const daysOld = Math.floor((currentDate - createdAt) / (1000 * 60 * 60 * 24));
                if (daysOld > maxDays) {
                    result.isCompliant = false;
                    result.issues.push(`Data retention exceeded by ${daysOld - maxDays} days`);
                }
            }
        }
    }

    return result;
}

// Example usage:
/*
const userData = {
    name: 'John Doe',
    email: 'enc:abc123',
    ssn: 'enc:xyz789',
    createdAt: '2023-01-01'
};

const policy = {
    requiredFields: ['name', 'email', 'ssn'],
    sensitiveFields: ['email', 'ssn'],
    retentionPolicy: {
        maxDays: 365
    }
};

const complianceResult = checkPrivacyCompliance(userData, policy);
console.log(complianceResult);
*/
```
