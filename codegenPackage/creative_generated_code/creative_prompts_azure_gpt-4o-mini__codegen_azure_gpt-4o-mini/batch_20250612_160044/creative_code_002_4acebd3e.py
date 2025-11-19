"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tether.ac
Prompt: Generate a code snippet for a smart contract that accepts Tether AC-X tokens (XUSD₮) as payment on the Ethereum blockchain.
Generated: DETERMINISTIC_4acebd3e1f957f60
Batch ID: 20250612_160044
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

// Import the interface for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract to accept Tether AC-X tokens (XUSD₮) as payment
contract TetherPayment {
    // State variable to store the address of the Tether token contract
    IERC20 public tetherToken;

    // Event emitted when a payment is received
    event PaymentReceived(address indexed payer, uint256 amount);

    // Constructor to set the address of the Tether token contract
    constructor(address _tetherTokenAddress) {
        require(_tetherTokenAddress != address(0), "Invalid token address");
        tetherToken = IERC20(_tetherTokenAddress);
    }

    // Function to accept payments in Tether tokens
    function pay(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer Tether tokens from payer to this contract
        bool success = tetherToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");

        // Emit the payment received event
        emit PaymentReceived(msg.sender, amount);
    }

    // Function to withdraw Tether tokens from the contract
    function withdraw(uint256 amount) external {
        // Only the contract owner can withdraw funds
        require(msg.sender == owner(), "Only the owner can withdraw");

        // Check balance before withdrawal
        uint256 balance = tetherToken.balanceOf(address(this));
        require(balance >= amount, "Insufficient balance");

        // Transfer Tether tokens to the owner
        bool success = tetherToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");
    }

    // Function to get the balance of Tether tokens held by the contract
    function getBalance() external view returns (uint256) {
        return tetherToken.balanceOf(address(this));
    }
    
    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner(), "Only the owner can perform this action");
        _;
    }

    // Function to get the contract owner's address
    function owner() public view returns (address) {
        // Placeholder for owner's address logic or simply replace with actual implementation
        return address(0); // Replace with actual owner address logic
    }
}
```

Note: The function `owner()` is currently a placeholder. In a production-ready contract, you should implement proper ownership management, such as using OpenZeppelin's `Ownable` contract or a similar mechanism to manage ownership securely.
