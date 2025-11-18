"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blog.firstflytravel.com
Prompt: Develop a function in JavaScript that calculates the cheapest day to book flights based on the tips provided by First Fly Travel's blog.
Generated: DETERMINISTIC_af61123480d91490
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the cheapest day to book flights based on given price data.
 * 
 * @param {Array<number>} prices - An array of flight prices for the upcoming days.
 * @returns {Object} - An object containing the cheapest price and the corresponding day index.
 * @throws {Error} - Throws an error if the input array is empty or contains non-numeric values.
 */
function calculateCheapestDay(prices) {
    // Validate input
    if (!Array.isArray(prices) || prices.length === 0) {
        throw new Error("Input must be a non-empty array of prices.");
    }

    // Initialize variables to track the cheapest price and day index
    let cheapestPrice = Infinity;
    let cheapestDayIndex = -1;

    // Iterate through the prices to find the cheapest one
    for (let i = 0; i < prices.length; i++) {
        const price = prices[i];
        
        // Validate that the current price is a number
        if (typeof price !== 'number' || price < 0) {
            throw new Error(`Invalid price at index ${i}: ${price}. All prices must be non-negative numbers.`);
        }

        // Update cheapest price and day index if a new lowest price is found
        if (price < cheapestPrice) {
            cheapestPrice = price;
            cheapestDayIndex = i;
        }
    }

    // Return the cheapest price and the corresponding day index
    return {
        cheapestPrice: cheapestPrice,
        cheapestDayIndex: cheapestDayIndex
    };
}

// Example usage
try {
    const flightPrices = [200, 150, 300, 120, 180]; // Example prices for the next 5 days
    const result = calculateCheapestDay(flightPrices);
    console.log(`Cheapest Price: $${result.cheapestPrice} on Day Index: ${result.cheapestDayIndex}`);
} catch (error) {
    console.error(error.message);
}
```
