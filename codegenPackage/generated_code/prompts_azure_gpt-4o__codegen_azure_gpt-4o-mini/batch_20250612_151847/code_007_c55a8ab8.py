"""
Generated Code Metadata:
========================
Original URL: https://ethereumcv.io
Prompt: Develop a Solidity-based decentralized exchange smart contract for Ethereum Classic Vision, incorporating features mentioned in the ETCV white paper.
Generated: DETERMINISTIC_c55a8ab80f997f1b
Batch ID: 20250612_151847
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Decentralized Exchange Smart Contract
contract DecentralizedExchange {
    // Event emitted when a trade occurs
    event Trade(
        address indexed buyer,
        address indexed seller,
        address indexed token,
        uint256 amount,
        uint256 price
    );

    // Struct to hold order details
    struct Order {
        address seller;
        uint256 amount;
        uint256 price; // Price in wei per token
    }

    // Mapping to store orders by token address
    mapping(address => Order[]) public orders;

    // Function to place an order
    function placeOrder(address _token, uint256 _amount, uint256 _price) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_price > 0, "Price must be greater than zero");

        // Transfer tokens from seller to the contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Create a new order and add it to the orders mapping
        orders[_token].push(Order({
            seller: msg.sender,
            amount: _amount,
            price: _price
        }));
    }

    // Function to execute a trade
    function executeTrade(address _token, uint256 _orderIndex) external payable {
        // Retrieve the order
        Order storage order = orders[_token][_orderIndex];

        // Ensure the order exists and has not been filled
        require(order.amount > 0, "Order does not exist or has been filled");
        require(msg.value >= order.price * order.amount, "Insufficient payment");

        // Transfer the tokens from the contract to the buyer
        IERC20(_token).transfer(msg.sender, order.amount);

        // Transfer the payment to the seller
        payable(order.seller).transfer(msg.value);

        // Emit the trade event
        emit Trade(msg.sender, order.seller, _token, order.amount, order.price);

        // Mark the order as filled
        order.amount = 0; // Set amount to zero to indicate the order is filled
    }

    // Function to withdraw tokens from the contract (for the owner)
    function withdrawTokens(address _token, uint256 _amount) external {
        // Only the contract owner can withdraw tokens
        require(msg.sender == address(this), "Only contract owner can withdraw tokens");
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the contract to the owner
        IERC20(_token).transfer(msg.sender, _amount);
    }

    // Function to withdraw Ether from the contract (for the owner)
    function withdrawEther(uint256 _amount) external {
        // Only the contract owner can withdraw Ether
        require(msg.sender == address(this), "Only contract owner can withdraw Ether");
        require(_amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient balance");

        // Transfer Ether to the owner
        payable(msg.sender).transfer(_amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
