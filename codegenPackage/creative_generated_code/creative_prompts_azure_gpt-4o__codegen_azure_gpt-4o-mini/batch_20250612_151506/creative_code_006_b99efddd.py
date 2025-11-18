"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftsolutionchain.web.app
Prompt: Generate a smart contract for staking tokens, including APR activation functionality, based on the features highlighted on Swift Solution Chain.
Generated: DETERMINISTIC_b99efdddd5789168
Batch ID: 20250612_151506
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

// Importing OpenZeppelin contracts for ERC20 token interface and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for token staking and APR activation
contract TokenStaking is Ownable {
    // Struct to hold information for each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Token being staked
    IERC20 public token;

    // APR represented in percentage (e.g., 5 for 5%)
    uint256 public apr;
    
    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of staker addresses to their corresponding data
    mapping(address => Staker) public stakers;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the staking contract
    constructor(IERC20 _token, uint256 _apr) {
        token = _token;
        apr = _apr;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from the staker to the contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Withdraw amount exceeds staked amount");

        // Update staker's information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the staker
        token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to calculate pending rewards
    function calculateReward(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;

        // Calculate reward based on APR, time staked, and total staked
        uint256 reward = (staker.amountStaked * apr * timeStaked) / (100 * 365 days);
        return reward;
    }

    // Function to claim staking rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update reward debt and last staked time
        staker.rewardDebt += reward;
        staker.lastStakedTime = block.timestamp;

        // Transfer rewards to the staker
        token.transfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to set a new APR (only owner can call this)
    function setAPR(uint256 newApr) external onlyOwner {
        apr = newApr;
    }

    // Function to withdraw emergency tokens from the contract (only owner can call this)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(owner(), amount);
    }
}
```
