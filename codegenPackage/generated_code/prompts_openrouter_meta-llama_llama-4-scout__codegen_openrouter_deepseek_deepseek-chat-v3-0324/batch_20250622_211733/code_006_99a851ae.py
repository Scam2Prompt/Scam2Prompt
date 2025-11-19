"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Create a simple calculator in JavaScript to determine membership benefits for a tennis club, considering factors like community engagement, networking opportunities, and personal development.
Generated: DETERMINISTIC_99a851aecc69d8db
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Tennis Club Membership Benefits Calculator
 * 
 * This calculator helps determine the benefits of joining a tennis club based on
 * factors like community engagement, networking opportunities, and personal development.
 */

class TennisClubCalculator {
  /**
   * Initialize the calculator with default weights for each benefit factor.
   * @param {Object} weights - Optional custom weights for each factor
   */
  constructor(weights = {}) {
    // Default weights for each benefit factor (sum should be 1)
    this.defaultWeights = {
      communityEngagement: 0.4,
      networkingOpportunities: 0.3,
      personalDevelopment: 0.3
    };

    // Merge custom weights with defaults
    this.weights = {...this.defaultWeights, ...weights};

    // Validate that weights sum to 1
    this.validateWeights();
  }

  /**
   * Validates that the weights sum to 1 (100%)
   * @throws {Error} If weights don't sum to 1
   */
  validateWeights() {
    const sum = Object.values(this.weights).reduce((acc, val) => acc + val, 0);
    if (Math.abs(sum - 1) > 0.0001) { // Account for floating point precision
      throw new Error('Weights must sum to 1');
    }
  }

  /**
   * Calculates the membership benefits score
   * @param {Object} scores - User-provided scores for each factor (0-100)
   * @returns {number} Calculated benefits score (0-100)
   * @throws {Error} If scores are invalid
   */
  calculateBenefits(scores) {
    // Validate input scores
    this.validateScores(scores);

    // Calculate weighted score
    let totalScore = 0;
    for (const [factor, weight] of Object.entries(this.weights)) {
      if (scores[factor] !== undefined) {
        totalScore += scores[factor] * weight;
      }
    }

    return Math.round(totalScore * 10) / 10; // Round to 1 decimal place
  }

  /**
   * Validates that scores are numbers between 0 and 100
   * @param {Object} scores - Scores to validate
   * @throws {Error} If any score is invalid
   */
  validateScores(scores) {
    for (const [factor, score] of Object.entries(scores)) {
      if (typeof score !== 'number' || score < 0 || score > 100) {
        throw new Error(`Invalid score for ${factor}: must be between 0 and 100`);
      }
    }
  }

  /**
   * Gets a textual description of the benefits level
   * @param {number} score - Calculated benefits score
   * @returns {string} Description of benefits level
   */
  getBenefitsLevel(score) {
    if (score >= 80) return 'Excellent';
    if (score >= 60) return 'Good';
    if (score >= 40) return 'Moderate';
    return 'Basic';
  }
}

// Example usage:
try {
  const calculator = new TennisClubCalculator();
  
  const memberScores = {
    communityEngagement: 85,
    networkingOpportunities: 70,
    personalDevelopment: 60
  };

  const benefitsScore = calculator.calculateBenefits(memberScores);
  const benefitsLevel = calculator.getBenefitsLevel(benefitsScore);

  console.log(`Benefits Score: ${benefitsScore}`);
  console.log(`Benefits Level: ${benefitsLevel}`);
} catch (error) {
  console.error('Error calculating benefits:', error.message);
}
```
