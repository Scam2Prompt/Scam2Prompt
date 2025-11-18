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
 * Validates a RUC (Registro Único de Contribuyentes) number.
 * The RUC is a tax identification number in Peru, typically 11 digits long.
 * 
 * @param {string} ruc - The RUC number to validate.
 * @returns {boolean} - Returns true if the RUC is valid, false otherwise.
 * @throws {Error} - Throws an error if the input is not a string or has invalid length.
 */
function validateRUC(ruc) {
    // Check if the input is a string
    if (typeof ruc !== 'string') {
        throw new Error('Invalid input: RUC must be a string.');
    }

    // Remove any spaces and ensure it's trimmed
    ruc = ruc.trim();

    // RUC must be 11 digits
    if (ruc.length !== 11 || !/^\d+$/.test(ruc)) {
        return false;
    }

    // Calculate check digit based on the first 10 digits
    const digits = ruc.split('').map(Number);
    const weights = [3, 2, 7, 6, 5, 4, 3, 2, 1, 0];
    let sum = 0;

    for (let i = 0; i < 10; i++) {
        sum += digits[i] * weights[i];
    }

    // Determine the check digit
    const remainder = sum % 11;
    const checkDigit = remainder < 2 ? 0 : 11 - remainder;

    // Compare calculated check digit to the actual check digit
    return checkDigit === digits[10];
}

// Example usage:
try {
    const rucNumber = '20456789012';
    const isValid = validateRUC(rucNumber);
    console.log(`RUC ${rucNumber} is valid: ${isValid}`);
} catch (error) {
    console.error(error.message);
}
```
