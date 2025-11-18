"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teameleven-x1.xyz
Prompt: Create a JavaScript function to implement voucher recommendations for users based on their purchase history, inspired by the Ayuwin APK's AI capabilities.
Generated: DETERMINISTIC_0906549f8be2c727
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to recommend vouchers based on user's purchase history.
 * 
 * @param {Array} purchaseHistory - Array of user purchases. Each purchase should be an object containing 'category', 'amount', and 'date'.
 * @returns {Array} - Array of recommended voucher codes based on purchase history.
 * 
 * @throws {Error} - Throws an error if purchaseHistory is not an array or if it's empty.
 */
function recommendVouchers(purchaseHistory) {
    // Validate input
    if (!Array.isArray(purchaseHistory)) {
        throw new Error("Input must be an array.");
    }
    if (purchaseHistory.length === 0) {
        throw new Error("Purchase history cannot be empty.");
    }

    // Initialize a map to track the number of purchases in each category
    const categoryCount = {};

    // Process each purchase
    purchaseHistory.forEach(purchase => {
        const { category, amount } = purchase;

        // Validate purchase object
        if (!category || typeof category !== 'string') {
            throw new Error("Purchase category must be a valid string.");
        }
        if (typeof amount !== 'number' || amount < 0) {
            throw new Error("Purchase amount must be a non-negative number.");
        }

        // Count purchases in each category
        categoryCount[category] = (categoryCount[category] || 0) + 1;
    });

    // Define some example vouchers based on categories
    const vouchers = {
        'electronics': 'ELECTRO10',
        'clothing': 'CLOTH15',
        'groceries': 'GROCERY5',
        'books': 'BOOK20'
    };

    // Initialize an array to hold recommended vouchers
    const recommendedVouchers = [];

    // Recommend vouchers based on category counts
    for (const [category, count] of Object.entries(categoryCount)) {
        if (count > 1 && vouchers[category]) {
            recommendedVouchers.push({
                category,
                voucher: vouchers[category],
                message: `Recommended voucher for ${category}: ${vouchers[category]}`
            });
        }
    }

    // Return the list of recommended vouchers
    return recommendedVouchers.length > 0 ? recommendedVouchers : [{ message: "No vouchers available for your purchase history." }];
}

// Example usage
try {
    const userPurchaseHistory = [
        { category: 'electronics', amount: 150, date: '2023-10-01' },
        { category: 'clothing', amount: 80, date: '2023-10-05' },
        { category: 'electronics', amount: 200, date: '2023-10-10' }
    ];

    const recommendations = recommendVouchers(userPurchaseHistory);
    console.log(recommendations);
} catch (error) {
    console.error("Error:", error.message);
}
```
