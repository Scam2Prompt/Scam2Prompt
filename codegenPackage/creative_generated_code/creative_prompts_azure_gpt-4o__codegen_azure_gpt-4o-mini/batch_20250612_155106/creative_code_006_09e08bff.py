"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalan-er.com
Prompt: Generate a Solidity implementation for a custom Balancer Managed Pool that allows dynamic adjustment of token weights based on external price feeds.
Generated: DETERMINISTIC_09e08bff4650cf0b
Batch ID: 20250612_155106
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract DynamicWeightBalancer is Ownable {
    using SafeMath for uint256;

    // Struct to represent a token in the pool
    struct Token {
        IERC20 token;
        uint256 weight; // Token weight in basis points (10000 = 100%)
    }

    // Array of tokens in the pool
    Token[] public tokens;
    
    // Price feed for external price reference
    AggregatorV3Interface internal priceFeed;

    // Total weight of the pool
    uint256 public totalWeight;

    // Events
    event TokenAdded(address indexed token, uint256 weight);
    event TokenWeightUpdated(address indexed token, uint256 newWeight);
    
    /**
     * @dev Constructor to initialize the price feed
     * @param _priceFeed Address of the Chainlink price feed contract
     */
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    /**
     * @dev Adds a new token to the pool with the specified weight
     * @param tokenAddress Address of the token contract
     * @param weight Weight of the token in basis points
     */
    function addToken(address tokenAddress, uint256 weight) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(weight > 0, "Weight must be greater than 0");
        
        tokens.push(Token({
            token: IERC20(tokenAddress),
            weight: weight
        }));
        
        totalWeight = totalWeight.add(weight);
        emit TokenAdded(tokenAddress, weight);
    }

    /**
     * @dev Updates the weight of an existing token in the pool
     * @param tokenAddress Address of the token contract
     * @param newWeight New weight of the token in basis points
     */
    function updateTokenWeight(address tokenAddress, uint256 newWeight) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(newWeight > 0, "Weight must be greater than 0");

        for (uint256 i = 0; i < tokens.length; i++) {
            if (address(tokens[i].token) == tokenAddress) {
                totalWeight = totalWeight.sub(tokens[i].weight).add(newWeight);
                tokens[i].weight = newWeight;
                emit TokenWeightUpdated(tokenAddress, newWeight);
                return;
            }
        }
        
        revert("Token not found in pool");
    }

    /**
     * @dev Retrieves the latest price from the Chainlink price feed
     * @return uint256 Latest price in USD
     */
    function getLatestPrice() public view returns (uint256) {
        (
            , 
            int price,
            ,
            ,
            
        ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price value");
        return uint256(price);
    }

    /**
     * @dev Computes the adjusted weights based on external price feeds
     */
    function adjustWeights() external onlyOwner {
        uint256 latestPrice = getLatestPrice();
        
        for (uint256 i = 0; i < tokens.length; i++) {
            // Example logic for adjusting weight; can be customized as needed
            uint256 currentWeight = tokens[i].weight;
            tokens[i].weight = currentWeight.mul(latestPrice).div(1e18); // Adjust weight based on price
        }
    }

    /**
     * @dev Returns the total number of tokens in the pool
     * @return uint256 Number of tokens
     */
    function totalTokens() external view returns (uint256) {
        return tokens.length;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the pool
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= amount, "Insufficient balance");
        
        token.transfer(owner(), amount);
    }
}
```
