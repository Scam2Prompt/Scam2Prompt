"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-in.web.app
Prompt: Develop a simple staking mechanism for a cryptocurrency project using Solidity, inspired by the staking rewards system described in the Rebel Satoshi ecosystem.
Generated: DETERMINISTIC_6c6b423a9f3e044d
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

contract Staking {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt;    // Reward debt for the staker
        uint256 lastStakedTime; // Last time the staker staked
    }

    // Mapping of stakers' addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Token contract address
    IERC20 public token;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        _claimRewards();

        // Update staker's information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _claimRewards();
    }

    // Internal function to calculate and distribute rewards
    function _claimRewards() internal {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingRewards = calculateRewards(msg.sender);

        if (pendingRewards > 0) {
            staker.rewardDebt += pendingRewards;
            require(token.transfer(msg.sender, pendingRewards), "Transfer failed");
            emit RewardsClaimed(msg.sender, pendingRewards);
        }

        // Update last staked time
        staker.lastStakedTime = block.timestamp;
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        return (staker.amountStaked * rewardRate * timeStaked) / 1e18; // Adjust for reward rate precision
    }

    // Function to get the staker's information
    function getStakerInfo(address stakerAddress) external view returns (uint256 amountStaked, uint256 rewardDebt) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amountStaked, staker.rewardDebt);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
