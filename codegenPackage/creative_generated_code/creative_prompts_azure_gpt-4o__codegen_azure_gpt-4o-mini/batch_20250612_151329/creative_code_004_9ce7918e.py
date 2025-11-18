"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiedan.vip
Prompt: Create a function that calculates the total supply of TIEDAN tokens and verifies that the contract is renounced, as described in the tokenomics section.
Generated: DETERMINISTIC_9ce7918e3f6f8157
Batch ID: 20250612_151329
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

contract TIEDANToken {
    // Total supply of TIEDAN tokens
    uint256 private _totalSupply;

    // Address that holds the contract ownership
    address private _owner;

    // Event to log the total supply
    event TotalSupplyCalculated(uint256 totalSupply);

    // Modifier to check if the caller is the owner
    modifier onlyOwner() {
        require(msg.sender == _owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract with a total supply
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _totalSupply = initialSupply;
        _owner = msg.sender; // Set the contract creator as the owner
    }

    // Function to calculate the total supply of TIEDAN tokens
    function getTotalSupply() external view returns (uint256) {
        emit TotalSupplyCalculated(_totalSupply);
        return _totalSupply;
    }

    // Function to check if the contract is renounced
    function isContractRenounced() external view returns (bool) {
        // A renounced contract will have the owner set to address(0)
        return _owner == address(0);
    }

    // Function to renounce ownership
    function renounceOwnership() external onlyOwner {
        _owner = address(0); // Set the owner to address(0) to renounce ownership
    }
}
```
