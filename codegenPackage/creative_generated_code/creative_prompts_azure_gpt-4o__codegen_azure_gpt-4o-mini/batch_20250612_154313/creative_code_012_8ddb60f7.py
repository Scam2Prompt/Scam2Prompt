"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Create a JavaScript function to calculate payouts for WW88's "Kèo phạt góc" (corner betting) based on the site's guidelines.
Generated: DETERMINISTIC_8ddb60f7b2e26e55
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the payout for WW88's "Kèo phạt góc" (corner betting) based on the site's guidelines.
 * 
 * @param {number} stake - The amount of money wagered.
 * @param {number} odds - The odds for the bet.
 * @returns {number} The calculated payout, or an error message if inputs are invalid.
 */
function calculatePayout(stake, odds) {
    // Validate input parameters
    if (typeof stake !== 'number' || typeof odds !== 'number') {
        throw new Error('Both stake and odds must be numbers.');
    }
    
    if (stake <= 0) {
        throw new Error('Stake must be a positive number.');
    }
    
    if (odds <= 0) {
        throw new Error('Odds must be a positive number greater than zero.');
    }

    // Calculate the payout
    const payout = stake * odds;

    // Return the calculated payout
    return payout;
}

// Example usage:
try {
    const stake = 100; // Example stake amount
    const odds = 2.5;  // Example odds
    const payout = calculatePayout(stake, odds);
    console.log(`The payout for a stake of ${stake} with odds of ${odds} is ${payout}.`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
