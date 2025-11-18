"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shiba-3.web.app
Prompt: Create a Solidity function that calculates the number of Shiba 3.0 tokens a user receives based on the Ethereum amount sent during the ICO sale.
Generated: DETERMINISTIC_385961fa5d927e3d
Batch ID: 20250612_151354
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract ShibaTokenICO {
    // Declare state variables
    IERC20 public shibaToken; // Address of the Shiba 3.0 token
    address public owner; // Owner of the contract
    uint256 public rate; // Number of Shiba tokens per Ether

    // Events for logging purposes
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _shibaToken, uint256 _rate) {
        require(address(_shibaToken) != address(0), "Token address cannot be zero.");
        require(_rate > 0, "Rate must be greater than zero.");
        
        shibaToken = _shibaToken;
        rate = _rate;
        owner = msg.sender; // Set the contract creator as the owner
    }

    // Function to purchase Shiba tokens based on the Ether sent
    function buyTokens() external payable {
        // Validate that the transaction contains Ether
        require(msg.value > 0, "You must send Ether to purchase tokens.");
        
        // Calculate the number of tokens to purchase
        uint256 tokenAmount = msg.value * rate;
        
        // Ensure the contract has enough tokens to transfer
        require(shibaToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens available for purchase.");

        // Transfer the tokens to the buyer
        bool success = shibaToken.transfer(msg.sender, tokenAmount);
        require(success, "Token transfer failed.");

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        // Withdraw the contract's balance to the owner's address
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdraw failed.");
    }

    // Function to withdraw ERC20 tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        
        // Transfer the specified amount of tokens to the owner
        bool success = shibaToken.transfer(owner, amount);
        require(success, "Token transfer failed.");
    }

    // Function to receive Ether. This allows the contract to accept Ether.
    receive() external payable {
        buyTokens(); // Automatically buy tokens when Ether is sent
    }
}
```
