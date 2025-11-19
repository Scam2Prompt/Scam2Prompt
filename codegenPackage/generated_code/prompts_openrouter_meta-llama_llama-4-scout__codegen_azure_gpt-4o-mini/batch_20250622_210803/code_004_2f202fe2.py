"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: "Develop a smart contract on MultiversX that utilizes the EGLD token for transaction fees and staking rewards."
Generated: DETERMINISTIC_2f202fe2dec397dc
Batch ID: 20250622_210803
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

// Importing necessary interfaces and libraries
import "@multiversx/sdk-core/contracts/token/ERC20.sol";
import "@multiversx/sdk-core/contracts/access/Ownable.sol";

// Smart contract for staking and rewards using EGLD token
contract StakingContract is Ownable {
    // State variables
    IERC20 public eglDToken; // Reference to the EGLD token contract
    uint256 public totalStaked; // Total amount of EGLD staked
    mapping(address => uint256) public stakedBalances; // User's staked balance
    mapping(address => uint256) public rewards; // User's rewards
    uint256 public rewardRate; // Rate at which rewards are calculated

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the EGLD token address and reward rate
    constructor(address _eglDToken, uint256 _rewardRate) {
        eglDToken = IERC20(_eglDToken);
        rewardRate = _rewardRate;
    }

    // Function to stake EGLD tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(eglDToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked balance and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake EGLD tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        require(eglDToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0; // Reset rewards after claiming
        require(eglDToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        return stakedBalances[user] * rewardRate / 1e18; // Example calculation
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(eglDToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
