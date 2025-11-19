"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: Create a smart contract in Solidity that implements a presale mechanism for a cryptocurrency token, ensuring the total supply does not exceed 100,000,000 tokens.
Generated: DETERMINISTIC_14a07d61a5789210
Batch ID: 20250612_152739
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PresaleToken
 * @dev This contract implements a presale mechanism for a cryptocurrency token.
 * The total supply of the token is capped at 100,000,000 tokens.
 */
contract PresaleToken is ERC20, Ownable {
    // Maximum total supply of the token
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10 ** 18; // 100 million tokens with 18 decimals

    // Presale parameters
    uint256 public presalePrice; // Price per token in wei
    uint256 public tokensSold; // Total tokens sold during the presale
    bool public presaleActive; // Flag to indicate if presale is active

    // Events
    event PresaleStarted(uint256 price);
    event PresaleEnded();
    event TokensPurchased(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to initialize the token with a name and symbol.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        presaleActive = false;
    }

    /**
     * @dev Start the presale with a specified price per token.
     * @param price Price per token in wei.
     */
    function startPresale(uint256 price) external onlyOwner {
        require(!presaleActive, "Presale is already active");
        require(price > 0, "Price must be greater than zero");

        presalePrice = price;
        presaleActive = true;

        emit PresaleStarted(price);
    }

    /**
     * @dev End the presale.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");

        presaleActive = false;

        emit PresaleEnded();
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(presaleActive, "Presale is not active");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount * presalePrice, "Incorrect Ether value sent");
        require(tokensSold + amount <= MAX_SUPPLY, "Exceeds maximum supply");

        tokensSold += amount;
        _mint(msg.sender, amount * 10 ** 18); // Mint tokens with 18 decimals

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Withdraw the contract's balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
