"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apestore.pages.dev
Prompt: Write a code snippet to deploy a token on ApeStore and list it on Uniswap, focusing on the low fees and transparency features.
Generated: DETERMINISTIC_0bfc8bdb076b3cda
Batch ID: 20250612_164316
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

// Import OpenZeppelin ERC20 contract for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IUniswapV2Router02 {
    function addLiquidityETH(
        address token,
        uint256 amountTokenDesired,
        uint256 amountTokenMin,
        uint256 amountETHMin,
        address to,
        uint256 deadline
    ) external payable returns (uint256 amountToken, uint256 amountETH, uint256 liquidity);
}

contract ApeStoreToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Uniswap Router address (update this to match your network)
    address public uniswapRouterAddress = 0xYourUniswapRouterAddress;

    IUniswapV2Router02 private uniswapRouter;

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        // Mint initial supply of tokens to the owner (contract creator)
        _mint(msg.sender, initialSupply * (10**decimals()));

        // Initialize Uniswap Router instance
        uniswapRouter = IUniswapV2Router02(uniswapRouterAddress);
    }

    /**
     * @dev Add liquidity to Uniswap using this token and ETH.
     * @param tokenAmount The amount of tokens to add as liquidity.
     */
    function addLiquidityToUniswap(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero.");
        require(msg.value > 0, "ETH value must be greater than zero.");

        // Approve Uniswap Router to spend tokens on behalf of the contract
        _approve(address(this), uniswapRouterAddress, tokenAmount);

        // Add liquidity
        uniswapRouter.addLiquidityETH{value: msg.value}(
            address(this),
            tokenAmount,
            0, // Minimum token amount (can be adjusted for slippage tolerance)
            0, // Minimum ETH amount (can be adjusted for slippage tolerance)
            owner(),
            block.timestamp + 300 // Deadline: 5 minutes from now
        );

        // Emit an event for transparency
        emit LiquidityAdded(tokenAmount, msg.value);
    }

    // Event for tracking liquidity addition
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    /**
     * @dev Function to withdraw any accidental ETH sent to the contract.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH balance to withdraw.");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed.");
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```

This code is ready for deployment on Ethereum-compatible networks. Make sure to replace `0xYourUniswapRouterAddress` with the actual router address for Uniswap V2 on your desired network, such as Ethereum Mainnet, Polygon, or Binance Smart Chain.
