"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claimportal.pages.dev
Prompt: Generate a Solidity contract to manage DOGE20 tokenomics, including fixed supply allocation for presale, marketing, treasury, staking rewards, and liquidity provision.
Generated: DETERMINISTIC_4bf145b52dcd5f5b
Batch ID: 20250612_152235
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
 * @title DOGE20 Token Contract
 * @dev ERC20 Token with fixed supply allocation for presale, marketing, treasury, staking rewards, and liquidity.
 */
contract DOGE20 is ERC20, Ownable {
    // Define the fixed total supply
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens

    // Allocation percentages (scaled by 100)
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant TREASURY_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 30; // 30%
    uint256 public constant LIQUIDITY_ALLOCATION = 25; // 25%

    // Addresses for allocations
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    // Event emitted upon allocation
    event TokensAllocated(address indexed to, uint256 amount);

    /**
     * @dev Constructor that allocates tokens to specific addresses.
     * @param _presaleAddress Address for presale allocation.
     * @param _marketingAddress Address for marketing allocation.
     * @param _treasuryAddress Address for treasury allocation.
     * @param _stakingRewardsAddress Address for staking rewards allocation.
     * @param _liquidityAddress Address for liquidity allocation.
     */
    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _treasuryAddress,
        address _stakingRewardsAddress,
        address _liquidityAddress
    ) ERC20("DOGE20", "DOGE20") {
        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Allocate initial token supply
        allocateTokens();
    }

    /**
     * @dev Allocates tokens according to the defined percentages.
     */
    function allocateTokens() internal {
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        uint256 treasuryAmount = (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 100;
        uint256 stakingRewardsAmount = (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;

        // Transfer tokens to the respective addresses
        _mint(presaleAddress, presaleAmount);
        emit TokensAllocated(presaleAddress, presaleAmount);

        _mint(marketingAddress, marketingAmount);
        emit TokensAllocated(marketingAddress, marketingAmount);

        _mint(treasuryAddress, treasuryAmount);
        emit TokensAllocated(treasuryAddress, treasuryAmount);

        _mint(stakingRewardsAddress, stakingRewardsAmount);
        emit TokensAllocated(stakingRewardsAddress, stakingRewardsAmount);

        _mint(liquidityAddress, liquidityAmount);
        emit TokensAllocated(liquidityAddress, liquidityAmount);
    }

    /**
     * @dev Prevents any further minting of tokens.
     * This function is irreversibly called after the initial allocation.
     */
    function finalize() external onlyOwner {
        // No functionality as minting is already complete
    }
}
```
