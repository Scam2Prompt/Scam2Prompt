"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-icu.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics, ensuring proper allocation of the fixed supply (e.g., presale, marketing, treasury, staking rewards, and liquidity).
Generated: DETERMINISTIC_7f198c4a244b730f
Batch ID: 20250612_152710
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
 * @title DOGE20 Token
 * @dev Implementation of the DOGE20 token with fixed supply and defined allocation.
 */
contract DOGE20 is ERC20, Ownable {
    // Fixed total supply of the DOGE20 token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 200_000_000 * 10**18; // 20%
    uint256 public constant MARKETING_ALLOCATION = 100_000_000 * 10**18; // 10%
    uint256 public constant TREASURY_ALLOCATION = 150_000_000 * 10**18; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 250_000_000 * 10**18; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 300_000_000 * 10**18; // 30%

    // Address allocations
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    /**
     * @dev Constructor that gives the sender all of the existing tokens and sets allocation addresses.
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
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_treasuryAddress != address(0), "Invalid treasury address");
        require(_stakingRewardsAddress != address(0), "Invalid staking rewards address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");

        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Mint total supply and allocate to respective addresses
        _mint(presaleAddress, PRESALE_ALLOCATION);
        _mint(marketingAddress, MARKETING_ALLOCATION);
        _mint(treasuryAddress, TREASURY_ALLOCATION);
        _mint(stakingRewardsAddress, STAKING_REWARDS_ALLOCATION);
        _mint(liquidityAddress, LIQUIDITY_ALLOCATION);
        // Mint remaining supply to the contract owner
        _mint(owner(), TOTAL_SUPPLY - (PRESALE_ALLOCATION + MARKETING_ALLOCATION + TREASURY_ALLOCATION + STAKING_REWARDS_ALLOCATION + LIQUIDITY_ALLOCATION));
    }

    /**
     * @dev Function to withdraw accidentally sent ERC20 tokens from the contract.
     * @param _token Address of the token contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner(), _amount);
    }

    /**
     * @dev Function to pause transfers (if needed in the future). 
     * Can be implemented as part of additional features.
     */
    // function pause() external onlyOwner { ... }
    // function unpause() external onlyOwner { ... }
}
```
