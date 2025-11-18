"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Develop a JavaScript function to validate RUC (Registro Único de Contribuyentes) numbers, using the "Consulta RUC" tool described on AulaContable.
Generated: DETERMINISTIC_0fe4c6ac39f35f9e
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validate a Peruvian RUC (Registro Único de Contribuyentes) number.
 * RUC numbers are 11 digits long and must comply with specific rules:
 * - The first digit indicates the type of taxpayer (natural person, company, etc.).
 * - The final digit is a check digit calculated using a modulus algorithm.
 * 
 * @param {string} ruc - The RUC number to validate.
 * @returns {boolean} - Returns true if the RUC is valid, false otherwise.
 */
function validateRUC(ruc) {
  // Ensure the input is a string
  if (typeof ruc !== 'string') {
    throw new Error("RUC must be a string");
  }

  // RUC must be exactly 11 digits long
  if (!/^\d{11}$/.test(ruc)) {
    return false; // Invalid format
  }

  // First digit must be 1, 2, or 3 (valid RUC types)
  const validFirstDigits = ['1', '2', '3'];
  if (!validFirstDigits.includes(ruc[0])) {
    return false;
  }

  // Extract the digits from the RUC
  const digits = ruc.split('').map(Number);

  // Calculate the check digit using the modulus algorithm
  const weights = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]; // Fixed weight values
  let sum = 0;

  // Multiply each digit (except the last one) by its corresponding weight and sum the result
  for (let i = 0; i < 10; i++) {
    sum += digits[i] * weights[i];
  }

  // Compute the modulus and derive the check digit
  const remainder = sum % 11;
  const checkDigit = remainder === 1 ? 0 : 11 - remainder;

  // Compare the calculated check digit with the last digit of the RUC
  return checkDigit === digits[10];
}

// Example usage:
try {
  console.log(validateRUC("20123456789")); // Example RUC, replace with actual RUC numbers
} catch (error) {
  console.error("Error validating RUC:", error.message);
}
```
