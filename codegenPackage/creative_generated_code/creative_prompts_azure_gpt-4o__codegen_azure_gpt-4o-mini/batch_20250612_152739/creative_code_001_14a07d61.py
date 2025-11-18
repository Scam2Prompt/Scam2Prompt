"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Create a smart contract in Solidity that implements a presale mechanism for a cryptocurrency token, ensuring the total supply does not exceed 100,000,000 tokens.
Generated: DETERMINISTIC_14a07d61a5789210
Batch ID: 20250612_152739
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

// Importing the OpenZeppelin ERC20 Token contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PresaleToken
 * @dev This smart contract implements a presale mechanism for an ERC20 token.
 * The total supply is capped at 100 million tokens, and it allows users to buy tokens during the presale.
 */
contract PresaleToken is ERC20, Ownable {
    // Maximum supply of the token
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10 ** decimals();
    // Amount of tokens sold during the presale
    uint256 public tokensSold;
    // Price of one token in wei
    uint256 public tokenPrice;
    // Boolean to track if the presale is active
    bool public presaleActive;

    // Event to log the sale of tokens
    event TokensPurchased(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * Sets the initial token price and marks the presale as inactive.
     * @param _tokenPrice The price of one token in wei.
     */
    constructor(uint256 _tokenPrice) ERC20("PresaleToken", "PST") {
        require(_tokenPrice > 0, "Token price must be greater than 0");
        tokenPrice = _tokenPrice;
        presaleActive = false;
    }

    /**
     * @dev Function to start the presale.
     * Can only be called by the contract owner.
     */
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale is already active");
        presaleActive = true;
    }

    /**
     * @dev Function to stop the presale.
     * Can only be called by the contract owner.
     */
    function stopPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
    }

    /**
     * @dev Function for users to purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(presaleActive, "Presale is not active");
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent");
        
        uint256 totalAmount = tokensSold + amount;
        require(totalAmount <= MAX_SUPPLY, "Exceeds maximum supply");

        // Update the state and transfer tokens
        tokensSold = totalAmount;
        _mint(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * Can only be called by the contract owner.
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");
        payable(owner()).transfer(contractBalance);
    }

    /**
     * @dev Function to get the current balance of the contract.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
