"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythget.com
Prompt: Write a smart contract in Solidity that connects to Pythget oracles to fetch live market data for token swaps.
Generated: DETERMINISTIC_781a4814444e8131
Batch ID: 20250612_155015
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IPyth {
    function getPrice(string memory assetId) external view returns (int256 price);
}

contract TokenSwap is Ownable {
    // Instance of the Pyth oracle
    IPyth public pythOracle;

    // Event emitted when a swap occurs
    event TokenSwapped(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to store token prices
    mapping(string => address) private tokenAddresses;

    // Constructor to set the Pyth oracle address
    constructor(address _pythOracle) {
        require(_pythOracle != address(0), "Invalid Pyth oracle address");
        pythOracle = IPyth(_pythOracle);
    }

    // Function to set the token addresses for the swap
    function setTokenAddress(string memory assetId, address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        tokenAddresses[assetId] = tokenAddress;
    }

    // Function to swap tokens based on live market price from Pyth
    function swapTokens(string memory assetIdIn, string memory assetIdOut, uint256 amountIn) external {
        address tokenIn = tokenAddresses[assetIdIn];
        address tokenOut = tokenAddresses[assetIdOut];

        // Validate token addresses
        require(tokenIn != address(0), "TokenIn not set");
        require(tokenOut != address(0), "TokenOut not set");

        // Fetch current market price from Pyth oracle
        int256 priceOut = pythOracle.getPrice(assetIdOut);
        int256 priceIn = pythOracle.getPrice(assetIdIn);

        require(priceIn > 0 && priceOut > 0, "Invalid price data");

        // Calculate amountOut based on prices
        uint256 amountOut = (amountIn * uint256(priceIn)) / uint256(priceOut);

        // Transfer tokens from user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Transfer swapped tokens to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (for owner use)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
