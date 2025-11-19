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
 * Calculates membership benefits based on community engagement, 
 * networking opportunities, and personal development.
 */

// Define a class for TennisClubMembershipBenefitsCalculator
class TennisClubMembershipBenefitsCalculator {
  /**
   * Constructor to initialize the calculator
   */
  constructor() {
    this.communityEngagementWeight = 0.3;
    this.networkingOpportunitiesWeight = 0.2;
    this.personalDevelopmentWeight = 0.5;
  }

  /**
   * Calculate membership benefits
   * 
   * @param {number} communityEngagementScore - Score for community engagement (1-10)
   * @param {number} networkingOpportunitiesScore - Score for networking opportunities (1-10)
   * @param {number} personalDevelopmentScore - Score for personal development (1-10)
   * @returns {object} Membership benefits details
   */
  calculateMembershipBenefits(communityEngagementScore, networkingOpportunitiesScore, personalDevelopmentScore) {
    try {
      // Validate input scores
      if (!this.isValidScore(communityEngagementScore) || 
          !this.isValidScore(networkingOpportunitiesScore) || 
          !this.isValidScore(personalDevelopmentScore)) {
        throw new Error('Invalid score. Scores must be between 1 and 10.');
      }

      // Calculate weighted scores
      const communityEngagementBenefit = communityEngagementScore * this.communityEngagementWeight;
      const networkingOpportunitiesBenefit = networkingOpportunitiesScore * this.networkingOpportunitiesWeight;
      const personalDevelopmentBenefit = personalDevelopmentScore * this.personalDevelopmentWeight;

      // Calculate total benefit
      const totalBenefit = communityEngagementBenefit + networkingOpportunitiesBenefit + personalDevelopmentBenefit;

      // Return membership benefits details
      return {
        communityEngagementBenefit: communityEngagementBenefit.toFixed(2),
        networkingOpportunitiesBenefit: networkingOpportunitiesBenefit.toFixed(2),
        personalDevelopmentBenefit: personalDevelopmentBenefit.toFixed(2),
        totalBenefit: totalBenefit.toFixed(2)
      };
    } catch (error) {
      // Log and rethrow error
      console.error(error.message);
      throw error;
    }
  }

  /**
   * Check if a score is valid (between 1 and 10)
   * 
   * @param {number} score - Score to validate
   * @returns {boolean} True if score is valid, false otherwise
   */
  isValidScore(score) {
    return typeof score === 'number' && score >= 1 && score <= 10;
  }
}

// Example usage
function main() {
  const calculator = new TennisClubMembershipBenefitsCalculator();
  const communityEngagementScore = 8;
  const networkingOpportunitiesScore = 6;
  const personalDevelopmentScore = 9;

  try {
    const benefits = calculator.calculateMembershipBenefits(communityEngagementScore, networkingOpportunitiesScore, personalDevelopmentScore);
    console.log('Membership Benefits:');
    console.log(`Community Engagement: ${benefits.communityEngagementBenefit}`);
    console.log(`Networking Opportunities: ${benefits.networkingOpportunitiesBenefit}`);
    console.log(`Personal Development: ${benefits.personalDevelopmentBenefit}`);
    console.log(`Total Benefit: ${benefits.totalBenefit}`);
  } catch (error) {
    console.error('Error calculating membership benefits:', error.message);
  }
}

main();
```
