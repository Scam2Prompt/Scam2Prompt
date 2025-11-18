"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Generate code using JavaScript to implement a voucher system for an e-commerce app, where users can apply discounts like those mentioned on Indotip.
Generated: DETERMINISTIC_1ac5c364aea81034
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Voucher System for E-commerce Application

class Voucher {
    constructor(code, discountType, discountValue, expiryDate) {
        this.code = code; // Unique code for the voucher
        this.discountType = discountType; // Type of discount: 'percentage' or 'fixed'
        this.discountValue = discountValue; // Value of the discount
        this.expiryDate = new Date(expiryDate); // Expiry date of the voucher
    }

    // Method to validate if the voucher is still valid
    isValid() {
        const today = new Date();
        return this.expiryDate >= today;
    }

    // Method to apply the voucher to a total price
    apply(totalPrice) {
        if (!this.isValid()) {
            throw new Error('Voucher has expired.');
        }
        
        let discountAmount = 0;

        if (this.discountType === 'percentage') {
            discountAmount = (this.discountValue / 100) * totalPrice;
        } else if (this.discountType === 'fixed') {
            discountAmount = this.discountValue;
        } else {
            throw new Error('Invalid discount type.');
        }

        // Ensure discount does not exceed total price
        if (discountAmount > totalPrice) {
            discountAmount = totalPrice;
        }

        return totalPrice - discountAmount; // Return the new total after applying the discount
    }
}

// Example usage
try {
    // Creating a new voucher for 20% off
    const voucher = new Voucher('SUMMER20', 'percentage', 20, '2023-12-31');

    // Total price before discount
    const totalPrice = 100;

    // Applying the voucher
    const newTotal = voucher.apply(totalPrice);
    console.log(`New total after applying voucher: $${newTotal.toFixed(2)}`);

} catch (error) {
    console.error(`Error applying voucher: ${error.message}`);
}
```
