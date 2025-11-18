"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orchidprotocols.com
Prompt: Create a smart contract in Solidity that interacts with Orchid’s OXT token for staking and accessing decentralized services.
Generated: DETERMINISTIC_3c40d5081974ecc9
Batch ID: 20250612_151912
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

interface IOXTToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @title OrchidStaking
 * @dev Smart contract for staking OXT tokens to access decentralized services
 */
contract OrchidStaking {
    // State variables
    IOXTToken public oxtToken; // Interface to interact with OXT token
    mapping(address => uint256) public stakedAmount; // User's staked amounts
    mapping(address => uint256) public rewards; // User's accumulated rewards
    uint256 public totalStaked; // Total amount of OXT staked
    uint256 public rewardRate; // Reward rate for staking

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the OXT token address and reward rate
     * @param _oxtToken Address of the OXT token contract
     * @param _rewardRate Reward rate for staking
     */
    constructor(address _oxtToken, uint256 _rewardRate) {
        oxtToken = IOXTToken(_oxtToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake OXT tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(oxtToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user staking information
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked OXT tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update user staking information
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(oxtToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        uint256 userRewards = calculateRewards(msg.sender);
        require(userRewards > 0, "No rewards to claim");

        // Reset user's rewards
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(oxtToken.transfer(msg.sender, userRewards), "Transfer failed");

        emit RewardClaimed(msg.sender, userRewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param user Address of the user
     * @return Amount of rewards eligible for the user
     */
    function calculateRewards(address user) public view returns (uint256) {
        return (stakedAmount[user] * rewardRate) / 1e18; // Assuming rewardRate is set with 18 decimals
    }
}
```
