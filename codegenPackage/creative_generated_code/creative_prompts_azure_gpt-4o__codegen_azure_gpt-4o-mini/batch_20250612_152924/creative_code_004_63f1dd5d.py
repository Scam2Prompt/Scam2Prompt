"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-wormhole-one.vercel.app
Prompt: Write JavaScript code to create an eligibility checker for $JUP and $WEN wallets, similar to the Wormhole $W airdrop tool.
Generated: DETERMINISTIC_63f1dd5d430eae05
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// EligibilityChecker class to determine if a wallet is eligible for $JUP and $WEN airdrops
class EligibilityChecker {
    constructor(wallets) {
        // Initialize with a list of wallets
        this.wallets = wallets;
    }

    /**
     * Check eligibility for $JUP and $WEN
     * @returns {Object} Results of eligibility check for each wallet
     */
    checkEligibility() {
        const results = {};

        // Iterate over each wallet to check eligibility
        for (const wallet of this.wallets) {
            results[wallet] = {
                isEligibleForJUP: this.isEligibleForJUP(wallet),
                isEligibleForWEN: this.isEligibleForWEN(wallet),
                error: null
            };
        }

        return results;
    }

    /**
     * Determine if a wallet is eligible for $JUP
     * @param {string} wallet - The wallet address to check
     * @returns {boolean} True if eligible, otherwise false
     */
    isEligibleForJUP(wallet) {
        // Placeholder eligibility criteria for $JUP
        // Replace this logic as necessary based on actual criteria
        return this.validateWallet(wallet) && wallet.startsWith("JUP");
    }

    /**
     * Determine if a wallet is eligible for $WEN
     * @param {string} wallet - The wallet address to check
     * @returns {boolean} True if eligible, otherwise false
     */
    isEligibleForWEN(wallet) {
        // Placeholder eligibility criteria for $WEN
        // Replace this logic as necessary based on actual criteria
        return this.validateWallet(wallet) && wallet.startsWith("WEN");
    }

    /**
     * Validate the wallet address format
     * @param {string} wallet - The wallet address to validate
     * @returns {boolean} True if valid, otherwise false
     */
    validateWallet(wallet) {
        // Basic regex for wallet address validation
        const walletRegex = /^[a-zA-Z0-9]{42}$/;
        if (!walletRegex.test(wallet)) {
            console.error(`Invalid wallet address: ${wallet}`);
            return false;
        }
        return true;
    }
}

// Example usage
try {
    // Sample wallet addresses for eligibility check
    const walletsToCheck = [
        "JUP123456789012345678901234567890123456",
        "WEN123456789012345678901234567890123456",
        "INVALIDWALLETADDRESS"
    ];

    // Create an instance of EligibilityChecker
    const checker = new EligibilityChecker(walletsToCheck);
    
    // Perform eligibility check
    const eligibilityResults = checker.checkEligibility();
    
    // Output the results
    console.log("Eligibility Results:", eligibilityResults);
} catch (error) {
    console.error("An error occurred while checking eligibility:", error);
}
```
