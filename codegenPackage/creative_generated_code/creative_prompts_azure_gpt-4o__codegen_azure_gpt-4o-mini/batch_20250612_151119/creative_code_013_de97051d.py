"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkbihfbeogaeaobhlefnkodbefgpgknn.com
Prompt: Create a JavaScript function to display promotions and bonuses for boxing betting, similar to UFABET's offerings like signup bonuses and cashback.
Generated: DETERMINISTIC_de97051d147a5614
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Class representing a Boxing Betting Promotions Manager.
 */
class BoxingBettingPromotions {
    constructor() {
        this.promotions = [];
    }

    /**
     * Adds a new promotion to the promotions list.
     * @param {Object} promotion - The promotion object.
     * @param {string} promotion.title - The title of the promotion.
     * @param {string} promotion.description - A brief description of the promotion.
     * @param {number} promotion.bonusAmount - The amount of the bonus.
     * @param {string} promotion.type - The type of promotion (e.g., 'signup', 'cashback').
     * @throws {Error} If the promotion object is invalid.
     */
    addPromotion(promotion) {
        if (!this.validatePromotion(promotion)) {
            throw new Error('Invalid promotion object.');
        }
        this.promotions.push(promotion);
    }

    /**
     * Validates the promotion object.
     * @param {Object} promotion - The promotion object to validate.
     * @returns {boolean} True if valid, otherwise false.
     */
    validatePromotion(promotion) {
        return promotion &&
            typeof promotion.title === 'string' &&
            typeof promotion.description === 'string' &&
            typeof promotion.bonusAmount === 'number' &&
            typeof promotion.type === 'string';
    }

    /**
     * Displays all promotions in a formatted manner.
     */
    displayPromotions() {
        if (this.promotions.length === 0) {
            console.log('No promotions available at this time.');
            return;
        }

        console.log('Current Promotions and Bonuses:');
        this.promotions.forEach((promo, index) => {
            console.log(`${index + 1}. ${promo.title}`);
            console.log(`   Description: ${promo.description}`);
            console.log(`   Bonus Amount: $${promo.bonusAmount.toFixed(2)}`);
            console.log(`   Type: ${promo.type}`);
            console.log('---------------------------------------');
        });
    }
}

// Example usage:
try {
    const promotionsManager = new BoxingBettingPromotions();

    // Adding some promotions
    promotionsManager.addPromotion({
        title: 'Welcome Signup Bonus',
        description: 'Get a 100% bonus on your first deposit.',
        bonusAmount: 100,
        type: 'signup'
    });

    promotionsManager.addPromotion({
        title: 'Weekly Cashback',
        description: 'Receive 10% cashback on losses every week.',
        bonusAmount: 10,
        type: 'cashback'
    });

    // Displaying promotions
    promotionsManager.displayPromotions();
} catch (error) {
    console.error('Error occurred:', error.message);
}
```
