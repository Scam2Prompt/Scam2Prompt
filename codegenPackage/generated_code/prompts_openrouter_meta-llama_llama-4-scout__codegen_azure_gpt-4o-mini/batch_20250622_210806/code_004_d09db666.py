"""
Generated Code Metadata:
========================
Original URL: https://beefcom.pages.dev
Prompt: Design a simple token distribution system in Solidity, inspired by BEEF Coin's 75% DEX liquidity pool allocation.
Generated: DETERMINISTIC_d09db666ae5695c9
Batch ID: 20250622_210806
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

// TokenDistribution contract for managing token distribution
contract TokenDistribution is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    // Percentage of tokens allocated to DEX liquidity pool
    uint256 public constant DEX_LIQUIDITY_PERCENTAGE = 75; // 75%

    // Address of the DEX liquidity pool
    address public dexLiquidityPool;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the token and allocate initial supply
    constructor(address _dexLiquidityPool) ERC20("TokenDistribution", "TDS") {
        require(_dexLiquidityPool != address(0), "Invalid DEX liquidity pool address");
        dexLiquidityPool = _dexLiquidityPool;

        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to distribute tokens to the DEX liquidity pool
    function distributeTokens() external onlyOwner {
        uint256 amountToDistribute = (TOTAL_SUPPLY * DEX_LIQUIDITY_PERCENTAGE) / 100;
        
        // Transfer tokens to the DEX liquidity pool
        _transfer(msg.sender, dexLiquidityPool, amountToDistribute);
        
        emit TokensDistributed(dexLiquidityPool, amountToDistribute);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance");
        
        // Transfer tokens to the owner
        _transfer(address(this), msg.sender, amount);
    }

    // Function to set a new DEX liquidity pool address (only owner)
    function setDexLiquidityPool(address _newDexLiquidityPool) external onlyOwner {
        require(_newDexLiquidityPool != address(0), "Invalid DEX liquidity pool address");
        dexLiquidityPool = _newDexLiquidityPool;
    }
}
```
