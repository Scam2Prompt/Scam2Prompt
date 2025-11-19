"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-en.web.app
Prompt: Develop a simple smart contract in Solidity for staking Poodl Inu tokens on the Ethereum blockchain, including functions for staking, claiming rewards, and checking balances.
Generated: DETERMINISTIC_d3c8b214f7888ceb
Batch ID: 20250622_210703
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
 * @title Poodl Inu Staking Contract
 * @dev A simple smart contract for staking Poodl Inu tokens, claiming rewards, and checking balances.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PoodlInuStaking {
    // Address of the Poodl Inu token contract
    IERC20 public poodlToken;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastUpdated; // Last time rewards were calculated
        uint256 rewardDebt; // Accumulated rewards
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _poodlToken Address of the Poodl Inu token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _poodlToken, uint256 _rewardRate) {
        poodlToken = _poodlToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake Poodl Inu tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(poodlToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Calculate the reward to be claimed
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(poodlToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Claimed(msg.sender, reward);
    }

    /**
     * @dev Withdraw staked tokens.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Update staking information
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        require(poodlToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Check the staked balance of a user.
     * @param _user Address of the user.
     * @return The staked balance of the user.
     */
    function stakedBalance(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    /**
     * @dev Check the pending rewards of a user.
     * @param _user Address of the user.
     * @return The pending rewards of the user.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake memory stakeInfo = stakes[_user];
        uint256 accumulatedRewards = (block.timestamp - stakeInfo.lastUpdated) * rewardRate * stakeInfo.amount;
        return accumulatedRewards + stakeInfo.rewardDebt;
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage stakeInfo = stakes[_user];
        if (stakeInfo.amount > 0) {
            uint256 accumulatedRewards = (block.timestamp - stakeInfo.lastUpdated) * rewardRate * stakeInfo.amount;
            stakeInfo.rewardDebt += accumulatedRewards;
        }
        stakeInfo.lastUpdated = block.timestamp;
    }
}
```
