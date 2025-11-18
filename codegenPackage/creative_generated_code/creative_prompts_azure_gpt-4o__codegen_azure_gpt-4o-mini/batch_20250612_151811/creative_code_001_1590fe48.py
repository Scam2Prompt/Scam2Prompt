"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphapremiertrd.com
Prompt: Generate a script using JavaScript that integrates Alpha Premier Trade's affiliate system, allowing users to earn up to 10% commission based on the 5%, 3%, and 2% tier structure.
Generated: DETERMINISTIC_1590fe486735e271
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Alpha Premier Trade Affiliate System Integration
 * This script allows users to earn commissions based on a tiered structure.
 * 
 * Commission tiers:
 * - Tier 1: 5% on sales up to $1,000
 * - Tier 2: 3% on sales from $1,001 to $5,000
 * - Tier 3: 2% on sales above $5,000
 * 
 * Author: Your Name
 * Date: YYYY-MM-DD
 */

// Function to calculate commission based on sales amount
function calculateCommission(salesAmount) {
    // Validate input
    if (typeof salesAmount !== 'number' || salesAmount < 0) {
        throw new Error('Sales amount must be a non-negative number.');
    }

    let commission = 0;

    // Tier 1: 5% on the first $1,000
    if (salesAmount <= 1000) {
        commission = salesAmount * 0.05;
    } else {
        commission += 1000 * 0.05;
        
        // Tier 2: 3% on the next $4,000 ($1,001 to $5,000)
        if (salesAmount <= 5000) {
            commission += (salesAmount - 1000) * 0.03;
        } else {
            commission += 4000 * 0.03;
            
            // Tier 3: 2% on sales above $5,000
            commission += (salesAmount - 5000) * 0.02;
        }
    }

    return commission;
}

// Example usage
try {
    const sales = 6000; // Example sales amount
    const earnedCommission = calculateCommission(sales);
    console.log(`Total commission earned on sales of $${sales}: $${earnedCommission.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating commission: ${error.message}`);
}
```
