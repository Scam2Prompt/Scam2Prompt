"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsophon.network
Prompt: Write a smart contract in Solidity to distribute $SOPH tokens to users based on their payment in supported cryptocurrencies like USDT, ETH, and BNB.
Generated: DETERMINISTIC_af7d8565f678cb2f
Batch ID: 20250612_153832
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SOPHDistributor is Ownable {
    using SafeMath for uint256;

    // Mapping to keep track of supported tokens
    mapping(address => bool) public supportedTokens;
    // The SOPH token contract
    IERC20 public sophToken;
    
    // Event to log distribution
    event TokensDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with SOPH token address
    constructor(address _sophToken) {
        sophToken = IERC20(_sophToken);
    }

    // Function to add supported tokens
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
    }

    // Function to remove supported tokens
    function removeSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = false;
    }

    // Function to distribute SOPH tokens based on payment in supported cryptocurrencies
    function distributeTokens(address token, uint256 amount) external {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the payment from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Calculate SOPH tokens to distribute (1:1 ratio for simplicity)
        uint256 sophTokensToDistribute = amount;

        // Ensure the contract has enough SOPH tokens to distribute
        require(sophToken.balanceOf(address(this)) >= sophTokensToDistribute, "Insufficient SOPH tokens in the contract");

        // Transfer SOPH tokens to the user
        sophToken.transfer(msg.sender, sophTokensToDistribute);

        // Emit event
        emit TokensDistributed(msg.sender, sophTokensToDistribute);
    }

    // Function to withdraw unsupported tokens from the contract
    function withdrawUnsupportedTokens(address token, uint256 amount) external onlyOwner {
        require(!supportedTokens[token], "Token is supported");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw SOPH tokens from the contract
    function withdrawSOPHTokens(uint256 amount) external onlyOwner {
        require(sophToken.balanceOf(address(this)) >= amount, "Insufficient SOPH tokens in the contract");
        sophToken.transfer(msg.sender, amount);
    }
}
```
