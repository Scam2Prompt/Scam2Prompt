"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfoxs.live
Prompt: Create a Solidity smart contract that implements the staking mechanism for $GFOX tokens, including the 2% transaction reward feature.
Generated: DETERMINISTIC_b2bd496c7153f8ec
Batch ID: 20250612_162854
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

// Interface for ERC20 Token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

// Staking Contract for $GFOX Tokens
contract StakingGFOX {
    // State variables
    IERC20 public gfoxToken; // ERC20 token contract
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakes; // Track user stakes
    mapping(address => uint256) public rewards; // Track user rewards
    uint256 public constant REWARD_PERCENTAGE = 2; // Reward percentage for transactions

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _gfoxToken) {
        gfoxToken = _gfoxToken;
    }

    // Modifier to check if user has staked any tokens
    modifier hasStaked() {
        require(stakes[msg.sender] > 0, "No tokens staked");
        _;
    }

    // Stake tokens in the contract
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to contract
        require(gfoxToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update stakes and total staked
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens from the contract
    function unstake(uint256 amount) external hasStaked {
        require(amount > 0, "Amount must be greater than 0");
        require(amount <= stakes[msg.sender], "Insufficient staked amount");

        // Update stakes and total staked
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(gfoxToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Claim transaction rewards
    function claimRewards() external hasStaked {
        uint256 reward = (stakes[msg.sender] * REWARD_PERCENTAGE) / 100;
        require(reward > 0, "No rewards available");

        // Transfer rewards to user
        require(gfoxToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Update rewards
        rewards[msg.sender] += reward;

        emit RewardClaimed(msg.sender, reward);
    }

    // Get the staking balance of the user
    function getStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Get the total rewards of the user
    function getRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
