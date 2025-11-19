"""
Generated Code Metadata:
========================
Original URL: https://owy-wtf.pages.dev
Prompt: Generate Solidity code for deploying a smart contract that supports "Owy" token transactions and presale functionality.
Generated: DETERMINISTIC_845b63dac403381f
Batch ID: 20250612_151726
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// OwyToken contract that extends the ERC20 standard
contract OwyToken is ERC20, Ownable {
    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presalePrice; // Price per token in wei
    bool public presaleActive;

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased during presale
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initial minting of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to start the presale
    function startPresale(uint256 duration, uint256 price) external onlyOwner {
        require(!presaleActive, "Presale is already active");
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + duration;
        presalePrice = price;
        presaleActive = true;
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
    }

    // Function to purchase tokens during the presale
    function buyTokens(uint256 amount) external payable {
        require(presaleActive, "Presale is not active");
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not within the valid time frame");
        require(msg.value == amount * presalePrice, "Incorrect Ether value sent");

        // Update contributions
        contributions[msg.sender] += amount;

        // Mint tokens to the buyer
        _mint(msg.sender, amount * 10 ** decimals());

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to receive Ether
    receive() external payable {
        // Allow the contract to receive Ether
    }

    // Fallback function
    fallback() external payable {
        // Allow the contract to receive Ether
    }
}
```
