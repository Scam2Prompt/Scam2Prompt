"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfa-ai.pages.dev
Prompt: How can I implement a smart contract to facilitate the 1:1 token swap for $NFAI V1 to $NFAI V2?
Generated: DETERMINISTIC_f223c4bbeb02ff11
Batch ID: 20250612_162228
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the 1:1 token swap from $NFAI V1 to $NFAI V2
contract TokenSwap is Ownable {
    // Address of the V1 token contract
    IERC20 public tokenV1;
    // Address of the V2 token contract
    IERC20 public tokenV2;

    // Event to log successful swaps
    event TokensSwapped(address indexed user, uint256 amount);

    // Constructor to set initial token addresses
    constructor(address _tokenV1, address _tokenV2) {
        require(_tokenV1 != address(0), "Invalid V1 token address");
        require(_tokenV2 != address(0), "Invalid V2 token address");

        tokenV1 = IERC20(_tokenV1);
        tokenV2 = IERC20(_tokenV2);
    }

    // Function to swap V1 tokens for V2 tokens
    function swapTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tokenV1.balanceOf(msg.sender) >= amount, "Insufficient V1 balance");

        // Transfer V1 tokens from user to the contract
        tokenV1.transferFrom(msg.sender, address(this), amount);
        
        // Mint or transfer V2 tokens to the user
        // Assuming that the V2 token contract has a mint function
        require(tokenV2.balanceOf(address(this)) >= amount, "Insufficient V2 balance in contract");
        tokenV2.transfer(msg.sender, amount);

        // Emit the swap event
        emit TokensSwapped(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to update the V1 token address (only owner)
    function updateTokenV1(address newTokenV1) external onlyOwner {
        require(newTokenV1 != address(0), "Invalid address");
        tokenV1 = IERC20(newTokenV1);
    }

    // Function to update the V2 token address (only owner)
    function updateTokenV2(address newTokenV2) external onlyOwner {
        require(newTokenV2 != address(0), "Invalid address");
        tokenV2 = IERC20(newTokenV2);
    }
}
```
