"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsdexprotocols.xyz
Prompt: Create a dApp feature for managing snapshots and claiming rewards, based on the BlockchainDeFi protocol specifications.
Generated: DETERMINISTIC_e886b2d1e64b2d52
Batch ID: 20250612_154057
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Snapshot feature
interface ISnapshot {
    function createSnapshot() external returns (uint256);
    function getSnapshot(uint256 snapshotId) external view returns (address[] memory);
}

// Main contract for managing snapshots and claiming rewards
contract SnapshotManager is Ownable {
    // Event emitted when a snapshot is created
    event SnapshotCreated(uint256 indexed snapshotId);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold snapshot information
    struct Snapshot {
        uint256 id;
        address[] participants;
        mapping(address => uint256) rewards;
    }

    // Mapping of snapshots by ID
    mapping(uint256 => Snapshot) private snapshots;

    // Counter for snapshot IDs
    uint256 private snapshotCounter;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Modifier to ensure a valid snapshot ID
    modifier validSnapshot(uint256 snapshotId) {
        require(snapshotId < snapshotCounter, "Invalid snapshot ID");
        _;
    }

    // Constructor to set the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Function to create a new snapshot
    function createSnapshot() external onlyOwner returns (uint256) {
        uint256 snapshotId = snapshotCounter++;
        Snapshot storage newSnapshot = snapshots[snapshotId];

        // Add participants (for example purposes, using msg.sender)
        newSnapshot.participants.push(msg.sender);

        emit SnapshotCreated(snapshotId);
        return snapshotId;
    }

    // Function to get participants of a specific snapshot
    function getSnapshot(uint256 snapshotId) external view validSnapshot(snapshotId) returns (address[] memory) {
        return snapshots[snapshotId].participants;
    }

    // Function to claim rewards for a specific snapshot
    function claimRewards(uint256 snapshotId) external validSnapshot(snapshotId) {
        Snapshot storage snapshot = snapshots[snapshotId];
        uint256 rewardAmount = snapshot.rewards[msg.sender];

        // Check if the user has rewards to claim
        require(rewardAmount > 0, "No rewards available");

        // Reset the user's reward to prevent re-entrancy
        snapshot.rewards[msg.sender] = 0;

        // Transfer rewards to the user
        bool success = rewardToken.transfer(msg.sender, rewardAmount);
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to set rewards for participants in a snapshot
    function setRewards(uint256 snapshotId, address user, uint256 amount) external onlyOwner validSnapshot(snapshotId) {
        snapshots[snapshotId].rewards[user] = amount;
    }
}
```
