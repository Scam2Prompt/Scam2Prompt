"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.zh-imtokenwallet.com
Prompt: Develop a smart contract that integrates with imToken's ecosystem to enable staking and real-time yield tracking for ATOM tokens.
Generated: DETERMINISTIC_e916030356d6dcf4
Batch ID: 20250612_150816
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AtomStaking
 * @dev A smart contract for staking ATOM tokens and tracking real-time yields.
 */
contract AtomStaking is Ownable {
    // State variables for staking
    IERC20 public atomToken;        // ERC20 token interface for ATOM
    uint256 public totalStaked;     // Total amount of ATOM staked
    uint256 public rewardRate;       // Annual reward rate in basis points (1% = 100)
    
    // Mapping for user stakes and rewards
    mapping(address => uint256) private stakes;         // Tracks individual user stakes
    mapping(address => uint256) private rewards;        // Tracks individual user rewards
    mapping(address => uint256) private lastUpdate;     // Last update timestamp for user rewards

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @param _atomToken Address of the ATOM token contract
     * @param _rewardRate Annual reward rate in basis points
     */
    constructor(address _atomToken, uint256 _rewardRate) {
        atomToken = IERC20(_atomToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake ATOM tokens.
     * @param amount Amount of ATOM tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(atomToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user rewards before staking
        _updateRewards(msg.sender);

        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked ATOM tokens.
     * @param amount Amount of ATOM tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user rewards before withdrawing
        _updateRewards(msg.sender);

        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        require(atomToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];

        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;

        // Assuming the contract has enough balance to pay rewards
        require(atomToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user The address of the user
     */
    function _updateRewards(address user) internal {
        // Calculate rewards based on the time staked and the reward rate
        if (stakes[user] > 0) {
            uint256 reward = (stakes[user] * rewardRate * (block.timestamp - lastUpdate[user])) / (365 days * 10000);
            rewards[user] += reward;
        }
        // Update last update timestamp
        lastUpdate[user] = block.timestamp;
    }

    /**
     * @dev Returns the staked amount of a user.
     * @param user The address of the user
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @dev Returns the pending rewards of a user.
     * @param user The address of the user
     */
    function getPendingRewards(address user) external view returns (uint256) {
        uint256 reward = rewards[user];
        if (stakes[user] > 0) {
            reward += (stakes[user] * rewardRate * (block.timestamp - lastUpdate[user])) / (365 days * 10000);
        }
        return reward;
    }
}
```
