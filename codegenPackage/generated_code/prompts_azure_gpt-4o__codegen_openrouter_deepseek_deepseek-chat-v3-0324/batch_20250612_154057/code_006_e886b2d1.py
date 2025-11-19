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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract RewardManager is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Reward token interface
    IERC20 public rewardToken;

    // Snapshot structure
    struct Snapshot {
        uint256 snapshotId;
        uint256 timestamp;
        uint256 totalRewards;
        uint256 totalStaked;
        mapping(address => uint256) userStakes;
    }

    // Snapshots mapping
    mapping(uint256 => Snapshot) public snapshots;
    uint256 public currentSnapshotId;

    // User rewards tracking
    mapping(address => mapping(uint256 => bool)) public hasClaimed;

    // Events
    event SnapshotCreated(uint256 indexed snapshotId, uint256 timestamp, uint256 totalRewards, uint256 totalStaked);
    event RewardsClaimed(address indexed user, uint256 indexed snapshotId, uint256 amount);
    event RewardTokenChanged(address indexed newToken);

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Create a new snapshot of staked balances
     * @param _totalRewards Total rewards to distribute for this snapshot
     * @param _stakes Array of user addresses and their staked amounts
     */
    function createSnapshot(
        uint256 _totalRewards,
        address[] memory _users,
        uint256[] memory _stakes
    ) external onlyOwner {
        require(_users.length == _stakes.length, "Arrays length mismatch");
        require(_totalRewards > 0, "Rewards must be greater than 0");

        currentSnapshotId++;
        Snapshot storage newSnapshot = snapshots[currentSnapshotId];
        newSnapshot.snapshotId = currentSnapshotId;
        newSnapshot.timestamp = block.timestamp;
        newSnapshot.totalRewards = _totalRewards;

        uint256 totalStaked;
        for (uint256 i = 0; i < _users.length; i++) {
            require(_users[i] != address(0), "Invalid user address");
            require(_stakes[i] > 0, "Stake must be greater than 0");
            
            newSnapshot.userStakes[_users[i]] = _stakes[i];
            totalStaked = totalStaked.add(_stakes[i]);
        }

        newSnapshot.totalStaked = totalStaked;
        
        // Transfer rewards to contract
        require(
            rewardToken.transferFrom(msg.sender, address(this), _totalRewards),
            "Reward transfer failed"
        );

        emit SnapshotCreated(currentSnapshotId, block.timestamp, _totalRewards, totalStaked);
    }

    /**
     * @dev Calculate user's reward for a specific snapshot
     * @param _user User address
     * @param _snapshotId Snapshot ID to calculate rewards for
     * @return rewardAmount Calculated reward amount
     */
    function calculateReward(address _user, uint256 _snapshotId) public view returns (uint256) {
        require(_snapshotId <= currentSnapshotId && _snapshotId > 0, "Invalid snapshot ID");
        
        Snapshot storage snapshot = snapshots[_snapshotId];
        if (snapshot.totalStaked == 0) return 0;
        
        uint256 userStake = snapshot.userStakes[_user];
        if (userStake == 0) return 0;
        
        return snapshot.totalRewards.mul(userStake).div(snapshot.totalStaked);
    }

    /**
     * @dev Claim rewards for a specific snapshot
     * @param _snapshotId Snapshot ID to claim rewards from
     */
    function claimReward(uint256 _snapshotId) external nonReentrant {
        require(_snapshotId <= currentSnapshotId && _snapshotId > 0, "Invalid snapshot ID");
        require(!hasClaimed[msg.sender][_snapshotId], "Rewards already claimed");

        uint256 rewardAmount = calculateReward(msg.sender, _snapshotId);
        require(rewardAmount > 0, "No rewards to claim");

        hasClaimed[msg.sender][_snapshotId] = true;
        
        require(
            rewardToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, _snapshotId, rewardAmount);
    }

    /**
     * @dev Batch claim rewards for multiple snapshots
     * @param _snapshotIds Array of snapshot IDs to claim rewards from
     */
    function batchClaimRewards(uint256[] memory _snapshotIds) external nonReentrant {
        uint256 totalReward;
        
        for (uint256 i = 0; i < _snapshotIds.length; i++) {
            uint256 snapshotId = _snapshotIds[i];
            
            require(snapshotId <= currentSnapshotId && snapshotId > 0, "Invalid snapshot ID");
            require(!hasClaimed[msg.sender][snapshotId], "Rewards already claimed");
            
            uint256 rewardAmount = calculateReward(msg.sender, snapshotId);
            if (rewardAmount > 0) {
                hasClaimed[msg.sender][snapshotId] = true;
                totalReward = totalReward.add(rewardAmount);
            }
        }
        
        require(totalReward > 0, "No rewards to claim");
        
        require(
            rewardToken.transfer(msg.sender, totalReward),
            "Reward transfer failed"
        );

        for (uint256 i = 0; i < _snapshotIds.length; i++) {
            if (calculateReward(msg.sender, _snapshotIds[i]) > 0) {
                emit RewardsClaimed(msg.sender, _snapshotIds[i], calculateReward(msg.sender, _snapshotIds[i]));
            }
        }
    }

    /**
     * @dev Change the reward token (owner only)
     * @param _newToken Address of the new reward token
     */
    function changeRewardToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        rewardToken = IERC20(_newToken);
        emit RewardTokenChanged(_newToken);
    }

    /**
     * @dev Withdraw any ERC20 tokens (owner only)
     * @param _token Address of the token to withdraw
     * @param _amount Amount to withdraw
     */
    function withdrawERC20(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(_token);
        require(
            token.transfer(msg.sender, _amount),
            "Token transfer failed"
        );
    }
}
```
