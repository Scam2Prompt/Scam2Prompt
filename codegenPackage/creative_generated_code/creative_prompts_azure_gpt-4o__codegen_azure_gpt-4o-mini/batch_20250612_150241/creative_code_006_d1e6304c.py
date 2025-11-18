"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presale.pages.dev
Prompt: Generate a Solidity contract that implements the tokenomics of $99BTC, including allocations for presale, staking, project funds, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_d1e6304ce1c52ee5
Batch ID: 20250612_150241
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

// Import the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title 99BTC Token Contract
// @dev This contract implements a simple ERC20 token with specific tokenomics for $99BTC.
contract NinetyNineBTC is ERC20, Ownable {
    // Define allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 30; // 30% for presale
    uint256 public constant STAKING_ALLOCATION = 20; // 20% for staking
    uint256 public constant PROJECT_FUNDS_ALLOCATION = 15; // 15% for project funds
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 15; // 15% for community rewards
    uint256 public constant LIQUIDITY_ALLOCATION = 10; // 10% for liquidity
    uint256 public constant MARKETING_ALLOCATION = 10; // 10% for marketing

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens

    // Addresses for allocations
    address public presaleWallet;
    address public stakingWallet;
    address public projectFundsWallet;
    address public communityRewardsWallet;
    address public liquidityWallet;
    address public marketingWallet;

    // Events to log allocation transfers
    event TokensAllocated(address indexed receiver, uint256 amount);

    // Constructor to set up the ERC20 token and allocate tokens
    constructor(
        address _presaleWallet,
        address _stakingWallet,
        address _projectFundsWallet,
        address _communityRewardsWallet,
        address _liquidityWallet,
        address _marketingWallet
    ) ERC20("99BTC Token", "99BTC") {
        // Set wallet addresses
        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        projectFundsWallet = _projectFundsWallet;
        communityRewardsWallet = _communityRewardsWallet;
        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;

        // Allocate tokens based on defined percentages
        _allocateTokens();
    }

    // Internal function to allocate tokens
    function _allocateTokens() internal {
        uint256 presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 stakingTokens = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        uint256 projectFundsTokens = (TOTAL_SUPPLY * PROJECT_FUNDS_ALLOCATION) / 100;
        uint256 communityRewardsTokens = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100;
        uint256 liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        uint256 marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;

        // Transfer allocated tokens to respective wallets
        _mint(presaleWallet, presaleTokens);
        emit TokensAllocated(presaleWallet, presaleTokens);
        
        _mint(stakingWallet, stakingTokens);
        emit TokensAllocated(stakingWallet, stakingTokens);
        
        _mint(projectFundsWallet, projectFundsTokens);
        emit TokensAllocated(projectFundsWallet, projectFundsTokens);
        
        _mint(communityRewardsWallet, communityRewardsTokens);
        emit TokensAllocated(communityRewardsWallet, communityRewardsTokens);
        
        _mint(liquidityWallet, liquidityTokens);
        emit TokensAllocated(liquidityWallet, liquidityTokens);
        
        _mint(marketingWallet, marketingTokens);
        emit TokensAllocated(marketingWallet, marketingTokens);
    }

    // Override the transfer function to include error handling
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for transfer");

        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }
}
```
