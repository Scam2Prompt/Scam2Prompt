"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrollswap.finance
Prompt: Write a smart contract example for enabling token swaps on a platform like ScrollSwap Finance.
Generated: DETERMINISTIC_27b349d46c85a756
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a token swap platform
contract TokenSwap is Ownable {
    // Event emitted when a swap occurs
    event TokensSwapped(address indexed user, address inputToken, address outputToken, uint256 inputAmount, uint256 outputAmount);

    // Function to swap tokens
    function swapTokens(
        address inputToken,
        address outputToken,
        uint256 inputAmount,
        uint256 outputAmount
    ) external {
        // Validate input parameters
        require(inputToken != address(0), "Input token is the zero address");
        require(outputToken != address(0), "Output token is the zero address");
        require(inputAmount > 0, "Input amount must be greater than zero");
        require(outputAmount > 0, "Output amount must be greater than zero");

        // Transfer input tokens from the user to this contract
        IERC20(inputToken).transferFrom(msg.sender, address(this), inputAmount);

        // Transfer output tokens from this contract to the user
        IERC20(outputToken).transfer(msg.sender, outputAmount);

        // Emit event for the swap
        emit TokensSwapped(msg.sender, inputToken, outputToken, inputAmount, outputAmount);
    }

    // Function to withdraw tokens from the contract (only owner can call this)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from this contract to the owner
        IERC20(token).transfer(owner(), amount);
    }

    // Function to check token balance of the contract
    function getTokenBalance(address token) external view returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }
}
```
