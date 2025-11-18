"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-finance-en.web.app
Prompt: Write Solidity code for a smart contract that integrates Retik Finance's multi-chain non-custodial wallet functionality, ensuring compatibility with Ethereum-based tokens.
Generated: DETERMINISTIC_785f68213380b688
Batch ID: 20250612_152526
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract integrates with Retik Finance's multi-chain non-custodial wallet
// functionality, allowing Ethereum-based token transfers.
contract RetikWalletIntegration is Ownable {
    // Event emitted when tokens are transferred
    event TokensTransferred(address indexed token, address indexed to, uint256 amount);

    // Function to transfer ERC20 tokens to a specified address
    // This function requires the caller to approve this contract to spend the tokens beforehand
    // @param token The address of the ERC20 token contract
    // @param to The recipient address
    // @param amount The amount of tokens to send
    function transferTokens(address token, address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 erc20Token = IERC20(token);
        
        // Ensure the contract has enough tokens to transfer
        uint256 tokenBalance = erc20Token.balanceOf(address(this));
        require(tokenBalance >= amount, "Insufficient token balance in contract");

        // Transfer tokens
        bool success = erc20Token.transfer(to, amount);
        require(success, "Token transfer failed");

        // Emit an event for tracking purposes
        emit TokensTransferred(token, to, amount);
    }

    // Function to withdraw any ERC20 tokens sent to this contract by mistake
    // @param token The address of the ERC20 token contract
    // @param amount The amount of tokens to withdraw
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        IERC20 erc20Token = IERC20(token);
        
        // Ensure the contract has enough tokens to withdraw
        uint256 tokenBalance = erc20Token.balanceOf(address(this));
        require(tokenBalance >= amount, "Insufficient token balance in contract");

        // Transfer tokens to the owner
        bool success = erc20Token.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }

    // Function to get the balance of a specific ERC20 token in this contract
    // @param token The address of the ERC20 token contract
    // @return The balance of the specified token
    function getTokenBalance(address token) external view returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }
}
```
