"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Write a Solidity contract for token distribution based on the tokenomics described in WienerAI, ensuring allocations for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_7e6972d4c537bce0
Batch ID: 20250612_151255
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Token contract for WienerAI
contract WienerAIToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_ALLOCATION = 25; // 25%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 20; // 20%

    // Allocated amounts
    uint256 public presaleTokens;
    uint256 public stakingTokens;
    uint256 public communityRewardsTokens;
    uint256 public liquidityTokens;
    uint256 public marketingTokens;

    // Events for tracking allocations
    event TokensAllocated(string allocationType, uint256 amount);

    // Constructor to initialize the token and allocate tokens
    constructor() ERC20("WienerAI Token", "WAI") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Calculate allocations
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        stakingTokens = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        communityRewardsTokens = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100;
        liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;

        // Emit events for allocations
        emit TokensAllocated("Presale", presaleTokens);
        emit TokensAllocated("Staking", stakingTokens);
        emit TokensAllocated("Community Rewards", communityRewardsTokens);
        emit TokensAllocated("Liquidity", liquidityTokens);
        emit TokensAllocated("Marketing", marketingTokens);
    }

    // Function to allocate presale tokens to a specific address
    function allocatePresaleTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= presaleTokens, "Insufficient presale tokens available");
        presaleTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to allocate staking tokens to a specific address
    function allocateStakingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= stakingTokens, "Insufficient staking tokens available");
        stakingTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to allocate community rewards tokens to a specific address
    function allocateCommunityRewardsTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= communityRewardsTokens, "Insufficient community rewards tokens available");
        communityRewardsTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to allocate liquidity tokens to a specific address
    function allocateLiquidityTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= liquidityTokens, "Insufficient liquidity tokens available");
        liquidityTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to allocate marketing tokens to a specific address
    function allocateMarketingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= marketingTokens, "Insufficient marketing tokens available");
        marketingTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to retrieve remaining tokens for a specific allocation
    function getRemainingTokens(string memory allocationType) external view returns (uint256) {
        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Presale"))) {
            return presaleTokens;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Staking"))) {
            return stakingTokens;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Community Rewards"))) {
            return communityRewardsTokens;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Liquidity"))) {
            return liquidityTokens;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("Marketing"))) {
            return marketingTokens;
        } else {
            revert("Invalid allocation type");
        }
    }
}
```
