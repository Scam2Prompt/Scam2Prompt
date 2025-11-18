"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockbanki.pages.dev
Prompt: Write a Solidity contract to manage the allocation of $PEPU tokens based on the tokenomics breakdown (e.g., presale, staking, marketing, liquidity).
Generated: DETERMINISTIC_9dd29d23842e43d7
Batch ID: 20250612_151246
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

// @title PEPU Token Management Contract
// @notice This contract manages the allocation of $PEPU tokens based on predefined tokenomics.
contract PEPUTokenManager is ERC20, Ownable {
    // Total supply of PEPU tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals();

    // Allocation breakdown percentages
    uint256 public constant PRESALE_ALLOCATION = 30; // 30%
    uint256 public constant STAKING_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 15; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 25; // 25%
    uint256 public constant TEAM_ALLOCATION = 10; // 10%

    // Allocated tokens for each category
    uint256 public presaleTokens;
    uint256 public stakingTokens;
    uint256 public marketingTokens;
    uint256 public liquidityTokens;
    uint256 public teamTokens;

    // Events for allocation tracking
    event TokensAllocated(string category, uint256 amount);

    constructor() ERC20("PEPU Token", "PEPU") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Calculate allocations based on percentages
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        stakingTokens = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        teamTokens = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;
        
        // Emit events for each allocation
        emit TokensAllocated("Presale", presaleTokens);
        emit TokensAllocated("Staking", stakingTokens);
        emit TokensAllocated("Marketing", marketingTokens);
        emit TokensAllocated("Liquidity", liquidityTokens);
        emit TokensAllocated("Team", teamTokens);
    }

    // @notice Withdraw allocated tokens to the specified address
    // @param _to Address to receive the tokens
    // @param _amount Amount of tokens to withdraw
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(_to != address(0), "Invalid address");
        require(balanceOf(address(this)) >= _amount, "Insufficient tokens in contract");

        // Transfer the specified amount of tokens
        _transfer(address(this), _to, _amount);
    }

    // @notice View function to get the allocation of a specific category
    // @param category The category to query allocation for
    // @return amount The allocated amount of tokens for the category
    function getAllocation(string memory category) external view returns (uint256 amount) {
        if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("Presale"))) {
            return presaleTokens;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("Staking"))) {
            return stakingTokens;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("Marketing"))) {
            return marketingTokens;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("Liquidity"))) {
            return liquidityTokens;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("Team"))) {
            return teamTokens;
        } else {
            revert("Invalid category");
        }
    }
}
```
