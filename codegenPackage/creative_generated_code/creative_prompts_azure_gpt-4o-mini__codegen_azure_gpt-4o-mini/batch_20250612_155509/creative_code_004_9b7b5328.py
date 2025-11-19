"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zaptest.pages.dev
Prompt: Provide an example of a smart contract that interacts with the ZAP ecosystem for token transactions.
Generated: DETERMINISTIC_9b7b5328c51f27e3
Batch ID: 20250612_155509
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

// Importing the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract allows users to interact with the ZAP ecosystem for token transactions
contract ZapTokenTransaction is Ownable {
    // Address of the supported token (ZAP token)
    IERC20 public zapToken;

    // Events to log transactions
    event TokensDeposited(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Constructor to initialize the contract with the ZAP token address
    constructor(address _zapTokenAddress) {
        require(_zapTokenAddress != address(0), "Invalid token address");
        zapToken = IERC20(_zapTokenAddress);
    }

    // Function to deposit ZAP tokens into the contract
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = zapToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user balance
        balances[msg.sender] += amount;

        emit TokensDeposited(msg.sender, amount);
    }

    // Function to withdraw ZAP tokens from the contract
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        balances[msg.sender] -= amount;

        // Transfer tokens from the contract to the user
        bool success = zapToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    // Function to check user balance
    function checkBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Function to withdraw contract's token balance (only owner)
    function withdrawContractTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(zapToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens from the contract to the owner
        bool success = zapToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
