"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dextoolsnode.pages.dev
Prompt: Create a JavaScript application to track token burns and display statistics, referencing DEXTools' burn dashboard feature.
Generated: DETERMINISTIC_8bb01bacbac62f06
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Token Burn Tracker Application
// This application tracks token burns and displays statistics similar to DEXTools' burn dashboard feature.

// Best practices:
// 1. Modularized functions for scalability
// 2. Error handling and data validation
// 3. Simple, readable, and maintainable code

// Define the main application object
const TokenBurnTracker = (() => {
    const burns = []; // Array to store burn data
    const stats = {
        totalBurned: 0,
        latestBurn: null,
    };

    /**
     * Add a token burn to the tracker
     * @param {string} tokenName - Name of the token
     * @param {number} amount - Amount burned
     */
    const addBurn = (tokenName, amount) => {
        try {
            // Validate inputs
            if (!tokenName || typeof tokenName !== "string") {
                throw new Error("Invalid token name.");
            }
            if (!amount || typeof amount !== "number" || amount <= 0) {
                throw new Error("Invalid burn amount.");
            }

            const burnData = {
                tokenName,
                amount,
                date: new Date().toISOString(),
            };

            // Add the burn data to the array
            burns.push(burnData);

            // Update statistics
            stats.totalBurned += amount;
            stats.latestBurn = burnData;

            console.log("Burn added successfully:", burnData);
        } catch (error) {
            console.error("Error adding burn:", error.message);
        }
    };

    /**
     * Get statistics of the burns
     * @returns {object} - Statistics including total burned and last burn data
     */
    const getStatistics = () => {
        try {
            // Return a copy of the stats
            return { ...stats };
        } catch (error) {
            console.error("Error retrieving statistics:", error.message);
        }
    };

    /**
     * Display all burns in the tracker
     */
    const displayBurns = () => {
        try {
            if (burns.length === 0) {
                console.log("No burns to display.");
                return;
            }

            console.log("Token Burns:");
            burns.forEach((burn, index) => {
                console.log(`${index + 1}. Token: ${burn.tokenName}, Amount: ${burn.amount}, Date: ${burn.date}`);
            });
        } catch (error) {
            console.error("Error displaying burns:", error.message);
        }
    };

    // Return public methods
    return {
        addBurn,
        getStatistics,
        displayBurns,
    };
})();

// Example usage of the TokenBurnTracker application
TokenBurnTracker.addBurn("TokenABC", 500);
TokenBurnTracker.addBurn("TokenXYZ", 1000);
TokenBurnTracker.displayBurns();

const stats = TokenBurnTracker.getStatistics();
console.log("Statistics:", stats);
```
