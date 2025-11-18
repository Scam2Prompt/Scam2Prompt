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

// Import required interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

interface IBalancerPool {
    function setTokenWeight(address token, uint256 weight) external;
    function getTokenWeight(address token) external view returns (uint256);
}

contract ManagedBalancerPool is Ownable, Pausable {
    // Address of the Balancer pool contract
    IBalancerPool public balancerPool;

    // Struct to hold dynamic token information
    struct TokenInfo {
        address tokenAddress;
        address priceFeed; // Chainlink price feed address
    }

    // Token list and mapping for weights
    TokenInfo[] public tokens;
    mapping(address => uint256) public tokenWeight;

    // Event for logging weight adjustments
    event TokenWeightAdjusted(address indexed token, uint256 newWeight);

    // Constructor to initialize the Balancer pool contract
    constructor(address _balancerPool) {
        require(_balancerPool != address(0), "Balancer pool address cannot be zero");
        balancerPool = IBalancerPool(_balancerPool);
    }

    // Function to add a token to the pool with its Chainlink price feed address
    function addToken(address _token, address _priceFeed) external onlyOwner {
        require(_token != address(0), "Token address cannot be zero");
        require(_priceFeed != address(0), "Price feed address cannot be zero");
        tokens.push(TokenInfo({tokenAddress: _token, priceFeed: _priceFeed}));
    }

    // Function to dynamically adjust token weights based on external price feeds
    function adjustWeights() external whenNotPaused {
        require(tokens.length > 0, "No tokens available for adjustment");

        uint256 totalWeight = 0;

        // Array to store new weights for tokens
        uint256[] memory newWeights = new uint256[](tokens.length);

        for (uint256 i = 0; i < tokens.length; i++) {
            TokenInfo memory tokenInfo = tokens[i];

            // Get the latest price from Chainlink price feed
            AggregatorV3Interface priceFeed = AggregatorV3Interface(tokenInfo.priceFeed);
            (, int256 price, , , ) = priceFeed.latestRoundData();
            require(price > 0, "Invalid price data");

            // Calculate the weight based on price
            uint256 weight = uint256(price);
            newWeights[i] = weight;
            totalWeight += weight;
        }

        // Normalize and update weights in the Balancer pool
        for (uint256 i = 0; i < tokens.length; i++) {
            uint256 normalizedWeight = (newWeights[i] * 1e18) / totalWeight; // Normalize weights
            tokenWeight[tokens[i].tokenAddress] = normalizedWeight;
            balancerPool.setTokenWeight(tokens[i].tokenAddress, normalizedWeight);

            emit TokenWeightAdjusted(tokens[i].tokenAddress, normalizedWeight);
        }
    }

    // Function to pause the contract
    function pause() external onlyOwner {
        _pause();
    }

    // Function to unpause the contract
    function unpause() external onlyOwner {
        _unpause();
    }

    // Function to get the current weight of a token
    function getTokenWeight(address _token) external view returns (uint256) {
        return tokenWeight[_token];
    }

    // Function to retrieve the list of tokens in the pool
    function getTokens() external view returns (TokenInfo[] memory) {
        return tokens;
    }
}
```
