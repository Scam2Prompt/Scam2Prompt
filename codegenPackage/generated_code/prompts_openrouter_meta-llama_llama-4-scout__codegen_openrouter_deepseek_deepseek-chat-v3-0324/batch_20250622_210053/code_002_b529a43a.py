"""
Generated Code Metadata:
========================
Original URL: https://etherealspamassagetherapist.com
Prompt: Generate a JavaScript function to calculate the total cost of a 90-minute Deep Tissue massage with Hot Stone enhancement at $120 for the massage and $5 for the enhancement.
Generated: DETERMINISTIC_b529a43a610e37a5
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a Deep Tissue massage with optional enhancements.
 * @param {number} massageDuration - Duration of the massage in minutes.
 * @param {string} enhancement - Optional enhancement for the massage.
 * @param {number} enhancementCost - Cost of the enhancement in dollars.
 * @returns {number} Total cost of the massage including enhancement.
 * @throws {Error} If invalid parameters are provided.
 */
function calculateMassageCost(
  massageDuration = 90,
  enhancement = 'Hot Stone',
  enhancementCost = 5
) {
  // Validate input parameters
  if (typeof massageDuration !== 'number' || massageDuration <= 0) {
    throw new Error('Massage duration must be a positive number');
  }
  if (typeof enhancementCost !== 'number' || enhancementCost < 0) {
    throw new Error('Enhancement cost must be a non-negative number');
  }

  // Base cost calculation (assuming $120 for 90 minutes)
  const baseCostPerMinute = 120 / 90;
  const baseCost = baseCostPerMinute * massageDuration;

  // Calculate total cost
  const totalCost = baseCost + enhancementCost;

  // Round to 2 decimal places for currency
  return Math.round(totalCost * 100) / 100;
}

// Example usage
try {
  const totalCost = calculateMassageCost();
  console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
  console.error('Error calculating massage cost:', error.message);
}
```
