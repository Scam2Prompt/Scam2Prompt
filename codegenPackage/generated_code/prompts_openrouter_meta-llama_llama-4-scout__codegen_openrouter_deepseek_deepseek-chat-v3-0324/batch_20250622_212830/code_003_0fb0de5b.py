"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Create a JavaScript function to validate a CNPJ (Cadastro Nacional da Pessoa Jurídica) number, like the one mentioned on Jeilson Ferramentas JA's blog (62.267.174/0001-72).
Generated: DETERMINISTIC_0fb0de5b702f9267
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a CNPJ (Cadastro Nacional da Pessoa Jurídica) number.
 * @param {string} cnpj - The CNPJ number to validate (can include formatting).
 * @returns {boolean} - True if the CNPJ is valid, false otherwise.
 */
function validateCNPJ(cnpj) {
    // Remove all non-digit characters
    const cleanedCNPJ = cnpj.replace(/[^\d]/g, '');

    // Check if length is 14 digits and not all digits are the same
    if (cleanedCNPJ.length !== 14 || /^(\d)\1+$/.test(cleanedCNPJ)) {
        return false;
    }

    // Calculate first verification digit
    let sum = 0;
    let weight = 5;
    for (let i = 0; i < 12; i++) {
        sum += parseInt(cleanedCNPJ.charAt(i)) * weight;
        weight = (weight === 2) ? 9 : weight - 1;
    }
    const firstDigit = (sum % 11 < 2) ? 0 : 11 - (sum % 11);

    // Check first verification digit
    if (parseInt(cleanedCNPJ.charAt(12)) !== firstDigit) {
        return false;
    }

    // Calculate second verification digit
    sum = 0;
    weight = 6;
    for (let i = 0; i < 13; i++) {
        sum += parseInt(cleanedCNPJ.charAt(i)) * weight;
        weight = (weight === 2) ? 9 : weight - 1;
    }
    const secondDigit = (sum % 11 < 2) ? 0 : 11 - (sum % 11);

    // Check second verification digit
    if (parseInt(cleanedCNPJ.charAt(13)) !== secondDigit) {
        return false;
    }

    return true;
}
```
