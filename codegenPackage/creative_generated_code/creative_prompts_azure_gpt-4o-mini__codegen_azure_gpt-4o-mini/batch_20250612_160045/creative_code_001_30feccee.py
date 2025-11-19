"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Write a JavaScript function that allows users to place bets on sports events using the BaxBet platform, ensuring secure cryptocurrency transactions.
Generated: DETERMINISTIC_30feccee2a9eee4a
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @module BaxBet
 * @description A module for handling bets on sports events using the BaxBet platform.
 */

class BaxBet {
    constructor() {
        // Initialize an empty array for bets
        this.bets = [];
    }

    /**
     * Places a bet on a sports event.
     *
     * @param {string} userId - The ID of the user placing the bet.
     * @param {string} eventId - The ID of the sports event.
     * @param {number} amount - The amount in cryptocurrency to bet.
     * @param {string} currency - The type of cryptocurrency (e.g., 'BTC', 'ETH').
     * @throws {Error} Will throw an error if the amount is less than or equal to zero.
     * @throws {Error} Will throw an error if the currency is not supported.
     * @returns {object} The placed bet object.
     */
    placeBet(userId, eventId, amount, currency) {
        // Validate the amount
        if (amount <= 0) {
            throw new Error('Bet amount must be greater than zero.');
        }

        // Validate the currency
        const supportedCurrencies = ['BTC', 'ETH', 'LTC'];
        if (!supportedCurrencies.includes(currency)) {
            throw new Error(`Currency not supported. Supported currencies are: ${supportedCurrencies.join(', ')}`);
        }

        // Create a bet object
        const bet = {
            userId,
            eventId,
            amount,
            currency,
            timestamp: new Date().toISOString(),
        };

        // Store the bet
        this.bets.push(bet);
        return bet;
    }

    /**
     * Retrieves the list of all bets placed by a specific user.
     *
     * @param {string} userId - The ID of the user whose bets to retrieve.
     * @returns {Array} Array of bets placed by the user.
     */
    getUserBets(userId) {
        return this.bets.filter(bet => bet.userId === userId);
    }

    /**
     * Retrieves all bets placed on a specific event.
     *
     * @param {string} eventId - The ID of the event whose bets to retrieve.
     * @returns {Array} Array of bets placed on the event.
     */
    getEventBets(eventId) {
        return this.bets.filter(bet => bet.eventId === eventId);
    }
}

// Example usage:
try {
    const baxBet = new BaxBet();
    const bet1 = baxBet.placeBet('user123', 'event456', 0.5, 'BTC');
    console.log('Bet placed:', bet1);
    
    const userBets = baxBet.getUserBets('user123');
    console.log('User Bets:', userBets);
    
    const eventBets = baxBet.getEventBets('event456');
    console.log('Event Bets:', eventBets);
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
