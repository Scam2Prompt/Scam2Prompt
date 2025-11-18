"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Develop a function in Solidity to enable OUSD holders to stake OGV tokens and earn rewards while participating in decentralized governance.
Generated: DETERMINISTIC_9d2a104d0101720a
Batch ID: 20250612_153526
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the OGV token
interface IOGV is IERC20 {
    function mint(address to, uint256 amount) external;
}

// The Staking contract to stake OGV tokens and earn rewards
contract OGVStaking is ReentrancyGuard, Ownable {
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // State variables
    IOGV public ogvToken; // OGV token contract
    mapping(address => uint256) public stakes; // User stakes
    mapping(address => uint256) public rewards; // User rewards
    uint256 public totalStaked; // Total OGV staked
    uint256 public rewardRate; // Reward rate per staked token

    // Constructor to set the OGV token and reward rate
    constructor(IOGV _ogvToken, uint256 _rewardRate) {
        ogvToken = _ogvToken;
        rewardRate = _rewardRate;
    }

    // Function to stake OGV tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer OGV tokens from the user to the contract
        ogvToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user stakes and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        // Emit stake event
        emit Staked(msg.sender, amount);
    }
    
    // Function to unstake OGV tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user stakes and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer OGV tokens back to the user
        ogvToken.transfer(msg.sender, amount);
        
        // Emit unstake event
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        // Calculate rewards for the user based on their stakes
        uint256 userRewards = calculateRewards(msg.sender);

        require(userRewards > 0, "No rewards to claim");

        // Update rewards mapping before transfer to avoid reentrancy
        rewards[msg.sender] = 0;

        // Mint and distribute rewards
        ogvToken.mint(msg.sender, userRewards);

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, userRewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        return stakes[user] * rewardRate;
    }

    // Function to set the reward rate, only owner can call this
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
