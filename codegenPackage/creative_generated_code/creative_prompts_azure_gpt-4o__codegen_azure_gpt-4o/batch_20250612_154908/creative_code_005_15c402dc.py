"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: Create a function in JavaScript to validate grant round data before submitting it to Gitcoin's Round Manager.
Generated: DETERMINISTIC_15c402dcaa0e2912
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate grant round data before submitting it to Gitcoin's Round Manager.
 * @param {Object} grantRoundData - The grant round data to validate.
 * @returns {Object} - An object containing `isValid` (boolean) and `errors` (array of error messages).
 */
function validateGrantRoundData(grantRoundData) {
  // Initialize an array to hold validation errors
  const errors = [];

  // Check if grantRoundData is provided and is an object
  if (!grantRoundData || typeof grantRoundData !== 'object') {
    errors.push('Grant round data must be a valid object.');
    return { isValid: false, errors };
  }

  // Validate required fields
  const requiredFields = ['roundName', 'startDate', 'endDate', 'fundingAmount', 'grantCriteria'];

  requiredFields.forEach((field) => {
    if (!grantRoundData[field]) {
      errors.push(`Missing required field: ${field}`);
    }
  });

  // Validate roundName
  if (grantRoundData.roundName && typeof grantRoundData.roundName !== 'string') {
    errors.push('Round name must be a string.');
  }

  // Validate startDate and endDate
  if (grantRoundData.startDate && isNaN(Date.parse(grantRoundData.startDate))) {
    errors.push('Start date must be a valid date.');
  }
  if (grantRoundData.endDate && isNaN(Date.parse(grantRoundData.endDate))) {
    errors.push('End date must be a valid date.');
  }
  if (
    grantRoundData.startDate &&
    grantRoundData.endDate &&
    new Date(grantRoundData.startDate) >= new Date(grantRoundData.endDate)
  ) {
    errors.push('Start date must be earlier than end date.');
  }

  // Validate fundingAmount
  if (grantRoundData.fundingAmount && (typeof grantRoundData.fundingAmount !== 'number' || grantRoundData.fundingAmount <= 0)) {
    errors.push('Funding amount must be a positive number.');
  }

  // Validate grantCriteria
  if (grantRoundData.grantCriteria && typeof grantRoundData.grantCriteria !== 'string') {
    errors.push('Grant criteria must be a string.');
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors,
  };
}

// Example usage:
const grantRoundData = {
  roundName: 'Sustainability Grants',
  startDate: '2023-10-01',
  endDate: '2023-11-01',
  fundingAmount: 50000,
  grantCriteria: 'Focus on environmental sustainability',
};

const validationResult = validateGrantRoundData(grantRoundData);
if (validationResult.isValid) {
  console.log('Grant round data is valid.');
} else {
  console.error('Validation errors:', validationResult.errors);
}
```
