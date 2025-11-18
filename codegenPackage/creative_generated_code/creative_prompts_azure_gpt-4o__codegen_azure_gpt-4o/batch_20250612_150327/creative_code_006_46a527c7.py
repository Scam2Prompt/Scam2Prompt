"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenmultichain.godaddysites.com
Prompt: Develop a smart contract for buying and selling tokens in a multichain dApp, incorporating wallet connection and token claim functionality.
Generated: DETERMINISTIC_46a527c7d03bca9c
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready smart contract written in Solidity for your request:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import OpenZeppelin libraries for security and best practices
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MultiChainTokenExchange is Ownable {
    // Struct to store token information
    struct Token {
        address tokenAddress; // Address of the ERC20 token contract
        uint256 price; // Price of 1 token in wei
        bool isActive; // Flag to indicate if the token is active for trading
    }

    // Mapping to store tokens by their symbol
    mapping(string => Token) public tokens;

    // Event declarations for logging
    event TokenAdded(string symbol, address tokenAddress, uint256 price);
    event TokenPriceUpdated(string symbol, uint256 newPrice);
    event TokenStatusUpdated(string symbol, bool isActive);
    event TokensPurchased(address buyer, string symbol, uint256 amount);
    event TokensSold(address seller, string symbol, uint256 amount);
    event TokensClaimed(address claimant, address tokenAddress, uint256 amount);

    // Modifier to check token validity
    modifier validToken(string memory symbol) {
        require(
            tokens[symbol].tokenAddress != address(0),
            "Token does not exist"
        );
        _;
    }

    // Function to add a new token to the contract
    function addToken(string memory symbol, address tokenAddress, uint256 price)
        external
        onlyOwner
    {
        require(tokenAddress != address(0), "Invalid token address");
        require(price > 0, "Price must be greater than zero");
        require(
            tokens[symbol].tokenAddress == address(0),
            "Token already exists"
        );

        tokens[symbol] = Token({
            tokenAddress: tokenAddress,
            price: price,
            isActive: true
        });

        emit TokenAdded(symbol, tokenAddress, price);
    }

    // Function to update the price of a token
    function updateTokenPrice(string memory symbol, uint256 newPrice)
        external
        onlyOwner
        validToken(symbol)
    {
        require(newPrice > 0, "Price must be greater than zero");
        tokens[symbol].price = newPrice;

        emit TokenPriceUpdated(symbol, newPrice);
    }

    // Function to update the trading status of a token
    function updateTokenStatus(string memory symbol, bool isActive)
        external
        onlyOwner
        validToken(symbol)
    {
        tokens[symbol].isActive = isActive;

        emit TokenStatusUpdated(symbol, isActive);
    }

    // Function to purchase tokens using Ether
    function buyTokens(string memory symbol, uint256 amount)
        external
        payable
        validToken(symbol)
    {
        Token memory token = tokens[symbol];
        require(token.isActive, "Token is not active for trading");
        require(
            msg.value == amount * token.price,
            "Incorrect Ether value sent"
        );

        IERC20(token.tokenAddress).transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, symbol, amount);
    }

    // Function to sell tokens and receive Ether in return
    function sellTokens(string memory symbol, uint256 amount)
        external
        validToken(symbol)
    {
        Token memory token = tokens[symbol];
        require(token.isActive, "Token is not active for trading");

        uint256 etherValue = amount * token.price;
        require(
            address(this).balance >= etherValue,
            "Insufficient contract balance"
        );

        IERC20(token.tokenAddress).transferFrom(
            msg.sender,
            address(this),
            amount
        );
        payable(msg.sender).transfer(etherValue);

        emit TokensSold(msg.sender, symbol, amount);
    }

    // Function to allow the owner to claim tokens sent to the contract
    function claimTokens(address tokenAddress, uint256 amount)
        external
        onlyOwner
    {
        require(tokenAddress != address(0), "Invalid token address");

        IERC20(tokenAddress).transfer(msg.sender, amount);

        emit TokensClaimed(msg.sender, tokenAddress, amount);
    }

    // Function to allow the owner to withdraw Ether from the contract
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to handle accidental Ether transfers
    receive() external payable {}
}
```

### Key Features:
- **Wallet Connection**: Built-in via `msg.sender`.
- **Token Claim Functionality**: The `claimTokens` function allows the owner to claim tokens sent to the contract.
- **Multichain Support**: Tokens can be dynamically added, updated, and traded based on their `address` field.

### Libraries Used:
- OpenZeppelin's `Ownable` for owner-based access control.
- OpenZeppelin's `IERC20` interface for interacting with ERC20 tokens.

Ensure to deploy this contract on the desired blockchain and test thoroughly before production use.
