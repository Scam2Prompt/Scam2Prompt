"""
Generated Code Metadata:
========================
Original URL: https://orikod.com
Prompt: Develop a smart contract for a micro-payment app using Arbitrum AnyTrust chains, ensuring maximum speed and minimal cost while maintaining full security guarantees.
Generated: DETERMINISTIC_1a0f96e119995951
Batch ID: 20250622_212817
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a micro-payment application
contract MicroPaymentApp is Ownable {
    // Event emitted when a payment is made
    event PaymentMade(address indexed payer, address indexed payee, uint256 amount, string message);

    // Mapping to track balances of users
    mapping(address => uint256) private balances;

    // ERC20 token interface
    IERC20 public token;

    // Constructor to initialize the contract with the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to make a payment
    function makePayment(address _payee, uint256 _amount, string memory _message) external {
        require(_payee != address(0), "Invalid payee address");
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens from payer to payee
        token.transferFrom(msg.sender, _payee, _amount);

        // Emit payment event
        emit PaymentMade(msg.sender, _payee, _amount, _message);
    }

    // Function to check the balance of a user
    function checkBalance() external view returns (uint256) {
        return token.balanceOf(msg.sender);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        token.transfer(msg.sender, _amount);
    }

    // Function to set a new token address (only owner)
    function setTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        token = IERC20(_newTokenAddress);
    }
}
```
