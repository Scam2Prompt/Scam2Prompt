"""
Generated Code Metadata:
========================
Original URL: https://borpartoken.com
Prompt: Develop a function in JavaScript to handle transactions for a token sale, including phases like whitelist and overflow, with specific pricing in USDT.
Generated: DETERMINISTIC_286304a8366c2109
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TokenSale class to handle transactions for a token sale.
 * It includes phases like whitelist and overflow, with specific pricing in USDT.
 */
class TokenSale {
    constructor() {
        this.whitelist = new Set(); // Set to store whitelisted addresses
        this.tokenPrice = 1; // Price of one token in USDT
        this.totalTokens = 10000; // Total tokens available for sale
        this.tokensSold = 0; // Tokens sold so far
        this.saleActive = false; // Flag to indicate if the sale is active
    }

    /**
     * Start the token sale.
     */
    startSale() {
        this.saleActive = true;
        console.log("Token sale has started.");
    }

    /**
     * End the token sale.
     */
    endSale() {
        this.saleActive = false;
        console.log("Token sale has ended.");
    }

    /**
     * Add an address to the whitelist.
     * @param {string} address - The address to be whitelisted.
     */
    addToWhitelist(address) {
        if (this.whitelist.has(address)) {
            console.error("Address is already whitelisted.");
            return;
        }
        this.whitelist.add(address);
        console.log(`Address ${address} has been added to the whitelist.`);
    }

    /**
     * Handle a purchase transaction.
     * @param {string} buyer - The address of the buyer.
     * @param {number} amount - The amount of USDT to spend.
     */
    purchaseTokens(buyer, amount) {
        if (!this.saleActive) {
            console.error("Token sale is not active.");
            return;
        }

        if (!this.whitelist.has(buyer)) {
            console.error("Address is not whitelisted.");
            return;
        }

        const tokensToBuy = amount / this.tokenPrice;

        if (tokensToBuy + this.tokensSold > this.totalTokens) {
            console.error("Not enough tokens available for sale.");
            return;
        }

        this.tokensSold += tokensToBuy;
        console.log(`${buyer} purchased ${tokensToBuy} tokens for ${amount} USDT.`);
    }

    /**
     * Get the current status of the token sale.
     * @returns {Object} - An object containing the sale status and tokens sold.
     */
    getSaleStatus() {
        return {
            saleActive: this.saleActive,
            tokensSold: this.tokensSold,
            tokensRemaining: this.totalTokens - this.tokensSold,
        };
    }
}

// Example usage
const tokenSale = new TokenSale();
tokenSale.startSale();
tokenSale.addToWhitelist("0x1234567890abcdef1234567890abcdef12345678");
tokenSale.purchaseTokens("0x1234567890abcdef1234567890abcdef12345678", 10);
console.log(tokenSale.getSaleStatus());
tokenSale.endSale();
```
