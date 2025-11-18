"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jwzt-dashboard-inqubeta.pages.dev
Prompt: Write a Solidity function that calculates rewards for $QUBE token staking based on the sell tax contributions to the rewards pool, as described in InQubeta's staking system.
Generated: DETERMINISTIC_5a7277f8b207cd5b
Batch ID: 20250612_145619
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

// Interface for the ERC20 QUBE token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Main contract for handling staking and reward calculations
contract InQubetaStaking {
    // Address of the QUBE token contract
    IERC20 public qubeToken;

    // Struct to hold staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardsEarned;
        uint256 lastRewardBlock;
    }

    // Mapping of stakers' addresses to their staking info
    mapping(address => Staker) public stakers;

    // Total rewards pool
    uint256 public rewardsPool;

    // Event to be emitted when rewards are distributed
    event RewardsDistributed(address indexed staker, uint256 rewards);

    // Modifier to check if the sender is a staker
    modifier onlyStaker() {
        require(stakers[msg.sender].stakedAmount > 0, "Not a staker");
        _;
    }

    // Constructor to initialize the QUBE token address
    constructor(address _qubeToken) {
        qubeToken = IERC20(_qubeToken);
    }

    // Function to stake QUBE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(qubeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.lastRewardBlock = block.number; // Track the last block for rewards calculation
    }

    // Function to calculate and distribute rewards
    function calculateRewards() internal {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = (staker.stakedAmount * (block.number - staker.lastRewardBlock)) / 100; // Simplified reward calculation

        if (reward > 0) {
            staker.rewardsEarned += reward;
            rewardsPool -= reward; // Deduct from rewards pool
            emit RewardsDistributed(msg.sender, reward);
        }

        // Update the last reward block
        staker.lastRewardBlock = block.number;
    }

    // Function to claim rewards
    function claimRewards() external onlyStaker {
        calculateRewards();

        Staker storage staker = stakers[msg.sender];
        uint256 rewardsToClaim = staker.rewardsEarned;
        staker.rewardsEarned = 0; // Reset rewards after claiming

        require(rewardsToClaim > 0, "No rewards to claim");
        require(rewardsPool >= rewardsToClaim, "Insufficient rewards pool");

        require(qubeToken.transfer(msg.sender, rewardsToClaim), "Transfer failed");
    }

    // Function to handle incoming sell tax contributions
    function contributeToRewardsPool(uint256 amount) external {
        require(amount > 0, "Contribution must be greater than zero");
        
        // Here we assume the contract can receive QUBE tokens and this function could be called by a predefined address or a contract
        require(qubeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        rewardsPool += amount; // Add to rewards pool
    }
}
```
