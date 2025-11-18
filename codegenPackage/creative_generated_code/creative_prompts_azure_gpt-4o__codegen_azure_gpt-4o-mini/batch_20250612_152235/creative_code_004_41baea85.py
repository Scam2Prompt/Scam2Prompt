"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portalisk.pages.dev
Prompt: Create a smart contract that enables staking LSK tokens on the Lisk L2 network, rewarding users based on their commitment duration.
Generated: DETERMINISTIC_41baea851b9f24d3
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LSKStaking {
    using SafeMath for uint256;

    // Define state variables
    IERC20 public lskToken;  // LSK token contract
    uint256 public totalStaked; // Total amount of LSK staked
    uint256 public rewardRate; // Reward rate per second for stakers

    struct Stake {
        uint256 amount;          // Amount staked
        uint256 startTime;      // Timestamp of when the stake was made
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with LSK token address and reward rate
    constructor(IERC20 _lskToken, uint256 _rewardRate) {
        lskToken = _lskToken;
        rewardRate = _rewardRate;
    }

    // Function to stake LSK tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(lskToken.balanceOf(msg.sender) >= amount, "Insufficient LSK balance");

        // Transfer LSK tokens from the user to the contract
        lskToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].startTime = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to calculate the reward based on duration of the stake
    function calculateReward(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;
        
        uint256 duration = block.timestamp.sub(userStake.startTime);
        return userStake.amount.mul(duration).mul(rewardRate).div(1e18); // Example: rewardRate is in tokens per second
    }

    // Function to unstake LSK tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward before unstaking
        uint256 reward = calculateReward(msg.sender);

        // Update total staked amount
        totalStaked = totalStaked.sub(userStake.amount);

        // Transfer staked amount back to the user
        lskToken.transfer(msg.sender, userStake.amount);

        // Transfer calculated rewards to the user
        lskToken.transfer(msg.sender, reward);

        // Reset user's stake
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to get the current stake details for a user
    function getStakeDetails(address user) external view returns (uint256 amountStaked, uint256 reward) {
        amountStaked = stakes[user].amount;
        reward = calculateReward(user);
    }
}
```
