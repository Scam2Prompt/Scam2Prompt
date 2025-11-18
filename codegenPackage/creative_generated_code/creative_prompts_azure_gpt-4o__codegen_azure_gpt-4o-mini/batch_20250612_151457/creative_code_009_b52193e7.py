"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://le13emeart.com
Prompt: Write a JavaScript function to calculate the total cost of tickets for a group booking at "Le 13e Art," factoring in discounts for corporate or school groups as mentioned on the website.
Generated: DETERMINISTIC_b52193e7698de8e9
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of tickets for a group booking at "Le 13e Art".
 * 
 * @param {number} numTickets - The number of tickets to be purchased.
 * @param {string} groupType - The type of group booking (either 'corporate' or 'school').
 * @returns {number} - The total cost of tickets after applicable discounts.
 * @throws {Error} - Throws an error if the number of tickets is less than or equal to 0,
 *                   or if the group type is invalid.
 */
function calculateTotalCost(numTickets, groupType) {
    // Define the standard ticket price
    const ticketPrice = 20; // Assuming each ticket costs 20 units
    let discountRate = 0;

    // Validate input
    if (numTickets <= 0) {
        throw new Error("Number of tickets must be greater than 0.");
    }

    // Determine the discount rate based on group type
    switch (groupType.toLowerCase()) {
        case 'corporate':
            discountRate = 0.1; // 10% discount for corporate groups
            break;
        case 'school':
            discountRate = 0.15; // 15% discount for school groups
            break;
        default:
            throw new Error("Invalid group type. Please use 'corporate' or 'school'.");
    }

    // Calculate total cost
    const totalCost = numTickets * ticketPrice * (1 - discountRate);
    
    // Return the total cost, rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage (uncomment for testing):
// try {
//     const totalCost = calculateTotalCost(10, 'corporate');
//     console.log(`Total cost for corporate booking: $${totalCost}`);
// } catch (error) {
//     console.error(error.message);
// }
```
