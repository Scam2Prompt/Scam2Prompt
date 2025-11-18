"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vuyper.pages.dev
Prompt: Create a Solidity smart contract that integrates with Vyper DEX to automate trades based on predefined conditions using Pyth data feeds for blue-chip cryptocurrencies.
Generated: DETERMINISTIC_005ecfa88bbbf865
Batch ID: 20250612_152326
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

// Importing interfaces for Pyth data feeds and Vyper DEX
interface IPyth {
    function getPrice(bytes32 priceFeedId) external view returns (int256, uint256, uint256);
}

interface IVyperDEX {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}

contract AutomatedTradingBot {
    // Address of the Pyth data feed contract
    address public pythDataFeedAddress;
    // Address of the Vyper DEX router contract
    address public vyperDEXAddress;

    // Owner of the contract
    address public owner;

    // Blue-chip cryptocurrency price feed IDs from Pyth
    mapping(string => bytes32) public priceFeedIds;

    // Trade conditions
    uint256 public priceThreshold; // Example: Price threshold in USD * 10^8

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not owner");
        _;
    }

    // Events
    event TradeExecuted(uint256 amountIn, uint256 amountOut);
    event PriceThresholdUpdated(uint256 oldThreshold, uint256 newThreshold);

    /**
     * @dev Constructor to initialize the contract.
     * @param _pythDataFeedAddress Address of the Pyth data feed contract.
     * @param _vyperDEXAddress Address of the Vyper DEX router contract.
     */
    constructor(address _pythDataFeedAddress, address _vyperDEXAddress) {
        require(_pythDataFeedAddress != address(0), "Invalid Pyth contract address");
        require(_vyperDEXAddress != address(0), "Invalid VyperDEX address");
        pythDataFeedAddress = _pythDataFeedAddress;
        vyperDEXAddress = _vyperDEXAddress;
        owner = msg.sender; // Set contract deployer as owner
    }

    /**
     * @dev Update price feed ID mapping for blue-chip cryptocurrencies.
     * @param assetName Symbol of the cryptocurrency (e.g., BTC, ETH).
     * @param feedId Pyth price feed ID for the asset.
     */
    function setPriceFeedId(string memory assetName, bytes32 feedId) external onlyOwner {
        priceFeedIds[assetName] = feedId;
    }

    /**
     * @dev Update the price threshold for executing trades.
     * @param newThreshold New price threshold in USD * 10^8.
     */
    function updatePriceThreshold(uint256 newThreshold) external onlyOwner {
        emit PriceThresholdUpdated(priceThreshold, newThreshold);
        priceThreshold = newThreshold;
    }

    /**
     * @dev Executes a trade if the predefined condition is met.
     * @param assetName Symbol of the cryptocurrency (e.g., BTC, ETH).
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input tokens for the trade.
     * @param amountOutMin Minimum amount of output tokens expected (for slippage protection).
     * @param path Array of token addresses for the swap path.
     */
    function executeTrade(
        string memory assetName,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path
    ) external onlyOwner {
        // Fetch price from Pyth data feed
        bytes32 feedId = priceFeedIds[assetName];
        require(feedId != bytes32(0), "Price feed ID not set");

        (int256 price, , ) = IPyth(pythDataFeedAddress).getPrice(feedId);
        require(price > 0, "Invalid price data");

        uint256 normalizedPrice = uint256(price); // Convert int256 to uint256 for comparison

        // Check if the price meets the threshold condition
        require(normalizedPrice >= priceThreshold, "Price condition not met");

        // Approve tokens for the swap
        IERC20(tokenIn).approve(vyperDEXAddress, amountIn);

        // Execute the trade on Vyper DEX
        uint256[] memory amounts = IVyperDEX(vyperDEXAddress)
            .swapExactTokensForTokens(amountIn, amountOutMin, path, address(this), block.timestamp + 60);

        emit TradeExecuted(amountIn, amounts[amounts.length - 1]);
    }

    /**
     * @dev Withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}

    /**
     * @dev Emergency withdraw function to withdraw ETH balance.
     */
    function emergencyWithdrawETH() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
