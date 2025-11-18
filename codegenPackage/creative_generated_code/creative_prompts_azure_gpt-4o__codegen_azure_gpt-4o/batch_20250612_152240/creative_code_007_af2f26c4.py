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
/**
 * Function to check if a wallet is eligible for free minting of Samoyed Coin.
 * Eligibility is determined based on token ownership criteria.
 * 
 * @param walletAddress - The wallet address to check eligibility for.
 * @param tokenHoldings - An object representing token holdings in the wallet. 
 *                        Keys are token IDs and values are the quantity owned.
 * @param requiredTokens - An array of token IDs required for eligibility.
 * @param minimumQuantity - Minimum quantity of each required token needed for eligibility.
 * @returns true if the wallet is eligible, false otherwise.
 */
function isEligibleForFreeMint(
  walletAddress: string,
  tokenHoldings: Record<string, number>,
  requiredTokens: string[],
  minimumQuantity: number
): boolean {
  // Validate wallet address format (basic validation)
  if (!walletAddress || typeof walletAddress !== "string" || walletAddress.length === 0) {
    throw new Error("Invalid wallet address.");
  }

  // Validate inputs
  if (!tokenHoldings || typeof tokenHoldings !== "object") {
    throw new Error("Invalid token holdings data.");
  }
  if (!Array.isArray(requiredTokens) || requiredTokens.length === 0) {
    throw new Error("Invalid required tokens list.");
  }
  if (minimumQuantity <= 0) {
    throw new Error("Minimum quantity must be greater than 0.");
  }

  // Check token ownership criteria
  for (const tokenId of requiredTokens) {
    const ownedQuantity = tokenHoldings[tokenId] || 0;
    if (ownedQuantity < minimumQuantity) {
      return false; // Not eligible if any required token is below minimum quantity
    }
  }

  // If all criteria are met, wallet is eligible
  return true;
}

// Example Usage:
const walletAddress = "0x123456789abcdef";
const tokenHoldings = {
  "SAMO": 10,
  "SOL": 5,
  "USDC": 20,
};
const requiredTokens = ["SAMO", "SOL"];
const minimumQuantity = 5;

try {
  const eligibility = isEligibleForFreeMint(walletAddress, tokenHoldings, requiredTokens, minimumQuantity);
  console.log(`Wallet ${walletAddress} is eligible for free minting: ${eligibility}`);
} catch (error) {
  console.error(`Error checking eligibility: ${error.message}`);
}
```
