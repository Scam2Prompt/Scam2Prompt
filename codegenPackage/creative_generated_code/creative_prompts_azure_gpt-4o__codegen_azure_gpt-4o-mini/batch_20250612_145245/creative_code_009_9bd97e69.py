"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.unisocks.fi
Prompt: Develop a smart contract that interacts with the Unisocks platform to facilitate the buying and selling of $SOCKS tokens.
Generated: DETERMINISTIC_9bd97e69ccb5980f
Batch ID: 20250612_145245
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

// Import required interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the Smart Contract for interacting with Unisocks
contract UnisocksMarketplace is Ownable {
    // ERC20 token instance for $SOCKS
    IERC20 public socksToken;

    // Event emitted when a purchase occurs
    event Purchased(address indexed buyer, uint256 amount);

    // Event emitted when a sale occurs
    event Sold(address indexed seller, uint256 amount);

    // Constructor to set the $SOCKS token address
    constructor(address _socksTokenAddress) {
        require(_socksTokenAddress != address(0), "Invalid token address");
        socksToken = IERC20(_socksTokenAddress);
    }

    // Function to buy $SOCKS tokens
    function buySocks(uint256 amount) external payable {
        // Check that the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        
        // Calculate the price of the tokens (assuming 1 TOKEN = 0.01 ETH)
        uint256 priceInEth = amount * 0.01 ether;
        require(msg.value >= priceInEth, "Insufficient ETH sent");

        // Transfer $SOCKS tokens to the buyer
        require(socksToken.transfer(msg.sender, amount), "Transfer failed");

        // Emit the purchase event
        emit Purchased(msg.sender, amount);
        
        // Refund excess ETH
        if (msg.value > priceInEth) {
            payable(msg.sender).transfer(msg.value - priceInEth);
        }
    }

    // Function to sell $SOCKS tokens
    function sellSocks(uint256 amount) external {
        // Check that the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer $SOCKS tokens from the seller to the contract
        require(socksToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate the price in ETH to pay for the tokens (assuming 1 TOKEN = 0.01 ETH)
        uint256 payment = amount * 0.01 ether;
        
        // Ensure the contract has enough ETH to pay the seller
        require(address(this).balance >= payment, "Insufficient contract balance");

        // Transfer payment to the seller
        payable(msg.sender).transfer(payment);

        // Emit the sale event
        emit Sold(msg.sender, amount);
    }

    // Function to withdraw contract funds (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to receive ETH
    receive() external payable {}
}
```
