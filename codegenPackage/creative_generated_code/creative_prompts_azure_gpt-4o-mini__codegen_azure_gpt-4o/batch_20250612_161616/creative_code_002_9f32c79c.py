"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purebite.fi
Prompt: Create a JavaScript function that calculates the total price for a three-course meal set, based on the pricing model used by Purebite for their weekend offers.
Generated: DETERMINISTIC_9f32c79c430d8296
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price for a three-course meal set based on Purebite's weekend pricing model.
 * 
 * Pricing model:
 * - Starter: $10
 * - Main Course: $20
 * - Dessert: $8
 * - Weekend Discount: 10% off the total price
 * 
 * @returns {number} Total price for the three-course meal set after discount
 */
function calculateThreeCourseMealPrice() {
    try {
        // Define prices for each course
        const starterPrice = 10;  // Price for the starter
        const mainCoursePrice = 20;  // Price for the main course
        const dessertPrice = 8;  // Price for the dessert
        
        // Calculate total price before discount
        const totalPriceBeforeDiscount = starterPrice + mainCoursePrice + dessertPrice;
        
        // Apply weekend discount (10% off the total price)
        const discountRate = 0.10;  // Discount rate as a decimal
        const discountAmount = totalPriceBeforeDiscount * discountRate; // Amount of discount
        const totalPriceAfterDiscount = totalPriceBeforeDiscount - discountAmount;
        
        // Return the final price
        return totalPriceAfterDiscount;
    } catch (error) {
        // Log any potential error
        console.error('An error occurred while calculating the meal price:', error);
        throw new Error('Unable to calculate total price for the meal set.');
    }
}

// Example usage
// Uncomment the line below to test the function in the console
// console.log(`Total price for the three-course meal set: $${calculateThreeCourseMealPrice().toFixed(2)}`);
```
