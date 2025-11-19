"""
Generated Code Metadata:
========================
Original URL: https://wlfi.vercel.app
Prompt: Write a smart contract in Solidity to create a simple decentralized exchange (DEX) for trading $WLFI tokens.
Generated: DETERMINISTIC_4ac23eda8e2a42fd
Batch ID: 20250622_205552
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

// Importing the ERC20 interface for the $WLFI token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Simple Decentralized Exchange (DEX) contract for trading $WLFI tokens
contract SimpleDEX is Ownable {
    // Event emitted when a trade occurs
    event Trade(address indexed buyer, uint256 amountIn, uint256 amountOut);

    // Mapping to store the token prices (in terms of $WLFI)
    mapping(address => uint256) public tokenPrices;

    // Function to set the price of a token
    function setTokenPrice(address token, uint256 price) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(price > 0, "Price must be greater than zero");
        tokenPrices[token] = price;
    }

    // Function to trade $WLFI tokens for another token
    function trade(address token, uint256 amountIn) external {
        require(tokenPrices[token] > 0, "Token not supported");
        require(amountIn > 0, "Amount must be greater than zero");

        // Calculate the amount of tokens to send back to the user
        uint256 amountOut = (amountIn * tokenPrices[token]) / (10 ** 18); // Assuming prices are in wei

        // Transfer $WLFI tokens from the user to the contract
        IERC20 wlfiToken = IERC20(address(this));
        require(wlfiToken.transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Transfer the output tokens to the user
        IERC20(token).transfer(msg.sender, amountOut);

        // Emit the trade event
        emit Trade(msg.sender, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw $WLFI tokens from the contract (only owner)
    function withdrawWLFI(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        IERC20 wlfiToken = IERC20(address(this));
        wlfiToken.transfer(msg.sender, amount);
    }
}
```
