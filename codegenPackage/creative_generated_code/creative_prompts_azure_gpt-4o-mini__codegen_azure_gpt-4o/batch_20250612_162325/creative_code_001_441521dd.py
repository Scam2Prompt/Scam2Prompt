"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerfairdrop.vercel.app
Prompt: Write a JavaScript function to calculate the percentage of tokens burned at launch for the $Slerf token, using the total supply and the amount burned mentioned on the Slerf Fair Drop page.
Generated: DETERMINISTIC_441521dd4f5e2a40
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
 * Function to calculate the percentage of tokens burned at launch.
 * 
 * @param {number} totalSupply - The total supply of the $Slerf tokens.
 * @param {number} amountBurned - The amount of tokens burned at launch.
 * @returns {string} - The percentage of tokens burned at launch formatted as a string.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateBurnPercentage(totalSupply, amountBurned) {
  // Input validation
  if (typeof totalSupply !== 'number' || typeof amountBurned !== 'number') {
    throw new Error('Both totalSupply and amountBurned must be numbers.');
  }
  
  if (totalSupply <= 0) {
    throw new Error('Total supply must be greater than 0.');
  }
  
  if (amountBurned < 0) {
    throw new Error('Amount burned cannot be negative.');
  }

  if (amountBurned > totalSupply) {
    throw new Error('Amount burned cannot exceed total supply.');
  }

  // Calculate the burn percentage
  const burnPercentage = (amountBurned / totalSupply) * 100;

  // Return the formatted percentage
  return `${burnPercentage.toFixed(2)}%`;
}

// Example usage
try {
  const totalSupply = 1000000; // Replace with the actual total supply
  const amountBurned = 250000; // Replace with the actual burned amount
  const burnPercentage = calculateBurnPercentage(totalSupply, amountBurned);
  console.log(`Burn Percentage: ${burnPercentage}`);
} catch (error) {
  console.error(`Error calculating burn percentage: ${error.message}`);
}
```
