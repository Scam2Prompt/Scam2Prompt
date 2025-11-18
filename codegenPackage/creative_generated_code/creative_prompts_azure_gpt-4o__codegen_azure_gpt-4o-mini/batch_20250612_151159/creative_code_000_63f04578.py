"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-wienerdog.pages.dev
Prompt: Write a smart contract in Solidity that mimics the tokenomics of WienerAI ($WAI), including presale allocation, staking rewards, and community rewards distribution.
Generated: DETERMINISTIC_63f045785716ec70
Batch ID: 20250612_151159
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WienerAI is ERC20, Ownable, ReentrancyGuard {
    
    // Presale allocation percentage (in basis points, e.g. 1000 = 10%)
    uint256 public constant PRESALE_ALLOCATION = 2000; // 20%
    uint256 public constant STAKING_REWARD_ALLOCATION = 5000; // 50%
    uint256 public constant COMMUNITY_REWARD_ALLOCATION = 3000; // 30%
    
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens
    
    // Mapping for staking rewards
    mapping(address => uint256) public stakingBalances;
    
    // Events for logging actions
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);
    
    // Constructor to initialize the token
    constructor() ERC20("WienerAI", "WAI") {
        // Allocate tokens upon deployment
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000;
        _mint(msg.sender, presaleAmount); // Presale allocation to the deployer
        _mint(address(this), TOTAL_SUPPLY - presaleAmount); // Mint remaining for future allocations
    }

    // Function to stake tokens for rewards
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        
        // Update the staking balance
        stakingBalances[msg.sender] += amount;
        
        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the staking balance
        stakingBalances[msg.sender] -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);
        
        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to distribute staking rewards based on staked amount
    function distributeRewards() external onlyOwner {
        for (uint256 i = 0; i < totalSupply(); i++) {
            address user = address(uint160(i));
            uint256 reward = (stakingBalances[user] * STAKING_REWARD_ALLOCATION) / TOTAL_SUPPLY;

            if (reward > 0) {
                _transfer(address(this), user, reward);
                emit RewardsDistributed(user, reward);
            }
        }
    }

    // Function to withdraw community rewards by the owner
    function withdrawCommunityRewards() external onlyOwner {
        uint256 communityRewardsAmount = (TOTAL_SUPPLY * COMMUNITY_REWARD_ALLOCATION) / 10000;
        require(balanceOf(address(this)) >= communityRewardsAmount, "Insufficient community rewards balance");

        // Transfer community rewards to the owner
        _transfer(address(this), msg.sender, communityRewardsAmount);
    }
}
```
