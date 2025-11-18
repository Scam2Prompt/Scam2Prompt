"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency token that includes features like token burning, airdrops, and liquidity pool allocation, inspired by the $MEDA tokenomics described on the Milei Moneda website.
Generated: DETERMINISTIC_e0840432ff9c18a3
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MEDAToken
 * @dev Implementation of a token with burning, airdrop, and liquidity pool allocation features.
 */
contract MEDAToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Events
    event TokensBurned(address indexed burner, uint256 amount);
    event Airdrop(address indexed recipient, uint256 amount);

    // Airdrop allocation percentage (in basis points; e.g., 1000 = 10%)
    uint256 public airdropPercentage = 500; // 5% of total supply can be airdropped
    uint256 public liquidityPoolPercentage = 2000; // 20% for liquidity pool

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("MEDA Token", "MEDA") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Burn a specific amount of tokens from the caller's account.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Airdrop tokens to a specified address.
     * @param recipient Address to receive the airdrop.
     * @param amount Amount of tokens to airdrop.
     */
    function airdrop(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Cannot airdrop to the zero address");
        require(amount > 0, "Amount must be greater than 0");
        require(totalSupply().mul(airdropPercentage).div(10000) >= amount, "Amount exceeds airdrop limit");
        
        _transfer(owner(), recipient, amount);
        emit Airdrop(recipient, amount);
    }

    /**
     * @dev Allocate tokens for liquidity pool.
     */
    function allocateLiquidityPool() external onlyOwner {
        uint256 liquidityAmount = totalSupply().mul(liquidityPoolPercentage).div(10000);
        require(liquidityAmount > 0, "No liquidity to allocate");
        
        _transfer(owner(), address(this), liquidityAmount);
        // Implement further logic to add to liquidity pool if necessary
    }

    /**
     * @dev Update airdrop percentage.
     * @param newPercentage New airdrop percentage in basis points.
     */
    function updateAirdropPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage must be 100% or less");
        airdropPercentage = newPercentage;
    }

    /**
     * @dev Update liquidity pool percentage.
     * @param newPercentage New liquidity pool percentage in basis points.
     */
    function updateLiquidityPoolPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage must be 100% or less");
        liquidityPoolPercentage = newPercentage;
    }

    /**
     * @dev Withdraw ETH from the contract. Only owner can call this.
     */
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}
}
```
