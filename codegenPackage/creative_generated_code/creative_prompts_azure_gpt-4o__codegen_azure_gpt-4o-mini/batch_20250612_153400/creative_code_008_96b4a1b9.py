"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Create a Solidity contract that calculates rewards for staking QUBE tokens, distributing them from the 5% sell tax reward pool, as described in the InQubeta staking system.
Generated: DETERMINISTIC_96b4a1b9ee9ed30c
Batch ID: 20250612_153400
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with QUBE token
interface IQUBE is IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Staking contract for QUBE token rewards
contract QubeStaking is Ownable {
    // State variables
    IQUBE public qubeToken; // Reference to QUBE token contract
    uint256 public totalStaked; // Total amount of QUBE staked
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastUpdateBlock; // Last block when rewards were updated

    // Mapping for staking balances and reward debt
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardDebt;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with QUBE token address and reward rate
    constructor(address _qubeToken, uint256 _rewardRate) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = IQUBE(_qubeToken);
        rewardRate = _rewardRate; // Set the reward rate for staking
        lastUpdateBlock = block.number; // Initialize last update block
    }

    // Function to stake QUBE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Must stake more than 0");
        updateRewards(msg.sender); // Update rewards before staking

        // Transfer QUBE tokens from user to this contract
        require(qubeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake QUBE tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Must unstake more than 0");
        require(stakedBalances[msg.sender] >= amount, "Not enough staked balance");
        
        updateRewards(msg.sender); // Update rewards before unstaking

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer QUBE tokens back to user
        require(qubeToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim accumulated rewards
    function claimRewards() external {
        updateRewards(msg.sender); // Update rewards before claiming
        uint256 reward = rewardDebt[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt and transfer rewards
        rewardDebt[msg.sender] = 0;
        require(qubeToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a given user
    function updateRewards(address user) internal {
        // Calculate rewards based on the staked amount and time elapsed
        if (totalStaked > 0) {
            uint256 pendingReward = (block.number - lastUpdateBlock) * rewardRate * stakedBalances[user] / totalStaked;
            rewardDebt[user] += pendingReward; // Update reward debt for user
        }
        lastUpdateBlock = block.number; // Update last block to current block
    }

    // Function to withdraw contract's balance of QUBE tokens (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= qubeToken.balanceOf(address(this)), "Insufficient balance");
        require(qubeToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
