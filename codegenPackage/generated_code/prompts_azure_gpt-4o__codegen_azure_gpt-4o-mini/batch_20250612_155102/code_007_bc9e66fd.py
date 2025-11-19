"""
Generated Code Metadata:
========================
Original URL: https://safemoonx.xyz
Prompt: Write a Solidity smart contract that burns liquidity upon deployment, similar to the mechanism described for SafeMoonX.
Generated: DETERMINISTIC_bc9e66fdd013489d
Batch ID: 20250612_155102
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// LiquidityBurner contract to burn liquidity upon deployment
contract LiquidityBurner is Ownable {
    // Address of the token to be burned
    IERC20 public token;

    // Event to log the burning of liquidity
    event LiquidityBurned(address indexed token, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to burn liquidity by transferring tokens to the zero address
    function burnLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance to burn");

        // Transfer tokens to the zero address to burn them
        token.transfer(address(0), amount);

        // Emit an event for the burned liquidity
        emit LiquidityBurned(address(token), amount);
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address _tokenAddress, uint256 amount) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(_tokenAddress).transfer(msg.sender, amount);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
