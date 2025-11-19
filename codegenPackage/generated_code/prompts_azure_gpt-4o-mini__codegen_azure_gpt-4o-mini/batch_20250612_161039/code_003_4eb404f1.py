"""
Generated Code Metadata:
========================
Original URL: https://activefusionnet.vercel.app
Prompt: Generate an example of a smart contract that interacts with multiple blockchain networks in a decentralized application.
Generated: DETERMINISTIC_4eb404f1cb3bb3e2
Batch ID: 20250612_161039
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

// Importing necessary libraries for cross-chain interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with another blockchain network
interface IExternalContract {
    function transferTo(address recipient, uint256 amount) external returns (bool);
}

// Main smart contract
contract CrossChainWallet is Ownable {
    // Mapping to track balances of users
    mapping(address => uint256) private balances;

    // Event emitted when funds are deposited
    event Deposited(address indexed user, uint256 amount);
    
    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when funds are transferred to another network
    event TransferredToExternal(address indexed user, address indexed externalContract, uint256 amount);

    // Function to deposit tokens into the contract
    function deposit(IERC20 token, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from user to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        
        // Update the user's balance
        balances[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract
    function withdraw(IERC20 token, uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to transfer tokens to an external contract on another blockchain
    function transferToExternal(IExternalContract externalContract, uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance for transfer");

        // Update the user's balance
        balances[msg.sender] -= amount;

        // Call the external contract to transfer tokens
        require(externalContract.transferTo(msg.sender, amount), "External transfer failed");

        emit TransferredToExternal(msg.sender, address(externalContract), amount);
    }

    // Function to check the balance of a user
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}
```
