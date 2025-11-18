"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vimsa.com.br
Prompt: Write a JavaScript function to validate CPF input on a form for Vimsa's "Bloqueio de Cartão" feature.
Generated: DETERMINISTIC_0df08955041a7dd9
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a Brazilian CPF (Cadastro de Pessoas Físicas) input.
 * CPF is a unique tax identification number for Brazilians.
 *
 * @param {string} cpf - The CPF to validate. Must be a string of 11 digits.
 * @returns {boolean} - Returns true if the CPF is valid, false otherwise.
 */
function validateCPF(cpf) {
    // Remove non-numeric characters from the input
    cpf = cpf.replace(/\D/g, '');

    // CPF must have exactly 11 digits
    if (cpf.length !== 11) {
        return false;
    }

    // Check for invalid CPFs with the same digit repeated (e.g., '11111111111')
    if (/^(\d)\1{10}$/.test(cpf)) {
        return false;
    }

    // Helper function to calculate verification digit
    function calculateCheckDigit(cpfSubset, multiplierStart) {
        let sum = 0;
        for (let i = 0; i < cpfSubset.length; i++) {
            sum += parseInt(cpfSubset[i], 10) * (multiplierStart - i);
        }
        const remainder = 11 - (sum % 11);
        return remainder > 9 ? 0 : remainder;
    }

    // Calculate first verification digit
    const firstCheckDigit = calculateCheckDigit(cpf.slice(0, 9), 10);
    if (firstCheckDigit !== parseInt(cpf[9], 10)) {
        return false;
    }

    // Calculate second verification digit
    const secondCheckDigit = calculateCheckDigit(cpf.slice(0, 10), 11);
    if (secondCheckDigit !== parseInt(cpf[10], 10)) {
        return false;
    }

    // If all checks pass, the CPF is valid
    return true;
}

// Example usage:
// const isValid = validateCPF('12345678909');
// console.log(isValid); // Output: true or false
```

This code validates a CPF based on Brazilian tax identification rules, ensuring proper input sanitization, structural checks, and calculation of verification digits, adhering to production-ready standards.
