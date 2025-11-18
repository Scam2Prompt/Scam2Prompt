"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-web3.pages.dev
Prompt: Write a Solidity smart contract for deploying a dapp on Linea's zkEVM ecosystem, ensuring compatibility with EVM bytecode and leveraging low gas fees.
Generated: DETERMINISTIC_0ec72123ac41fd1c
Batch ID: 20250612_150323
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
 * @title LineaDApp
 * @dev A simple smart contract deployed on Linea's zkEVM ecosystem. 
 * Compatible with EVM bytecode and optimized for low gas fees.
 */
contract LineaDApp {
    // State variable to store data
    string public data;

    // Address of the contract owner
    address public owner;

    // Event emitted when the data is updated
    event DataUpdated(string oldData, string newData);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Contract constructor that sets the initial owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update the stored data.
     * @param _newData The new data to be stored.
     */
    function updateData(string calldata _newData) external onlyOwner {
        // Emit an event before updating to preserve the old state
        emit DataUpdated(data, _newData);
        data = _newData;
    }

    /**
     * @dev Function to retrieve the stored data. 
     * This function is public and gas-efficient due to its lightweight nature.
     * @return The current stored data.
     */
    function getData() external view returns (string memory) {
        return data;
    }

    /**
     * @dev Allows the owner to transfer contract ownership to another address.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid address");
        owner = _newOwner;
    }
}
```
