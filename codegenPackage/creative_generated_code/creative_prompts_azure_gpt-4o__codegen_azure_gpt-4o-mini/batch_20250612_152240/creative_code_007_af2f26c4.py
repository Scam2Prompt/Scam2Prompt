"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samoyed-wl.web.app
Prompt: Create a TypeScript function to check if a wallet is eligible for free minting of Samoyed Coin based on token ownership criteria.
Generated: DETERMINISTIC_af2f26c48aa20847
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules
import { BigNumber } from 'bignumber.js';

// Define an interface for the wallet information
interface Wallet {
    address: string;
    ownedTokens: string[];
}

/**
 * Function to check if a wallet is eligible for free minting of Samoyed Coin.
 * Eligibility is based on specific token ownership criteria.
 * 
 * @param wallet - The wallet object containing address and owned tokens
 * @param requiredTokens - An array of token IDs that must be owned for eligibility
 * @returns boolean - Returns true if eligible, false otherwise
 */
function isEligibleForFreeMint(wallet: Wallet, requiredTokens: string[]): boolean {
    try {
        // Validate input parameters
        if (!wallet || !wallet.address || !Array.isArray(wallet.ownedTokens)) {
            throw new Error("Invalid wallet information provided.");
        }
        if (!Array.isArray(requiredTokens)) {
            throw new Error("Invalid required tokens list provided.");
        }

        // Check ownership of required tokens
        const hasRequiredTokens = requiredTokens.every(token => 
            wallet.ownedTokens.includes(token)
        );

        return hasRequiredTokens;
    } catch (error) {
        // Log the error for debugging purposes and return false
        console.error(`Error checking eligibility: ${error.message}`);
        return false;
    }
}

// Example usage
const userWallet: Wallet = {
    address: "0x1234...abcd",
    ownedTokens: ["token1", "token2", "token3"]
};

const requiredTokens: string[] = ["token2", "token3"];

const eligible = isEligibleForFreeMint(userWallet, requiredTokens);
console.log(`Wallet ${userWallet.address} eligibility for free minting: ${eligible}`);
```
