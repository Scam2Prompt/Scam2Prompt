"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mong-life-mong.pages.dev
Prompt: Create a JavaScript function that calculates the total supply of Mongoose Coin ($MONG) based on the provided hard cap of 690 trillion.
Generated: DETERMINISTIC_a0d4bdbc23f6aaa7
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total supply of Mongoose Coin ($MONG)
 * based on a provided hard cap.
 *
 * @returns {string} The total supply of Mongoose Coin formatted as a string.
 * @throws {Error} Throws an error if the hard cap is not a positive number.
 */
function calculateTotalSupply() {
    const HARD_CAP = 690_000_000_000_000; // 690 trillion

    // Validate the hard cap
    if (typeof HARD_CAP !== 'number' || HARD_CAP <= 0) {
        throw new Error('Hard cap must be a positive number');
    }

    // Return the total supply formatted as a string
    return `${HARD_CAP.toLocaleString()} MONG`;
}

// Example usage
try {
    const totalSupply = calculateTotalSupply();
    console.log(`Total Supply of Mongoose Coin: ${totalSupply}`);
} catch (error) {
    console.error(`Error calculating total supply: ${error.message}`);
}
```
