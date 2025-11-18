"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr.pages.dev
Prompt: Develop a smart contract for cross-chain perpetuals using SYNTHR's liquidity layer. Ensure it supports omnichain prediction markets.
Generated: DETERMINISTIC_d532e28e30c63299
Batch ID: 20250612_152439
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Defining the Smart Contract for Cross-Chain Perpetuals
contract CrossChainPerpetuals is Ownable {
    // State variables
    struct Market {
        address creator;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidityProviders;
    }

    // Mapping of markets by their ID
    mapping(uint256 => Market) public markets;

    // Events for logging actions
    event MarketCreated(uint256 indexed marketId, address indexed creator, uint256 initialLiquidity);
    event LiquidityAdded(uint256 indexed marketId, address indexed provider, uint256 amount);
    event LiquidityRemoved(uint256 indexed marketId, address indexed provider, uint256 amount);
    
    // Error definitions
    error MarketNotFound(uint256 marketId);
    error InsufficientLiquidity(uint256 marketId, uint256 amountRequested);
    
    // Function to create a new market
    function createMarket(uint256 marketId, uint256 initialLiquidity) external onlyOwner {
        require(markets[marketId].creator == address(0), "Market already exists");
        
        markets[marketId].creator = msg.sender;
        markets[marketId].totalLiquidity = initialLiquidity;
        markets[marketId].liquidityProviders[msg.sender] = initialLiquidity;
        
        emit MarketCreated(marketId, msg.sender, initialLiquidity);
    }
    
    // Function to add liquidity to a market
    function addLiquidity(uint256 marketId, uint256 amount) external {
        Market storage market = markets[marketId];
        if (market.creator == address(0)) revert MarketNotFound(marketId);
        
        // Transfer tokens from sender to contract
        IERC20 token = IERC20(address(this)); // Assuming the contract itself is the token contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        
        market.totalLiquidity += amount;
        market.liquidityProviders[msg.sender] += amount;
        
        emit LiquidityAdded(marketId, msg.sender, amount);
    }
    
    // Function to remove liquidity from a market
    function removeLiquidity(uint256 marketId, uint256 amount) external {
        Market storage market = markets[marketId];
        if (market.creator == address(0)) revert MarketNotFound(marketId);
        
        // Check if the provider has sufficient liquidity
        if (market.liquidityProviders[msg.sender] < amount) revert InsufficientLiquidity(marketId, amount);
        
        // Update market state
        market.totalLiquidity -= amount;
        market.liquidityProviders[msg.sender] -= amount;

        // Transfer tokens back to the provider
        IERC20 token = IERC20(address(this)); // Assuming the contract is the token contract
        require(token.transfer(msg.sender, amount), "Token transfer failed");
        
        emit LiquidityRemoved(marketId, msg.sender, amount);
    }
    
    // Function to get market details
    function getMarketDetails(uint256 marketId) external view returns (address creator, uint256 totalLiquidity) {
        Market storage market = markets[marketId];
        if (market.creator == address(0)) revert MarketNotFound(marketId);
        
        return (market.creator, market.totalLiquidity);
    }
}
```
