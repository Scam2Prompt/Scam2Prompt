"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearmybrand.com
Prompt: Develop a JavaScript function to optimize paid advertising campaigns by dynamically adjusting ad spend based on performance metrics, in line with Bear My Brand's digital marketing strategies.
Generated: DETERMINISTIC_7c27f2214bb95cc3
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to optimize ad spend dynamically based on performance metrics.
 * 
 * This function takes in campaign performance data and adjusts ad spend
 * according to metrics like click-through rate (CTR), conversion rate, and cost-per-click (CPC).
 * It follows Bear My Brand's digital marketing strategies.
 *
 * @param {Array<Object>} campaigns - Array of campaign objects containing performance data.
 * Each campaign object must include:
 *   - campaignId {string} : ID of the campaign
 *   - ctr {number} : Click-through rate (percentage)
 *   - conversionRate {number} : Conversion rate (percentage)
 *   - cpc {number} : Cost-per-click
 *   - currentSpend {number} : Current spend amount
 * @returns {Array<Object>} Updated campaigns with adjusted ad spend.
 */
function optimizeAdSpend(campaigns) {
  // Constants defining thresholds and adjustment factors
  const CTR_THRESHOLD = 5; // Minimum acceptable CTR percentage
  const CONVERSION_RATE_THRESHOLD = 2; // Minimum acceptable conversion rate percentage
  const MAX_SPEND_ADJUSTMENT_PERCENTAGE = 20; // Max adjustment percentage for ad spend
  
  // Input validation: Ensure campaigns is an array
  if (!Array.isArray(campaigns)) {
    throw new Error('Invalid input: campaigns must be an array of objects');
  }

  // Iterate over campaigns and adjust their ad spend
  return campaigns.map((campaign) => {
    // Validate campaign data
    if (
      !campaign.hasOwnProperty('campaignId') ||
      typeof campaign.campaignId !== 'string' ||
      typeof campaign.ctr !== 'number' ||
      typeof campaign.conversionRate !== 'number' ||
      typeof campaign.cpc !== 'number' ||
      typeof campaign.currentSpend !== 'number'
    ) {
      throw new Error(
        `Invalid campaign data for campaignId: ${campaign.campaignId || 'unknown'}`
      );
    }

    // Calculate adjustment factor based on performance metrics
    let adjustmentFactor = 0;

    if (campaign.ctr >= CTR_THRESHOLD && campaign.conversionRate >= CONVERSION_RATE_THRESHOLD) {
      // Increase spend for high-performing campaigns
      adjustmentFactor = MAX_SPEND_ADJUSTMENT_PERCENTAGE / 100;
    } else if (campaign.ctr < CTR_THRESHOLD || campaign.conversionRate < CONVERSION_RATE_THRESHOLD) {
      // Decrease spend for low-performing campaigns
      adjustmentFactor = -(MAX_SPEND_ADJUSTMENT_PERCENTAGE / 100);
    }

    // Apply adjustment to current spend
    const adjustedSpend = campaign.currentSpend + (campaign.currentSpend * adjustmentFactor);

    // Ensure spend is not negative
    const finalSpend = Math.max(adjustedSpend, 0);

    // Return updated campaign object
    return {
      ...campaign,
      adjustedSpend: finalSpend, // Add a new field for the adjusted spend
    };
  });
}

// Example usage
const campaigns = [
  {
    campaignId: 'campaign1',
    ctr: 6.5,
    conversionRate: 3.2,
    cpc: 1.5,
    currentSpend: 1000,
  },
  {
    campaignId: 'campaign2',
    ctr: 4.2,
    conversionRate: 1.8,
    cpc: 2.0,
    currentSpend: 800,
  },
];

try {
  const optimizedCampaigns = optimizeAdSpend(campaigns);
  console.log('Optimized Campaigns:', optimizedCampaigns);
} catch (error) {
  console.error('Error optimizing campaigns:', error.message);
}
```
