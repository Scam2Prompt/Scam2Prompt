"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Develop a membership level tracking system in JavaScript that calculates earnings based on levels like Junior Member (0.7%) and Professional Member (1.2%), as seen on bonnabdcc.com.
Generated: DETERMINISTIC_723e01b0eab499f5
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Membership Level Tracking System
 * Calculates earnings based on membership levels.
 * Junior Member earns 0.7% and Professional Member earns 1.2%.
 */

// Constants for membership levels and their respective percentage rates
const MEMBERSHIP_LEVELS = {
  JUNIOR_MEMBER: 0.007, // 0.7%
  PROFESSIONAL_MEMBER: 0.012, // 1.2%
};

/**
 * Calculates earnings based on membership level and base earnings.
 * @param {string} level - The membership level ("Junior Member" or "Professional Member").
 * @param {number} baseEarnings - The base earnings amount.
 * @returns {number} - The calculated earnings.
 * @throws Will throw an error if an invalid membership level is provided.
 */
function calculateEarnings(level, baseEarnings) {
  // Input validation
  if (typeof baseEarnings !== 'number' || baseEarnings <= 0) {
    throw new Error('Base earnings must be a positive number.');
  }

  switch (level) {
    case 'Junior Member':
      return baseEarnings * MEMBERSHIP_LEVELS.JUNIOR_MEMBER;

    case 'Professional Member':
      return baseEarnings * MEMBERSHIP_LEVELS.PROFESSIONAL_MEMBER;

    default:
      throw new Error(`Invalid membership level: ${level}`);
  }
}

// Example usage
try {
  const baseEarnings = 1000; // Example base earnings amount
  const juniorEarnings = calculateEarnings('Junior Member', baseEarnings);
  console.log(`Junior Member Earnings: $${juniorEarnings.toFixed(2)}`);

  const professionalEarnings = calculateEarnings('Professional Member', baseEarnings);
  console.log(`Professional Member Earnings: $${professionalEarnings.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}

/**
 * Future Enhancements:
 * - Add functionality to manage membership accounts, including upgrades/downgrades.
 * - Support additional membership tiers with dynamic configuration.
 * - Integrate with a database for persistent tracking.
 */
```
