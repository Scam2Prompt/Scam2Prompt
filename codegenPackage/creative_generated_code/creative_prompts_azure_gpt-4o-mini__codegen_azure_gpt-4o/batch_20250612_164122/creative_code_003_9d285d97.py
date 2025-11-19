"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Create a JavaScript function that calculates rush charges for environmental testing based on A & B Labs' pricing structure.
Generated: DETERMINISTIC_9d285d97c6d52c3a
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate rush charges for environmental testing based on A & B Labs' pricing structure.
 * 
 * Pricing Structure:
 * - Standard turnaround time: $0 rush charge
 * - 3-day turnaround time: $50 rush charge
 * - 2-day turnaround time: $100 rush charge
 * - 1-day turnaround time: $150 rush charge
 * - Same-day turnaround time: $200 rush charge
 * 
 * @param {number} turnaroundTime - Turnaround time in days (integer).
 * @returns {number} - The rush charge associated with the given turnaround time.
 * @throws {Error} - Throws an error if the input is invalid or unsupported.
 */
function calculateRushCharges(turnaroundTime) {
  // Validate input
  if (typeof turnaroundTime !== 'number' || !Number.isInteger(turnaroundTime) || turnaroundTime < 0) {
    throw new Error('Invalid turnaround time. It must be a positive integer.');
  }

  // Define rush charges based on turnaround time
  const rushCharges = {
    0: 200, // Same-day turnaround time
    1: 150, // 1-day turnaround time
    2: 100, // 2-day turnaround time
    3: 50,  // 3-day turnaround time
  };

  // Return the corresponding rush charge or 0 for standard turnaround time
  return rushCharges[turnaroundTime] || 0;
}

// Example usage
try {
  console.log(calculateRushCharges(2));  // Output: 100
  console.log(calculateRushCharges(5));  // Output: 0 (Standard turnaround time)
} catch (error) {
  console.error(error.message);
}
```
