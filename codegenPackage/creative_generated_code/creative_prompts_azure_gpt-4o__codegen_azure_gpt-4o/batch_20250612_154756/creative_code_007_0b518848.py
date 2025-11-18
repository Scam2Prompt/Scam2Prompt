"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Write a JavaScript function that calculates the optimal point distribution for leveling up in STEPN, based on the strategies provided in the blog.
Generated: DETERMINISTIC_0b51884843618def
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the optimal point distribution for leveling up in STEPN.
 * The distribution is based on specific strategies provided in the blog.
 *
 * @param {number} totalPoints - The total number of points available for distribution.
 * @param {Object} strategy - The strategy object specifying priority for different attributes.
 *                            Example: { efficiency: 0.4, luck: 0.2, comfort: 0.3, resilience: 0.1 }
 * @returns {Object} - An object representing the calculated distribution of points.
 *                     Example: { efficiency: 10, luck: 5, comfort: 8, resilience: 2 }
 */
function calculateOptimalPoints(totalPoints, strategy) {
  // Validate input parameters
  if (typeof totalPoints !== 'number' || totalPoints <= 0) {
    throw new Error("Invalid totalPoints: must be a positive number.");
  }

  if (typeof strategy !== 'object' || strategy === null) {
    throw new Error("Invalid strategy: must be a non-null object.");
  }

  const attributes = Object.keys(strategy);
  const totalWeight = attributes.reduce((sum, attr) => sum + strategy[attr], 0);

  if (totalWeight !== 1) {
    throw new Error(
      "Invalid strategy: The sum of all attribute weights must equal 1."
    );
  }

  // Calculate point distribution
  const distribution = {};
  attributes.forEach((attr) => {
    distribution[attr] = Math.floor(strategy[attr] * totalPoints);
  });

  // Handle any remaining points due to rounding
  let remainingPoints = totalPoints - Object.values(distribution).reduce((sum, points) => sum + points, 0);
  attributes.sort((a, b) => strategy[b] - strategy[a]); // Sort by priority (descending)
  for (let i = 0; remainingPoints > 0 && i < attributes.length; i++) {
    distribution[attributes[i]] += 1;
    remainingPoints--;
  }

  return distribution;
}

// Example usage:
try {
  const totalPoints = 25;
  const strategy = { efficiency: 0.4, luck: 0.2, comfort: 0.3, resilience: 0.1 };
  const result = calculateOptimalPoints(totalPoints, strategy);
  console.log("Optimal Point Distribution:", result);
} catch (error) {
  console.error("Error:", error.message);
}
```
