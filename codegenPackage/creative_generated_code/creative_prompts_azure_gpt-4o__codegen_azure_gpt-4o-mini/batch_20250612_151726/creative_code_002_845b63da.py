"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.pages.dev
Prompt: Generate Solidity code for deploying a smart contract that supports "Owy" token transactions and presale functionality.
Generated: DETERMINISTIC_845b63dac403381f
Batch ID: 20250612_151726
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title OwyToken
 * @dev Implementation of the Owy token with presale functionality
 */
contract OwyToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Presale parameters
    uint256 public presalePrice; // Price per token during presale
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd;   // Presale end time
    mapping(address => uint256) public presaleBalances; // Track presale contributions

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event PresaleUpdated(uint256 start, uint256 end, uint256 price);

    /**
     * @dev Constructor that gives msg.sender all existing tokens and initializes presale parameters.
     */
    constructor(uint256 initialSupply) ERC20("Owy Token", "OWY") {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to deployer
    }

    /**
     * @dev Start or update the presale parameters.
     * @param _start The presale start timestamp.
     * @param _end The presale end timestamp.
     * @param _price The price per token during presale.
     */
    function updatePresale(uint256 _start, uint256 _end, uint256 _price) external onlyOwner {
        require(_start < _end, "Start time must be before end time");
        require(_price > 0, "Price must be greater than 0");

        presaleStart = _start;
        presaleEnd = _end;
        presalePrice = _price;

        emit PresaleUpdated(_start, _end, _price);
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable {
        require(block.timestamp >= presaleStart, "Presale has not started");
        require(block.timestamp <= presaleEnd, "Presale has ended");
        require(msg.value == amount.mul(presalePrice), "Incorrect value sent");
        require(amount > 0, "Amount must be greater than 0");

        // Record the presale balance
        presaleBalances[msg.sender] = presaleBalances[msg.sender].add(amount);
        
        // Mint the tokens to the buyer
        _mint(msg.sender, amount * (10 ** decimals()));

        emit TokensPurchased(msg.sender, amount, msg.value);
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Override the transfer function to restrict transfers until presale is over.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        
        // Prevent transfers during presale
        require(block.timestamp > presaleEnd, "Transfers are disabled during presale");
    }
}
```
