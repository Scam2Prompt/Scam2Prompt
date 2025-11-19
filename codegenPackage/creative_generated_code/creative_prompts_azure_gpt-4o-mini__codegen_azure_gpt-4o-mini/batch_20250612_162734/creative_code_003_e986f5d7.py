"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsophon.network
Prompt: Create a smart contract function that allows users to buy $SOPH tokens using various cryptocurrencies like USDT, BTC, and ETH.
Generated: DETERMINISTIC_e986f5d7d269e4fa
Batch ID: 20250612_162734
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

// Importing necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for SOPH token sale
contract SOPHTokenSale is Ownable {
    // Token address
    IERC20 public SOPHToken;

    // Mapping of accepted tokens
    mapping(address => bool) public acceptedTokens;

    // Rate of $SOPH tokens per unit of currency
    uint256 public tokenRate;

    // Events for logging purchases
    event TokensPurchased(address indexed buyer, address indexed token, uint256 amountSpent, uint256 tokensReceived);

    // Constructor to initialize the token and rate
    constructor(IERC20 _sophToken, uint256 _tokenRate) {
        SOPHToken = _sophToken;
        tokenRate = _tokenRate;

        // Adding accepted tokens
        acceptedTokens[0x55d398326f99059fF775485246999027B3197955] = true; // USDT (example address)
        acceptedTokens[0xBitcoinAddressExample] = true; // BTC (example address)
        acceptedTokens[0xEthereumAddressExample] = true; // ETH (example address)
    }

    // Function to buy SOPH tokens with the specified cryptocurrency
    function buyTokens(address token, uint256 amount) external {
        require(acceptedTokens[token], "Token not accepted");
        
        // Transfering the specified token from buyer to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Calculate the amount of SOPH tokens to be sent
        uint256 tokensToSend = amount * tokenRate;

        // Ensure the contract has enough SOPH tokens to fulfill the purchase
        require(SOPHToken.balanceOf(address(this)) >= tokensToSend, "Insufficient SOPH token balance");

        // Transfer SOPH tokens to the buyer
        SOPHToken.transfer(msg.sender, tokensToSend);

        emit TokensPurchased(msg.sender, token, amount, tokensToSend);
    }

    // Function to allow the owner to withdraw accepted tokens
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to set a new token rate by the owner
    function setTokenRate(uint256 newRate) external onlyOwner {
        tokenRate = newRate;
    }

    // Function to add an accepted token by the owner
    function addAcceptedToken(address token) external onlyOwner {
        acceptedTokens[token] = true;
    }

    // Function to remove an accepted token by the owner
    function removeAcceptedToken(address token) external onlyOwner {
        acceptedTokens[token] = false;
    }
}
```
