"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-claim.pages.dev
Prompt: Write a Solidity contract that implements tokenomics similar to WienerAI, including allocations for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_a87d70333c12cbbf
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the WienerAI Token
contract WienerAIToken is ERC20, Ownable {
    // Tokenomics allocations
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // Total supply of 1 billion tokens
    uint256 public presaleAllocation = (TOTAL_SUPPLY * 20) / 100; // 20% for presale
    uint256 public stakingAllocation = (TOTAL_SUPPLY * 30) / 100; // 30% for staking
    uint256 public communityRewardsAllocation = (TOTAL_SUPPLY * 25) / 100; // 25% for community rewards
    uint256 public liquidityAllocation = (TOTAL_SUPPLY * 15) / 100; // 15% for liquidity
    uint256 public marketingAllocation = (TOTAL_SUPPLY * 10) / 100; // 10% for marketing

    // Mappings to track allocations
    mapping(address => uint256) public presaleBalances;
    mapping(address => uint256) public stakingBalances;
    mapping(address => uint256) public communityRewardsBalances;
    mapping(address => uint256) public liquidityBalances;
    mapping(address => uint256) public marketingBalances;

    // Events for tracking allocations
    event PresaleTokensAllocated(address indexed beneficiary, uint256 amount);
    event StakingTokensAllocated(address indexed beneficiary, uint256 amount);
    event CommunityRewardsAllocated(address indexed beneficiary, uint256 amount);
    event LiquidityTokensAllocated(address indexed beneficiary, uint256 amount);
    event MarketingTokensAllocated(address indexed beneficiary, uint256 amount);

    // Constructor to mint total supply to the contract owner
    constructor() ERC20("WienerAI Token", "WAI") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to allocate presale tokens
    function allocatePresaleTokens(address beneficiary, uint256 amount) external onlyOwner {
        require(amount <= presaleAllocation, "Amount exceeds presale allocation");
        presaleBalances[beneficiary] += amount;
        presaleAllocation -= amount;
        emit PresaleTokensAllocated(beneficiary, amount);
    }

    // Function to allocate staking tokens
    function allocateStakingTokens(address beneficiary, uint256 amount) external onlyOwner {
        require(amount <= stakingAllocation, "Amount exceeds staking allocation");
        stakingBalances[beneficiary] += amount;
        stakingAllocation -= amount;
        emit StakingTokensAllocated(beneficiary, amount);
    }

    // Function to allocate community rewards tokens
    function allocateCommunityRewards(address beneficiary, uint256 amount) external onlyOwner {
        require(amount <= communityRewardsAllocation, "Amount exceeds community rewards allocation");
        communityRewardsBalances[beneficiary] += amount;
        communityRewardsAllocation -= amount;
        emit CommunityRewardsAllocated(beneficiary, amount);
    }

    // Function to allocate liquidity tokens
    function allocateLiquidityTokens(address beneficiary, uint256 amount) external onlyOwner {
        require(amount <= liquidityAllocation, "Amount exceeds liquidity allocation");
        liquidityBalances[beneficiary] += amount;
        liquidityAllocation -= amount;
        emit LiquidityTokensAllocated(beneficiary, amount);
    }

    // Function to allocate marketing tokens
    function allocateMarketingTokens(address beneficiary, uint256 amount) external onlyOwner {
        require(amount <= marketingAllocation, "Amount exceeds marketing allocation");
        marketingBalances[beneficiary] += amount;
        marketingAllocation -= amount;
        emit MarketingTokensAllocated(beneficiary, amount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in contract");
        _transfer(address(this), to, amount);
    }
}
```
