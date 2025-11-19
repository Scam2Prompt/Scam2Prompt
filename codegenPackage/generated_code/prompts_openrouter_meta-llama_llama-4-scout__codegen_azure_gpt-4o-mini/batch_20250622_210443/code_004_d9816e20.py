"""
Generated Code Metadata:
========================
Original URL: https://new-ej0.pages.dev
Prompt: Develop a Solidity smart contract that allows users to buy and open WEB3BOX Mystery boxes, distributing $WT and WUSD tokens accordingly.
Generated: DETERMINISTIC_d9816e20af560d7f
Batch ID: 20250622_210443
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the WEB3BOX Mystery Box
contract WEB3BOX is Ownable {
    // State variables
    IERC20 public wtToken; // $WT token contract
    IERC20 public wusdToken; // WUSD token contract

    // Event emitted when a box is purchased
    event BoxPurchased(address indexed buyer, uint256 boxId, uint256 wtAmount, uint256 wusdAmount);

    // Mapping to track the number of boxes purchased by each user
    mapping(address => uint256) public boxesPurchased;

    // Constructor to initialize the contract with token addresses
    constructor(address _wtToken, address _wusdToken) {
        require(_wtToken != address(0), "Invalid $WT token address");
        require(_wusdToken != address(0), "Invalid WUSD token address");
        
        wtToken = IERC20(_wtToken);
        wusdToken = IERC20(_wusdToken);
    }

    // Function to buy a mystery box
    function buyBox(uint256 boxId) external {
        // Define the amounts of tokens to distribute
        uint256 wtAmount = 100 * 10 ** 18; // Example amount for $WT
        uint256 wusdAmount = 50 * 10 ** 18; // Example amount for WUSD

        // Transfer tokens from the buyer to the contract
        require(wtToken.transferFrom(msg.sender, address(this), wtAmount), "Transfer of $WT failed");
        require(wusdToken.transferFrom(msg.sender, address(this), wusdAmount), "Transfer of WUSD failed");

        // Update the number of boxes purchased by the user
        boxesPurchased[msg.sender] += 1;

        // Emit the event for the box purchase
        emit BoxPurchased(msg.sender, boxId, wtAmount, wusdAmount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to set new token addresses (only owner)
    function setTokenAddresses(address _wtToken, address _wusdToken) external onlyOwner {
        require(_wtToken != address(0), "Invalid $WT token address");
        require(_wusdToken != address(0), "Invalid WUSD token address");

        wtToken = IERC20(_wtToken);
        wusdToken = IERC20(_wusdToken);
    }
}
```
