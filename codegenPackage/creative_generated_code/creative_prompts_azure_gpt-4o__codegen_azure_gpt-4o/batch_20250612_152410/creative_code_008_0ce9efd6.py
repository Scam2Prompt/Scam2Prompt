"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Generate a TypeScript smart contract for Neo N3 that supports GAS rewards distribution for governance participation and voting.
Generated: DETERMINISTIC_0ce9efd6a559023b
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Neo N3 Smart Contract for GAS rewards distribution based on governance participation and voting.
// SPDX-License-Identifier: MIT
import { storage, Blockchain, Contract, Runtime, u, Wallet } from '@neo-one/smart-contract';

// Constants
const OWNER = 'NdXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'; // Replace with contract owner's address
const VOTE_STORAGE_PREFIX = 'vote_';
const REWARDS_STORAGE_PREFIX = 'reward_';
const TOTAL_REWARDS_KEY = 'total_rewards';
const MIN_VOTE_AMOUNT = 10; // Minimum amount of GAS for participation

// Error messages
const ERR_NOT_OWNER = 'Caller is not the owner.';
const ERR_INSUFFICIENT_GAS = 'Insufficient GAS sent for voting.';
const ERR_NO_VOTES = 'No votes recorded for this address.';
const ERR_ALREADY_RECORDED = 'Vote already recorded.';

// Smart Contract
export class GovernanceRewardsContract {
  /**
   * @notice Vote by sending GAS and assigning participation.
   * @param voteId - Unique identifier for the vote being participated in.
   */
  public static vote(voteId: string): boolean {
    // Ensure the caller sends enough GAS for participation.
    const contribution = Runtime.checkWitness(Blockchain.currentTransaction.sender);
    if (!contribution || Blockchain.currentTransaction.amount < MIN_VOTE_AMOUNT) {
      throw new Error(ERR_INSUFFICIENT_GAS);
    }

    const sender = Blockchain.currentTransaction.sender.toString();
    const voteKey = `${VOTE_STORAGE_PREFIX}${sender}_${voteId}`;

    // Check for duplicate votes.
    if (storage.get(voteKey) !== undefined) {
      throw new Error(ERR_ALREADY_RECORDED);
    }

    // Record the vote and contribution.
    storage.set(voteKey, Blockchain.currentTransaction.amount.toString());
    GovernanceRewardsContract._increaseTotalRewards(Blockchain.currentTransaction.amount);
    return true;
  }

  /**
   * @notice Claim rewards for participation.
   * @param voteId - The vote for which rewards should be claimed.
   */
  public static claimRewards(voteId: string): number {
    const sender = Blockchain.currentTransaction.sender.toString();
    const voteKey = `${VOTE_STORAGE_PREFIX}${sender}_${voteId}`;

    // Retrieve the stored GAS contribution.
    const contribution = storage.get(voteKey);
    if (contribution === undefined) {
      throw new Error(ERR_NO_VOTES);
    }

    const rewardKey = `${REWARDS_STORAGE_PREFIX}${sender}_${voteId}`;
    const alreadyClaimed = storage.get(rewardKey) !== undefined;
    if (alreadyClaimed) {
      throw new Error(ERR_ALREADY_RECORDED);
    }

    // Calculate rewards (e.g., 10% of contribution).
    const rewardAmount = u.BigInteger.fromString(contribution).div(10);
    Contract.transfer(Runtime.executingScriptHash, sender, rewardAmount);

    // Mark rewards as claimed.
    storage.set(rewardKey, rewardAmount.toString());
    return rewardAmount.toNumber();
  }

  /**
   * @notice Add GAS rewards balance to the contract (only owner).
   */
  public static fundContract(): boolean {
    if (!Runtime.checkWitness(OWNER)) {
      throw new Error(ERR_NOT_OWNER);
    }

    GovernanceRewardsContract._increaseTotalRewards(Blockchain.currentTransaction.amount);
    return true;
  }

  /**
   * @notice Retrieve the total rewards balance of the contract.
   */
  public static totalRewards(): number {
    const totalRewards = storage.get(TOTAL_REWARDS_KEY);
    return totalRewards ? u.BigInteger.fromString(totalRewards).toNumber() : 0;
  }

  /**
   * @private Increase the total rewards balance in storage.
   * @param amount - The amount of GAS to increase.
   */
  private static _increaseTotalRewards(amount: u.BigInteger): void {
    const currentRewards = storage.get(TOTAL_REWARDS_KEY);
    const updatedRewards = currentRewards
      ? u.BigInteger.fromString(currentRewards).add(amount)
      : amount;
    storage.set(TOTAL_REWARDS_KEY, updatedRewards.toString());
  }
}
```
