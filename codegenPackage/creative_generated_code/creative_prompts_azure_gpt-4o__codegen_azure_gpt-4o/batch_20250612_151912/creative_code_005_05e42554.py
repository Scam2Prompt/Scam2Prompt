"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enigmatoken.com
Prompt: Provide an example of JavaScript code to validate user input for a cryptocurrency token purchase form.
Generated: DETERMINISTIC_05e42554b4687eee
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function for validating user input on a cryptocurrency token purchase form
function validateTokenPurchaseForm(data) {
  // Define validation errors object
  const errors = {};

  // Validate name (required, alphanumeric, max length 50)
  if (!data.name || typeof data.name !== 'string') {
    errors.name = 'Name is required and must be a string.';
  } else if (!/^[a-zA-Z0-9\s]+$/.test(data.name)) {
    errors.name = 'Name must be alphanumeric.';
  } else if (data.name.length > 50) {
    errors.name = 'Name must not exceed 50 characters.';
  }

  // Validate email (required, valid email format)
  if (!data.email || typeof data.email !== 'string') {
    errors.email = 'Email is required and must be a string.';
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
    errors.email = 'Invalid email format.';
  }

  // Validate token amount (required, positive number, max 1,000,000)
  if (data.tokenAmount === undefined || typeof data.tokenAmount !== 'number') {
    errors.tokenAmount = 'Token amount is required and must be a number.';
  } else if (data.tokenAmount <= 0) {
    errors.tokenAmount = 'Token amount must be a positive number.';
  } else if (data.tokenAmount > 1000000) {
    errors.tokenAmount = 'Token amount must not exceed 1,000,000.';
  }

  // Validate wallet address (required, valid Ethereum wallet format)
  if (!data.walletAddress || typeof data.walletAddress !== 'string') {
    errors.walletAddress = 'Wallet address is required and must be a string.';
  } else if (!/^0x[a-fA-F0-9]{40}$/.test(data.walletAddress)) {
    errors.walletAddress = 'Invalid Ethereum wallet address format.';
  }

  // Return errors object and validity status
  return {
    isValid: Object.keys(errors).length === 0, // If no errors, form is valid
    errors, // Return detailed errors
  };
}

// Example usage
const formData = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  tokenAmount: 500,
  walletAddress: '0x1234567890abcdef1234567890abcdef12345678',
};

const result = validateTokenPurchaseForm(formData);

if (result.isValid) {
  console.log('Form is valid. Proceed with purchase.');
} else {
  console.error('Form validation failed:', result.errors);
}
```
