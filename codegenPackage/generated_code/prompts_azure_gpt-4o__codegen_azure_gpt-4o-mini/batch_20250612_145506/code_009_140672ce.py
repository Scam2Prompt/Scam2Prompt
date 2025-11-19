"""
Generated Code Metadata:
========================
Original URL: https://degenroyale.com
Prompt: Write JavaScript code to implement free spins and deposit matching bonuses for an online casino game, inspired by Royal Reels Casino promotions.
Generated: DETERMINISTIC_140672cef4ab6d19
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CasinoBonusManager class to handle free spins and deposit matching bonuses
class CasinoBonusManager {
    constructor() {
        this.bonuses = [];
    }

    /**
     * Adds a new bonus to the bonuses list.
     * @param {string} type - The type of bonus (e.g., 'free spins', 'deposit match').
     * @param {number} amount - The amount of the bonus (e.g., number of spins or percentage).
     * @param {Date} expiryDate - The date when the bonus expires.
     */
    addBonus(type, amount, expiryDate) {
        if (!type || !amount || !expiryDate) {
            throw new Error("Invalid parameters: type, amount, and expiryDate are required.");
        }

        if (!(expiryDate instanceof Date)) {
            throw new Error("Invalid expiryDate: must be a Date object.");
        }

        this.bonuses.push({ type, amount, expiryDate });
    }

    /**
     * Retrieves all active bonuses.
     * @returns {Array} - An array of active bonuses.
     */
    getActiveBonuses() {
        const now = new Date();
        return this.bonuses.filter(bonus => bonus.expiryDate > now);
    }

    /**
     * Applies a deposit match bonus to a player's deposit.
     * @param {number} depositAmount - The amount the player is depositing.
     * @returns {number} - The total amount after applying the deposit match bonus.
     */
    applyDepositMatch(depositAmount) {
        const activeBonuses = this.getActiveBonuses();
        let totalBonus = 0;

        activeBonuses.forEach(bonus => {
            if (bonus.type === 'deposit match') {
                totalBonus += (depositAmount * (bonus.amount / 100));
            }
        });

        return depositAmount + totalBonus;
    }

    /**
     * Retrieves the number of free spins available.
     * @returns {number} - The total number of free spins from active bonuses.
     */
    getTotalFreeSpins() {
        const activeBonuses = this.getActiveBonuses();
        return activeBonuses.reduce((total, bonus) => {
            return bonus.type === 'free spins' ? total + bonus.amount : total;
        }, 0);
    }
}

// Example usage
try {
    const bonusManager = new CasinoBonusManager();

    // Adding bonuses
    bonusManager.addBonus('free spins', 10, new Date('2023-12-31'));
    bonusManager.addBonus('deposit match', 50, new Date('2023-12-31'));

    // Applying deposit match
    const depositAmount = 100;
    const totalAfterBonus = bonusManager.applyDepositMatch(depositAmount);
    console.log(`Total after deposit match: $${totalAfterBonus}`);

    // Getting total free spins
    const totalFreeSpins = bonusManager.getTotalFreeSpins();
    console.log(`Total free spins available: ${totalFreeSpins}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
