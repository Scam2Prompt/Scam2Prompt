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
 * Validates a Brazilian CPF (Cadastro de Pessoas Físicas) number.
 * CPF is an identification number issued to Brazilian citizens and residents.
 *
 * @param {string} cpf - The CPF number to validate.
 * @returns {boolean} - Returns true if the CPF is valid, false otherwise.
 */
function validateCPF(cpf) {
    // Remove non-numeric characters from the CPF
    cpf = cpf.replace(/\D/g, '');

    // Check if the CPF is of valid length
    if (cpf.length !== 11) {
        return false;
    }

    // Check for repeated digits (invalid CPFs)
    const invalidCPFs = [
        '00000000000', '11111111111', '22222222222', '33333333333',
        '44444444444', '55555555555', '66666666666', '77777777777',
        '88888888888', '99999999999'
    ];
    if (invalidCPFs.includes(cpf)) {
        return false;
    }

    // Validate CPF using the checksum algorithm
    const calculateDigit = (base) => {
        let sum = 0;
        let weight = base.length + 1;

        for (let i = 0; i < base.length; i++) {
            sum += parseInt(base.charAt(i), 10) * weight;
            weight--;
        }

        const remainder = (sum * 10) % 11;
        return remainder === 10 || remainder === 11 ? 0 : remainder;
    };

    // Calculate the first verification digit
    const firstPart = cpf.slice(0, 9);
    const firstDigit = calculateDigit(firstPart);
    if (firstDigit !== parseInt(cpf.charAt(9), 10)) {
        return false;
    }

    // Calculate the second verification digit
    const secondPart = cpf.slice(0, 10);
    const secondDigit = calculateDigit(secondPart);
    if (secondDigit !== parseInt(cpf.charAt(10), 10)) {
        return false;
    }

    // CPF is valid
    return true;
}

// Example usage:
try {
    const cpfInput = "123.456.789-09"; // Sample CPF input
    if (validateCPF(cpfInput)) {
        console.log("Valid CPF");
    } else {
        console.log("Invalid CPF");
    }
} catch (error) {
    console.error("An error occurred during CPF validation:", error);
}
```
