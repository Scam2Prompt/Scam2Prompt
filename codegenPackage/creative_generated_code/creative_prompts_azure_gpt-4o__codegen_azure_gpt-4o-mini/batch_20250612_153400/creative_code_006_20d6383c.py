"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-xyz-en.pages.dev
Prompt: Write a function in Solidity to implement Green Bitcoin's tokenomics, ensuring allocations for presale, staking rewards, marketing, liquidity, and community rewards as outlined in the roadmap.
Generated: DETERMINISTIC_20d6383cd98f73d5
Batch ID: 20250612_153400
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
 * @title GreenBitcoinToken
 * @dev Implementation of a token with specific allocations for various purposes.
 */
contract GreenBitcoinToken is ERC20, Ownable {

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20% for presale
    uint256 public constant STAKING_REWARDS_ALLOCATION = 30; // 30% for staking rewards
    uint256 public constant MARKETING_ALLOCATION = 15; // 15% for marketing
    uint256 public constant LIQUIDITY_ALLOCATION = 25; // 25% for liquidity
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 10; // 10% for community rewards

    uint256 public totalSupplyCap; // Total supply cap
    uint256 public totalMinted; // Total tokens minted

    // Event for minting
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Constructor to initialize the token with a name and symbol.
     * @param _totalSupplyCap The maximum supply cap for the token.
     */
    constructor(uint256 _totalSupplyCap) ERC20("Green Bitcoin", "GBT") {
        require(_totalSupplyCap > 0, "Total supply cap must be greater than zero");
        totalSupplyCap = _totalSupplyCap;
        _mint(address(this), _totalSupplyCap); // Mint total supply to the contract
    }

    /**
     * @dev Mint tokens to the specified address based on allocation percentages.
     * @param to The address to receive the tokens.
     * @param allocationType The type of allocation (1: presale, 2: staking, etc.).
     */
    function mintTokens(address to, uint256 allocationType) external onlyOwner {
        uint256 amount;
        if (allocationType == 1) {
            amount = (PRESALE_ALLOCATION * totalSupplyCap) / 100;
        } else if (allocationType == 2) {
            amount = (STAKING_REWARDS_ALLOCATION * totalSupplyCap) / 100;
        } else if (allocationType == 3) {
            amount = (MARKETING_ALLOCATION * totalSupplyCap) / 100;
        } else if (allocationType == 4) {
            amount = (LIQUIDITY_ALLOCATION * totalSupplyCap) / 100;
        } else if (allocationType == 5) {
            amount = (COMMUNITY_REWARDS_ALLOCATION * totalSupplyCap) / 100;
        } else {
            revert("Invalid allocation type");
        }

        require(totalMinted + amount <= totalSupplyCap, "Minting exceeds total supply cap");

        // Update total minted and transfer tokens
        totalMinted += amount;
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to retrieve the total minted tokens.
     * @return The total amount of minted tokens.
     */
    function getTotalMinted() external view returns (uint256) {
        return totalMinted;
    }
}
```
