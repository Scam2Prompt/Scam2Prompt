"""
Generated Code Metadata:
========================
Original URL: https://dappsdexprotocols.xyz
Prompt: Create a dApp feature for managing snapshots and claiming rewards, based on the BlockchainDeFi protocol specifications.
Generated: DETERMINISTIC_e886b2d1e64b2d52
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SnapshotManager
 * @dev A smart contract for managing snapshots and claiming rewards in a DeFi protocol.
 */
contract SnapshotManager is Ownable {
    // Event emitted when a new snapshot is created
    event SnapshotCreated(uint256 indexed snapshotId, uint256 timestamp);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold snapshot data
    struct Snapshot {
        uint256 id;
        uint256 timestamp;
        mapping(address => uint256) balances; // User balances at the time of snapshot
    }

    // Mapping of snapshot ID to Snapshot data
    mapping(uint256 => Snapshot) private snapshots;
    uint256 private currentSnapshotId;

    // Token used for rewards
    IERC20 public rewardToken;

    // Mapping to track claimed rewards
    mapping(address => uint256) public claimedRewards;

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Creates a new snapshot and records the balances of all users.
     */
    function createSnapshot() external onlyOwner {
        currentSnapshotId++;
        Snapshot storage newSnapshot = snapshots[currentSnapshotId];
        newSnapshot.id = currentSnapshotId;
        newSnapshot.timestamp = block.timestamp;

        // Record balances of all users (this is a simplified example)
        // In a real implementation, you would iterate over a list of users
        // and record their balances.
        emit SnapshotCreated(currentSnapshotId, block.timestamp);
    }

    /**
     * @dev Allows users to claim rewards based on their snapshot balances.
     * @param snapshotId The ID of the snapshot to claim rewards from.
     */
    function claimRewards(uint256 snapshotId) external {
        require(snapshotId <= currentSnapshotId, "Invalid snapshot ID");
        Snapshot storage snapshot = snapshots[snapshotId];

        // Check if the user has a balance in the snapshot
        uint256 userBalance = snapshot.balances[msg.sender];
        require(userBalance > 0, "No rewards to claim");

        // Calculate the reward amount (this is a placeholder logic)
        uint256 rewardAmount = userBalance; // Replace with actual reward calculation

        // Ensure the contract has enough tokens to pay the reward
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient reward tokens");

        // Transfer the reward tokens to the user
        claimedRewards[msg.sender] += rewardAmount;
        rewardToken.transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows the owner to withdraw any tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        rewardToken.transfer(owner(), amount);
    }
}
```
