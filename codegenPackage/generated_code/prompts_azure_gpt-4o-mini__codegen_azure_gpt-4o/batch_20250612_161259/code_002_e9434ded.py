"""
Generated Code Metadata:
========================
Original URL: https://richnaturalfoods.com
Prompt: Create an example of a JavaScript function that validates deposit amounts for a service like Situs Gacor, ensuring they meet the minimum requirement of 5000.
Generated: DETERMINISTIC_e9434dedf0a01580
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a deposit amount to ensure it meets the minimum requirement.
 * 
 * @param {number} depositAmount - The amount to be deposited.
 * @returns {Object} - An object containing validation status and a message.
 */
function validateDepositAmount(depositAmount) {
  // Define the minimum deposit requirement
  const MIN_DEPOSIT_AMOUNT = 5000;

  // Check if the input is a valid number
  if (typeof depositAmount !== 'number' || isNaN(depositAmount)) {
    return {
      isValid: false,
      message: 'Invalid input: Deposit amount must be a valid number.'
    };
  }

  // Check if the deposit amount meets the minimum requirement
  if (depositAmount < MIN_DEPOSIT_AMOUNT) {
    return {
      isValid: false,
      message: `Deposit amount must be at least ${MIN_DEPOSIT_AMOUNT}.`
    };
  }

  // If all validations pass, return success
  return {
    isValid: true,
    message: 'Deposit amount is valid.'
  };
}

// Example usage:
const result = validateDepositAmount(6000);
console.log(result); // { isValid: true, message: 'Deposit amount is valid.' }
```
