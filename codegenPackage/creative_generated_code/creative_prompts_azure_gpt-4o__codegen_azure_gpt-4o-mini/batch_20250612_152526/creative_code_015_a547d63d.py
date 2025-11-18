"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metisdap.pages.dev
Prompt: Provide example code for deploying a decentralized exchange (DEX) on Metis Layer 2, ensuring frictionless transactions and affordable gas fees.
Generated: DETERMINISTIC_a547d63d9bf8760d
Batch ID: 20250612_152526
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

// Import OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DEX Contract
contract DecentralizedExchange is Ownable {
    // Event emitted when a trade occurs
    event Trade(address indexed trader, address indexed tokenSold, uint256 amountSold, address indexed tokenBought, uint256 amountBought);

    // Structure to hold trading pair details
    struct TradingPair {
        uint256 reserveTokenA;
        uint256 reserveTokenB;
        uint256 rate; // The rate at which token A can be traded for token B
    }

    // Mapping of trading pairs
    mapping(address => mapping(address => TradingPair)) public tradingPairs;

    // Function to add a trading pair
    function addTradingPair(address tokenA, address tokenB, uint256 initialRate) external onlyOwner {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(initialRate > 0, "Rate must be greater than zero");

        tradingPairs[tokenA][tokenB] = TradingPair(0, 0, initialRate);
    }

    // Function to create liquidity for a trading pair
    function provideLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external {
        require(amountA > 0 && amountB > 0, "Amount must be greater than zero");
        require(tradingPairs[tokenA][tokenB].rate > 0, "Trading pair does not exist");

        // Transfer tokens from the user to the contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountB);

        // Update reserves
        tradingPairs[tokenA][tokenB].reserveTokenA += amountA;
        tradingPairs[tokenA][tokenB].reserveTokenB += amountB;
    }

    // Function to execute a trade
    function trade(address tokenSold, address tokenBought, uint256 amountSold) external {
        TradingPair storage pair = tradingPairs[tokenSold][tokenBought];

        require(pair.rate > 0, "Trading pair does not exist");
        require(amountSold > 0, "Amount sold must be greater than zero");
        require(pair.reserveTokenA >= amountSold, "Insufficient liquidity");

        // Calculate amount of token bought based on the rate
        uint256 amountBought = (amountSold * pair.rate) / 1e18; // Assuming rate is scaled by 1e18

        require(pair.reserveTokenB >= amountBought, "Insufficient liquidity for trade");

        // Transfer tokens
        IERC20(tokenSold).transferFrom(msg.sender, address(this), amountSold);
        IERC20(tokenBought).transfer(msg.sender, amountBought);

        // Update reserves
        pair.reserveTokenA -= amountSold;
        pair.reserveTokenB -= amountBought;

        // Emit trade event
        emit Trade(msg.sender, tokenSold, amountSold, tokenBought, amountBought);
    }

    // Function to withdraw tokens for maintenance
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
