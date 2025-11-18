"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-en.pages.dev
Prompt: Generate a Solidity smart contract snippet to implement tokenomics similar to WienerAI's allocation percentages (e.g., presale, staking, rewards, liquidity, marketing).
Generated: DETERMINISTIC_b0f968524fee949a
Batch ID: 20250612_151117
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

/**
 * @title WienerAIToken
 * @dev This contract implements a simple ERC20 token with tokenomics features 
 * including presale, staking, rewards, liquidity, and marketing allocations.
 */
contract WienerAIToken is ERC20, Ownable {
    // Allocation percentages (in basis points, i.e., 10000 = 100%)
    uint256 public constant PRESALE_ALLOCATION = 2000; // 20%
    uint256 public constant STAKING_ALLOCATION = 3000; // 30%
    uint256 public constant REWARDS_ALLOCATION = 2500; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 1500; // 15%
    uint256 public constant MARKETING_ALLOCATION = 1000; // 10%
    
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18; // 1 million tokens

    // Events
    event TokensAllocated(string allocationType, uint256 amount);

    // Constructor to initialize the token and allocate initial supply
    constructor() ERC20("WienerAI Token", "WAI") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Allocate tokens according to the specified percentages
        allocateTokens();
    }

    // Function to allocate tokens based on predefined percentages
    function allocateTokens() internal {
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000;
        uint256 stakingAmount = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 10000;
        uint256 rewardsAmount = (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 10000;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10000;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000;

        // Emit allocation events for tracking
        emit TokensAllocated("Presale", presaleAmount);
        emit TokensAllocated("Staking", stakingAmount);
        emit TokensAllocated("Rewards", rewardsAmount);
        emit TokensAllocated("Liquidity", liquidityAmount);
        emit TokensAllocated("Marketing", marketingAmount);

        // Placeholders for real allocation logic (e.g., transferring tokens to relevant addresses)
        // In a real implementation, the following lines should transfer the respective amounts to the allocated addresses
        // _transfer(msg.sender, presaleAddress, presaleAmount);
        // _transfer(msg.sender, stakingAddress, stakingAmount);
        // _transfer(msg.sender, rewardsAddress, rewardsAmount);
        // _transfer(msg.sender, liquidityAddress, liquidityAmount);
        // _transfer(msg.sender, marketingAddress, marketingAmount);
    }

    // Modifier to ensure that the function caller is an authorized address (owner or approved address)
    modifier onlyAuthorized() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Add more functions for staking, rewards distribution, liquidity management, etc.
    // Ensure to include necessary checks and balances
}
```
