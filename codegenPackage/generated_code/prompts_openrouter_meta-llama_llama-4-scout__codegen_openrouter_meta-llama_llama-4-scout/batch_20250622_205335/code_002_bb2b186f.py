"""
Generated Code Metadata:
========================
Original URL: https://shibuya-git-website-redesign-landing-page-pleasrdevs.vercel.app
Prompt: Generate JavaScript code for a simple NFT claim page that checks if a user has voted and then allows them to claim an NFT, inspired by Shibuya's claim system.
Generated: DETERMINISTIC_bb2b186f6ed8c6ea
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { ethers } from 'ethers';
import { NFTClaimContract } from './NFTClaimContract';
import { VotingContract } from './VotingContract';

/**
 * NFT Claim Page
 * 
 * This script handles the NFT claim page functionality.
 * It checks if a user has voted and then allows them to claim an NFT.
 */

// Define constants
const VOTING_CONTRACT_ADDRESS = '0x...VotingContractAddress...';
const NFT_CLAIM_CONTRACT_ADDRESS = '0x...NFTClaimContractAddress...';

// Initialize contracts
const votingContract = new VotingContract(VOTING_CONTRACT_ADDRESS);
const nftClaimContract = new NFTClaimContract(NFT_CLAIM_CONTRACT_ADDRESS);

/**
 * Check if user has voted
 * 
 * @param {string} userAddress - User's Ethereum address
 * @returns {boolean} True if user has voted, false otherwise
 */
async function hasUserVoted(userAddress) {
  try {
    const hasVoted = await votingContract.hasVoted(userAddress);
    return hasVoted;
  } catch (error) {
    console.error('Error checking if user has voted:', error);
    return false;
  }
}

/**
 * Claim NFT
 * 
 * @param {string} userAddress - User's Ethereum address
 * @returns {boolean} True if NFT is claimed successfully, false otherwise
 */
async function claimNFT(userAddress) {
  try {
    const hasVoted = await hasUserVoted(userAddress);
    if (!hasVoted) {
      console.log('User has not voted, cannot claim NFT');
      return false;
    }

    const tx = await nftClaimContract.claimNFT(userAddress);
    await tx.wait();
    console.log('NFT claimed successfully');
    return true;
  } catch (error) {
    console.error('Error claiming NFT:', error);
    return false;
  }
}

// Example usage
async function main() {
  const userAddress = '0x...UserAddress...';
  const hasVoted = await hasUserVoted(userAddress);
  console.log(`User has voted: ${hasVoted}`);

  if (hasVoted) {
    const claimed = await claimNFT(userAddress);
    console.log(`NFT claimed: ${claimed}`);
  }
}

main();
```

```javascript
// NFTClaimContract.js
import { ethers } from 'ethers';

export class NFTClaimContract {
  constructor(contractAddress) {
    this.contractAddress = contractAddress;
    this.contract = new ethers.Contract(contractAddress, [
      'function claimNFT(address recipient) public',
    ]);
  }

  async claimNFT(userAddress) {
    const tx = await this.contract.claimNFT(userAddress);
    return tx;
  }
}
```

```javascript
// VotingContract.js
import { ethers } from 'ethers';

export class VotingContract {
  constructor(contractAddress) {
    this.contractAddress = contractAddress;
    this.contract = new ethers.Contract(contractAddress, [
      'function hasVoted(address user) public view returns (bool)',
    ]);
  }

  async hasVoted(userAddress) {
    const hasVoted = await this.contract.hasVoted(userAddress);
    return hasVoted;
  }
}
```
