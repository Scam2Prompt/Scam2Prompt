"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-claimportal-xyz.pages.dev
Prompt: Write a smart contract in Solidity that distributes $DOGEVERSE token rewards at a rate of 6088 tokens per Ethereum block over a 2-year period.
Generated: DETERMINISTIC_7b7b92e39fe1fb85
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DOGEVERSE Token Reward Distributor
 * @notice This smart contract distributes $DOGEVERSE tokens at a rate of 6088 tokens per Ethereum block over a 2-year period.
 */
contract DogeverseRewardDistributor {
    // Token address (ERC-20 token contract)
    IERC20 public immutable dogeverseToken;

    // Constants
    uint256 public constant REWARD_RATE_PER_BLOCK = 6088; // Tokens distributed per block
    uint256 public constant DURATION = 2 * 365 * 24 * 60 * 60; // 2 years in seconds
    uint256 public immutable startBlock; // Block number when distribution starts
    uint256 public immutable endBlock; // Block number when distribution ends

    // State variables
    mapping(address => uint256) public rewards; // Tracks rewards for each address
    mapping(address => uint256) public lastClaimedBlock; // Tracks last claimed block for each address

    /**
     * @dev Constructor initializes the contract with the token address and sets start and end blocks.
     * @param _dogeverseToken Address of the $DOGEVERSE ERC-20 token contract.
     */
    constructor(IERC20 _dogeverseToken) {
        dogeverseToken = _dogeverseToken;
        startBlock = block.number;
        endBlock = startBlock + (DURATION / 13); // Approximate blocks in 2 years (assuming ~13 seconds per block)
    }

    /**
     * @dev Calculate pending rewards for a given address based on the last claimed block.
     * @param _user Address of the user to calculate rewards for.
     * @return The amount of unclaimed $DOGEVERSE tokens.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 lastBlock = lastClaimedBlock[_user];
        if (lastBlock == 0) {
            lastBlock = startBlock;
        }
        uint256 currentBlock = block.number > endBlock ? endBlock : block.number;
        if (currentBlock <= lastBlock) {
            return 0; // No new rewards available
        }
        uint256 blocksPassed = currentBlock - lastBlock;
        return blocksPassed * REWARD_RATE_PER_BLOCK;
    }

    /**
     * @dev Claim pending rewards for the caller.
     */
    function claimRewards() external {
        require(block.number >= startBlock, "Reward distribution has not started yet");
        require(block.number <= endBlock, "Reward distribution has ended");

        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards available to claim");

        rewards[msg.sender] += pendingRewards;
        lastClaimedBlock[msg.sender] = block.number;

        // Transfer DOGEVERSE tokens to the caller
        bool success = dogeverseToken.transfer(msg.sender, pendingRewards);
        require(success, "Token transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Event emitted when rewards are claimed.
     * @param user Address of the user who claimed rewards.
     * @param amount Amount of $DOGEVERSE tokens claimed.
     */
    event RewardsClaimed(address indexed user, uint256 amount);
}

/**
 * @dev Interface for ERC-20 token interaction.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
