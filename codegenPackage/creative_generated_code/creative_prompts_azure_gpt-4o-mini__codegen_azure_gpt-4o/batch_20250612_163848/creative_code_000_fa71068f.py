"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btceftoken.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to stake Bitcoin ETF Tokens (BTCETF) and earn rewards based on the amount staked.
Generated: DETERMINISTIC_fa71068fc58238c6
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a smart contract written in Solidity for Ethereum. It allows users to stake Bitcoin ETF Tokens (BTCETF) and earn rewards based on the amount staked.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title BTCETF Staking Contract
 * @dev This contract allows users to stake BTCETF tokens and earn rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BTCETFStaking {
    // Address of BTCETF token contract
    IERC20 public immutable btcetfToken;

    // Reward rate (e.g., 0.1% per block)
    uint256 public immutable rewardRate;

    // Staker information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Rewards already paid out
        uint256 lastUpdated;    // Last staking update timestamp
    }

    // Mapping of staker addresses to their staking info
    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets the token contract address and reward rate.
     * @param _btcetfToken Address of the BTCETF token contract.
     * @param _rewardRate Reward rate per block (e.g., 0.001% = 1).
     */
    constructor(IERC20 _btcetfToken, uint256 _rewardRate) {
        require(address(_btcetfToken) != address(0), "Invalid token address");
        btcetfToken = _btcetfToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake BTCETF tokens.
     * @param _amount Number of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");
        
        Staker storage staker = stakers[msg.sender];

        // Update rewards before change
        _updateRewards(msg.sender);

        // Transfer tokens from sender to contract
        require(btcetfToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker and total staked amount
        staker.amount += _amount;
        staker.lastUpdated = block.number;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to claim staking rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked tokens");

        // Update rewards
        _updateRewards(msg.sender);

        uint256 reward = staker.rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        staker.rewardDebt = 0;

        // Transfer rewards to staker
        require(btcetfToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to unstake BTCETF tokens.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update rewards before change
        _updateRewards(msg.sender);

        // Reduce staker and total staked amount
        staker.amount -= _amount;
        staker.lastUpdated = block.number;
        totalStaked -= _amount;

        // Transfer tokens back to staker
        require(btcetfToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param _user Staker address.
     */
    function _updateRewards(address _user) internal {
        Staker storage staker = stakers[_user];

        // Calculate pending rewards
        uint256 pendingRewards = ((block.number - staker.lastUpdated) * staker.amount * rewardRate) / 1e4;

        // Add pending rewards to reward debt
        staker.rewardDebt += pendingRewards;

        // Update last updated block
        staker.lastUpdated = block.number;
    }

    /**
     * @dev View function to check pending rewards for a staker.
     * @param _user Staker address.
     * @return Pending reward amount.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];

        // Calculate rewards as if the user claimed now
        uint256 pendingRewards = ((block.number - staker.lastUpdated) * staker.amount * rewardRate) / 1e4;

        return staker.rewardDebt + pendingRewards;
    }
}
```

This code should meet all your requirements.
