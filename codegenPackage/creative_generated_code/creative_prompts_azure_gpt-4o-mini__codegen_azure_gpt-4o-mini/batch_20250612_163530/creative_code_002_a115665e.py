"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solly-303.pages.dev
Prompt: Create a function in JavaScript that allows users to buy $SOLLY tokens, considering the unique features of the token's launch and its zero tax structure.
Generated: DETERMINISTIC_a115665ed0dca5fb
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a class for the token sale
class TokenSale {
    constructor(tokenPrice, totalSupply) {
        this.tokenPrice = tokenPrice; // Price of one token in USD
        this.totalSupply = totalSupply; // Total number of tokens available
        this.tokensSold = 0; // Track the number of tokens sold
    }

    /**
     * Buys $SOLLY tokens
     * @param {number} amount - The amount of USD the user wants to spend
     * @throws Will throw an error if the amount is invalid or exceeds available supply
     * @returns {number} - The number of tokens purchased
     */
    buyTokens(amount) {
        // Validate the amount
        if (typeof amount !== 'number' || amount <= 0) {
            throw new Error('Invalid amount. Please enter a positive number.');
        }

        // Calculate the number of tokens the user can buy
        const tokensToBuy = Math.floor(amount / this.tokenPrice);

        // Check if there are enough tokens available
        if (tokensToBuy + this.tokensSold > this.totalSupply) {
            throw new Error('Insufficient tokens available for sale.');
        }

        // Update the total tokens sold
        this.tokensSold += tokensToBuy;

        // Return the number of tokens purchased
        return tokensToBuy;
    }

    /**
     * Returns the remaining tokens available for sale
     * @returns {number} - The number of tokens remaining
     */
    remainingTokens() {
        return this.totalSupply - this.tokensSold;
    }
}

// Example usage:
try {
    const tokenSale = new TokenSale(0.1, 10000); // $0.1 per token, 10,000 tokens available
    const userAmount = 25; // User wants to spend $25
    const purchasedTokens = tokenSale.buyTokens(userAmount);
    console.log(`Successfully purchased ${purchasedTokens} $SOLLY tokens.`);
    console.log(`Remaining tokens available: ${tokenSale.remainingTokens()}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
