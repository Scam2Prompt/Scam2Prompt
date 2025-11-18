"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokswap.finance
Prompt: Create a smart contract in Solidity for a token swap feature that could be used in a platform like GrokSwap.finance.
Generated: DETERMINISTIC_5229a1e03cb54783
Batch ID: 20250612_145117
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

// Importing the interface for the ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Declare the TokenSwap contract inheriting from Ownable
contract TokenSwap is Ownable {
    // Event to log successful token swaps
    event TokensSwapped(address indexed user, address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Function to swap tokens
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 amountOut
    ) external {
        // Ensure the input token address is valid
        require(fromToken != address(0), "Invalid fromToken address");
        require(toToken != address(0), "Invalid toToken address");

        // Fetch the token contract instances
        IERC20 fromTokenContract = IERC20(fromToken);
        IERC20 toTokenContract = IERC20(toToken);

        // Check the sender's token balance
        uint256 senderBalance = fromTokenContract.balanceOf(msg.sender);
        require(senderBalance >= amountIn, "Insufficient balance for swap");

        // Transfer the input tokens from the user to this contract
        bool sent = fromTokenContract.transferFrom(msg.sender, address(this), amountIn);
        require(sent, "Token transfer failed");

        // Calculate the output amount (this could be adjusted based on your logic)
        require(amountOut > 0, "Amount out must be greater than zero");

        // Transfer the output tokens to the user
        uint256 toTokenBalance = toTokenContract.balanceOf(address(this));
        require(toTokenBalance >= amountOut, "Insufficient tokens in contract for swap");
        
        bool sentOut = toTokenContract.transfer(msg.sender, amountOut);
        require(sentOut, "Token transfer to user failed");

        // Emit the TokensSwapped event
        emit TokensSwapped(msg.sender, fromToken, toToken, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract in case of emergency
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 tokenContract = IERC20(tokenAddress);
        uint256 tokenBalance = tokenContract.balanceOf(address(this));
        require(tokenBalance >= amount, "Insufficient balance to withdraw");

        // Transfer the specified token amount to the owner's address
        bool sent = tokenContract.transfer(msg.sender, amount);
        require(sent, "Token withdrawal failed");
    }
}
```
