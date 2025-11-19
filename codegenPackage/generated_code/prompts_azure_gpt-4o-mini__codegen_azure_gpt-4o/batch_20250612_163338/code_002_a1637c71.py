"""
Generated Code Metadata:
========================
Original URL: https://daddysunversity.com
Prompt: Create a Solidity smart contract that allows users to stake $DADDY tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_a1637c71fada9b6f
Batch ID: 20250612_163338
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

/**
 * @title DaddyTokenStaking
 * @dev A smart contract that allows users to stake $DADDY tokens and earn rewards based on their holdings.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DaddyTokenStaking {
    // Address of the $DADDY token contract
    IERC20 public daddyToken;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Last time the stake was updated
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _daddyToken Address of the $DADDY token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _daddyToken, uint256 _rewardRate) {
        daddyToken = _daddyToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $DADDY tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(daddyToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Update staking information
        stakes[msg.sender].amount -= _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(daddyToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Calculate the reward to be claimed
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(daddyToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage stakeInfo = stakes[_user];

        // Calculate pending rewards
        uint256 pendingRewards = (block.timestamp - stakeInfo.lastUpdated) * stakeInfo.amount * rewardRate;

        // Update reward debt and last updated timestamp
        stakeInfo.rewardDebt += pendingRewards;
        stakeInfo.lastUpdated = block.timestamp;
    }

    /**
     * @dev View function to check pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage stakeInfo = stakes[_user];
        uint256 pendingRewards = (block.timestamp - stakeInfo.lastUpdated) * stakeInfo.amount * rewardRate;
        return stakeInfo.rewardDebt + pendingRewards;
    }
}
```
