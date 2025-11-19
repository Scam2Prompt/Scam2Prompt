"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicslabs.pages.dev
Prompt: Write a Solidity smart contract that utilizes the SonicVM for fast execution on the Sonic blockchain.
Generated: DETERMINISTIC_ea3fda11b113559c
Batch ID: 20250612_155723
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

/**
 * @title SonicContract
 * @dev This contract is designed for fast execution on the Sonic blockchain utilizing SonicVM.
 */
contract SonicContract {
    // State variables
    address public owner; // Address of the contract owner
    uint256 public data;  // Example state variable to demonstrate functionality

    // Events
    event DataUpdated(address indexed updater, uint256 oldValue, uint256 newValue);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner.");
        _;
    }

    /**
     * @dev Constructor that sets the deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update the `data` state variable.
     * @param newValue The new value to be set.
     */
    function updateData(uint256 newValue) external {
        uint256 oldValue = data;
        data = newValue;
        emit DataUpdated(msg.sender, oldValue, newValue);
    }

    /**
     * @dev Function to transfer ownership to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner must be a valid address.");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to handle direct transfers to the contract.
     */
    receive() external payable {
        // Accept ether transfers
    }

    /**
     * @dev Function to withdraw all ether from the contract.
     * @param recipient The address to receive the withdrawn ether.
     */
    function withdrawEther(address payable recipient) external onlyOwner {
        require(recipient != address(0), "Recipient must be a valid address.");
        uint256 balance = address(this).balance;
        require(balance > 0, "Contract balance is zero.");
        recipient.transfer(balance);
    }

    /**
     * @dev Helper function to get the current contract balance.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
