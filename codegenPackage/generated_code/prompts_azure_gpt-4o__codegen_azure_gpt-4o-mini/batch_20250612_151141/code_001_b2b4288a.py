"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-ie.web.app
Prompt: Generate Solidity code for an ERC-20 token contract similar to $KANG, ensuring it includes features for buybacks, liquidity control, and integration with play-to-earn mechanics.
Generated: DETERMINISTIC_b2b4288a1965f6ec
Batch ID: 20250612_151141
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// KANGToken is an ERC20 token with buyback and liquidity control features
contract KANGToken is ERC20, Ownable {
    // Events for logging buybacks and liquidity changes
    event BuybackExecuted(uint256 amount);
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Buyback percentage (in basis points, e.g., 500 = 5%)
    uint256 public buybackPercentage = 500; 
    // Liquidity percentage (in basis points, e.g., 300 = 3%)
    uint256 public liquidityPercentage = 300; 

    // Address for the liquidity pool
    address public liquidityPool;

    // Constructor to initialize the token
    constructor() ERC20("KANG Token", "KANG") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply
    }

    // Function to set the liquidity pool address
    function setLiquidityPool(address _liquidityPool) external onlyOwner {
        liquidityPool = _liquidityPool;
    }

    // Function to execute buybacks
    function executeBuyback() external onlyOwner payable {
        require(msg.value > 0, "Must send ETH for buyback");

        uint256 buybackAmount = (msg.value * buybackPercentage) / 10_000;
        _mint(address(this), buybackAmount); // Mint tokens for buyback
        emit BuybackExecuted(buybackAmount);
    }

    // Function to add liquidity to the pool
    function addLiquidity(uint256 tokenAmount) external onlyOwner {
        require(liquidityPool != address(0), "Liquidity pool not set");
        require(balanceOf(address(this)) >= tokenAmount, "Insufficient tokens");

        uint256 ethAmount = (tokenAmount * liquidityPercentage) / 10_000;
        require(address(this).balance >= ethAmount, "Insufficient ETH for liquidity");

        // Transfer tokens to the liquidity pool
        _transfer(address(this), liquidityPool, tokenAmount);
        emit LiquidityAdded(tokenAmount, ethAmount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Insufficient tokens");
        _transfer(address(this), owner(), amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
