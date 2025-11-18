"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degenroyale.com
Prompt: Write JavaScript code to implement free spins and deposit matching bonuses for an online casino game, inspired by Royal Reels Casino promotions.
Generated: DETERMINISTIC_140672cef4ab6d19
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
class CasinoPromotion {
    constructor() {
        this.freeSpins = 0; // Number of free spins available
        this.depositBonus = 0; // Deposit match bonus amount
        this.isActive = false; // Status of the promotion
    }

    // Activate the promotion with free spins and deposit bonus
    activatePromotion(freeSpins, depositBonus) {
        if (freeSpins < 0 || depositBonus < 0) {
            throw new Error("Free spins and deposit bonus must be non-negative.");
        }
        this.freeSpins = freeSpins;
        this.depositBonus = depositBonus;
        this.isActive = true;
        console.log(`Promotion activated: ${this.freeSpins} free spins and ${this.depositBonus}% deposit match.`);
    }

    // Deactivate the promotion
    deactivatePromotion() {
        this.freeSpins = 0;
        this.depositBonus = 0;
        this.isActive = false;
        console.log("Promotion deactivated.");
    }

    // Retrieve the current promotion details
    getPromotionDetails() {
        if (!this.isActive) {
            return "No active promotions.";
        }
        return `Active Promotion: ${this.freeSpins} free spins, ${this.depositBonus}% deposit match.`;
    }

    // Use free spins
    useFreeSpins(spinsToUse) {
        if (!this.isActive) {
            throw new Error("No active promotion to use free spins.");
        }
        if (spinsToUse < 1 || spinsToUse > this.freeSpins) {
            throw new Error(`You can only use between 1 and ${this.freeSpins} free spins.`);
        }
        this.freeSpins -= spinsToUse;
        console.log(`${spinsToUse} free spins used. Remaining: ${this.freeSpins}`);
    }

    // Calculate the deposit match bonus
    calculateDepositMatch(depositAmount) {
        if (!this.isActive) {
            throw new Error("No active promotion to calculate deposit match.");
        }
        if (depositAmount <= 0) {
            throw new Error("Deposit amount must be greater than zero.");
        }
        const bonus = (this.depositBonus / 100) * depositAmount;
        console.log(`Deposit match bonus: $${bonus.toFixed(2)}`);
        return bonus;
    }
}

// Example usage:
try {
    const promotion = new CasinoPromotion();
    promotion.activatePromotion(10, 100); // Activate with 10 free spins and 100% deposit match
    console.log(promotion.getPromotionDetails());
    
    promotion.useFreeSpins(5); // Use 5 free spins
    const bonus = promotion.calculateDepositMatch(200); // Calculate bonus for a $200 deposit
    
    console.log(`Bonus amount received: $${bonus.toFixed(2)}`);
    
    promotion.deactivatePromotion(); // Deactivate promotion
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
