"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whales-market.pages.dev
Prompt: Generate a smart contract in Solidity that supports a whitelisting portal for token purchases, similar to the Whales Market's whitelisting system for $WHALES tokens.
Generated: DETERMINISTIC_b10296c1ac4ef69d
Batch ID: 20250612_152620
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

// Importing OpenZeppelin's Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";
// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// WhitelistTokenSale is a contract for managing a token sale with a whitelisting mechanism
contract WhitelistTokenSale is Ownable {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Token price in wei
    uint256 public tokenPrice;

    // Keeps track of whitelisted addresses
    mapping(address => bool) public whitelist;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to check if an address is whitelisted
    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "You are not whitelisted");
        _;
    }

    // Constructor to initialize the token and price
    constructor(IERC20 _token, uint256 _tokenPrice) {
        token = _token;
        tokenPrice = _tokenPrice;
    }

    // Function to update the token price, only callable by the owner
    function updateTokenPrice(uint256 newPrice) external onlyOwner {
        tokenPrice = newPrice;
    }

    // Function to whitelist an address, only callable by the owner
    function whitelistAddress(address _address) external onlyOwner {
        whitelist[_address] = true;
    }

    // Function to remove an address from the whitelist
    function removeWhitelistedAddress(address _address) external onlyOwner {
        whitelist[_address] = false;
    }

    // Function for users to purchase tokens
    function purchaseTokens(uint256 amount) external payable onlyWhitelisted {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount.mul(tokenPrice), "Incorrect Ether value sent");

        // Transfer tokens from the contract to the buyer
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens in the contract");
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract, only callable by the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to withdraw unsold tokens from the contract, only callable by the owner
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(owner(), balance);
    }
}
```
