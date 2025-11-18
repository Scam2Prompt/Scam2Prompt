"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordifypro.pages.dev
Prompt: Develop a smart contract for staking ORFY tokens on Ordify's Launchpad, ensuring compatibility with both Bitcoin Layer-2 chains and EVM chains.
Generated: DETERMINISTIC_0a0b7106b6ec5af7
Batch ID: 20250612_152710
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

// Import interfaces from OpenZeppelin for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with Layer-2 protocols
interface ILayer2 {
    function deposit(address user, uint256 amount) external;
    function withdraw(address user, uint256 amount) external;
}

// Smart contract for staking ORFY tokens on Ordify's Launchpad
contract OrdifyStaking is Ownable {
    // State variables
    IERC20 public stakingToken; // Reference to the ORFY token contract
    ILayer2 public layer2Protocol; // Reference to the Layer-2 protocol
    mapping(address => uint256) public stakedAmounts; // Track staked amounts per user
    mapping(address => uint256) public rewards; // Track rewards per user
    uint256 public rewardRate; // The rate of rewards
    uint256 public totalStaked; // Total amount staked in the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize staking token and Layer-2 protocol
    constructor(IERC20 _stakingToken, ILayer2 _layer2Protocol, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        layer2Protocol = _layer2Protocol;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staked amount and total staked
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked amount and total staked
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update rewards mapping
        rewards[msg.sender] += reward;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, reward);

        // Emit the RewardPaid event
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate rewards based on staked amount and reward rate
    function calculateReward(address user) public view returns (uint256) {
        return (stakedAmounts[user] * rewardRate) / 1e18; // Adjusted for precision
    }

    // Function to update reward rate (only owner can update)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to deposit tokens in Layer-2
    function depositToLayer2(uint256 amount) external {
        require(amount > 0 && stakedAmounts[msg.sender] >= amount, "Invalid amount");
        stakedAmounts[msg.sender] -= amount;
        layer2Protocol.deposit(msg.sender, amount);
    }

    // Function to withdraw tokens from Layer-2
    function withdrawFromLayer2(uint256 amount) external {
        require(amount > 0, "Invalid amount");
        layer2Protocol.withdraw(msg.sender, amount);
    }
}
```
