"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.seedify.de
Prompt: Recommend best practices for securing smart contracts in a blockchain launchpad to prevent vulnerabilities like reentrancy attacks.
Generated: DETERMINISTIC_46055fad0e3dc8fe
Batch ID: 20250612_151858
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

contract SecureLaunchpad {
    // State variable to track active contracts
    mapping(address => bool) public activeContracts;

    // Event to log contract activation
    event ContractActivated(address indexed contractAddress);

    // Modifier to prevent reentrancy attacks
    modifier nonReentrant() {
        require(!locked, "ReentrancyGuard: reentrant call");
        locked = true;
        _;
        locked = false;
    }

    // Boolean state to prevent reentrancy
    bool private locked;

    // Function to activate a contract on the launchpad
    function activateContract(address _contractAddress) external nonReentrant {
        require(_contractAddress != address(0), "Invalid address");
        require(!activeContracts[_contractAddress], "Contract already active");

        // Activate the contract
        activeContracts[_contractAddress] = true;

        // Emit event for contract activation
        emit ContractActivated(_contractAddress);
    }

    // Function to deactivate a contract
    function deactivateContract(address _contractAddress) external {
        require(activeContracts[_contractAddress], "Contract not active");

        // Deactivate the contract
        activeContracts[_contractAddress] = false;
    }

    // Fallback function to prevent Ether from being sent directly to the contract
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }

    // Function to withdraw Ether from the contract
    function withdraw(address payable _to, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient balance");

        // Transfer Ether to the specified address
        (bool success, ) = _to.call{value: _amount}("");        
        require(success, "Transfer failed");

        // Additional security: ensure the recipient didn't fall victim to a reentrancy attack
        require(activeContracts[_to], "Recipient contract must be active");
    }

    // Function to check balance of the contract
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
