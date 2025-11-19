"""
Generated Code Metadata:
========================
Original URL: https://claim-coolcoinwtf.pages.dev
Prompt: Write a JavaScript application that integrates with Solana blockchain to display the claiming status of $COOL tokens for a given NFT number using the NFT Checker tool.
Generated: DETERMINISTIC_ee83268fb9831693
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const axios = require('axios');

/**
 * NFT Checker class to interact with Solana blockchain and check claiming status of $COOL tokens.
 */
class NFTChecker {
  /**
   * Initialize the NFTChecker with a Solana connection.
   */
  constructor() {
    // Establish a connection to the Solana devnet cluster
    this.connection = new Connection(clusterApiUrl('devnet'));
  }

  /**
   * Get the claiming status of $COOL tokens for a given NFT number.
   * @param {string} nftNumber - The NFT number to check.
   * @returns {Promise<boolean>} - A promise resolving to the claiming status.
   */
  async getClaimingStatus(nftNumber) {
    try {
      // Replace with the actual NFT metadata program ID
      const nftMetadataProgramId = new PublicKey('metaqbxxUerdcvi4RpiTGL3QPLmii7G2MFF6uzjp2v');
      // Replace with the actual $COOL token program ID
      const coolTokenProgramId = new PublicKey('4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU');

      // Get the NFT metadata account
      const nftMetadataAccount = await this.getNFTMetadataAccount(nftNumber, nftMetadataProgramId);

      // Check if the NFT has been claimed
      const claimingStatus = await this.isClaimed(nftMetadataAccount, coolTokenProgramId);

      return claimingStatus;
    } catch (error) {
      console.error(`Error getting claiming status: ${error.message}`);
      throw error;
    }
  }

  /**
   * Get the NFT metadata account for a given NFT number.
   * @param {string} nftNumber - The NFT number.
   * @param {PublicKey} nftMetadataProgramId - The NFT metadata program ID.
   * @returns {Promise<PublicKey>} - A promise resolving to the NFT metadata account.
   */
  async getNFTMetadataAccount(nftNumber, nftMetadataProgramId) {
    // Replace with the actual NFT metadata account calculation logic
    // For demonstration purposes, assume the metadata account is derived from the NFT number
    const nftMetadataAccount = new PublicKey(nftNumber);

    return nftMetadataAccount;
  }

  /**
   * Check if an NFT has been claimed by verifying the $COOL token balance.
   * @param {PublicKey} nftMetadataAccount - The NFT metadata account.
   * @param {PublicKey} coolTokenProgramId - The $COOL token program ID.
   * @returns {Promise<boolean>} - A promise resolving to the claiming status.
   */
  async isClaimed(nftMetadataAccount, coolTokenProgramId) {
    try {
      // Get the $COOL token account
      const coolTokenAccount = await this.getCoolTokenAccount(nftMetadataAccount, coolTokenProgramId);

      // Check if the $COOL token balance is greater than 0
      const claimingStatus = (await this.getTokenBalance(coolTokenAccount)) > 0;

      return claimingStatus;
    } catch (error) {
      console.error(`Error checking claiming status: ${error.message}`);
      throw error;
    }
  }

  /**
   * Get the $COOL token account for a given NFT metadata account.
   * @param {PublicKey} nftMetadataAccount - The NFT metadata account.
   * @param {PublicKey} coolTokenProgramId - The $COOL token program ID.
   * @returns {Promise<PublicKey>} - A promise resolving to the $COOL token account.
   */
  async getCoolTokenAccount(nftMetadataAccount, coolTokenProgramId) {
    // Replace with the actual $COOL token account calculation logic
    // For demonstration purposes, assume the token account is derived from the NFT metadata account
    const coolTokenAccount = new PublicKey(nftMetadataAccount.toString());

    return coolTokenAccount;
  }

  /**
   * Get the balance of a token account.
   * @param {PublicKey} tokenAccount - The token account.
   * @returns {Promise<number>} - A promise resolving to the token balance.
   */
  async getTokenBalance(tokenAccount) {
    try {
      const balance = await this.connection.getTokenAccountBalance(tokenAccount);

      return balance.uiAmount;
    } catch (error) {
      console.error(`Error getting token balance: ${error.message}`);
      throw error;
    }
  }
}

// Example usage
async function main() {
  const nftChecker = new NFTChecker();
  const nftNumber = 'example-nft-number';

  try {
    const claimingStatus = await nftChecker.getClaimingStatus(nftNumber);
    console.log(`Claiming status for NFT ${nftNumber}: ${claimingStatus}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main();
```
