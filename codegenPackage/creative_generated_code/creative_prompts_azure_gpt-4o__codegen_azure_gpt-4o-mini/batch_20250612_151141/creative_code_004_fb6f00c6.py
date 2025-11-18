"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoinvip.pages.dev
Prompt: Write Solidity smart contract code for a token swap mechanism that supports $PEIPEI and ensures zero tax transactions as described in the tokenomics.
Generated: DETERMINISTIC_fb6f00c6084aff0b
Batch ID: 20250612_151141
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

// Importing the ERC20 interface to interact with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenSwap is Ownable {
    // Address of the PEIPEI token
    IERC20 public peipeiToken;

    // Events for logging swaps
    event TokenSwapped(address indexed user, uint256 amountIn, uint256 amountOut);

    // Constructor to set the PEIPEI token address
    constructor(address _peipeiToken) {
        require(_peipeiToken != address(0), "Invalid token address");
        peipeiToken = IERC20(_peipeiToken);
    }

    // Function to swap tokens
    function swapTokens(uint256 amountIn, uint256 amountOut) external {
        // Ensure that the amountIn is greater than zero
        require(amountIn > 0, "Amount in must be greater than zero");
        require(amountOut > 0, "Amount out must be greater than zero");

        // Transfer the PEIPEI tokens from the sender to this contract
        require(peipeiToken.transferFrom(msg.sender, address(this), amountIn), "Transfer of tokens failed");

        // Ensure the contract has enough tokens for the swap
        require(peipeiToken.balanceOf(address(this)) >= amountOut, "Insufficient tokens in contract for swap");

        // Transfer the output tokens to the user
        require(peipeiToken.transfer(msg.sender, amountOut), "Transfer of output tokens failed");

        // Emit the swap event
        emit TokenSwapped(msg.sender, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (for contract owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(peipeiToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the tokens to the owner
        require(peipeiToken.transfer(msg.sender, amount), "Withdrawal of tokens failed");
    }

    // Function to view contract's token balance
    function getContractTokenBalance() external view returns (uint256) {
        return peipeiToken.balanceOf(address(this));
    }
}
```
