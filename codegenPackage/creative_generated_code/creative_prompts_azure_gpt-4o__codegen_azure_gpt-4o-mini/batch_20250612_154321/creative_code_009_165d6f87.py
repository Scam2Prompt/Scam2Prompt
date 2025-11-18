"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumcreator-pro.pages.dev
Prompt: Provide an example of a smart contract for creating a token with a $1 creation fee and full ownership, as described on EthereumCreator-Pro.
Generated: DETERMINISTIC_165d6f874f91db42
Batch ID: 20250612_154321
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CustomToken
 * @dev ERC20 Token that charges a $1 creation fee and gives full ownership to the creator.
 */
contract CustomToken is ERC20, Ownable {
    // Fee in wei (1 USD at the current conversion rate, adjust as necessary)
    uint256 public creationFee;

    // Event emitted when a new token is created
    event TokenCreated(address indexed creator, string tokenName, string tokenSymbol);

    /**
     * @dev Constructor that initializes the token name and symbol, and sets the creation fee.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _creationFee The fee to create a token in wei.
     */
    constructor(string memory _name, string memory _symbol, uint256 _creationFee) 
        ERC20(_name, _symbol) 
    {
        creationFee = _creationFee;
    }

    /**
     * @dev Function to create new tokens. Only the owner can call this.
     * @param amount The amount of tokens to mint.
     */
    function createToken(uint256 amount) public payable onlyOwner {
        // Check if the creation fee is paid
        require(msg.value == creationFee, "Incorrect creation fee sent");
        
        // Mint the new tokens to the owner's address
        _mint(msg.sender, amount);
        
        // Emit an event for token creation
        emit TokenCreated(msg.sender, name(), symbol());
    }

    /**
     * @dev Function to withdraw Ether from the contract. Only the owner can call this.
     */
    function withdraw() public onlyOwner {
        // Transfer the contract balance to the owner
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether sent directly to the contract.
     */
    receive() external payable {}

    /**
     * @dev Function to set a new creation fee. Only the owner can call this.
     * @param newFee The new creation fee in wei.
     */
    function setCreationFee(uint256 newFee) public onlyOwner {
        creationFee = newFee;
    }
}
```
