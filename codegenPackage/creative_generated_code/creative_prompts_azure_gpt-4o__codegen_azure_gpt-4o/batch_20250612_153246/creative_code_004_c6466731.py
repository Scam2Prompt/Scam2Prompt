"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Write a function in JavaScript to calculate cashback or discounts (e.g., 100% cashback) for slot game deposits based on promotional offers.
Generated: DETERMINISTIC_c646673183898546
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate cashback or discounts for slot game deposits based on promotional offers.
 * 
 * @param {number} depositAmount - The amount deposited by the user.
 * @param {string} promoType - The type of promotional offer ("cashback" or "discount").
 * @param {number} promoValue - The value of the promotional offer (e.g., 100 for 100% cashback or 20 for 20% discount).
 * @returns {object} - An object containing the final deposit amount and the cashback/discount amount.
 * @throws {Error} - Throws an error if invalid inputs are provided.
 */
function calculatePromotion(depositAmount, promoType, promoValue) {
    // Input validation
    if (typeof depositAmount !== 'number' || depositAmount <= 0) {
        throw new Error("Invalid deposit amount. It must be a positive number.");
    }
    if (typeof promoType !== 'string' || !["cashback", "discount"].includes(promoType.toLowerCase())) {
        throw new Error("Invalid promo type. It must be either 'cashback' or 'discount'.");
    }
    if (typeof promoValue !== 'number' || promoValue < 0 || promoValue > 100) {
        throw new Error("Invalid promo value. It must be a number between 0 and 100.");
    }

    // Initialize result object
    let result = {
        finalAmount: depositAmount,
        promoAmount: 0
    };

    // Calculate promotional offer
    if (promoType.toLowerCase() === "cashback") {
        result.promoAmount = (depositAmount * promoValue) / 100;
        result.finalAmount = depositAmount; // Cashback doesn't reduce the deposit amount
    } else if (promoType.toLowerCase() === "discount") {
        result.promoAmount = (depositAmount * promoValue) / 100;
        result.finalAmount = depositAmount - result.promoAmount; // Discount reduces the deposit amount
    }

    return result;
}

// Example usage
try {
    const deposit = 100; // Example deposit amount
    const promo = "cashback"; // Example promotion type
    const value = 100; // Example promotion value (e.g., 100% cashback)

    const promotionResult = calculatePromotion(deposit, promo, value);
    console.log("Promotion Result:", promotionResult);
    // Output: { finalAmount: 100, promoAmount: 100 }
} catch (error) {
    console.error("Error:", error.message);
}
```
