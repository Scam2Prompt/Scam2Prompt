"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://future-lolex.pages.dev
Prompt: Create a JavaScript function that implements a multi-level affiliate program for LOLEX, allowing users to track commissions from referrals.
Generated: DETERMINISTIC_52852c95a03e88ff
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Affiliate Program for LOLEX
 * This module implements a multi-level affiliate program that tracks commissions from referrals.
 */

// Class to represent an Affiliate
class Affiliate {
    constructor(id, name, commissionRate) {
        this.id = id; // Unique identifier for the affiliate
        this.name = name; // Name of the affiliate
        this.commissionRate = commissionRate; // Commission rate as a decimal (e.g., 0.10 for 10%)
        this.referrals = []; // Array to store the direct referrals of the affiliate
    }

    /**
     * Adds a referral to this affiliate's list.
     * @param {Affiliate} referral - The affiliate being referred.
     */
    addReferral(referral) {
        if (!(referral instanceof Affiliate)) {
            throw new Error('Invalid referral. Must be an instance of Affiliate.');
        }
        this.referrals.push(referral);
    }
}

/**
 * Class to manage the Affiliate Program
 */
class AffiliateProgram {
    constructor() {
        this.affiliates = new Map(); // Store affiliates by their ID
    }

    /**
     * Adds a new affiliate to the program.
     * @param {string} id - Unique identifier for the affiliate.
     * @param {string} name - Name of the affiliate.
     * @param {number} commissionRate - Commission rate as a decimal.
     */
    addAffiliate(id, name, commissionRate) {
        if (this.affiliates.has(id)) {
            throw new Error('Affiliate with this ID already exists.');
        }
        const affiliate = new Affiliate(id, name, commissionRate);
        this.affiliates.set(id, affiliate);
    }

    /**
     * Links an affiliate to another as a referral.
     * @param {string} referrerId - ID of the affiliate making the referral.
     * @param {string} referralId - ID of the affiliate being referred.
     */
    linkReferrals(referrerId, referralId) {
        const referrer = this.affiliates.get(referrerId);
        const referral = this.affiliates.get(referralId);

        if (!referrer || !referral) {
            throw new Error('Referrer or referral not found.');
        }
        
        referrer.addReferral(referral);
    }

    /**
     * Calculates the total commission for a specific affiliate.
     * @param {string} affiliateId - The ID of the affiliate for whom to calculate the total commissions.
     * @returns {number} The total commission earned by the affiliate.
     */
    calculateCommission(affiliateId) {
        const affiliate = this.affiliates.get(affiliateId);

        if (!affiliate) {
            throw new Error('Affiliate not found.');
        }

        let totalCommission = 0;

        // Calculate commission from direct referrals
        for (const referral of affiliate.referrals) {
            totalCommission += referral.commissionRate;
            // Recursive call to calculate commission from deeper levels
            totalCommission += this.calculateCommission(referral.id);
        }

        return totalCommission;
    }
}

// Example usage
const affiliateProgram = new AffiliateProgram();

try {
    affiliateProgram.addAffiliate('1', 'Alice', 0.10);
    affiliateProgram.addAffiliate('2', 'Bob', 0.15);
    affiliateProgram.addAffiliate('3', 'Charlie', 0.20);

    affiliateProgram.linkReferrals('1', '2'); // Alice refers Bob
    affiliateProgram.linkReferrals('2', '3'); // Bob refers Charlie

    const aliceCommission = affiliateProgram.calculateCommission('1');
    console.log(`Total commission for Alice: ${aliceCommission}`); // Outputs total commission
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```

This code implements a multi-level affiliate program for LOLEX, allowing for the tracking of commissions from referrals while ensuring clean structure, proper error handling, and documentation.
