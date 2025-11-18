"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-ethereum.com
Prompt: Write code to create a smart contract that interacts with an Ethereum wallet for staking ETH in a DeFi protocol.
Generated: DETERMINISTIC_5fe8cd236e05aad6
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

// Importing relevant interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the StakingContract
contract StakingContract is Ownable {
    // State variables
    IERC20 public stakingToken; // The ERC20 token to be staked
    mapping(address => uint256) public stakes; // Mapping of user stakes
    mapping(address => uint256) public rewards; // Mapping of user rewards

    uint256 public rewardRate = 100; // Reward rate per block
    uint256 public totalStaked; // Total amount staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender] >= amount, "Insufficient stake");

        // Update user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards
    function calculateReward(address user) public view returns (uint256) {
        return (stakes[user] * rewardRate) / 1e18; // Adjust for precision
    }

    // Function to claim rewards
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update the rewards mapping before transferring
        rewards[msg.sender] += reward; 

        // Transfer rewards to the user (in this case, using ETH)
        payable(msg.sender).transfer(reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Fallback function to accept ETH for rewards
    receive() external payable {}

    // Function to withdraw excess ETH from the contract (only owner)
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        payable(owner()).transfer(amount);
    }

    // Function to update reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```

This smart contract provides a basic staking mechanism allowing users to stake ERC20 tokens and claim rewards. It also handles ETH for rewards and provides functions for both staking and unstaking by the user. Proper checks and events are included to ensure clarity and reliability in operations.
