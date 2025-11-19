"""
Generated Code Metadata:
========================
Original URL: https://avilhasdolarbraz.blogspot.com
Prompt: Create a JavaScript function to calculate the total cost of items in a shopping cart, considering discounts and installment plans with interest.
Generated: DETERMINISTIC_8a9d5850ff423963
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of items in a shopping cart, applying discounts and installment options.
 * @param {Array} items - Array of item objects with price and quantity
 * @param {number} discountPercentage - Discount percentage (0-100)
 * @param {number} installmentMonths - Number of months for installment (0 for no installment)
 * @param {number} annualInterestRate - Annual interest rate for installment (0 for no interest)
 * @returns {Object} An object containing total, discountedTotal, and installment details
 * @throws {Error} If invalid parameters are provided
 */
function calculateCartTotal(items, discountPercentage = 0, installmentMonths = 0, annualInterestRate = 0) {
    // Validate input parameters
    if (!Array.isArray(items)) {
        throw new Error('Items must be an array');
    }
    if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 100) {
        throw new Error('Discount percentage must be between 0 and 100');
    }
    if (typeof installmentMonths !== 'number' || installmentMonths < 0) {
        throw new Error('Installment months must be a non-negative number');
    }
    if (typeof annualInterestRate !== 'number' || annualInterestRate < 0) {
        throw new Error('Annual interest rate must be a non-negative number');
    }

    // Calculate subtotal
    const subtotal = items.reduce((sum, item) => {
        if (typeof item.price !== 'number' || item.price < 0) {
            throw new Error('Item price must be a non-negative number');
        }
        if (typeof item.quantity !== 'number' || item.quantity < 1) {
            throw new Error('Item quantity must be at least 1');
        }
        return sum + (item.price * item.quantity);
    }, 0);

    // Apply discount
    const discountAmount = subtotal * (discountPercentage / 100);
    const discountedTotal = subtotal - discountAmount;

    // Calculate installment details if applicable
    let installmentDetails = null;
    if (installmentMonths > 0) {
        const monthlyInterestRate = annualInterestRate / 100 / 12;
        let monthlyPayment;
        
        if (monthlyInterestRate === 0) {
            monthlyPayment = discountedTotal / installmentMonths;
        } else {
            const interestFactor = Math.pow(1 + monthlyInterestRate, installmentMonths);
            monthlyPayment = discountedTotal * monthlyInterestRate * interestFactor / (interestFactor - 1);
        }

        installmentDetails = {
            months: installmentMonths,
            monthlyPayment: parseFloat(monthlyPayment.toFixed(2)),
            totalWithInterest: parseFloat((monthlyPayment * installmentMonths).toFixed(2)),
            interestPaid: parseFloat((monthlyPayment * installmentMonths - discountedTotal).toFixed(2))
        };
    }

    return {
        subtotal: parseFloat(subtotal.toFixed(2)),
        discountAmount: parseFloat(discountAmount.toFixed(2)),
        discountedTotal: parseFloat(discountedTotal.toFixed(2)),
        installmentDetails
    };
}
```
