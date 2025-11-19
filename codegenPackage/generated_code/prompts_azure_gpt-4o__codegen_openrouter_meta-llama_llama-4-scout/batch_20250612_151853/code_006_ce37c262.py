"""
Generated Code Metadata:
========================
Original URL: https://doggodao.web.app
Prompt: Create a staking mechanism for Solana NFT projects that rewards users with $DOGGO tokens, including wallet integration and reward calculation.
Generated: DETERMINISTIC_ce37c262032c5609
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// staking-mechanism.js

/**
 * Staking mechanism for Solana NFT projects that rewards users with $DOGGO tokens.
 */

const { 
  Connection, 
  PublicKey, 
  Transaction, 
  clusterApiUrl 
} = require('@solana/web3.js');
const { 
  NFTStakingProgram, 
  DOGGOToken 
} = require('./programs');

/**
 * Initialize staking mechanism.
 * @param {string} rpcUrl - Solana RPC URL.
 * @param {string} nftStakingProgramId - NFT staking program ID.
 * @param {string} doggoTokenMint - $DOGGO token mint address.
 */
async function initStakingMechanism(rpcUrl, nftStakingProgramId, doggoTokenMint) {
  // Establish connection to Solana cluster.
  const connection = new Connection(rpcUrl, 'confirmed');

  // Initialize NFT staking program.
  const nftStakingProgram = new NFTStakingProgram(
    new PublicKey(nftStakingProgramId), 
    connection
  );

  // Initialize $DOGGO token.
  const doggoToken = new DOGGOToken(
    new PublicKey(doggoTokenMint), 
    connection
  );

  return { 
    connection, 
    nftStakingProgram, 
    doggoToken 
  };
}

/**
 * Stake an NFT.
 * @param {object} stakingMechanism - Staking mechanism object.
 * @param {string} nftMint - NFT mint address.
 * @param {string} userWallet - User wallet address.
 */
async function stakeNFT(stakingMechanism, nftMint, userWallet) {
  try {
    // Get user's stake account.
    const stakeAccount = await stakingMechanism.nftStakingProgram.getStakeAccount(
      new PublicKey(userWallet)
    );

    // Check if user has already staked an NFT.
    if (stakeAccount.nftMint.toString() !== '') {
      throw new Error('User has already staked an NFT.');
    }

    // Create stake transaction.
    const transaction = new Transaction();
    transaction.add(
      stakingMechanism.nftStakingProgram.stakeInstruction(
        new PublicKey(userWallet), 
        new PublicKey(nftMint)
      )
    );

    // Sign and send transaction.
    const signature = await stakingMechanism.connection.sendTransaction(
      transaction, 
      [new PublicKey(userWallet)]
    );

    return signature;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

/**
 * Unstake an NFT.
 * @param {object} stakingMechanism - Staking mechanism object.
 * @param {string} userWallet - User wallet address.
 */
async function unstakeNFT(stakingMechanism, userWallet) {
  try {
    // Get user's stake account.
    const stakeAccount = await stakingMechanism.nftStakingProgram.getStakeAccount(
      new PublicKey(userWallet)
    );

    // Check if user has staked an NFT.
    if (stakeAccount.nftMint.toString() === '') {
      throw new Error('User has not staked an NFT.');
    }

    // Create unstake transaction.
    const transaction = new Transaction();
    transaction.add(
      stakingMechanism.nftStakingProgram.unstakeInstruction(
        new PublicKey(userWallet)
      )
    );

    // Sign and send transaction.
    const signature = await stakingMechanism.connection.sendTransaction(
      transaction, 
      [new PublicKey(userWallet)]
    );

    return signature;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

/**
 * Calculate $DOGGO token reward.
 * @param {object} stakingMechanism - Staking mechanism object.
 * @param {string} userWallet - User wallet address.
 * @returns {number} Reward amount.
 */
async function calculateReward(stakingMechanism, userWallet) {
  try {
    // Get user's stake account.
    const stakeAccount = await stakingMechanism.nftStakingProgram.getStakeAccount(
      new PublicKey(userWallet)
    );

    // Calculate reward based on stake duration and NFT metadata.
    const reward = await stakingMechanism.nftStakingProgram.calculateReward(
      stakeAccount
    );

    return reward;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

// Example usage:
async function main() {
  // Replace with your Solana RPC URL.
  const rpcUrl = clusterApiUrl('devnet');

  // Replace with your NFT staking program ID.
  const nftStakingProgramId = 'your-nft-staking-program-id';

  // Replace with your $DOGGO token mint address.
  const doggoTokenMint = 'your-doggo-token-mint';

  // Initialize staking mechanism.
  const stakingMechanism = await initStakingMechanism(
    rpcUrl, 
    nftStakingProgramId, 
    doggoTokenMint
  );

  // Stake an NFT.
  const nftMint = 'your-nft-mint';
  const userWallet = 'your-user-wallet';
  const stakeSignature = await stakeNFT(
    stakingMechanism, 
    nftMint, 
    userWallet
  );
  console.log(`Stake signature: ${stakeSignature}`);

  // Calculate $DOGGO token reward.
  const reward = await calculateReward(
    stakingMechanism, 
    userWallet
  );
  console.log(`Reward: ${reward}`);

  // Unstake an NFT.
  const unstakeSignature = await unstakeNFT(
    stakingMechanism, 
    userWallet
  );
  console.log(`Unstake signature: ${unstakeSignature}`);
}

main();
```
