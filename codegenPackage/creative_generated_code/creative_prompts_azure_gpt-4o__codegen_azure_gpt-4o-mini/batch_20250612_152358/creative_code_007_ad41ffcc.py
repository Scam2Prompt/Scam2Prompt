"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomonnetwork.pages.dev
Prompt: Create a smart contract for managing liquidity positions on Web3.world, ensuring compliance with whitelisted token pairs.
Generated: DETERMINISTIC_ad41ffcc5dbd8b9c
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract LiquidityManager is Ownable {
    // Event emitted when a liquidity position is added
    event LiquidityPositionAdded(address indexed user, address indexed tokenA, address indexed tokenB, uint256 amountA, uint256 amountB);
    
    // Event emitted when a liquidity position is removed
    event LiquidityPositionRemoved(address indexed user, address indexed tokenA, address indexed tokenB, uint256 amountA, uint256 amountB);

    // Struct to represent a liquidity position
    struct LiquidityPosition {
        uint256 amountA; // Amount of token A
        uint256 amountB; // Amount of token B
    }

    // Mapping to store user liquidity positions
    mapping(address => mapping(address => mapping(address => LiquidityPosition))) public liquidityPositions; // user -> tokenA -> tokenB -> LiquidityPosition

    // Whitelisted token pairs
    mapping(address => mapping(address => bool)) public whitelistedPairs;

    // Modifier to check if token pair is whitelisted
    modifier onlyWhitelisted(address tokenA, address tokenB) {
        require(whitelistedPairs[tokenA][tokenB], "Tokens not whitelisted");
        _;
    }

    // Function to whitelist token pairs
    function whitelistTokenPair(address tokenA, address tokenB) external onlyOwner {
        whitelistedPairs[tokenA][tokenB] = true;
        whitelistedPairs[tokenB][tokenA] = true; // Ensure bi-directional whitelisting
    }

    // Function to remove token pair from whitelist
    function removeTokenPair(address tokenA, address tokenB) external onlyOwner {
        delete whitelistedPairs[tokenA][tokenB];
        delete whitelistedPairs[tokenB][tokenA];
    }

    // Function to add liquidity
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external onlyWhitelisted(tokenA, tokenB) {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than zero");

        // Transfer tokens from user to contract
        require(IERC20(tokenA).transferFrom(msg.sender, address(this), amountA), "Transfer of token A failed");
        require(IERC20(tokenB).transferFrom(msg.sender, address(this), amountB), "Transfer of token B failed");

        // Update liquidity position
        liquidityPositions[msg.sender][tokenA][tokenB].amountA += amountA;
        liquidityPositions[msg.sender][tokenA][tokenB].amountB += amountB;

        emit LiquidityPositionAdded(msg.sender, tokenA, tokenB, amountA, amountB);
    }

    // Function to remove liquidity
    function removeLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external {
        LiquidityPosition storage position = liquidityPositions[msg.sender][tokenA][tokenB];
        require(position.amountA >= amountA && position.amountB >= amountB, "Insufficient liquidity");

        // Update liquidity position
        position.amountA -= amountA;
        position.amountB -= amountB;

        // Transfer tokens back to user
        require(IERC20(tokenA).transfer(msg.sender, amountA), "Transfer of token A failed");
        require(IERC20(tokenB).transfer(msg.sender, amountB), "Transfer of token B failed");

        emit LiquidityPositionRemoved(msg.sender, tokenA, tokenB, amountA, amountB);
    }

    // Function to retrieve liquidity position
    function getLiquidityPosition(address user, address tokenA, address tokenB) external view returns (uint256 amountA, uint256 amountB) {
        LiquidityPosition storage position = liquidityPositions[user][tokenA][tokenB];
        return (position.amountA, position.amountB);
    }
}
```
