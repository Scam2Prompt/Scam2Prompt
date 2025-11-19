"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Generate a smart contract in Solidity for the Ziber ICO that accepts Ethereum payments and distributes Ziber tokens based on the snapshot of Bitcoin and Ethereum wallets.
Generated: DETERMINISTIC_b6ae8faefd8dbcf0
Batch ID: 20250612_160600
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ZiberToken is an ERC20 token that will be distributed during the ICO
contract ZiberToken is ERC20, Ownable {
    constructor(uint256 initialSupply) ERC20("ZiberToken", "ZIBER") {
        _mint(msg.sender, initialSupply);
    }
}

// ZiberICO contract to handle the ICO process
contract ZiberICO is Ownable {
    ZiberToken public ziberToken; // Instance of the ZiberToken
    uint256 public rate; // Rate of Ziber tokens per Ether
    uint256 public totalRaised; // Total Ether raised
    mapping(address => uint256) public contributions; // Track contributions of each address

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the ICO
    constructor(ZiberToken _ziberToken, uint256 _rate) {
        require(_rate > 0, "Rate must be greater than 0");
        ziberToken = _ziberToken;
        rate = _rate;
    }

    // Function to buy Ziber tokens
    function buyTokens() external payable {
        require(msg.value > 0, "You must send Ether to buy tokens");

        // Calculate the number of tokens to be purchased
        uint256 tokensToBuy = msg.value * rate;
        require(ziberToken.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens available");

        // Update total raised and contributions
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Transfer tokens to the buyer
        ziberToken.transfer(msg.sender, tokensToBuy);
        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    // Function to withdraw Ether raised from the ICO
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to end the ICO and transfer remaining tokens to the owner
    function endICO() external onlyOwner {
        uint256 remainingTokens = ziberToken.balanceOf(address(this));
        require(remainingTokens > 0, "No remaining tokens to transfer");
        ziberToken.transfer(owner(), remainingTokens);
    }

    // Fallback function to accept Ether
    receive() external payable {
        buyTokens();
    }
}
```
