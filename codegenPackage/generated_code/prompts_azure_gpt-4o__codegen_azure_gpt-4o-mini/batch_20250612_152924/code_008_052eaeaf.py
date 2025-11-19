"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Create a Solidity contract that integrates with an Ethereum wallet to allow users to participate in the SHROOM presale directly from their wallet.
Generated: DETERMINISTIC_052eaeaf732672f8
Batch ID: 20250612_152924
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

// Importing OpenZeppelin's SafeERC20 and Ownable contracts for secure token handling and ownership management
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// SHROOMPresale contract allows users to participate in the SHROOM presale
contract SHROOMPresale is Ownable {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public shroomToken; // The SHROOM token contract
    uint256 public presalePrice; // Price of SHROOM token in wei
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public totalTokensSold; // Total tokens sold during presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Constructor to initialize the contract
    constructor(
        address _shroomToken,
        uint256 _presalePrice,
        uint256 _presaleStart,
        uint256 _presaleEnd
    ) {
        require(_shroomToken != address(0), "Invalid token address");
        require(_presalePrice > 0, "Price must be greater than zero");
        require(_presaleStart < _presaleEnd, "Invalid presale period");

        shroomToken = IERC20(_shroomToken);
        presalePrice = _presalePrice;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    // Function to purchase SHROOM tokens
    function purchaseTokens(uint256 amount) external payable {
        require(block.timestamp >= presaleStart, "Presale has not started yet");
        require(block.timestamp <= presaleEnd, "Presale has ended");
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 totalCost = amount * presalePrice;
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Transfer SHROOM tokens to the buyer
        shroomToken.safeTransfer(msg.sender, amount);
        totalTokensSold += amount;

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, amount, totalCost);

        // Refund excess Ether sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to set a new presale price (only owner)
    function setPresalePrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero");
        presalePrice = newPrice;
    }

    // Function to update presale period (only owner)
    function updatePresalePeriod(uint256 newStart, uint256 newEnd) external onlyOwner {
        require(newStart < newEnd, "Invalid presale period");
        presaleStart = newStart;
        presaleEnd = newEnd;
    }

    // Function to retrieve the contract's Ether balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
