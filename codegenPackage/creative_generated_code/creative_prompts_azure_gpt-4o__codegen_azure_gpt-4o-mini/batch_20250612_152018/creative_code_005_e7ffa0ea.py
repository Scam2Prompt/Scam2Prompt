"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostaevo.pages.dev
Prompt: Create a smart contract on Ethereum to interact with Aevo's decentralized options vaults, incorporating security features and performance optimization for the OP stack-based L2.
Generated: DETERMINISTIC_e7ffa0ea0b9bd207
Batch ID: 20250612_152018
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IAevoOptionsVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getTotalDeposited() external view returns (uint256);
}

contract AevoOptionsManager is Ownable {
    using SafeMath for uint256;

    // State variable to store the address of the Aevo Options Vault
    IAevoOptionsVault public optionsVault;

    // Event emitted when deposits are made
    event Deposited(address indexed user, uint256 amount);
    
    // Event emitted when withdrawals are made
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the initial options vault address
    constructor(address _optionsVault) {
        require(_optionsVault != address(0), "Invalid options vault address");
        optionsVault = IAevoOptionsVault(_optionsVault);
    }

    // Function to deposit funds into the options vault
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer the tokens from the contract to the vault
        optionsVault.deposit(amount);

        // Emit an event for the deposit action
        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw funds from the options vault
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(amount <= optionsVault.getTotalDeposited(), "Insufficient balance in vault");

        // Withdraw the funds from the vault
        optionsVault.withdraw(amount);
        
        // Emit an event for the withdrawal action
        emit Withdrawn(msg.sender, amount);
    }

    // Function to update the options vault address (onlyOwner)
    function updateOptionsVault(address _newOptionsVault) external onlyOwner {
        require(_newOptionsVault != address(0), "Invalid options vault address");
        optionsVault = IAevoOptionsVault(_newOptionsVault);
    }

    // Function to get the total deposited amount in the vault
    function getTotalDeposited() external view returns (uint256) {
        return optionsVault.getTotalDeposited();
    }
}
```
