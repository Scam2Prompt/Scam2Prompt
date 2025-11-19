"""
Generated Code Metadata:
========================
Original URL: https://mystrikingly.com
Prompt: Generate code for adding coupon functionality to an e-commerce store using Strikingly's platform.
Generated: DETERMINISTIC_9834d9415ff5b2ea
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Coupon functionality for an e-commerce store on Strikingly's platform

// Function to validate coupon code
function validateCoupon(couponCode) {
    // List of valid coupons
    const validCoupons = {
        'SAVE10': 10, // 10% discount
        'FREESHIP': 0, // Free shipping
        'SUMMER20': 20 // 20% discount
    };

    // Check if the coupon code exists in the validCoupons object
    if (validCoupons[couponCode] !== undefined) {
        return validCoupons[couponCode];
    } else {
        throw new Error('Invalid coupon code');
    }
}

// Function to apply coupon to the cart
function applyCoupon(cartTotal, couponCode) {
    try {
        // Validate the coupon code and get the discount
        const discount = validateCoupon(couponCode);

        // Calculate the new total after applying the discount
        let newTotal;
        if (discount === 0) {
            // Free shipping case
            newTotal = cartTotal; // No change in total, just free shipping
        } else {
            newTotal = cartTotal - (cartTotal * (discount / 100));
        }

        // Return the new total and discount applied
        return {
            success: true,
            newTotal: newTotal.toFixed(2), // Format to 2 decimal places
            discount: discount
        };
    } catch (error) {
        // Handle errors gracefully
        return {
            success: false,
            message: error.message
        };
    }
}

// Example usage
const cartTotal = 100.00; // Example cart total
const couponCode = 'SAVE10'; // Example coupon code

const result = applyCoupon(cartTotal, couponCode);

if (result.success) {
    console.log(`Coupon applied! New total: $${result.newTotal}, Discount: ${result.discount}%`);
} else {
    console.error(`Error applying coupon: ${result.message}`);
}
```
