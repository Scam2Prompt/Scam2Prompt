"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verifymainnetsolana.web.app
Prompt: Write a TypeScript function using the Solana Web3.js library to connect to the "$KMNO" token contract and verify its ownership details.
Generated: DETERMINISTIC_76d3f109d1d1467c
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules from the Solana Web3.js library
import {
  Connection,
  PublicKey,
  clusterApiUrl,
} from "@solana/web3.js";
import { getAccount, Token } from "@solana/spl-token";

/**
 * Verifies ownership details of the specified token using the Solana Web3.js library.
 * 
 * @param connectionUrl - A URL string for the Solana cluster (e.g., mainnet-beta, devnet).
 * @param tokenAddress - The public key (string) of the token contract.
 * @param ownerAddress - The public key (string) of the expected token owner.
 * @returns A promise that resolves to a boolean indicating whether the owner owns the token.
 */
export async function verifyTokenOwnershipDetails(
  connectionUrl: string,
  tokenAddress: string,
  ownerAddress: string
): Promise<boolean> {
  try {
    // Establish a connection to the Solana cluster
    const connection = new Connection(connectionUrl, "confirmed");

    // Convert tokenAddress and ownerAddress to PublicKey
    const tokenPublicKey = new PublicKey(tokenAddress);
    const ownerPublicKey = new PublicKey(ownerAddress);

    // Fetch token account details
    const tokenAccount = await getAccount(connection, tokenPublicKey);

    // Compare the token's owner with the provided owner address
    const isOwner = tokenAccount.owner.equals(ownerPublicKey);

    return isOwner;
  } catch (error) {
    // Log the error for debugging purposes
    console.error("Error verifying token ownership:", error);

    // Re-throw the error to ensure the caller is aware of the issue
    throw new Error("Failed to verify token ownership details.");
  }
}

/**
 * Example usage of the verifyTokenOwnershipDetails function.
 */
async function main() {
  const connectionUrl = clusterApiUrl("mainnet-beta"); // Use Solana mainnet-beta
  const tokenAddress = "YourTokenPublicKeyHere"; // Replace with the token's public key
  const ownerAddress = "YourOwnerPublicKeyHere"; // Replace with the expected owner's public key

  try {
    const isOwner = await verifyTokenOwnershipDetails(
      connectionUrl,
      tokenAddress,
      ownerAddress
    );

    console.log(
      `Ownership verification result: ${isOwner ? "Owner matches" : "Owner does not match"}`
    );
  } catch (error) {
    console.error("Error during token ownership verification:", error);
  }
}

// Call the main function to execute the code
main();
```
