"""
Generated Code Metadata:
========================
Original URL: https://presale-hypeloot.com
Prompt: Generate a Solidity smart contract that allows users to stake $HPLT tokens and receive daily rewards based on the amount staked, as described in the Hypeloot ecosystem.
Generated: DETERMINISTIC_542e8987babd1404
Batch ID: 20250612_161035
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

// Interface for the HPLT token contract
interface IHPLT {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for HPLT tokens
contract HPLTStaking {
    // State variables
    IHPLT public hpltToken; // HPLT token contract
    uint256 public rewardRate; // Daily reward rate in HPLT tokens
    uint256 public totalStaked; // Total amount of HPLT tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastClaimed; // Last time rewards were claimed

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the HPLT token address and reward rate
    constructor(address _hpltToken, uint256 _rewardRate) {
        require(_hpltToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        hpltToken = IHPLT(_hpltToken);
        rewardRate = _rewardRate;
    }

    // Function to stake HPLT tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer HPLT tokens from the user to the contract
        require(hpltToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastClaimed[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake HPLT tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards();

        // Update staking information
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer HPLT tokens back to the user
        require(hpltToken.transferFrom(address(this), msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() public {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update last claimed time
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(hpltToken.transferFrom(address(this), msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 staked = stakedAmount[user];
        uint256 timeStaked = block.timestamp - lastClaimed[user];
        return (staked * rewardRate * timeStaked) / 1 days; // Daily rewards
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
