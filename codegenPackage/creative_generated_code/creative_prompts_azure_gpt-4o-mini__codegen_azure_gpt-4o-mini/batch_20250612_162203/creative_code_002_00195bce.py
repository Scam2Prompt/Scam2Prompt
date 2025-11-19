"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Generate a JavaScript function that converts FTM amounts into DRE tokens based on the presale rates provided on the DRE presale page.
Generated: DETERMINISTIC_00195bce5e00079d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Converts FTM amounts to DRE tokens based on the presale rates.
 * 
 * @param {number} ftmAmount - The amount of FTM to be converted.
 * @param {number} presaleRate - The rate at which FTM is converted to DRE tokens.
 * @returns {number} - The equivalent amount of DRE tokens.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function convertFTMToDRE(ftmAmount, presaleRate) {
    // Validate inputs
    if (typeof ftmAmount !== 'number' || typeof presaleRate !== 'number') {
        throw new Error('Both ftmAmount and presaleRate must be numbers.');
    }

    if (ftmAmount < 0 || presaleRate <= 0) {
        throw new Error('ftmAmount must be non-negative and presaleRate must be positive.');
    }

    // Calculate DRE tokens
    const dreAmount = ftmAmount * presaleRate;

    // Return the calculated amount of DRE tokens
    return dreAmount;
}

// Example usage
try {
    const ftmAmount = 10; // Amount of FTM to convert
    const presaleRate = 100; // Presale rate for conversion
    const dreTokens = convertFTMToDRE(ftmAmount, presaleRate);
    console.log(`Converted ${ftmAmount} FTM to ${dreTokens} DRE tokens.`);
} catch (error) {
    console.error('Error converting FTM to DRE:', error.message);
}
```
