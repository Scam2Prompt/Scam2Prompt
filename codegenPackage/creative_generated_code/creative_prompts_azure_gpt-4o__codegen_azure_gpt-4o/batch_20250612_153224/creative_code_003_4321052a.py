"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Develop a function in JavaScript to display the pricing tiers for hair transplants dynamically, using the cost breakdown provided by Auqual Hair Services.
Generated: DETERMINISTIC_4321052a4eead895
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically display pricing tiers for hair transplants
 * based on cost breakdown provided by Auqual Hair Services.
 * 
 * Pricing tiers are displayed as an array of objects, where each object contains:
 * - tierName: The name of the pricing tier
 * - minGrafts: Minimum number of grafts for the tier
 * - maxGrafts: Maximum number of grafts for the tier
 * - costPerGraft: Cost per graft in the tier
 * - totalCost: Calculated total cost for the tier
 */

/**
 * Pricing data from Auqual Hair Services
 * Array of objects representing pricing tiers
 */
const pricingData = [
    { tierName: 'Basic', minGrafts: 1000, maxGrafts: 2000, costPerGraft: 3 },
    { tierName: 'Standard', minGrafts: 2001, maxGrafts: 3000, costPerGraft: 2.75 },
    { tierName: 'Premium', minGrafts: 3001, maxGrafts: 4000, costPerGraft: 2.5 },
];

/**
 * Function to calculate total cost and display pricing tiers dynamically
 */
function displayPricingTiers() {
    try {
        // Validate pricing data
        if (!Array.isArray(pricingData) || pricingData.length === 0) {
            throw new Error('Invalid pricing data provided.');
        }

        // Calculate total cost for each tier and format the result
        const pricingTiers = pricingData.map((tier) => {
            if (
                typeof tier.minGrafts !== 'number' ||
                typeof tier.maxGrafts !== 'number' ||
                typeof tier.costPerGraft !== 'number'
            ) {
                throw new Error(`Invalid data format for tier: ${tier.tierName}`);
            }

            const totalCost = tier.costPerGraft * (tier.maxGrafts - tier.minGrafts + 1);

            return {
                tierName: tier.tierName,
                minGrafts: tier.minGrafts,
                maxGrafts: tier.maxGrafts,
                costPerGraft: tier.costPerGraft,
                totalCost: totalCost.toFixed(2),
            };
        });

        // Display results
        console.log('Hair Transplant Pricing Tiers:');
        pricingTiers.forEach((tier) => {
            console.log(
                `Tier: ${tier.tierName}, Grafts: ${tier.minGrafts}-${tier.maxGrafts}, Cost/Graft: $${tier.costPerGraft}, Total Cost: $${tier.totalCost}`
            );
        });
    } catch (error) {
        // Handle any errors gracefully
        console.error('Error displaying pricing tiers:', error.message);
    }
}

// Call the function to display pricing tiers
displayPricingTiers();
```
