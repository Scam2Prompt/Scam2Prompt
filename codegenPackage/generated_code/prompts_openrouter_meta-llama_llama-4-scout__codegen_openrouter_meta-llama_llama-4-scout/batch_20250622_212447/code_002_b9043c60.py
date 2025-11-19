"""
Generated Code Metadata:
========================
Original URL: https://monad-monadxyz-meme.testnet.nfts2.me
Prompt: Generate a JavaScript function to track and calculate referral earnings for a digital collectible minting platform, where the referral fee increases with the number of mints completed through a user's link.
Generated: DETERMINISTIC_b9043c60d618a7af
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ReferralEarningsCalculator class to track and calculate referral earnings.
 */
class ReferralEarningsCalculator {
  /**
   * Constructor to initialize referral earnings data.
   */
  constructor() {
    // Map to store user referral links and their corresponding mint counts.
    this.referralLinks = new Map();
    // Map to store user earnings.
    this.userEarnings = new Map();
    // Tiers for referral fees based on the number of mints.
    this.referralFeeTiers = [
      { minMints: 0, maxMints: 9, fee: 0.05 }, // 5% for 0-9 mints
      { minMints: 10, maxMints: 49, fee: 0.075 }, // 7.5% for 10-49 mints
      { minMints: 50, maxMints: Infinity, fee: 0.1 }, // 10% for 50+ mints
    ];
  }

  /**
   * Adds a new referral link for a user.
   * @param {string} userId - The ID of the user.
   * @param {string} link - The referral link.
   */
  addReferralLink(userId, link) {
    this.referralLinks.set(link, { userId, mintCount: 0 });
  }

  /**
   * Increments the mint count for a referral link and calculates earnings.
   * @param {string} link - The referral link.
   * @param {number} amount - The amount earned per mint.
   */
  incrementMintCount(link, amount) {
    if (!this.referralLinks.has(link)) {
      throw new Error(`Referral link ${link} not found.`);
    }

    const referralData = this.referralLinks.get(link);
    referralData.mintCount++;

    const fee = this.calculateReferralFee(referralData.mintCount);
    const earnings = amount * fee;

    this.updateUserEarnings(referralData.userId, earnings);
  }

  /**
   * Calculates the referral fee based on the number of mints.
   * @param {number} mintCount - The number of mints.
   * @returns {number} The referral fee.
   */
  calculateReferralFee(mintCount) {
    const tier = this.referralFeeTiers.find((tier) => mintCount >= tier.minMints && mintCount <= tier.maxMints);
    return tier ? tier.fee : 0;
  }

  /**
   * Updates the earnings for a user.
   * @param {string} userId - The ID of the user.
   * @param {number} earnings - The earnings to add.
   */
  updateUserEarnings(userId, earnings) {
    if (this.userEarnings.has(userId)) {
      const currentEarnings = this.userEarnings.get(userId);
      this.userEarnings.set(userId, currentEarnings + earnings);
    } else {
      this.userEarnings.set(userId, earnings);
    }
  }

  /**
   * Gets the earnings for a user.
   * @param {string} userId - The ID of the user.
   * @returns {number} The earnings for the user.
   */
  getUserEarnings(userId) {
    return this.userEarnings.get(userId) || 0;
  }

  /**
   * Gets the referral link data.
   * @param {string} link - The referral link.
   * @returns {object} The referral link data.
   */
  getReferralLinkData(link) {
    return this.referralLinks.get(link);
  }
}

// Example usage:
function main() {
  const calculator = new ReferralEarningsCalculator();

  calculator.addReferralLink('user1', 'link1');
  calculator.incrementMintCount('link1', 100);
  calculator.incrementMintCount('link1', 100);
  calculator.incrementMintCount('link1', 100);

  console.log(calculator.getUserEarnings('user1'));

  try {
    calculator.incrementMintCount('link2', 100);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
