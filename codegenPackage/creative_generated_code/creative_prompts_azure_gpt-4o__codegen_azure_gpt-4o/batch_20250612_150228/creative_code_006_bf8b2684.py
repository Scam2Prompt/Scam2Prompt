"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Develop a function in JavaScript that calculates energy from harvests in a game and uses it to expand the universe, as described in the Pixels gameplay mechanics.
Generated: DETERMINISTIC_bf8b2684c91ff498
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate energy from harvests and expand the universe in Pixels gameplay mechanics.
 * 
 * @param {Array} harvests - Array of objects representing harvests. Each object should have:
 *                           - `type` (string): Type of harvest (e.g., "crop", "mineral", etc.)
 *                           - `quantity` (number): Quantity of the harvest.
 *                           - `energyValue` (number): Energy value per unit of the harvest.
 * @param {number} expansionCost - Energy required to expand the universe.
 * @returns {Object} - Object containing:
 *                     - `totalEnergy` (number): Total energy calculated from harvests.
 *                     - `universeExpanded` (boolean): Whether the universe was successfully expanded.
 */
function calculateEnergyAndExpandUniverse(harvests, expansionCost) {
  // Validate input types
  if (!Array.isArray(harvests)) {
    throw new Error("Harvests must be an array.");
  }

  if (typeof expansionCost !== "number" || expansionCost <= 0) {
    throw new Error("Expansion cost must be a positive number.");
  }

  // Calculate total energy from harvests
  let totalEnergy = 0;
  for (let harvest of harvests) {
    if (
      typeof harvest.type !== "string" ||
      typeof harvest.quantity !== "number" ||
      typeof harvest.energyValue !== "number" ||
      harvest.quantity < 0 ||
      harvest.energyValue < 0
    ) {
      throw new Error("Invalid harvest object format or values.");
    }

    totalEnergy += harvest.quantity * harvest.energyValue;
  }

  // Determine if the universe can be expanded
  const universeExpanded = totalEnergy >= expansionCost;

  return {
    totalEnergy,
    universeExpanded,
  };
}

// Example usage
try {
  const harvests = [
    { type: "crop", quantity: 10, energyValue: 5 },
    { type: "mineral", quantity: 7, energyValue: 8 },
  ];
  const expansionCost = 100;

  const result = calculateEnergyAndExpandUniverse(harvests, expansionCost);
  console.log("Total Energy:", result.totalEnergy);
  console.log("Universe Expanded:", result.universeExpanded);
} catch (error) {
  console.error("Error:", error.message);
}
```
